# KB-01 — Intake-to-Prompt Protocol: from any one thing to the surgical prompt

*New synthesis for HyperVideo Man (merges the intent layer of the official HyperFrames skills, the 40-field brief schema from source B, and the 12-field prompt requirements and three-layer prompt system from source A).*

## 1. What the protocol guarantees

A user may arrive with a **goal** ("get youth to register"), a **topic** ("fast-offering controls"), an **angle** ("walk with me"), a **video type** ("a 30-second Reel"), an **audience**, a **platform**, a **length**, a **language**, **assets**, a **tone** — or only one of these. HyperVideo Man derives every other field, tags each value **stated / inferred / defaulted** with its receipt, asks **at most three** questions (one at a time, recommended option first), and returns a prompt set that a smart LLM can execute **without guessing**. The output is always complete: a missing fact becomes a labelled placeholder, never an invention.

## 2. The derivation order (run top to bottom)

| Step | Derive | From | Default when silent |
|---|---|---|---|
| 0 | **Mode** (PROMPT · DIRECT · FIX · COACH · AUDIT) and **project state** | Verbs in the request; presence of a project / BRIEF.md / render | PROMPT for "give me a prompt"; DIRECT for "make"; FIX for "it feels…/broken"; COACH for "why/how"; AUDIT for "score/review" |
| 1 | **Objective** = the viewer change | Goal words: understand · trust · register · buy · remember · act | Infer from type (promo → act; explainer → understand) |
| 2 | **Audience** (who, prior knowledge, language, device, sound state, culture) | Platform, topic, named group, user's language | Infer; ask only if a different answer changes the story or terminology |
| 3 | **Message** — one sentence, outcome language, ≤ 12 words | Goal + topic + angle | Derive, echo, confirm; never storyboard before it exists |
| 4 | **Destination → aspect** | Platform named or implied | Feed 1080×1080 · Reels/TikTok/Shorts 1080×1920 · YouTube/web/screen 1920×1080; state the derivation |
| 5 | **Length** | Type, material, platform | Route band with reason (social 7–30 s; promo 15–60 s; demo/explainer/brand 30–90 s; education 2–10 min); the voice decides the final duration |
| 6 | **Video type → playbook → route** | Deliverable, not a word in passing | Custom or > ~3 min → `/general-video` |
| 7 | **Concept** (formed vs unformed) | Does the request already shape the telling? | Unformed → pitch round (§4); formed → confirm |
| 8 | **Visual system** | Brand truth (frame.md / site / Figma) or preset by eye | House style with reasons; never an invented brand |
| 9 | **Audio** | Music decision rule; narration need; SFX style | Instrumental under voice; captions on for feeds |
| 10 | **Technical** | Installed version/skills/usage; credentials | Probe and report; never assume a flag |
| 11 | **Outputs** | Variants requested | MP4 H.264 1080p30 AAC + SRT + stems + assumptions list |
| 12 | **Acceptance** | — | Hard gates + 35-item checklist + 12-dimension rubric |
| 13 | **Integration check** | All of the above | Name the consequence no single answer showed; propose the adjustment |

## 3. The 40-field brief (canonical schema, from source B; A's twelve prompt fields map onto it)

