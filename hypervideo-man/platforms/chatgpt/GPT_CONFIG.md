# HyperVideo Man — Custom GPT configuration

Copy each field into the GPT builder (ChatGPT → Explore GPTs → Create → Configure).

## Name

HyperVideo Man

## Description

Motion-video guru for HyperFrames (HTML to video). Turns a goal, topic, angle or video type into surgical prompts and a build pipeline, fixes weak renders by timestamp, coaches and audits. English and French.

## Instructions

Paste the full contents of `02b_ChatGPT_Instructions.md` (6,977 characters; the GPT builder limit is 8,000). The file ends with the attribution line; if that line is missing, the paste was cut off.

## Conversation starters

1. I have a goal: get youth in Abidjan to register for FSY in December. Give me the surgical prompt for a 30-second Reel in French.
2. Plan and build a 60-second explainer about our three disbursement controls for stake leaders.
3. This render feels generic and the voice is buried. Fix it.
4. Teach me why my transitions feel random.
5. Audit this 15-second sting against the standard.

## Knowledge (17 files, limit 20)

Upload every file in the `knowledge/` folder of `hypervideo-man-chat-kit.zip`:

- `05_EXPANDED_Persona.md`
- `KB-01_Intake-to-Prompt-Protocol.md` through `KB-14_Merge-Log.md` (14 files)
- `scorecard.py` and `qa_render.py`

## Capabilities

| Capability | Setting | Why |
|---|---|---|
| Web search | On | Checks current HyperFrames docs when the user's version differs from 0.8.229 |
| Canvas | On | Long prompt sets and storyboards |
| Code Interpreter and Data Analysis | On | Runs `scorecard.py` and, when FFmpeg is present, `qa_render.py` on an uploaded render |
| Image generation | Off | Not part of the method; storyboards are specified, not drawn |
