#!/usr/bin/env python3
"""Credential-free workflow contract rehearsal. No network, no model, no send path."""
import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class Desk:
    def __init__(self):
        self.state = {'mode': 'cached', 'brief_version': 1, 'confirmed': False,
                      'candidates': [], 'draft': None, 'tasks': [], 'decisions': [],
                      'history': [], 'handoff': None}
        self.seen = {}

    def act(self, action, *, actor='human', thread='demo-thread', message_id=None,
            version=1, candidate='azure'):
        payload = (action, actor, thread, version, candidate)
        if message_id in self.seen and message_id is not None:
            old, result = self.seen[message_id]
            if old != payload:
                raise ValueError('idempotency conflict')
            return result
        s = self.state
        if action in ('send', 'schedule', 'connect-mailbox', 'purchase'):
            result = 'Refused: Room Rule 1 keeps every pitch unsent; approval records review only.'
        elif action == 'kickoff':
            result = 'cached: Proposed Singapore developer event, cloud infrastructure, 600 practitioners. Confirm this brief?'
        elif action == 'confirm':
            self.human(actor)
            s['confirmed'] = True
            result = 'Confirmed brief v' + str(s['brief_version'])
        elif action == 'candidates':
            self.require(s['confirmed'], 'confirm brief first')
            s['candidates'] = json.loads((ROOT/'fixtures/cached/candidates.json').read_text())
            result = '\n'.join(r['company']+' | '+r['receipts'][0]['tier']+' | '+r['receipts'][0]['source_url']+' | observed_at='+r['receipts'][0]['observed_at']+' | '+r['fit_inference'] for r in s['candidates'])
        elif action in ('shortlist', 'skip', 'not_now'):
            self.human(actor)
            row = next((r for r in s['candidates'] if r['candidate_id'] == candidate), None)
            self.require(row is not None, 'unknown candidate')
            row['decision'] = action
            if action != 'shortlist' and s['draft'] and s['draft']['candidate_id'] == candidate:
                s['draft']['status'] = 'stale'
            if action == 'shortlist':
                s['handoff'] = dict(type='sponsor_desk.handoff.v1', run_id='fixture-demo',
                    thread_id=thread, brief_version=s['brief_version'],candidate_id=candidate,
                    company=row['company'],domain=row['domain'],decision=action,
                    receipts=row['receipts'],fit_inference=row['fit_inference'],gaps=row['gaps'],
                    report_ref='fixture-report-v1',idempotency_key='fixture-demo:'+candidate+':handoff:v'+str(s['brief_version']))
                result = '@demo-outreach '+json.dumps(s['handoff'])
            else:
                result = candidate+' saved as '+action
        elif action == 'draft':
            h = s['handoff']
            self.require(h and h['candidate_id'] == candidate and h['thread_id'] == thread and h['brief_version'] == s['brief_version'] and s['confirmed'], 'missing/current handoff required')
            row = next(r for r in s['candidates'] if r['candidate_id'] == candidate)
            self.require(row['decision'] == 'shortlist', 'shortlist required')
            self.require(candidate == 'azure', 'only Azure pitch is cached; do not invent a saved draft')
            d = json.loads((ROOT/'fixtures/cached/draft.json').read_text())
            d['version'] = s['draft']['version']+1 if s['draft'] else 1
            d['brief_version'] = s['brief_version']
            d['thread_id'] = thread
            s['draft'] = d
            result = json.dumps(d)
        elif action == 'approve':
            self.human(actor)
            d = s['draft']
            self.require(d and d['status'] in ('unsent','approved_for_review') and d['version'] == version and d['thread_id'] == thread and d['brief_version'] == s['brief_version'] and s['confirmed'], 'current exact draft/thread required')
            self.require(message_id, 'approval message ID required')
            d['status'] = 'approved_for_review'
            entry = dict(draft_id=d['draft_id'], version=version, brief_version=s['brief_version'],
                         candidate_id=d['candidate_id'], approver=actor, message_id=message_id,
                         thread_id=thread, body_sha256=hashlib.sha256(d['body'].encode()).hexdigest(),
                         status='approved_for_review', sent=False)
            s['tasks'].append(dict(name='Task-'+d['draft_id']+'-v'+str(version), **entry))
            s['decisions'].append(dict(name='Decision-'+message_id, **entry))
            result = 'Local Task + Decision recorded; review approved; unsent.'
        elif action == 'correct':
            self.human(actor)
            s['brief_version'] += 1
            s['confirmed'] = False
            s['handoff'] = None
            if s['draft']:
                s['draft']['status'] = 'stale'
            result = 'Brief corrected; confirmation and fresh draft approval required.'
        else:
            raise ValueError('unsupported action')
        s['history'].append(dict(actor=actor,thread=thread,action=action,result=result))
        if message_id is not None:
            self.seen[message_id] = (payload, result)
        return result

    @staticmethod
    def require(ok, reason):
        if not ok:
            raise ValueError(reason)

    @staticmethod
    def human(actor):
        Desk.require(actor == 'human', 'human authorization required')


def rehearsal():
    desk = Desk()
    for action,kw in [('kickoff',{}),('confirm',{}),('candidates',{}),
                      ('skip',{'candidate':'aws'}),('not_now',{'candidate':'google'}),
                      ('shortlist',{}),('draft',{}),('approve',{'message_id':'human-approval-1'}),('send',{})]:
        desk.act(action,**kw)
    return desk


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'.local/rehearsal.json')
    args = parser.parse_args()
    desk = rehearsal()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(desk.state,indent=2)+'\n')
    for event in desk.state['history']:
        print(event['action'].upper()+': '+event['result'])
    print('LOCAL CONTRACT REHEARSAL ONLY — no Switch/agent/MCP execution')

if __name__ == '__main__':
    main()
