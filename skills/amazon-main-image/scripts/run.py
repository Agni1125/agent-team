#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DAG runner for a Coze workflow converted to a Claude Code skill.

Standard library only. Reads graph.json next to this file.

Default mode is --dry-run: nothing is sent over the network. Real execution
needs the explicit --execute flag because several nodes call paid APIs.

  python run.py                                  # dry run, prints the plan
  python run.py --inputs inputs.json             # dry run with real inputs
  python run.py --inputs inputs.json --execute   # REAL CALLS, COSTS MONEY
  python run.py --plan-json plan.json            # machine-readable plan
"""

import argparse
import asyncio
import json
import os
import re
import sys
import types
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH_PATH = os.path.join(HERE, 'graph.json')

# Node titles and prompts are Chinese; the Windows console default (cp950) cannot
# encode them and would abort the run with UnicodeEncodeError.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding='utf-8', errors='replace')
    except (AttributeError, ValueError):
        pass

REF_RE = re.compile(r'\{\{block_output_([0-9]+)\.([A-Za-z0-9_.\[\]]+)\}\}')
ENV_RE = re.compile(r'\$\{([A-Z][A-Z0-9_]*)\}')

# Node types this runner can actually execute locally.
EXECUTABLE = {'start', 'end', 'comment', 'condition', 'http', 'code', 'batch'}
# Node types that only exist inside Coze and have no local equivalent.
COZE_ONLY = {'llm', 'plugin', 'image_generate', 'async_job_call', 'to_json'}


class WorkflowError(Exception):
    pass


class MissingEnv(WorkflowError):
    pass


def load_graph():
    with open(GRAPH_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


# --------------------------------------------------------------------------
# environment / secrets
# --------------------------------------------------------------------------

def resolve_env(text, used=None):
    """Replace ${VAR} with os.environ[VAR]. Raises if a variable is missing."""
    missing = []

    def sub(m):
        name = m.group(1)
        val = os.environ.get(name)
        if val is None or val == '':
            missing.append(name)
            return m.group(0)
        if used is not None:
            used.add(name)
        return val

    out = ENV_RE.sub(sub, text)
    if missing:
        raise MissingEnv(
            'missing environment variable(s): %s. Set them before running with '
            '--execute, e.g.  $env:%s = "<value>"' % (', '.join(sorted(set(missing))),
                                                      sorted(set(missing))[0]))
    return out


def mask(text):
    """Never print a resolved secret."""
    return ENV_RE.sub(lambda m: '${%s}' % m.group(1), text)


# --------------------------------------------------------------------------
# variable references
# --------------------------------------------------------------------------

def dig(obj, path):
    """Follow a dotted path such as 'data.url' or 'items[0].url'."""
    cur = obj
    if path in (None, ''):
        return cur
    for part in re.split(r'\.', path):
        m = re.match(r'^([^\[\]]*)((\[\d+\])*)$', part)
        if not m:
            raise WorkflowError('bad path segment %r in %r' % (part, path))
        key, idxs = m.group(1), m.group(2)
        if key:
            if isinstance(cur, dict):
                if key not in cur:
                    raise WorkflowError('key %r not found (path %r)' % (key, path))
                cur = cur[key]
            else:
                raise WorkflowError('cannot index %s with %r (path %r)'
                                    % (type(cur).__name__, key, path))
        for i in re.findall(r'\[(\d+)\]', idxs or ''):
            cur = cur[int(i)]
    return cur


class State(object):
    def __init__(self):
        self.outputs = {}   # node id -> dict of outputs
        self.status = {}    # node id -> 'ok' | 'skipped' | 'unsupported' | 'pending'

    def get(self, node_id, path):
        if node_id not in self.outputs:
            raise WorkflowError('node %s has produced no output yet' % node_id)
        return dig(self.outputs[node_id], path)


def resolve_source(src, state):
    kind = src.get('kind')
    if kind == 'literal':
        return src.get('value')
    if kind == 'none':
        return None
    if kind == 'ref':
        return state.get(src['ref_node'], src.get('path'))
    return src.get('value')


def substitute_refs(text, state):
    """Replace {{block_output_<id>.<path>}} inside a template string."""
    def sub(m):
        v = state.get(m.group(1), m.group(2))
        if isinstance(v, str):
            return v
        return json.dumps(v, ensure_ascii=False)
    return REF_RE.sub(sub, text)


def substitute_refs_json(text, state):
    """Same as substitute_refs but JSON-escapes values so the result stays valid JSON.

    Bare (unquoted) placeholders are emitted as raw JSON; quoted ones are escaped
    for use inside a JSON string literal.
    """
    out = []
    i = 0
    n = len(text)
    in_str = False
    while i < n:
        c = text[i]
        if in_str:
            if c == '\\':
                out.append(text[i:i + 2])
                i += 2
                continue
            if c == '"':
                in_str = False
                out.append(c)
                i += 1
                continue
            m = REF_RE.match(text, i)
            if m:
                v = state.get(m.group(1), m.group(2))
                if not isinstance(v, str):
                    v = json.dumps(v, ensure_ascii=False)
                out.append(json.dumps(v, ensure_ascii=False)[1:-1])
                i = m.end()
                continue
            out.append(c)
            i += 1
            continue
        if c == '"':
            in_str = True
            out.append(c)
            i += 1
            continue
        m = REF_RE.match(text, i)
        if m:
            v = state.get(m.group(1), m.group(2))
            out.append(json.dumps(v, ensure_ascii=False))
            i = m.end()
            continue
        out.append(c)
        i += 1
    return ''.join(out)


# --------------------------------------------------------------------------
# node executors
# --------------------------------------------------------------------------

def run_http(node, state, timeout_default=600):
    spec = node['http']
    url = substitute_refs(spec['url'] or '', state)
    used = set()
    url = resolve_env(url, used)

    headers = {}
    for h in spec.get('headers') or []:
        val = h.get('value')
        if not isinstance(val, str):
            val = '' if val is None else str(val)
        headers[h['name']] = resolve_env(substitute_refs(val, state), used)

    query = []
    for p in spec.get('params') or []:
        val = p.get('value')
        if not isinstance(val, str):
            val = '' if val is None else str(val)
        query.append((p['name'], resolve_env(substitute_refs(val, state), used)))
    if query:
        from urllib.parse import urlencode
        url = url + ('&' if '?' in url else '?') + urlencode(query)

    data = None
    if spec.get('body_type') == 'JSON' and spec.get('body_json'):
        body_text = substitute_refs_json(spec['body_json'], state)
        body_text = resolve_env(body_text, used)
        json.loads(body_text)  # fail loudly on a malformed body before sending
        data = body_text.encode('utf-8')
        headers.setdefault('Content-Type', 'application/json')

    req = urllib.request.Request(url, data=data, headers=headers,
                                 method=spec.get('method') or 'GET')
    timeout = spec.get('timeout_s') or timeout_default
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode('utf-8', 'replace')
        status = resp.getcode()
        rheaders = dict(resp.headers.items())
    raw = normalize_llm_response(raw)
    return {'body': raw, 'statusCode': status, 'headers': json.dumps(rheaders, ensure_ascii=False)}


def normalize_llm_response(raw):
    """Anthropic /messages 回應 -> OpenAI chat/completions 形狀。

    只在偵測到 Anthropic 形狀時才動;其他回應原樣返回。
    glm-5.3 會先吐 thinking 區塊再吐 text,只取 type=="text" 的部分,
    否則下游會拿到模型的思考過程而不是答案。
    """
    try:
        d = json.loads(raw)
    except Exception:
        return raw
    if not isinstance(d, dict):
        return raw
    if d.get('type') != 'message' or not isinstance(d.get('content'), list):
        return raw
    text = ''.join(b.get('text', '') for b in d['content']
                   if isinstance(b, dict) and b.get('type') == 'text')
    u = d.get('usage') or {}
    out = {
        'id': d.get('id'),
        'object': 'chat.completion',
        'model': d.get('model'),
        'choices': [{
            'index': 0,
            'message': {'role': 'assistant', 'content': text},
            'finish_reason': 'length' if d.get('stop_reason') == 'max_tokens' else 'stop',
        }],
        'usage': {
            'prompt_tokens': u.get('input_tokens'),
            'completion_tokens': u.get('output_tokens'),
            'total_tokens': (u.get('input_tokens') or 0) + (u.get('output_tokens') or 0),
        },
        '_anthropic_stop_reason': d.get('stop_reason'),
    }
    if not text:
        # 全被 thinking 吃掉 = max_tokens 給太小,靜默回空字串會很難查。
        out['_warning'] = ('Anthropic 回應沒有 text 區塊(可能全是 thinking,'
                           'max_tokens 太小);stop_reason=%s' % d.get('stop_reason'))
    return json.dumps(out, ensure_ascii=False)


def run_code(node, state):
    spec = node['code']
    if spec['language'] != 'python':
        raise WorkflowError(
            'node %s (%s) is a %s code node; this runner only executes Python code nodes'
            % (node['id'], node['title'], spec['language']))
    params = {}
    for item in node.get('inputs') or []:
        params[item['name']] = resolve_source(item['source'], state)

    ns = {}
    exec(compile(spec['source'], '<node %s>' % node['id'], 'exec'), ns)  # noqa: S102
    main = ns.get('main')
    if main is None:
        raise WorkflowError('code node %s defines no main()' % node['id'])
    args = types.SimpleNamespace(params=params)
    if asyncio.iscoroutinefunction(main):
        result = asyncio.run(main(args))
    else:
        result = main(args)
    if not isinstance(result, dict):
        raise WorkflowError('code node %s returned %s, expected dict'
                            % (node['id'], type(result).__name__))
    return result


OPERATORS = {
    1: lambda a, b: a == b,
    2: lambda a, b: a != b,
    3: lambda a, b: len(a) == 0 if a is not None else True,
    4: lambda a, b: len(a) > 0 if a is not None else False,
    5: lambda a, b: a > b,
    6: lambda a, b: a >= b,
    7: lambda a, b: a < b,
    8: lambda a, b: a <= b,
    9: lambda a, b: b in a,
    10: lambda a, b: b not in a,
    11: lambda a, b: a is None,
    12: lambda a, b: a is not None,
}


def eval_condition(node, state):
    """Return True when the first branch matches (the 'true' port)."""
    for branch in node['condition']['branches']:
        results = []
        for c in branch['conditions']:
            left = resolve_source(c['left']['source'], state)
            right = resolve_source(c['right']['source'], state)
            op = OPERATORS.get(c['operator'])
            if op is None:
                raise WorkflowError('unknown condition operator %r on node %s'
                                    % (c['operator'], node['id']))
            results.append(bool(op(left, right)))
        # logic 2 == AND, logic 1 == OR (Coze encoding)
        ok = all(results) if branch.get('logic') == 2 else any(results)
        if ok:
            return True
    return False


# --------------------------------------------------------------------------
# planning / execution
# --------------------------------------------------------------------------

def describe(node, state, resolved_ok):
    """Human-readable one-node plan entry."""
    d = {'id': node['id'], 'type': node['type'], 'title': node['title']}
    if node['type'] == 'http':
        d['method'] = node['http']['method']
        d['url'] = mask(node['http']['url'] or '')
        d['headers'] = [{'name': h['name'], 'value': mask(str(h['value']))}
                        for h in node['http'].get('headers') or []]
        d['body_type'] = node['http'].get('body_type')
        d['body_refs'] = node['http'].get('refs')
    elif node['type'] == 'code':
        d['language'] = node['code']['language']
        d['inputs'] = [i['name'] for i in node.get('inputs') or []]
    elif node['type'] == 'llm':
        d['model'] = node['llm'].get('model_name')
        d['prompt_keys'] = [p['key'] for p in node.get('prompts') or []]
    elif node['type'] == 'plugin':
        d['plugin'] = node['plugin'].get('plugin_name')
        d['api'] = node['plugin'].get('api_name')
    elif node['type'] == 'batch':
        d['children'] = node['batch']['children']
        d['batch_size'] = node['batch']['batch_size']
    elif node['type'] == 'condition':
        d['branches'] = len(node['condition']['branches'])
    if node.get('prompts'):
        d['prompts'] = [{'key': p['key'], 'role': p['role'], 'sha256': p['sha256'],
                         'chars': len(p['text'])} for p in node['prompts']]
    d['runnable_here'] = node['type'] in EXECUTABLE
    return d


def collect_start_inputs(graph, supplied):
    start = None
    for n in graph['nodes'].values():
        if n['type'] == 'start':
            start = n
            break
    if start is None:
        raise WorkflowError('workflow has no start node')
    values = {}
    missing = []
    for o in start['outputs']:
        name = o['name']
        if name in supplied:
            values[name] = supplied[name]
        elif o.get('default_value') is not None:
            values[name] = o['default_value']
        elif o.get('required'):
            missing.append(name)
        else:
            values[name] = None
    return start['id'], values, missing


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--inputs', help='JSON file with the start-node input values')
    ap.add_argument('--execute', action='store_true',
                    help='actually call the APIs. WITHOUT THIS FLAG NOTHING IS SENT. '
                         'These workflows call paid APIs.')
    ap.add_argument('--dry-run', action='store_true',
                    help='explicit no-op flag; dry run is already the default')
    ap.add_argument('--only', metavar='NODE_ID', action='append',
                    help='restrict the plan/run to these node ids')
    ap.add_argument('--skip-unsupported', action='store_true',
                    help='with --execute, skip Coze-only nodes instead of stopping')
    ap.add_argument('--plan-json', metavar='PATH',
                    help='write the plan as JSON (useful for an agent driving the graph)')
    ap.add_argument('--show-prompt', metavar='NODE_ID',
                    help='print the verbatim prompt text of one node and exit')
    args = ap.parse_args(argv)

    graph = load_graph()
    nodes = graph['nodes']

    if args.show_prompt:
        n = nodes.get(args.show_prompt)
        if n is None:
            ap.error('no such node: %s' % args.show_prompt)
        for p in n.get('prompts') or []:
            sys.stdout.write('----- %s (%s) sha256=%s -----\n' % (p['key'], p['role'], p['sha256']))
            sys.stdout.write(p['text'])
            sys.stdout.write('\n')
        return 0

    supplied = {}
    if args.inputs:
        with open(args.inputs, 'r', encoding='utf-8') as f:
            supplied = json.load(f)

    start_id, start_values, missing = collect_start_inputs(graph, supplied)

    order = graph['execution_order']
    if args.only:
        order = [n for n in order if n in set(args.only)]

    state = State()
    state.outputs[start_id] = start_values

    mode = 'EXECUTE (real API calls)' if args.execute else 'DRY RUN (no network traffic)'
    print('workflow : %s' % graph['workflow']['name'])
    print('mode     : %s' % mode)
    print('nodes    : %d in topological order' % len(order))
    if graph.get('env_vars'):
        print('env vars : %s' % ', '.join(graph['env_vars']))
        unset = [v for v in graph['env_vars'] if not os.environ.get(v)]
        if unset:
            print('           NOT SET: %s' % ', '.join(unset))
    if missing:
        print('inputs   : MISSING REQUIRED %s' % ', '.join(missing))
    else:
        print('inputs   : %s' % ', '.join('%s=%s' % (k, _short(v)) for k, v in start_values.items()))
    print('')

    if args.execute and missing:
        raise SystemExit('refusing to execute: required start inputs missing: %s'
                         % ', '.join(missing))

    plan = []
    disabled = set()

    for idx, nid in enumerate(order, 1):
        node = nodes[nid]
        entry = describe(node, state, True)
        entry['step'] = idx

        if nid in disabled:
            entry['action'] = 'skipped (branch not taken)'
            state.status[nid] = 'skipped'
            plan.append(entry)
            print('%3d. [skip] %s %s (%s)' % (idx, node['type'], node['title'], nid))
            continue

        if node['type'] == 'comment':
            entry['action'] = 'canvas note, no execution'
            plan.append(entry)
            if not args.execute:
                print('%3d. [comment] (canvas note, not executed)' % idx)
            continue

        if not args.execute:
            entry['action'] = 'would run' if node['type'] in EXECUTABLE else 'NOT RUNNABLE LOCALLY'
            plan.append(entry)
            extra = ''
            if node['type'] == 'http':
                extra = ' -> %s %s' % (entry.get('method'), entry.get('url'))
            elif node['type'] == 'llm':
                extra = ' -> model %s' % entry.get('model')
            elif node['type'] == 'plugin':
                extra = ' -> coze plugin %s' % entry.get('plugin')
            print('%3d. [%s] %s (%s)%s%s'
                  % (idx, node['type'], node['title'] or '-', nid, extra,
                     '' if node['type'] in EXECUTABLE else '   << needs Coze'))
            continue

        # ---- real execution -------------------------------------------
        if node['type'] in COZE_ONLY:
            msg = ('node %s "%s" is a %s node; it runs inside Coze and has no local '
                   'equivalent' % (nid, node['title'], node['type']))
            if args.skip_unsupported:
                print('%3d. [unsupported] %s' % (idx, msg))
                state.status[nid] = 'unsupported'
                entry['action'] = 'unsupported, skipped'
                plan.append(entry)
                continue
            raise SystemExit(msg + '. Re-run with --skip-unsupported to continue past it.')

        if node['type'] == 'start':
            state.status[nid] = 'ok'
            continue
        if node['type'] == 'end':
            result = {}
            for i in node.get('inputs') or []:
                result[i['name']] = resolve_source(i['source'], state)
            state.outputs[nid] = result
            state.status[nid] = 'ok'
            print('%3d. [end] %s' % (idx, json.dumps(result, ensure_ascii=False)[:400]))
            continue
        if node['type'] == 'condition':
            taken = eval_condition(node, state)
            state.outputs[nid] = {'result': taken}
            state.status[nid] = 'ok'
            port = 'true' if taken else 'false'
            keep = set()
            drop = set()
            for e in graph['edges']:
                if e['source'] != nid:
                    continue
                if e.get('port') in (None, port):
                    keep |= _downstream(graph, e['target'])
                else:
                    drop |= _downstream(graph, e['target'])
            disabled |= (drop - keep)
            print('%3d. [condition] %s -> %s' % (idx, node['title'], port))
            continue
        if node['type'] == 'batch':
            raise SystemExit(
                'node %s "%s" is a batch container whose child (%s) is a %s node; '
                'batch execution is only meaningful once the child type is runnable'
                % (nid, node['title'], ','.join(node['batch']['children']),
                   nodes[node['batch']['children'][0]]['type']
                   if node['batch']['children'] else '?'))
        if node['type'] == 'http':
            out = run_http(node, state)
            state.outputs[nid] = out
            state.status[nid] = 'ok'
            print('%3d. [http] %s -> %s (%d bytes)'
                  % (idx, node['title'], out['statusCode'], len(out['body'])))
            continue
        if node['type'] == 'code':
            out = run_code(node, state)
            state.outputs[nid] = out
            state.status[nid] = 'ok'
            print('%3d. [code] %s -> %s' % (idx, node['title'], ', '.join(out.keys())))
            continue
        raise SystemExit('no executor for node type %r (node %s)' % (node['type'], nid))

    if args.plan_json:
        with open(args.plan_json, 'w', encoding='utf-8') as f:
            json.dump({'workflow': graph['workflow'], 'plan': plan}, f,
                      ensure_ascii=False, indent=2)
        print('\nplan written to %s' % args.plan_json)

    if not args.execute:
        print('\nDry run only. Nothing was sent. Add --execute to make real '
              '(billable) API calls.')
    return 0


def _downstream(graph, nid, seen=None):
    if seen is None:
        seen = set()
    if nid in seen:
        return seen
    seen.add(nid)
    for e in graph['edges']:
        if e['source'] == nid:
            _downstream(graph, e['target'], seen)
    return seen


def _short(v, n=60):
    s = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    return s if len(s) <= n else s[:n] + '...'


if __name__ == '__main__':
    sys.exit(main())
