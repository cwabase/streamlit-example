# Claude.ai setup (web, desktop and mobile)

Use both routes. The skill makes HyperVideo Man available in every chat and in Claude Cowork; the Project gives a focused workspace with the full knowledge base loaded.

## Route A — Skill (every chat, Claude desktop and Cowork)

Needs a Pro, Max, Team or Enterprise plan with code execution turned on.

1. Download `hypervideo-man/dist/hypervideo-man-skill.zip`. Do not unzip it.
2. In Claude, open Settings → Capabilities → Skills (some plans label the page Features) → Upload skill, and choose the zip.
3. Turn the skill on. In any new chat, ask for a motion video, or say "use HyperVideo Man".

## Route B — Project

1. Download `hypervideo-man/dist/hypervideo-man-chat-kit.zip` and unzip it.
2. Create a Project named HyperVideo Man.
3. Description: paste `instructions/01_Project_Description.md`.
4. Instructions: paste `instructions/02_Custom_Instructions.md` (9,992 characters). The file ends with the attribution line; if that line is missing, the paste was cut off.
5. Knowledge: upload all 17 files from `knowledge/`.
6. Start a chat. HyperVideo Man reports readiness and offers PROMPT · DIRECT · FIX · COACH · AUDIT.

## Claude Cowork plugin (adds slash commands and a subagent)

In Claude desktop, open Cowork → Customize → Plugins → upload `hypervideo-man/dist/hypervideo-man.plugin`. You get `/hypervideo-man:prompt`, `:direct`, `:fix`, `:coach` and `:audit` on top of the skill.

## Claude Code

`/plugin install hypervideo-man --marketplace cwabase/streamlit-example` (Claude Code 2.1.275 or later). Opening this repository in Claude Code also loads the skill straight from `.claude/skills/hypervideo-man`.
