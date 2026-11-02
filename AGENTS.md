# AGENTS.md

This repository holds two things:

- A Streamlit example app (`streamlit_app.py`, `requirements.txt`).
- The HyperVideo Man persona ecosystem (`hypervideo-man/`): a HyperFrames motion-video guru packaged for Claude Code, Claude Cowork, Claude.ai, ChatGPT, Codex and Microsoft 365 Copilot Cowork.

## HyperVideo Man skill

For any request about motion video, HyperFrames, HTML-to-video, video prompts, fixing a render, or coaching or auditing a film, use the `hypervideo-man` skill at `.agents/skills/hypervideo-man/SKILL.md` and follow it.

## Editing the ecosystem

- The canonical skill lives in `hypervideo-man/plugin/skills/hypervideo-man/`. `.agents/skills/hypervideo-man` and `.claude/skills/hypervideo-man` are symlinks to it. Edit the canonical folder only.
- After any change, run `python3 hypervideo-man/build.py`. It checks platform limits and rebuilds the packages in `hypervideo-man/dist/`. Commit the rebuilt packages with the change.
