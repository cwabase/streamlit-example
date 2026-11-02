#!/usr/bin/env python3
"""Validate and package the HyperVideo Man persona ecosystem for every platform.

Usage:
  python3 hypervideo-man/build.py                    check limits, then rebuild hypervideo-man/dist/
  python3 hypervideo-man/build.py check              check limits only
  python3 hypervideo-man/build.py install claude-code (--user | --project PATH) [--force]
  python3 hypervideo-man/build.py install codex       (--user | --project PATH) [--force]

Packages written to dist/:
  hypervideo-man-skill.zip       skill folder inside the zip: Claude.ai / Claude desktop skills upload, Codex
  hypervideo-man-skill-m365.zip  SKILL.md at the zip root: Microsoft 365 Copilot Cowork skill import
  hypervideo-man.plugin          plugin folder contents at the root: Claude Cowork plugin upload
  hypervideo-man-chat-kit.zip    instructions + flat knowledge files: Claude Project, ChatGPT GPT or
                                 Project, Microsoft 365 Copilot agent

Standard library only. Zips are deterministic: the same inputs give byte-identical files,
so rebuilding without content changes leaves git clean. Exit 0 = pass, 1 = a check failed.
"""
import argparse
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
PLUGIN = ROOT / 'plugin'
SKILL = PLUGIN / 'skills' / 'hypervideo-man'
PLATFORMS = ROOT / 'platforms'
DIST = ROOT / 'dist'
STAMP = (2026, 11, 2, 0, 0, 0)
IGNORED = {'__pycache__', '.DS_Store'}

# Platform limits. The skill description uses the Claude.ai upload limit (200), which is
# stricter than the Agent Skills spec (1,024), so one SKILL.md works everywhere.
LIMIT_NAME = 64
LIMIT_DESCRIPTION = 200
LIMIT_CLAUDE_PROJECT = 10_000   # Claude Projects custom instructions (kit budget)
LIMIT_GPT = 8_000               # ChatGPT GPT builder; Microsoft 365 Copilot agent instructions
LIMIT_GPT_DESCRIPTION = 300
LIMIT_MD_BYTES = 1_000_000      # Microsoft 365 Copilot Cowork, per .md file
LIMIT_KNOWLEDGE_FILES = 20      # ChatGPT GPT knowledge

INSTRUCTIONS = {
    '01_Project_Description.md': PLATFORMS / 'claude-ai' / '01_Project_Description.md',
    '02_Custom_Instructions.md': PLATFORMS / 'claude-ai' / '02_Custom_Instructions.md',
    '02b_ChatGPT_Instructions.md': PLATFORMS / 'chatgpt' / '02b_ChatGPT_Instructions.md',
    'GPT_CONFIG.md': PLATFORMS / 'chatgpt' / 'GPT_CONFIG.md',
}
SETUP_GUIDES = {
    'claude-ai.md': PLATFORMS / 'claude-ai' / 'README.md',
    'chatgpt.md': PLATFORMS / 'chatgpt' / 'README.md',
    'codex.md': PLATFORMS / 'codex' / 'README.md',
    'm365-copilot.md': PLATFORMS / 'm365-copilot' / 'README.md',
}
START_HERE = """# HyperVideo Man chat kit

Paste-and-upload files for chat platforms that take instructions plus knowledge files.

| Platform | Instructions field | Knowledge |
|---|---|---|
| Claude Project | instructions/02_Custom_Instructions.md (description: 01_Project_Description.md) | all files in knowledge/ |
| ChatGPT Custom GPT | instructions/02b_ChatGPT_Instructions.md (every field: GPT_CONFIG.md) | all files in knowledge/ |
| ChatGPT Project | instructions/02b_ChatGPT_Instructions.md | all files in knowledge/ |
| Microsoft 365 Copilot agent | instructions/02b_ChatGPT_Instructions.md | all files in knowledge/ |

Step-by-step guides for each platform are in setup/.
"""


def frontmatter(path):
    """Return (fields, problems) for a simple YAML frontmatter block."""
    text = path.read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not m:
        return {}, [f'{path}: no frontmatter block']
    fields, problems = {}, []
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(':')
        if not sep:
            problems.append(f'{path}: unreadable frontmatter line: {line!r}')
            continue
        value = value.strip()
        quoted = len(value) >= 2 and value[0] == value[-1] and value[0] in '"\''
        if quoted:
            value = value[1:-1]
        elif ': ' in value:
            problems.append(f'{path}: quote the value of "{key}" (it contains ": ")')
        fields[key.strip()] = value
    return fields, problems