| # | Field | Policy | # | Field | Policy |
|---|---|---|---|---|---|
| 1 | Route / workflow | Derive | 21 | Negative list | Default list + user's |
| 2 | Run shape | Ask last, separately | 22 | Palette roles (hex) | From brand truth |
| 3 | Objective | Ask if unclear | 23 | Typography | Bundled or `@font-face` |
| 4 | Audience | Infer; ask if it changes the story | 24 | Layout and depth | Defaults |
| 5 | Message (≤ 12 words) | Derive, echo, confirm | 25 | Narrative (structure, rhythm, beats) | Recommend |
| 6 | CTA (words + URL + hold) | Ask | 26 | Special beats (hook, breather, callback, spectacle) | Default |
| 7 | Success measure | Default | 27 | Beat table | Director writes |
| 8 | Destination | Infer | 28 | Motion language | Defaults |
| 9 | Format (aspect, resolution, fps) | Derive | 29 | Motion assertions (`*.motion.json`) | Director writes |
| 10 | Length + tolerance | Recommend with reason | 30 | Audio layers present/absent | Ask if unclear |
| 11 | Language / locale | User's language | 31 | Narration (voice, pace, pauses, lock) | Default by format |
| 12 | Source material | Ask | 32 | Music (decision + reason, mode, brief, licence) | Decision rule |
| 13 | Claim ledger | Ask; block if unsourced | 33 | Effects (budget, palette, sync, silences) | Default band |
| 14 | Assets (path, role, rights) | Ask; never invent | 34 | Mix and loudness | Default |
| 15 | Brand truth | Ask if brand matters | 35 | Captions and access | On for social |
| 16 | Mandatories / prohibitions | Ask | 36 | Technical (determinism, fonts, registry, version, variables) | Invariant |
| 17 | Concept (pitch) | Pitch round if unformed | 37 | Output specs | Ask for variants |
| 18 | Tone and references (quality to borrow) | Ask or derive | 38 | Acceptance | Default |
| 19 | Specification level | Default: style tokens | 39 | Logistics (usage, credentials, deadline, budget) | Check `usage` |
| 20 | Differentiation anchor (logo removed; typical direction rejected) | Default | 40 | Assumptions log | Always |

A's twelve prompt fields (objective, audience, message, creative direction, visual system, narrative structure, scene requirements, motion language, audio direction, technical constraints, output specification, acceptance criteria) are fields 3, 4, 5, 17–21, 22–24, 25–27, 28–29, 30–35, 36, 37, 38.

## 4. The pitch round (for unformed requests) — official doctrine, kept verbatim in spirit

1. Ask what the user is already picturing; an existing idea becomes one pitch and is never displaced.
2. Internally answer four questions: what does the subject look like; what does the target emotion look like as a frame; what does the playback surface demand; what does every other video on this subject look like (the anti-pattern).
3. Generate five concepts from five paths — the subject's world · the emotion · the audience (meet or break expectation) · the anti-pattern inverted · an unusual format (a letter, a countdown, a recipe, a front page, a map). At least two must sit below a 0.10 probability of being the median output; two concepts with the same silhouette are one concept.
4. Present each in three lines (concept · visual world with the one or two capabilities it rides, in plain language · opening hook). Show all five, then recommend one with a reason. Mixing is a first-class answer. One round.
5. The chosen concept answers `message` and `angle` and lands in `BRIEF.md § Intent`.

In autonomous mode, walk the same gate silently and report the pick, the typical direction left behind and the machinery it rides.

## 5. The three questions — how to choose them

Ask only when the answer **changes the route, the concept or the deliverable** and cannot be looked up. Candidates, in priority order: (1) the message if two readings of the goal lead to different films; (2) the destination if it changes aspect or type scale; (3) sell-or-show for product sites; (4) the CTA's exact words and URL; (5) rights or a credential that blocks a required capability; (6) run shape (storyboard first? collaborative or autonomous?) — asked last. Everything else is defaulted with a reason and logged. Factual fields take a numbered option list; creative fields take an anchored open question. Recommended option first, with its receipt.

## 6. Assembling the surgical prompt set (PROMPT mode output)

| Block | Contents | Length discipline |
|---|---|---|
| **Intake table** | field · value · stated/inferred/defaulted · receipt (40 rows or the subset that matters) | Table |
| **Questions** | ≤ 3, one at a time, recommended option first | Short |
| **META prompt** | How the executing LLM must work: probe `--version`/`skills check`/`usage`; evidence tags; ≤ 3 questions; work order; stops; reporting; never render without approval | ≈ 2–2.5 K characters (template in KB-03 §4.3.1) |
| **SYSTEM prompt** | The standard: story, structure, visual system, type, motion, contract, audio, gates, banned list | ≈ 5 K characters (KB-03 §4.3.2) |
| **MASTER prompt** | This film: project · source and facts · structure · visual system · motion · audio · technical · outputs · gates and acceptance — every bracket filled or labelled | ≈ 4–5 K characters (KB-03 §4.3.3) |
| **STAGE prompts** | plan · sketch · build · verify · refine · deliver (KB-03) | One line each |
| **EVALUATOR prompt** | A separate judge; evidence first, score second; pairwise comparisons; "Unknown" when evidence is missing | ≈ 1 K characters |
| **Pipeline & workflow** | The seventeen stages with the three user gates and six loops (KB-05) | Table |
| **Tips & angles** | The rejected typical direction; the signature move; the one spectacle beat; the hook type; the culture notes | Bullets |
| **Acceptance stack** | Hard gates → 35-item checklist → 12-dimension rubric with ship bar | Attached verbatim |

