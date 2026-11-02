# OpenAI Codex setup (CLI, IDE extension and cloud)

Codex loads skills from `.agents/skills/<name>/SKILL.md` in the repository and from `~/.agents/skills/` for the user.

## In this repository

Already wired. `AGENTS.md` points Codex to the skill, and `.agents/skills/hypervideo-man` links to the canonical skill folder. Open the repository in Codex and either describe the video task or mention the skill directly with `$hypervideo-man`.

## In another project

From a clone of this repository:

```bash
# one project
python3 hypervideo-man/build.py install codex --project /path/to/your/project
# every project for your user account
python3 hypervideo-man/build.py install codex --user
```

Without a clone: unzip `hypervideo-man/dist/hypervideo-man-skill.zip` into `<project>/.agents/skills/` (the zip already holds the `hypervideo-man/` folder).

Then add the lines in `AGENTS.snippet.md` to that project's `AGENTS.md`, so Codex reaches for the skill on motion-video work without being asked.

## Build tools

For DIRECT builds Codex needs Node, FFmpeg, FFprobe and Chrome. Check with `npx hyperframes doctor --json` and `python3 .agents/skills/hypervideo-man/scripts/qa_render.py --selftest`. Keep the official HyperFrames skills current with `npx hyperframes skills update`; HyperVideo Man sits on top of them and never replaces their technical contract.