def section(path, heading):
    text = path.read_text(encoding='utf-8')
    m = re.search(rf'^## {re.escape(heading)}\n+(.*?)(?=\n## |\Z)', text, re.S | re.M)
    return m.group(1).strip() if m else ''


def knowledge_files():
    return sorted((SKILL / 'references').glob('*.md')) + sorted((SKILL / 'scripts').glob('*.py'))


def check():
    errors, report = [], []

    fm, problems = frontmatter(SKILL / 'SKILL.md')
    errors += problems
    name, desc = fm.get('name', ''), fm.get('description', '')
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name) or len(name) > LIMIT_NAME:
        errors.append(f'skill name {name!r}: lowercase letters, digits and hyphens, at most {LIMIT_NAME}')
    if name != SKILL.name:
        errors.append(f'skill name {name!r} must match its folder {SKILL.name!r}')
    if any(word in name for word in ('anthropic', 'claude')):
        errors.append('skill name must not contain a reserved word (anthropic, claude)')
    if not desc or len(desc) > LIMIT_DESCRIPTION or '<' in desc or '>' in desc:
        errors.append(f'skill description: 1 to {LIMIT_DESCRIPTION} characters, no angle brackets (now {len(desc)})')
    report.append(('skill description', f'{len(desc)} / {LIMIT_DESCRIPTION} chars'))

    skill_text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
    for ref in sorted(set(re.findall(r'`((?:references|scripts)/[^`\s]+)', skill_text))):
        if not (SKILL / ref).is_file():
            errors.append(f'SKILL.md points to a missing file: {ref}')

    for label, path, limit in (
        ('Claude Project instructions', INSTRUCTIONS['02_Custom_Instructions.md'], LIMIT_CLAUDE_PROJECT),
        ('GPT / M365 agent instructions', INSTRUCTIONS['02b_ChatGPT_Instructions.md'], LIMIT_GPT),
    ):
        n = len(path.read_text(encoding='utf-8').rstrip('\n'))
        report.append((label, f'{n:,} / {limit:,} chars'))
        if n > limit:
            errors.append(f'{path.name}: {n:,} characters, limit {limit:,}')

    gpt_desc = section(INSTRUCTIONS['GPT_CONFIG.md'], 'Description')
    report.append(('GPT description', f'{len(gpt_desc)} / {LIMIT_GPT_DESCRIPTION} chars'))
    if not gpt_desc or len(gpt_desc) > LIMIT_GPT_DESCRIPTION:
        errors.append(f'GPT_CONFIG.md description: 1 to {LIMIT_GPT_DESCRIPTION} characters (now {len(gpt_desc)})')

    kfiles = knowledge_files()
    report.append(('knowledge files', f'{len(kfiles)} / {LIMIT_KNOWLEDGE_FILES}'))
    if len(kfiles) > LIMIT_KNOWLEDGE_FILES:
        errors.append(f'{len(kfiles)} knowledge files, ChatGPT allows {LIMIT_KNOWLEDGE_FILES}')
    biggest = max((p for p in SKILL.rglob('*.md')), key=lambda p: p.stat().st_size)
    report.append(('largest .md', f'{biggest.name} {biggest.stat().st_size:,} bytes'))
    if biggest.stat().st_size > LIMIT_MD_BYTES:
        errors.append(f'{biggest.name} exceeds {LIMIT_MD_BYTES:,} bytes (Copilot Cowork limit)')

    plugin = json.loads((PLUGIN / '.claude-plugin' / 'plugin.json').read_text(encoding='utf-8'))
    market = json.loads((REPO / '.claude-plugin' / 'marketplace.json').read_text(encoding='utf-8'))
    entry = next((p for p in market.get('plugins', []) if p.get('name') == plugin.get('name')), None)
    if not entry:
        errors.append('marketplace.json has no entry for the plugin')
    elif (REPO / entry['source']).resolve() != PLUGIN:
        errors.append(f'marketplace source {entry["source"]!r} does not point to {PLUGIN}')
    elif entry.get('version') != plugin.get('version'):
        errors.append('plugin.json and marketplace.json versions differ')
    for path in sorted((PLUGIN / 'commands').glob('*.md')) + sorted((PLUGIN / 'agents').glob('*.md')):
        fields, problems = frontmatter(path)
        errors += problems
        if not fields.get('description'):
            errors.append(f'{path.name}: missing description')

    for link in (REPO / '.claude' / 'skills' / 'hypervideo-man', REPO / '.agents' / 'skills' / 'hypervideo-man'):
        if link.exists() and link.resolve() != SKILL.resolve():
            errors.append(f'{link} does not resolve to the canonical skill folder')
        elif not link.exists():
            report.append((str(link.relative_to(REPO)), 'missing or unresolved symlink (warning)'))

    width = max(len(k) for k, _ in report)
    for k, v in report:
        print(f'  {k:<{width}}  {v}')
    return errors