Rules: doctrine lives in the SYSTEM prompt, facts in the MASTER prompt — never duplicate; quote copy with "/" for line breaks; name real screens in order; hex + one display and one text face; a tempo where something changes on every beat; an explicit avoid-list; the ending; **restate every hard specification in full at every later turn**.

## 7. From adjective to specification (the translation table HyperVideo Man applies silently)

| The user says | HyperVideo Man writes |
|---|---|
| "cinematic" | 24 fps; eases 0.8–2 s; one key light with rack focus on the hero; 10–20 % vignette; 2–4 % grain; music with long phrases; one hold ≥ 1.5 s |
| "make it pop" | one accent at full saturation on focal elements; `expo.out` 0.25–0.35 s entrances; hard cuts on the beat; one shader into the hero; impacts −3 to −6 dB in gaps |
| "premium" | 55–60 % negative space; weights 300/900; tracking −0.04 em; 0.5–0.8 s; SFX ≤ 8/min, foley over whooshes; bed −18 dB |
| "fast-paced" | new visual every 1.5–3 s; stagger 40 ms; transitions 0.15–0.2 s; VO 2.6–3.0 w/s; captions 2–3 words per group |
| "trustworthy" | calm palette (cream or deep navy); no red alarms; numbers with units and sources; beatless music out under the facts; VO 2.2 w/s |
| "like Apple" | keynote register; short declaratives; silence between sentences; one object per frame; near-black or white canvas; a single material accent |
| "fun for teens" | hook in 1 s; 110–128 BPM; colour panels, one accent leads; `back.out(1.5)` on one element per scene; captions always |
| "explain it simply" | one idea per frame; ≤ 7 words on screen; a metaphor mined from the source; music off during the mechanism; hold ≥ max(1.5 s, 0.5 + 0.4 s × words) |
| "use my brand" | not a specification — extract tokens from the brand files, site or Figma; quote hex and faces verbatim; record what is locked vs scalable |
| "for everyone" | not an audience — name the primary viewer, device and sound state; design the sound-off path first |

## 8. Worked micro-intakes

- **"A video about our audit findings."** Mode DIRECT or PROMPT (ask: prompt or build?) · Objective: adoption of controls · Audience: volunteer leaders, mixed expertise, LinkedIn + internal screens → captions on · Message: "Three controls prevent most disbursement losses" · 1920×1080, 60 s · Explainer → `/faceless-explainer` or `/general-video` · Formed (the findings shape the story) · `blue-professional` remix · Music: findings → beatless bed −22 dB, out under the figures · Questions: (1) exact CTA? (2) may names appear? · Integration check: a table of five categories will not read at 60 s — three metrics per frame.
- **"FSY, December, youth, Reels."** PROMPT · Objective: registration · Youth 14–18, phone, sound-off · Message: "FSY is where you walk with the Saviour and with friends who walk the same way" · 1080×1920 (+16:9 cut-down), 30 s · Promo → `/general-video` with variables for date/venue/URL · Formed by theme; pitch optional · Light canvas made cinematic, gold accent, Archivo Black + Montserrat · Music: cinematic-pop build 110–120 BPM, silence before scripture, Church standards · Questions: (1) date and venue (placeholder otherwise) · Culture: French VO at 2.2 w/s; captions mandatory.
- **"It feels generic."** FIX · Watch three ways; freeze three frames; scrub cuts; read lint/check/strips; diagnosis table; weakest scene first; revisions by timestamp (KB-09).
