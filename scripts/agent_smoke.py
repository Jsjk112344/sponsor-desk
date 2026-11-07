#!/usr/bin/env python3
"""Run both roles through the signed-in Claude CLI, with all tools/MCP disabled.
Uses existing provider entitlement; never configures an API key or paid fallback.
This checks instruction behavior, not Switch or real MCP persistence.
"""
import json
import os
from pathlib import Path
import subprocess
import tempfile
from desk import ROOT, rehearsal

def main():
    if os.environ.get('ANTHROPIC_API_KEY') or os.environ.get('ANTHROPIC_AUTH_TOKEN'):
        raise SystemExit('Refusing API-key mode; use existing subscription login')
    out = ROOT/'.local/agent-smoke'
    out.mkdir(parents=True, exist_ok=True)
    state = rehearsal().state
    data = '\n'.join((ROOT/p).read_text() for p in [
        'room/RULES.md','fixtures/devcon-apac-2027.brief.md',
        'fixtures/cached/candidates.json','fixtures/cached/draft.json'])
    for role in ('sourcer','outreach'):
        instructions = (ROOT/f'agents/{role}/INSTRUCTIONS.md').read_text()
        prompt = ('You are executing a fixture-only instruction conformance test, not connected to Switch. '
                  'All file contents are supplied below; tools are disabled. Never claim MCP or room persistence. '
                  'Human fixture transcript: event brief supplied, human confirmed exact v1, human said '
                  'shortlist Microsoft Azure, skip AWS, not_now Google Cloud. '
                  'Your teammate is @demo-outreach if Sourcer, @demo-sourcer if Outreach. '
                  'Sourcer: return five dated receipts and the handoff. Outreach: process this supplied '
                  'handoff and return full unsent role-addressed draft with ID/version; human then says '
                  'approved fixture-azure v1, then just send it. Describe the required room records '
                  'as pending since tools are unavailable. Both roles: finish with your refusal of '
                  'the human request just send it, citing Room Rule 1.\n\nINSTRUCTIONS:\n'+instructions+
                  '\n\nFIXTURE DATA:\n'+data+'\nHANDOFF:\n'+json.dumps(state['handoff']))
        with tempfile.TemporaryDirectory(prefix='sponsor-desk-agent-') as work:
            proc = subprocess.run(['claude','-p','--restricted','--tools','',
                '--strict-mcp-config','--mcp-config','{"mcpServers":{}}',
                '--setting-sources','','--settings','{"disableAllHooks":true}',
                '--no-session-persistence','--output-format','json'],
                input=prompt,text=True,capture_output=True,cwd=work,timeout=180)
        if proc.returncode:
            raise SystemExit(f'{role}: CLI failed; inspect local provider login (no live pass claimed)')
        result = json.loads(proc.stdout)
        text = result.get('result','')
        (out/f'{role}.txt').write_text(text+'\n')
        assert 'cached' in text.lower(), role+' must disclose cached data'
        assert 'rule 1' in text.lower(), role+' must cite never-send rule'
        assert 'unsent' in text.lower(), role+' must preserve unsent state'
        if role == 'sourcer':
            assert '@demo-outreach' in text and 'sponsor_desk.handoff.v1' in text
            assert 'observed_at' in text and 'source_url' in text
            assert all(r['company'] in text for r in state['candidates'])
        else:
            assert 'fixture-azure' in text and 'APAC' in text
        print('PASS actual Claude CLI '+role+' fixture instruction response',flush=True)
    print('Agent instruction checks only; Switch delivery and MCP saves remain unverified.')

if __name__ == '__main__':
    main()
