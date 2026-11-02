# Microsoft 365 Copilot setup

Copilot Cowork is the main route: it runs HyperVideo Man as a skill with all 15 reference files and the two scripts. The Copilot agent route is a lighter option for plain Copilot chat.

Your admin must turn Cowork on for your account before Route A works.

## Route A — Copilot Cowork skill (recommended)

Option 1, upload:

1. Download `hypervideo-man/dist/hypervideo-man-skill-m365.zip`. This zip has `SKILL.md` at its root, which is what Cowork expects.
2. In Copilot, open Cowork → Skills → import a skill, and choose the zip.

Option 2, OneDrive folder:

1. Unzip `hypervideo-man-skill-m365.zip`.
2. In OneDrive, open `Documents/Cowork/Skills/`, create a folder named `hypervideo-man`, and upload `SKILL.md`, the `references/` folder and the `scripts/` folder into it.

Either way, Cowork picks the skill up at the start of the next conversation. Ask for a motion video, or say "act as HyperVideo Man". Each `.md` file must stay under 1 MB; the largest reference file is about 85 KB.

## Route B — Copilot agent (Agent Builder)

1. In Microsoft 365 Copilot, open Agents → Create agent → Configure.
2. Name: HyperVideo Man. Description: copy it from `../chatgpt/GPT_CONFIG.md`.
3. Instructions: paste `instructions/02b_ChatGPT_Instructions.md` from `hypervideo-man-chat-kit.zip` (6,977 characters; the agent instruction limit is 8,000).
4. Knowledge: upload the files in `knowledge/`, or point the agent at the OneDrive folder from Route A, option 2.
5. Starter prompts: use the five in `../chatgpt/GPT_CONFIG.md`.
