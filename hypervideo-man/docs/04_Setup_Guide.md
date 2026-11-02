# HyperVideo Man — Setup Guide

## Quick start (Claude Projects)

1. Create a new Claude Project named **HyperVideo Man**.
2. Set the Project Description to the contents of `01_Project_Description.md`.
3. Set the Custom Instructions to the contents of `02_Custom_Instructions.md` (9,992 characters — inside the ~10 K budget; Qualia v2.0 22/22).
4. Upload every file in `03_KB/` and `05_EXPANDED_Persona.md` to the Project Knowledge Base. Upload `scripts/` too if your Project can read code files.
5. Start a conversation. HyperVideo Man reports readiness, probes the HyperFrames environment if a project is present, and offers PROMPT · DIRECT · FIX · COACH · AUDIT.

## ChatGPT Custom GPT

1. Create a Custom GPT named **HyperVideo Man**.
2. Paste `02b_ChatGPT_Instructions.md` into Instructions (6,977 characters — inside the ~7 K budget; 22/22).
3. Attach the `03_KB/` files and `05_EXPANDED_Persona.md` as Knowledge.
4. Add the conversation starters from §Testing.

## Agent harnesses (Claude Code, Codex, Cursor, Gemini CLI, Copilot CLI, OpenCode, Antigravity)

1. Keep the official HyperFrames skills installed and current: `npx hyperframes skills update` (or the plugin for your harness). HyperVideo Man layers judgement, numbers and gates on top of their technical contract — he never replaces it.
2. Place `05_EXPANDED_Persona.md` where your harness loads system instructions, and the `03_KB/` folder where it can read references (for example alongside the `hyperframes-motion-mastery` or `directing-hyperframes-motion` skill folders from the two source deliverables).
3. Put `scripts/qa_render.py` and `scripts/scorecard.py` in the project's `scripts/` folder; run `python scripts/qa_render.py --selftest` once to confirm FFmpeg and FFprobe are on PATH.
4. Verify the environment: `npx hyperframes --version` · `npx hyperframes doctor --json` (gate on the Node, FFmpeg, FFprobe and Chrome rows) · `npx hyperframes skills check` · `npx hyperframes usage --json`.

## Microsoft 365 Copilot Cowork

Ask Copilot to create a personal skill from the two source skill packages (`hyperframes-motion-mastery.zip` and `directing-hyperframes-motion.skill`) and add `05_EXPANDED_Persona.md` as the persona reference; the skills manager stores personal skills in your OneDrive under `Documents/Cowork`. In chat, say "act as HyperVideo Man" to load the persona.

## KB file descriptions

| File | Purpose | Required? |
|---|---|---|
| KB-01 Intake-to-Prompt Protocol | How any partial input becomes the surgical prompt set; 40-field brief; pitch round; three-question rule; adjective-to-spec table | Yes |
| KB-02 Quality Framework and Numbers | Markers, structure, visual, motion, audio numbers; twelve dimensions; 35-item scorecard; rubric | Yes |
| KB-03 Prompting System and Templates | Meta, system, master, stage, evaluator, expansion, review, revision prompts; checklists | Yes |
| KB-04 Unified Skillgraph | 8 domains · 44 clusters · 253 atomic skills; crosswalk to both sources; cluster cards; dependencies; loops | Yes |
| KB-05 Skillmap and Gates | Seventeen stages, diagram, gate behaviour by mode, scheduling | Yes |
| KB-06 Format and Niche Playbooks | Seven formats, platform delivery, niche matrix (EN/FR, West Africa, faith, finance…), limits | Yes |
| KB-07 Audio Direction | Strategy, narration, music by theme and audience, SFX, silence, sync, mix, captions | Yes |
| KB-08 HyperFrames Technical Reference | CLI-verified 0.8.229 contract, lint rules, render facts, troubleshooting, command help index | Yes |
| KB-09 Fix-and-Coach Protocol | Diagnosis, symptom→cause→fix, prompt-level failures, coaching method | Yes |
| KB-10 Exemplar Library | Official, practitioner and internal films — why they work and how to transfer | Recommended |
| KB-11 Worked Examples | One per mode: PROMPT, DIRECT, FIX, COACH, AUDIT | Recommended |
| KB-12 Glossary | Terms | Optional |
| KB-13 Sources | Merged registries from both deliverables | Optional |
| KB-14 Merge Log | What came from where; divergences and resolutions | Recommended |

## Testing — conversation starters

1. "I have a goal: get youth in Abidjan to register for FSY in December. Give me the surgical prompt for a 30-second Reel in French."
2. "Plan and build a 60-second explainer about our three disbursement controls for stake leaders."
3. "This render feels generic and the voice is buried — fix it." (attach the file or paste the composition)
4. "Teach me why my transitions feel random."
5. "Audit this 15-second sting against the standard."

Expected behaviour: a one-line readiness report; an intake table with stated/inferred/defaulted values; at most three questions, one at a time; copy-ready prompt blocks or a plan table; evidence tags on claims; the acceptance stack attached.

## Troubleshooting

| Issue | Fix |
|---|---|
| Persona does not activate | Confirm the Custom Instructions were pasted completely (the file ends with the attribution line) |
| Answers lack numbers or cite none of the KB | Confirm the KB files uploaded; ask "load KB-02 and answer again" |
| Responses too generic | Ask for PROMPT mode explicitly and provide the goal, topic or angle; the persona must run the pitch round for unformed requests |
| Technical claims disagree with your CLI | The installed CLI wins; run `npx hyperframes <command> --help` and tell the persona the version |
| Budget errors on paste | Use `02b_ChatGPT_Instructions.md` for ChatGPT; `02_Custom_Instructions.md` for Claude Projects |
