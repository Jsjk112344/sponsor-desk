#!/usr/bin/env python3
"""Exercise approval boundaries and evidence requirements, without credentials."""
import json
from pathlib import Path
import yaml
from desk import Desk, rehearsal, ROOT

def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('unsafe action accepted')

def main():
    t = yaml.safe_load((ROOT/'sponsor-desk.template.yaml').read_text())
    assert t['version'] == 1
    assert [a['name'] for a in t['agents']] == ['{team}-sourcer','{team}-outreach']
    assert t['room']['name'] == '{team}-sponsor-desk'
    assert t['room']['users'] == ['{$creator}']
    for a in t['agents']:
        for field in ('directory','location','provider','instructions','addressing'):
            assert a[field]
        assert a['addressing'] == 'owner-agents'
        assert a['directory'].endswith(a['name'])
    for r in json.loads((ROOT/'fixtures/cached/candidates.json').read_text()):
        for receipt in r['receipts']:
            assert all(receipt[k] for k in ('event','edition','tier','source_url','observed_at'))
            assert receipt['source_url'].startswith('https://')
    d = Desk()
    rejects(lambda: d.act('candidates'))
    rejects(lambda: d.act('confirm',actor='agent'))
    d.act('confirm'); d.act('candidates')
    rejects(lambda: d.act('shortlist',actor='agent'))
    rejects(lambda: d.act('draft'))
    d.act('shortlist'); d.act('draft')
    rejects(lambda: d.act('approve',actor='agent',message_id='fake'))
    rejects(lambda: d.act('approve',thread='other',message_id='wrong-thread'))
    rejects(lambda: d.act('approve',version=2,message_id='wrong-version'))
    rejects(lambda: d.act('approve'))
    d.act('approve',message_id='ok')
    d.act('approve',message_id='ok')
    assert len(d.state['decisions']) == 1
    rejects(lambda: d.act('approve',message_id='ok',version=2))
    d.act('draft')
    assert d.state['draft']['status'] == 'unsent'
    rejects(lambda: d.act('approve',version=1,message_id='stale-version'))
    d.act('correct')
    rejects(lambda: d.act('approve',version=2,message_id='stale-brief'))
    rejects(lambda: d.act('draft'))
    d = rehearsal()
    assert len(d.state['candidates']) == 5
    assert len(d.state['tasks']) == len(d.state['decisions']) == 1
    assert d.state['draft']['sent'] is False
    d.act('skip')
    rejects(lambda: d.act('draft'))
    rejects(lambda: d.act('approve',message_id='skip-approval'))
    for action in ('send','schedule','connect-mailbox','purchase'):
        assert 'Room Rule 1' in d.act(action)
    print('PASS: template contract, dated receipts, selection, handoff, approval identity/thread/version, replay, correction, skip and never-send')

if __name__ == '__main__': main()
