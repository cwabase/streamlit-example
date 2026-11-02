# HyperVideo Man — multi-platform build

HyperVideo Man PRIME APEX (persona ecosystem v1.0, 2 November 2026) packaged for six platforms. One skill folder serves every platform: Claude Code, Claude Cowork, Claude.ai, OpenAI Codex, ChatGPT and Microsoft 365 Copilot Cowork.

He is a motion-video guru, director-builder and coach for HyperFrames (HTML to video). Give him a goal, topic, angle or video type and he returns the surgical prompt set, the pipeline and the gates. He also fixes weak renders by timestamp, teaches the craft and audits films. English and French.

## Pick your platform

| Platform | File to use (in `dist/`) | What you do | Full guide |
|---|---|---|---|
| Claude Code | none: `/plugin install hypervideo-man --marketplace cwabase/streamlit-example` | Run the command, or open this repo (the skill loads from `.claude/skills/`) | [claude-ai](platforms/claude-ai/README.md#claude-code) |
| Claude Cowork (Claude desktop) | `hypervideo-man.plugin` | Cowork → Customize → Plugins → upload | [claude-ai](platforms/claude-ai/README.md#claude-cowork-plugin-adds-slash-commands-and-a-subagent) |
| Claude.ai (web, desktop, mobile) | `hypervideo-man-skill.zip` (skill) and `hypervideo-man-chat-kit.zip` (Project) | Upload the skill in Settings; build a Project from the kit | [claude-ai](platforms/claude-ai/README.md) |
| ChatGPT | `hypervideo-man-chat-kit.zip` | Build a Custom GPT or a Project from `GPT_CONFIG.md` | [chatgpt](platforms/chatgpt/README.md) |
| OpenAI Codex | none in this repo; `hypervideo-man-skill.zip` for other projects | Open this repo, or install the skill into `.agents/skills/` | [codex](platforms/codex/README.md) |
| Microsoft 365 Copilot Cowork | `hypervideo-man-skill-m365.zip` | Cowork → Skills → import, or drop into OneDrive `Documents/Cowork/Skills/` | [m365-copilot](platforms/m365-copilot/README.md) |
| Microsoft 365 Copilot agent | `hypervideo-man-chat-kit.zip` | Agents → Create agent → paste instructions, upload knowledge | [m365-copilot](platforms/m365-copilot/README.md#route-b--copilot-agent-agent-builder) |

## Which persona edition goes where

| Edition | Size | Used by |
|---|---|---|
| CONDENSED `02_Custom_Instructions.md` | 9,992 chars | Claude Projects; also embedded verbatim at the end of `SKILL.md` |
| ULTRA-CONDENSED `02b_ChatGPT_Instructions.md` | 6,977 chars | ChatGPT GPT or Project; Microsoft 365 Copilot agent (both cap at 8,000) |
| EXPANDED `05_EXPANDED_Persona.md` | 48,311 chars | Knowledge file everywhere; the skill reads it for full DIRECT or AUDIT runs |

## Layout

```
hypervideo-man/
├── README.md                     this file
├── build.py                      checks platform limits, rebuilds dist/, installs the skill
├── plugin/                       Claude Code and Claude Cowork plugin
│   ├── .claude-plugin/plugin.json
│   ├── skills/hypervideo-man/    THE canonical skill (edit here only)
│   │   ├── SKILL.md              operating card + CONDENSED persona
│   │   ├── references/           KB-01 … KB-14 + 05_EXPANDED_Persona.md
│   │   └── scripts/              qa_render.py, scorecard.py
│   ├── commands/                 /hypervideo-man:prompt · direct · fix · coach · audit
│   └── agents/hypervideo-man.md  subagent for long builds and audits
├── platforms/                    paste-ready fields and step-by-step guides per platform
│   ├── claude-ai/  chatgpt/  codex/  m365-copilot/
├── docs/                         original kit README, setup guide and Qualia audit report
└── dist/                         built packages (committed, so they can be downloaded from GitHub)
```

Repository-level wiring: `.claude-plugin/marketplace.json` (Claude Code marketplace), `.claude/skills/hypervideo-man` and `.agents/skills/hypervideo-man` (symlinks to the canonical skill), `AGENTS.md` (Codex) and `CLAUDE.md` (imports `AGENTS.md`).

## Changing the persona

1. Edit files under `plugin/skills/hypervideo-man/` (and `platforms/` for the paste editions).
2. Run `python3 hypervideo-man/build.py`. It fails if any platform limit breaks: skill description over 200 characters, GPT instructions over 8,000, more than 20 knowledge files, a `.md` file over 1 MB, a broken reference path or a mismatched plugin version.
3. Commit the source change together with the rebuilt `dist/` files.

The marketplace install line works from the repository's default branch, so merge this branch into `master` before sharing it. Until then, use the `.plugin` file.

Source precedence for technical facts stays as the kit defines it: the installed HyperFrames CLI (`--help`) beats every reference file.