def add_file(zf, src, arcname):
    info = zipfile.ZipInfo(arcname, STAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = (0o755 if src.suffix == '.py' else 0o644) << 16
    zf.writestr(info, src.read_bytes())


def add_text(zf, text, arcname):
    info = zipfile.ZipInfo(arcname, STAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    zf.writestr(info, text.encode('utf-8'))


def add_tree(zf, src, prefix):
    for path in sorted(src.rglob('*')):
        rel = path.relative_to(src)
        if path.is_file() and not IGNORED.intersection(rel.parts):
            add_file(zf, path, prefix + rel.as_posix())


def build():
    DIST.mkdir(exist_ok=True)
    outputs = []

    def package(filename, fill):
        target = DIST / filename
        with zipfile.ZipFile(target, 'w') as zf:
            fill(zf)
        outputs.append(target)

    package('hypervideo-man-skill.zip', lambda zf: add_tree(zf, SKILL, 'hypervideo-man/'))
    package('hypervideo-man-skill-m365.zip', lambda zf: add_tree(zf, SKILL, ''))
    package('hypervideo-man.plugin', lambda zf: add_tree(zf, PLUGIN, ''))

    def chat_kit(zf):
        add_text(zf, START_HERE, 'START_HERE.md')
        for arcname, src in INSTRUCTIONS.items():
            add_file(zf, src, f'instructions/{arcname}')
        for src in knowledge_files():
            add_file(zf, src, f'knowledge/{src.name}')
        for arcname, src in SETUP_GUIDES.items():
            add_file(zf, src, f'setup/{arcname}')
    package('hypervideo-man-chat-kit.zip', chat_kit)

    for target in outputs:
        with zipfile.ZipFile(target) as zf:
            count = len(zf.namelist())
        print(f'  {target.relative_to(REPO)}  {target.stat().st_size:,} bytes, {count} files')


def install(target, user, project, force):
    folder = '.claude/skills' if target == 'claude-code' else '.agents/skills'
    base = Path.home() / folder if user else Path(project).expanduser().resolve() / folder
    dest = base / SKILL.name
    if dest.exists() or dest.is_symlink():
        if not force:
            sys.exit(f'{dest} already exists. Re-run with --force to replace it.')
        if dest.is_symlink() or dest.is_file():
            dest.unlink()
        else:
            shutil.rmtree(dest)
    base.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SKILL, dest, ignore=shutil.ignore_patterns(*IGNORED, '*.pyc'))
    print(f'Installed {SKILL.name} into {dest}')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command')
    sub.add_parser('check', help='check platform limits only')
    sub.add_parser('build', help='check, then rebuild dist/ (default)')
    inst = sub.add_parser('install', help='copy the skill into a Claude Code or Codex skills folder')
    inst.add_argument('target', choices=['claude-code', 'codex'])
    where = inst.add_mutually_exclusive_group(required=True)
    where.add_argument('--user', action='store_true', help='install for your user account')
    where.add_argument('--project', metavar='PATH', help='install into one project')
    inst.add_argument('--force', action='store_true', help='replace an existing copy')
    args = parser.parse_args()

    if args.command == 'install':
        install(args.target, args.user, args.project, args.force)
        return 0
    print('Checks')
    errors = check()
    if errors:
        print('\nFAILED')
        for e in errors:
            print(f'  - {e}')
        return 1
    print('  all checks pass')
    if args.command != 'check':
        print('Packages')
        build()
    return 0


if __name__ == '__main__':
    sys.exit(main())
