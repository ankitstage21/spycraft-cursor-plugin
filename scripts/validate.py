#!/usr/bin/env python3
"""Dependency-free static checks; does not authenticate or call Spycraft."""
import json
import re
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
failures = []
checks = []

def check(ok, label):
    (checks if ok else failures).append(label)

try:
    manifest = json.loads((root / '.cursor-plugin/plugin.json').read_text())
    check(bool(re.fullmatch(r'[a-z0-9]+(?:[.-][a-z0-9]+)*', manifest['name'])), 'Plugin identifier')
    check(bool(re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])), 'Semantic version')
    check(bool(manifest.get('description')) and bool(manifest.get('author', {}).get('name')), 'Description and author')
    for field in ('skills', 'mcpServers', 'logo'):
        value = manifest[field]
        check(not Path(value).is_absolute() and '..' not in Path(value).parts and (root / value).exists(), f'Relative {field} path')
    mcp = json.loads((root / manifest['mcpServers']).read_text())
    check(mcp == {'mcpServers': {'spycraft': {'url': 'https://mcp.spycraft.co/mcp'}}}, 'Remote OAuth config without embedded credentials')
    skills = sorted((root / manifest['skills']).glob('*/SKILL.md'))
    check(len(skills) == 5, 'Five discovered skills')
    names = set()
    catalog = json.loads((root / 'docs/source-tools.json').read_text())
    source_tools = {tool['name'] for tool in catalog['tools']}
    for skill in skills:
        content = skill.read_text()
        fm = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n', content)
        check(bool(fm) and fm[1] == skill.parent.name and fm[1] not in names, f'{skill.parent.name} frontmatter')
        if fm:
            names.add(fm[1])
        check('../../docs/OPERATING-CONTRACT.md' in content and (skill.parent / '../../docs/OPERATING-CONTRACT.md').is_file(), f'{skill.parent.name} shared contract')
        for name in re.findall(r'`([a-z]+(?:_[a-z]+)+)`', content):
            if name not in {'page_id', 'run_id', 'not_followed', 'poll_after_seconds'}:
                check(name in source_tools, f'{skill.parent.name} tool exists in source: {name}')
    svg = ET.parse(root / manifest['logo']).getroot()
    check(svg.tag.endswith('svg'), 'Logo SVG parses')
    check(not any(el.tag.endswith('script') or any(k.rsplit('}', 1)[-1].lower().startswith('on') for k in el.attrib) for el in svg.iter()), 'Logo has no script/event attributes')
    check(not any(p.name.startswith('.env') for p in root.rglob('*')), 'No environment files bundled')
    check(all((root / p).is_file() for p in ['README.md', 'LICENSE', 'docs/SUBMISSION.md', 'docs/VERIFICATION.md', 'docs/OPERATING-CONTRACT.md']), 'Usage, license, submission and evidence docs')
except (KeyError, ValueError, OSError, ET.ParseError) as exc:
    failures.append(str(exc))

for failure in failures:
    print('FAIL:', failure)
print(f'{len(checks)} static checks passed; {len(failures)} failed.')
print('Authenticated client discovery, OAuth login, and data calls remain UNVERIFIED.')
sys.exit(bool(failures))
