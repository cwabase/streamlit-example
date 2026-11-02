# HyperVideo Man plugin (Claude Code and Claude Cowork)

HyperVideo Man PRIME APEX is a motion-video guru, director-builder and coach for HyperFrames (HTML to video). Give him a goal, topic, angle or video type and he returns the surgical prompt set, pipeline and gates. He also fixes weak renders by timestamp, teaches the craft and audits films. English and French.

## What is inside

| Part | Use |
|---|---|
| `skills/hypervideo-man/` | The persona, operating card, 15 reference files and 2 QA scripts. Loads automatically on motion-video requests. |
| `commands/` | `/hypervideo-man:prompt`, `:direct`, `:fix`, `:coach`, `:audit` start a mode directly. |
| `agents/hypervideo-man.md` | Subagent for long DIRECT builds or AUDIT passes. |

## Install

Claude Code (2.1.275 or later): `/plugin install hypervideo-man --marketplace cwabase/streamlit-example`

Claude Cowork: upload `hypervideo-man/dist/hypervideo-man.plugin`.

## Setup for builds

Node, FFmpeg, FFprobe and Chrome on PATH. Check with `npx hyperframes doctor --json`, then `python3 skills/hypervideo-man/scripts/qa_render.py --selftest`.
