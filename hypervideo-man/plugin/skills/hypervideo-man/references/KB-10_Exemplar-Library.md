# KB-10 — Exemplar Library: why strong films work and how to transfer the technique

*Composite. Part I is Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026) §3.8: HeyGen's launch film, the "$1.9T" beat, Linear.app, Social SDK and JetBrains, OneWave, and three internal productions ("The Price of AI", "Marche avec moi", "Journal IA, semaine 42"), with what the strongest demos share. Part II is Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229) §3.2: eight films analysed frame by frame, each with the transferable technique. Part III is B's research note on practice and exemplars: ten exemplar deep dives and the cross-exemplar craft patterns (story architectures, pacing benchmarks, typography, colour, motion, audio, endings). No film was watched by HyperVideo Man himself — every claim carries the analysis it rests on.*

*Section numbers inside each part keep the numbering of the source they came from (A = §2–§7 and appendices of the Skillgraph document; B = Parts 3–8 of the Claude Code document). Where the two parts disagree, the preface and KB-14 govern; where either disagrees with the installed CLI, the CLI wins.*

## 0. How to use an exemplar

Name the quality to borrow, never the look: "the restraint of the launch film's silent beats", "OneWave's one-accent discipline", "the Herk reel's cut-to-grid precision". Transfer the technique (a structure, a timing, a level, a transition rule), then re-derive it from this film's message and audience. An exemplar's weak spots (machine-regular typing, lists scrolling too fast, UI text too small for phones, dense square frames) are rubric evidence, not permission.

## Part I — Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026)

#### 3.8 Exemplar analyses — why strong HyperFrames films succeed

Each analysis names the technique and how to transfer it. Tags state what is documented versus demonstrated; full citations in §2.11.

##### 3.8.1 HeyGen's launch film, "Go make something" — [Demonstrated] public source repo `heygen-com/hyperframes-launches` (HANDOFF dated 2026-04-15)

**What it does.** 49.77 s at 1920×1080, 30 fps; one root and 17 sub-compositions; `STORYBOARD.md`, `SCRIPT.md` and `HANDOFF.md` alongside. The storyboard directs a cold open ("camera is already moving… No fade in. No preamble"), narration in an "Apple keynote presenter register" where "silence between sentences is a feature", a 14-second "flex" montage in which "each world should feel like it was made by a different designer in a different decade" cut with hard smash cuts, per-beat SFX motifs, and an underscore "already playing when the video starts". Proof beats ("Byte-identical" diff) replace adjectives. The narration reproduced in narration.md (~140 words) is the team reference for this film at 2.3 w/s. **Why it works.** Reverse iceberg in miniature; every sentence is a frame's worth of content; the montage's variety is the *argument* (anything a browser renders can be a frame), so the hard cuts are meaning, not laziness; the HANDOFF documents the fix for black flashes between beats (pad sub-timelines to their slot) — craft includes the post-mortem. **Transfer.** Write the script as frame-sized statements and count words against runtime; make the last line the lock-up; keep a HANDOFF.md of every fix so the next build inherits it. Two durations are quoted in sources (49.77 s in the repo, "62-second" in narration.md) — treat the repo as authoritative.

##### 3.8.2 The "$1.9T" beat — [Documented] beat-direction.md § Per-beat direction

**What it does.** The documented contrast between a mediocre direction ("Dark navy background. '$1.9T' in white, 280 px.") and a great one ("Camera is already mid-flight over a vast dark canvas … '$1.9T' SLAMS into existence with such force the wave ripples in response") is a lesson in direction. **Why it works.** The great version describes an *experience* with cause-and-effect physics (the slam makes the wave ripple), which forces a reactive secondary motion, a hero SFX and a light hit to be designed together. **Transfer.** Write each beat's concept as an experience first, then derive pixels, verbs, SFX and light from it.

##### 3.8.3 Linear.app launch, 45 s — [Documented] official prompting guide, "rendered from the prompt above, unedited"

**What it does.** The published prompt names the structure (hook → three feature beats with UI captures and one-line captions → end card with logo and CTA), the palette source (the product's site), the voice's gender and tone, a BGM ceiling (−18 dB), the length and the aspect. **Why it works.** Every lever an LLM would otherwise default is pinned; the brief is a production contract. **Transfer.** The master prompt in §4 is built on exactly this logic: specify structure, palette source, voice, music ceiling, length and aspect — and the avoid-list.

##### 3.8.4 Social SDK launch, 56 s (Leo, >120 K views on X) and JetBrains' Kotlin promo, 35 s — [Demonstrated, reported via working-ref, 2026-10]

**What they do.** Leo's rule — "DO NOT LET THE AGENT CHOOSE WHAT TO PUT. I told specifically about each part" — plus giving the agent the codebase and a component library of animations; JetBrains' film was "generated entirely by Claude Opus 5.5" with the HyperFrames skill pointed at kotlinlang.org. **Why they work.** Direction over delegation: real screens in order, brand tokens from the real site, a first scene chosen by a human. **Transfer.** Name 3–5 real screens in order; give the agent the landing page as the reference; approve the first scene before anything else.

##### 3.8.5 OneWave's 44-second hero clip and 73-second explainer — [Demonstrated] onewave-ai.com, 2026-09-04

**What they do.** A founder's phone-recorded voice, word-level transcription, lines cut to the beats; an HTML-built dashboard with an animated cursor instead of a screen recording; registry lower-third and film-grain blocks restyled to brand; three 9:16 podcast recuts generated from a script. **Why they work.** The product UI is crisp at any resolution because it is markup; the voice is real; every asset was restyled into one system. **Transfer.** Rebuild UI as HTML; transcribe to word level; restyle registry blocks rather than hand-build; script-generate variants.

##### 3.8.6 "The Price of AI" — Three.js + GLSL showreel, 2:27, English — [Demonstrated, internal production, Oct 2026]

**What it does.** Crisp CSS3D text over WebGL glass, metal and particle layers with a reflective floor; an Alphabet-$500B-drop headline as the hook; a verification loop on text size, overlap, frame edges, black or frozen frames and loudness. **Why it works.** Separating text (CSS3D, always sharp) from atmosphere (WebGL) kept legibility at compression while giving depth; the verification loop caught issues a lint pass cannot see. **Transfer.** Keep text out of the GPU texture path; render in 120-frame chunks when the environment can be lost; always run a frozen-frame and black-frame scan on the export. Capability limit: Three.js needs an explicit root `data-duration` because duration cannot be inferred [Documented] data-attributes.md; HeyGen's own film noted "GPU stall due to ReadPixels during the shader segment" and used a Canvas-2D fallback for headless Chrome [Demonstrated].

##### 3.8.7 "Marche avec moi" — 59 s French FSY promo, 16:9 — [Demonstrated, internal production, Oct 2026]

**What it does.** The 2026 youth theme (Moses 6:34) carried by AI voice, original music and AI imagery; "very intense motion graphics modelled on a Spotify AI DJ reel". **Why it works.** The theme line functions as the message and the button; music built hook → build → peak on the invitation → button, so cuts had a grid; captions and large type for sound-off feeds. **Transfer.** For faith-youth promos: cinematic-pop build 110–120 BPM, bed about −18 dB, silence before scripture, no drops mid-sentence; verify date and venue facts before build (they were not in the files — a labelled placeholder is the honest fallback).

##### 3.8.8 "Journal IA, semaine 42" — 11 min 50 s French long-form — [Demonstrated, internal production, Oct 2026]

**What it does.** A chaptered news-style essay with the author's own TTS voice, word-aligned captions, HTML/JS composition and a resumable render (~4 fps at 1080p on one CPU). **Why it works.** Chapters every 1.5–3 min with pattern interrupts kept a long piece watchable; a mandatory script-review stop (Word script + prompt + clean VO text) prevented narration rewrites after build; word-level alignment made captions exact. **Transfer.** Long-form = `/general-video` with a chapter plan, a locked script before TTS, and a render strategy that survives a lost environment (segments via `render --start/--end` [Documented, v0.8.222], checkpoints).

##### 3.8.9 What the strongest demos share — and what "AI slop" looks like

Across the sourced examples the recurring traits are: a first frame that is already composed; typography doing the work of imagery; one accent colour; motion that stops when text must be read; transitions as ideas rather than dissolves; and audio designed into the storyboard rather than added after. The failures that get called "AI-looking" are the inverse — Prompt Motion's data-backed banned list (glows/neon, template looks, particle bursts, long holds and dead time, crossfades everywhere, bouncy easing, gradients, gratuitous 3D, stock footage and UI kits, text in the corners, unseeded randomness); prompts carrying such avoid-lists scored a median of 56 likes against 7 overall [Demonstrated]. Tenex's verdict on a one-prompt Studio film — "it felt like AI slop… it just did generic work" — is the baseline this framework exists to beat.

## Part II — Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229)

### 3.2 Exemplars: why they work

The strongest public HyperFrames films are mostly HeyGen's own; independent creators mostly publish workflows and kits [DOC] [B-02] [DEMO] [B-28]. Seven were analysed frame by frame with Gemini video understanding (one call failed) [TESTED] [G-01]–[G-08]. Treat model-suggested techniques as candidates: two analyses recommended practices that break determinism [CONFLICT] [B-29].

| Film | Length / format | Why it works | Transferable technique |
|---|---|---|---|
| HyperFrames launch film (HeyGen) | 49.8 s, 16:9 | A ~110-word keynote voice-over as the spine, with two silent picture-only beats; builds synced to phrases; a montage where every cut is "a different designer in a different decade"; ends on the opening world [DOC] [B-07] [B-08] [B-09] | Write and cut the script first; give the montage its own rule and the rest one calm house style; bookend |
| Studio launch (HeyGen) | 30 s, 16:9 | Opens on a human deadline before any UI; the agent is a visible character doing the work; dark → light → dark value flips; one mint accent reserved for agent actions; ~3 s average shot [DEMO] [G-01] | Human stakes first; make the abstract actor visible; bind one accent to one meaning |
| "A launch video in 6 hours" (HeyGen) | 73 s, 16:9 | Problem act built from recognisable artifacts (file names, red-pen notes, a stuck progress bar), paced faster than the solution act; effects tied to on-screen actions; ~4 s end hold [DEMO] [G-02] | Pace pain faster than relief; close on a side-by-side delta, not a claim |
| "Storyboard first" (HeyGen) | 57 s, 16:9 | Deliberately slow, readable markup steps (~5.2 s shots); music turns from riser to groove on the "build" moment; a card-to-fullscreen context zoom [DEMO] [G-03] | Slow down where the viewer must read; land the music change on the narrative turn |
| "It's just HTML" (HeyGen) | 54.6 s, 16:9 | Five 1-second proofs of range with spec labels, then a slow annotated walkthrough, then a recap montage and an 8 s CTA hold; VO ~2.6 words/s [DEMO] [G-04] | Earn attention fast, then explain slowly; recap the hook to close the loop |
| "Claude Motion" (HeyGen) | 30.9 s, 1:1 | Container morphs keep spatial continuity; light app shells frame dark previews so content pops; the tool handoff is one clickable moment [DEMO] [G-05] | Halve UI density for square; show handoffs as a single visible action |
| Timeline Editor launch (HeyGen) | 33.8 s, 16:9 | A "word conveyor" intro, cut-the-curve seams with matched blur, documented production lessons (worker limits, video placement, WAV beds) [DOC] [B-12] | Document both sides of every seam; keep production notes |
| Nate Herk motion showreel | 15 s, 60 fps | One motif transformed through seven labelled chapters; cuts within 2 frames of a 129 BPM grid; one held-back color for the climax; bookend lockup [DEMO] [B-28] [B-31] | Encode sizzle grammar as a mode, never a default |

**Weak spots the analyses found** are just as instructive: machine-regular typing, an interpolation that snapped, lists scrolling too fast to read, UI text too small for phones, annotation clutter and dense square frames [DEMO] [G-01] [G-02] [G-04] [G-05]. Each maps to a rubric dimension below.

**Recurring story architectures** [DOC] [B-08] [DEMO] [G-02] [G-04] [G-07]: problem → solution contrast; hook → proof → payoff → brand; hook → explain → recap ("sandwich"); keynote voice-over with silent beats; motif transformation reel; character-as-agent.

## Part III — Source B research note: exemplars and cross-exemplar patterns

#### 3. Exemplar videos (strongest publicly available)

##### 3.1 Selection criteria

Chosen for public availability, documented provenance (made with HyperFrames), craft quality, and teaching value. I preferred pieces with source code or production notes. Seven are finished films; three are process exemplars (a public video showing the HyperFrames output and the loop that made it) [REC].

##### 3.2 Summary table

| # | Title | Creator | Date | Format | Length | Link | Analysis |
|---|---|---|---|---|---|---|---|
| E1 | HyperFrames launch film ("Go make something") | HeyGen | Apr 16–17, 2026 | 16:9, 1920×1080, 30 fps | 49.77 s | Source: https://github.com/heygen-com/hyperframes-launch-video | Docs only; no public MP4 located |
| E2 | Studio launch | HeyGen | ~Oct 2026 [UNVERIFIED] | 16:9 (card 1280×720) | 30.0 s | https://static.heygen.ai/hyperframes-oss/homepage/showcase/card/studio-launch-v1.mp4 | G-01 (frames only) |
| E3 | A launch video in 6 hours | HeyGen | undated | 16:9 (card 1280×720) | 73.0 s | https://static.heygen.ai/hyperframes-oss/homepage/showcase/card/studio-launch-pixel-v1.mp4 | G-02 |
| E4 | Storyboard first | HeyGen | undated | 16:9 (card 1280×720) | 57.05 s | https://static.heygen.ai/hyperframes-oss/homepage/showcase/card/launch-storyboard-first-v1.mp4 | G-03 |
| E5 | It's just HTML | HeyGen | undated | 16:9 (card 1280×720) | 54.57 s | https://static.heygen.ai/hyperframes-oss/homepage/showcase/card/just-html-v1.mp4 | G-04 |
| E6 | Claude Motion | HeyGen | undated | 1:1 (card 720×720) | 30.86 s | https://static.heygen.ai/hyperframes-oss/homepage/showcase/card/launch-claude-motion-v1.mp4 | G-05 |
| E7 | Timeline Editor launch v2 | HeyGen | 2026 | 16:9, 1920×1080 | 33.8 s | Source: https://github.com/heygen-com/hyperframes-launches/tree/main/timeline-launch | Docs only; viewer link dead |
| E8 | YouTube motion showreel | Nate Herk (built with his motion-showreel skill) | Sep 2026 | 16:9, 1920×1080, 60 fps | 15 s | https://github.com/user-attachments/assets/056b46e9-7379-4e71-b825-20fb9f8e9555 | G-06 failed; kit docs |
| E9 | "Claude Video Editing Just Became Unrecognizable" (process exemplar) | Nate Herk | Apr 23, 2026 | 16:9 | 28:13 | https://www.youtube.com/watch?v=Aw3BkmhYu4I | G-08 |
| E10 | Behind the Craft: Jake Moran (process exemplar) | Peter Yang, guest Jake Moran (HeyGen-affiliated) | Oct 25, 2026 | 16:9 | ~42 min [REC estimate] | https://www.youtube.com/watch?v=MC1g2fHYC88 | G-07 |

Sources for the table: E1 [DOC B-07, B-08, B-10]; E2–E6 durations and sizes measured from the official showcase MP4 metadata in the browser [DOC B-02]; E7 [DOC B-11, B-12]; E8 [DEMO B-28, B-31]; E9 [DEMO B-32, B-33]; E10 [DEMO B-35, B-36].

Caveats: showcase "card" files are 720p preview encodes, not necessarily masters [REC]. Creator credit and dates are not shown on homepage cards [DOC B-02] [UNVERIFIED].

##### 3.3 E1 — HyperFrames launch film (HeyGen)

**What it is.** It is the composition source for HeyGen's own launch video: a root `index.html` plus sub-compositions, using CSS animation, GSAP, Lottie, shaders, Three.js, footage, captions, and SFX. It has voiceover and SFX but no continuous music in the published render [DOC B-07]. Length and sub-composition counts differ across the documents. The README says 49.77 s and 17 sub-comps, the handoff says a 51.60 s master and 19 sub-comps, and the v3 storyboard header says a maximum of 60 s [DOC B-07, B-10, B-08] [CONFLICT]. Treat the README as describing the shipped state [REC].

**Story and script.** The v3 script is about 110 spoken words, down from about 140 in v2, delivered at a measured keynote pace. It has two silent picture-only beats: a roughly 3 s montage teaser and an A-roll creator beat [DOC B-09]. The v2→v3 change table shows editorial discipline. The cold open was rewritten, two beats were merged, the "flex" montage moved earlier and was reused as the teaser, the copy was corrected from "GSAP" to "JavaScript", the whole contrast beat was cut (about 6.4 s freed), and the CTA changed from CLI to skill [DOC B-09].

**Design principles in the storyboard.**
- The palette is chosen per beat.
- The look is light by default with brief dark departures.
- Every beat has at least one eye-drawing colour ("muted is fine; flat is not").
- Typography is distinct per beat.
- Motion errs toward more movement, because subtle motion reads as static at 30 fps.

[DOC B-08]

**Signature beats.**
- **Thesis line:** a staggered serif rise (y 24 px → 0, 0.4 s, power2.out), then a 101% scale pulse with a warm flash and a shutter click [DOC B-08].
- **"Flex" montage:** six hard smash cuts, each in a different palette, typeface, and visual language ("a different designer in a different decade") [DOC B-08].
- **Anatomy beat:** four builds, each synced to a spoken phrase with a four-note ascending chime [DOC B-08].
- **Close:** returns to the opening canvas as a bookend [DOC B-08].

**Audio.** VO at 1.0, underscore at 0.15, and one glockenspiel SFX at 0.2 timed to the words "sound effects", with its tail bleeding into the next shot [DOC B-10]. The handoff lists an underscore file, but the README says the render has no continuous music track [CONFLICT B-10 vs B-07].

**Document drift.** The fetched STORYBOARD.md still describes the "contrast" beat and the pre-rename "Hyperframe" naming that SCRIPT v3 removed. Read it as the planning stage, not the final cut [CONFLICT B-08 vs B-09].

**Production lessons.** See section 7. Black flashes came from timelines shorter than their slots; padding fixed them. Preview was silent until a user gesture (autoplay policy). There were float-precision gaps of 0.01 s at slot edges. The shader beat logged a "GPU stall due to ReadPixels" warning but the output was fine, and the close used Canvas 2D only to stay headless-safe [DOC B-10].

**Transferable techniques.** [REC from DOC B-08–B-10]
- Write and revise the VO script as the spine. Leave silent beats for picture.
- Give the montage a "different universe per cut" rule, and give the rest of the film one calm house style.
- Sync builds to phrases, one concept per phrase.
- Bookend: end on the opening world.

##### 3.4 E2 — Studio launch (HeyGen, 30 s)

**Arc.** A late-night live-action desk ("San Francisco 11:54 PM") opens the film. Then come a Slack ping, the app opening from the Dock, a typed launch prompt, and the green mascot reading a "Launch Videos for Dummies" book. The mascot builds a multi-track timeline, a preview expands to the full workspace, and the user draws a ring on the canvas and types "make this bigger" [DEMO·G-01].

**Craft.**
- Ten shots, average shot length (ASL) about 3.0 s, longest 5.5 s on the closing interaction [DEMO·G-01].
- A dark → white → dark value flip (dark UI, high-key mascot world, dark studio) [DEMO·G-01].
- A mint-green accent reserved for agent actions and selections [DEMO·G-01].
- Snappy overshoot on clicks and card placement, and directional motion blur on cuts [DEMO·G-01].
- **Audio:** G-01 used frames-only sampling, so its music/SFX claims are discarded [TESTED, section 15].

**Weak spots flagged.** Typing is uniformly machine-regular, and one text-scale change snaps instead of interpolating [DEMO·G-01].

**Transferable techniques.** [REC]
- Open on a human-stakes moment (a deadline) before any UI.
- Make the agent a visible character that physically does the work.
- End on the product's differentiator in use, not on a logo.

##### 3.5 E3 — "A launch video in 6 hours" (HeyGen, 73 s)

**Arc.** A problem-solution contrast film:
1. A "Without HyperFrames Studio" card, then a pain montage: tab sprawl, storyboard v1 → "v7 FINAL(2)" with red marks, keyframe-curve nudging, DAW beat alignment, and a render stuck at 4% while client messages arrive.
2. "6 hours. One video."
3. "With HyperFrames Studio": the agent builds, the user annotates, an "@Moments" preset repopulates the timeline, and export runs to 100%.
4. A split comparison: 6 hours alone vs 1 minute directing agents.
5. A brand hold.

[DEMO·G-02]

**Craft.**
- ASL about 2.2 s, frantic first act, a rest beat on the exhausted creator, then fluid acceleration [DEMO·G-02].
- A pixel-sprite character acts as the emotional surrogate [DEMO·G-02].
- The background is warm off-white with an iridescent sheen; mint marks success and coral/red marks pain [DEMO·G-02].
- About a 4 s end hold [DEMO·G-02].
- SFX are tied to on-screen actions: pencil scribble on red marks, a "plink" on clip insertion, a chime on 100% [DEMO·G-02].

**Weak spots.** An article list scrolls past too fast to read, and some UI text is too small for mobile [DEMO·G-02].

**Caution.** The "6 hours vs 1 minute" comparison is a narrative device, not a measured benchmark [MKT].

**Transferable techniques.** [REC]
- Build the problem act from recognisable artefacts (file names, progress bars, red-pen notes).
- Pace the pain section faster than the solution section.
- Close with a side-by-side delta rather than a claim.

##### 3.6 E4 — "Storyboard first" (HeyGen, 57 s)

**Arc.**
1. "Introducing", then a prompt using a `# Storyboard` tool.
2. The mascot "deals" a 12-card storyboard grid.
3. The user scribbles on frame 2, comments on frame 6, and the edits queue in a Claude Code panel.
4. The mascot regenerates the frames, the user types "build", and a hard-hat mascot hammers while progress fills.
5. The rendered commercial plays, then the lockup.

[DEMO·G-03]

**Craft.**
- ASL about 5.2 s, deliberately readable during the markup steps [DEMO·G-03].
- The music moves from riser to groove at about 0:39, landing on the "build" moment [DEMO·G-03].
- A 3 s end hold [DEMO·G-03].
- A thumbnail-to-fullscreen "context zoom" turns a storyboard card into the live video [DEMO·G-03].

**Why it matters.** It is HeyGen's own film about the storyboard-first workflow that its builders teach (section 5.2) [REC].

##### 3.7 E5 — "It's just HTML" (HeyGen, 54.6 s)

**Arc.** A hook-explain-recap sandwich:
1. Five 1-second generative showpieces, each with a HUD spec label: SDF raymarch, reaction-diffusion, 40k instanced meshes, 24k flow-field strokes, a 1M-particle galaxy.
2. "THIS WAS JUST CODE?"
3. A 25-second annotated code + scrubbing-preview walkthrough.
4. A zoom-out grid of dozens of compositions.
5. A beat-cut recap montage.
6. A `</>` glyph morphing into the brand.
7. A `npx hyperframes init` CTA held about 8 s.

[DEMO·G-04]

**Craft.**
- Male VO at about 2.6 words/s; music estimated at about 130 BPM [DEMO·G-04].
- Hand-drawn "chalk" annotations link code attributes to timeline behaviour [DEMO·G-04].

**Weak spots.** Annotation clutter at 0:23–0:27 and unreadable code in the grid [DEMO·G-04].

**Correction.** This is not the April launch film. Its content does not match the v3 script [DEMO·G-04 vs DOC B-09].

**Transferable techniques.** [REC]
- Earn attention with five 1-second proofs of range, then slow down for the explanation.
- Label spectacle with technical specs.
- Recap the hook at the end to close the loop.

##### 3.8 E6 — "Claude Motion" (HeyGen, 30.9 s, square)

**Arc.**
1. A terracotta pill "Motion Beta" morphs into a chat field.
2. The prompt "A 10-second logo lockup animation for acme.com." is typed and a palette chip ("Your navy") is picked.
3. The preview shows, then Export → "Send to HyperFrames by HeyGen".
4. The HyperFrames editor opens and a prompt adds SFX.
5. A dark telemetry showpiece plays.
6. A "Claude Motion → HeyGen HyperFrames" diagram holds about 2.5 s.

[DEMO·G-05]

**Craft.**
- Container morphs keep spatial continuity [DEMO·G-05].
- Light app shells frame dark preview canvases so the rendered content pops [DEMO·G-05].
- The cursor shows click ripples [DEMO·G-05].

**Weak spots.** Text gets dense in a square frame, and the telemetry scene is not set up by the prompt [DEMO·G-05].

**Transferable techniques.** [REC]
- For square/social, cut the UI density by half relative to 16:9.
- Put the "handoff" between two tools on screen as a single, clickable moment.

##### 3.9 E7 — Timeline Editor launch v2 (HeyGen, 33.8 s)

**Acts.** [DOC B-12]
1. An intro VO "word conveyor" ending on "timing is tricky", with a bell Lottie.
2. A Claude chat ask ending in a "Done." snap.
3. A reprise of the bell.
4. A 29-prompt spiral with a blur ramp and a cut-the-curve exit.
5. A "Not Anymore" reveal with a cursor drag.
6. A zoom-through into a Studio screen recording.
7. A three-row benefit reveal.
8. The HyperFrames and HeyGen logos.

**Production lessons.** [DOC B-12]
- **Render tool version:** `npx` pulled a stale cached version, so they pinned to local source.
- **Workers:** six render workers ran Chrome out of memory near frame 780; three were reliable.
- **Video placement:** a video inside a sub-composition froze on frame 0, so they moved the video to the root.
- **Asset paths:** a relative asset path broke only in render.
- **Pill growth:** a pill grew lopsidedly until its centering offsets were set at t=0.
- **Lint:** infinite repeats are banned (they use a computed finite count), and overlapping cursor tweens needed `overwrite: "auto"`.
- **Black gaps between acts:** fixed by setting the body background to the stage colour (`#f5f5f7`).
- **Music file:** background music stays WAV, because MP3 played choppy.
- **Volumes:** bell 0.3, click 0.8, music 0.15.

**Transferable technique.** Cut-the-curve seams need matched blur and opposite offsets on both sides. Document the pair so nobody edits one side alone [DOC B-12].

##### 3.10 E8 — Nate Herk's YouTube motion showreel (15 s) and the "Opus reel" reference

**The film.** It was made with the kit's motion-showreel skill: 15 s, 1920×1080, 60 fps, cut to a 129 BPM grid. A red scrubber dot travels through seven craft chapters and lands as the play button in the logo [DEMO B-28]. My Gemini call on it failed (section 15), so the analysis below rests on the kit's own documentation.

**The reference it was built from.** A 15.06 s, 60 fps "CLAUDE / MOTION REEL" made by Opus 5.5 for Nate Herk in Sep 2026, measured with the kit's analyzer [DEMO B-31]. Public availability of that reel is [UNVERIFIED].
- **Tempo:** 128 BPM; every hard cut lands within 2 frames of a beat line.
- **Pre-drop:** a dip (about −12 → −25 dB) right before the midpoint iris flash.
- **Luminance:** it flips value at every chapter change.
- **Palette:** ink, paper, and one red for 11 s; electric blue is held back for the climax flurry.
- **Cut curve:** accelerates (chapter lengths about 1.8, 3.5, 2.1, 1.9, 1.9 s), then six cuts in 1.9 s, then a 1.9 s lockup. That is roughly 75% development, 13% flurry, 12% resolve.
- **Bookend:** the first object returns as the final punctuation.

**The grammar it encodes.** [DEMO B-31]
- One motif transformed through every transition; hard cuts only in the flurry.
- Labelled craft chapters, each with a "show the work" tool overlay.
- A persistent HUD (crop marks, spec line, timecode, progress ruler, chapter label).
- Three type voices; physical finish (squash/stretch, motion blur, bloom, grain, vignette).
- A bookend lockup.

**Its verification.** [DEMO B-31]
- Re-run the analyzer on your own render: cuts must fall within about 35 ms of a beat or half-beat.
- Ten-frame strips across every transition.
- A brand test on 6 random frames with the HUD covered.
- About −14 LUFS, with the master WAV remuxed because HyperFrames re-encodes audio slightly quieter.

**Transferable.** This is the most rigorously specified "sizzle" grammar in the public record. Encode it as a mode, not a default [REC].

##### 3.11 E9 — Nate Herk, "Claude Video Editing Just Became Unrecognizable" (process exemplar)

**Pipeline shown.** [DEMO·G-08]
1. Claude Code is the orchestrator. It pulls skills from the hyperframes repo and browser-use/video-use.
2. video-use transcribes (ElevenLabs, or Whisper), builds an edit decision list, and cuts filler, silences, and retakes. The raw 50.3 s became 32.56 s.
3. HyperFrames builds motion graphics anchored to word timestamps.
4. Studio preview, a frame-sampling `verify/*.png` pass, and a render.

**HyperFrames output visible.** Liquid-glass cards with chrome-gradient headlines, a "+247%" chart card, pill subtitles, a split-screen, a PROMPT → HYPERFRAMES → VIDEO diagram, a "MISTAKES WILL BE CUT" scissors gag, Remotion vs HyperFrames comparison cards, and an outro that crops the facecam to a rounded vertical card beside "THANKS FOR WATCHING" [DEMO·G-08].

**Loop.**
- Plan Mode before building.
- Two revision rounds. Round 1 added the outro scene. Round 2 fixed a card covering the face, an unwanted full-frame grid overlay, and a vertical crop that cut only one side.
- Preview audio sounded distorted, but the export was clean.

[DEMO·G-08]

**Cost.** About 238.6k tokens of context were shown on screen [DEMO·G-08] [UNVERIFIED reading].

**Why it matters.** The "MOTION_PHILOSOPHY.md as a house-style doc" rule shown here became the kit's core [DEMO·G-08; DEMO B-29].

##### 3.12 E10 — Jake Moran on Behind the Craft (process exemplar, HeyGen-affiliated)

**Teaching content.** [DEMO·G-07]
- An editing vocabulary to direct the agent: rough cut, filler, pause clamp (about ≤0.25 s), retakes, jump cut, punch-in of 10–20%, hook, push-in/pull-back/crash zoom, easing, A/B-roll, overlay, whip pan, match cut, speed ramp, cutting to the beat.
- Parakeet, a local transcription model, for accurate word boundaries.

**Launch structure.** About 30–60 s in four parts: hook (0–5 s), proof/context, payoff, CTA/brand [DEMO·G-07].

**Launch film built from three images.** Claude planned four acts at 1920×1080/60 fps, produced a storyboard contact sheet of stills for review before the build, then coded it [DEMO·G-07]. The episode page calls the example 43 s; G-07 reports a plan of about 38 s [CONFLICT B-35 vs G-07].

**Other techniques.** [DEMO·G-07]
- **Style copy:** give a short (about 5 s) reference clip and state only the overrides (words, logos, palette, font).
- **Feedback:** draw on the paused frame and batch several annotations.

**Failure cases.** [DEMO·G-07]
- Claude inserted Jake's HeyGen avatar unasked.
- Default music came in too loud; prompt it at about 10% of the voice.
- "Use my brand" produced arbitrary colours; feed a brand kit URL or file.

**Related earlier episode.** Jake's five-step playbook [DEMO B-34]:
1. Assets + `frame.md`.
2. `storyboard.md`.
3. Pull animations from past HyperFrames launches.
4. Generate and review static frames.
5. Build and polish in Studio.

##### 3.13 Other notable showcase pieces (for study)

**Official homepage showcase (45 films).** Card durations and sizes measured on 2026-11-01 [DOC B-02]:

| Category | Films |
|---|---|
| Launch / product | Studio launch 30.0 s; A launch video in 6 hours 73.0 s; Storyboard first 57.05 s; Claude Motion 30.86 s (1:1); Moments catalog 31.86 s; From your website 31.81 s; Studio intro 80.81 s; Keynote line 27.7 s; Cow 1.0 (parody) 29.7 s |
| Captions / talking head | Don't tell my clients 25.52 s (4:5, 720×900); Tool demo 49.92 s (9:16) |
| Explainers | It's just HTML 54.57 s; The journey of "k" 53.61 s (9:16); Code2Video Bench 86.91 s |
| Story / character | Opening night (awards trailer) 50.01 s; The Frameys 43.51 s; Jake's favorite agent 52.63 s; Rackrats 42.01 s; Halloween party 47.51 s; Two lines (sitcom) 36.42 s (9:16); The last onigiri (manga) 25.5 s |
| VFX / 3D | Out of the billboard 10.22 s (9:16); Background removal 42.98 s; Jake & the Taycan 18.1 s (1:1); Giant keyboard 8.11 s (9:16); Axe chop 46.4 s (9:16); The Frameys dance 39.15 s |
| Real UI | Men walk on the Moon 8 s; How do cameras focus 8 s; Wikipedia 9 s; CCTV tracking 10 s |
| Type / logo / style | Going through a change 20.42 s; Wordmark 5 s; ASCII sharks 15 s; Shards 20.01 s; One horse, many looks 9.33 s (2560×720 triptych); This homepage (many looks) 18.6 s |
| Other | Square one (live-coded music) 30 s; Code is a material 60.07 s; Online business story 30 s; Reference any video 51.65 s; HeyGen Video 1 65.18 s; A game in one canvas 30.02 s; Remotion to HyperFrames 20.11 s; Everything was written 30 s |

**Inspiration "Remix in Studio" gallery.** Recreations of other companies' and creators' videos with new words and brand, several by Jake. Examples include Pond, Lovable, Figma Draw, Anduril, Linear Loops, ElevenLabs Reception, plus creator talking-head styles (Ali Abdaal, Dan Martell and others) [DOC B-03].

**Recreate 1:1 replicas.** THE OBLIST (38.58 s, 60 fps) and Srinika × Mercury (30.56 s, 25 fps, avatar footage) [DOC B-04].

**Caution.** Remixes reproduce third-party brand films. Use them as technique study; do not ship look-alikes of other brands [REC].

#### 4. Cross-exemplar craft patterns

##### 4.1 Story architectures that recur

| Architecture | Where seen | Shape |
|---|---|---|
| Problem → solution contrast | E3 | Pain montage → title card → solution → side-by-side delta → brand |
| Hook → proof → payoff → brand | E10, E6 | ≤5 s hook; demo; value; lockup/CTA |
| Hook → explain → recap ("sandwich") | E5 | 5 × 1 s proofs → slow walkthrough → recap montage → CTA |
| Keynote VO spine with silent beats | E1 | ~110 words; picture-only montage and A-roll beats |
| Motif transformation reel | E8 | One object becomes every chapter; bookend |
| Character-as-agent narrative | E2, E3, E4 | Mascot/sprite physically does the agent's work |

[DOC B-08, B-09; DEMO·G-01–G-05, G-07; DEMO B-31]

##### 4.2 Pacing benchmarks

| Context | ASL / cadence | Source |
|---|---|---|
| UI-demo launch films | ~2.2–5.2 s ASL; 3–8 s end holds | [DEMO·G-01–G-05] |
| Sizzle / brand spot (house philosophy) | Scenes 1.0–2.0 s; new element every 0.3–0.6 s; 1 s rest every 7–8 s; outro 4+ s | [DEMO B-29] |
| Showreel | Beat-locked; flurry of 1-beat and half-beat cuts; ~12% resolve | [DEMO B-31] |
| Talking-head reels (Nate's 27 top reels) | Shots 1.1–1.4 s, none over ~2.8 s; first cut 0.6–1.0 s; speech 4.0–4.7 words/s | [DEMO B-30] |
| Keynote VO launch | ~110 words in ~50 s, deliberate silences | [DOC B-09] |

[REC] Choose pacing by genre. Product UI must stay readable, so its ASL is longer. Sizzle reels earn speed with a beat grid. Do not apply sizzle pacing to tutorial UI.

##### 4.3 Typography

- **One typeface vs many** [CONFLICT, house styles]:
  - HeyGen's launch storyboard: typography distinct per beat, no single family across the video [DOC B-08].
  - Nate's MOTION_PHILOSOPHY says "single sans-serif" in one section and "every beat uses a different Google Fonts family" in another [DEMO B-29].
  - [REC] Reconcile as one calm house face for narrative beats plus deliberate face changes for montage/flurry beats.
- **Three type voices** in showreels: heavy display, an accent (italic serif or brand UI face), and wide-tracked mono for the "machine layer" [DEMO B-31].
- **Word-level reveals** beat character-level for narrative; the first word can "carry" momentum with decaying offsets on tail words. On punchlines, lead the visual about 0.2 s ahead of the audio [DEMO B-29].
- **Captions on talking heads** [DEMO B-30]:
  - 1–3 words per chunk, hard swaps, appearing 2 frames early.
  - One boxed look with a thin light edge.
  - Never white on light, and never over the mouth or chin.
- **Fonts as files:** download fonts into the project and use `@font-face`; never rely on system fonts [DEMO B-31].

##### 4.4 Colour and value

- **Value flips** at structural boundaries appear in nearly every strong piece: light UI ↔ dark preview (E2, E4, E6) and chapter value flips (E8) [DEMO·G-01, G-03, G-05; DEMO B-31].
- **Accent discipline:**
  - One accent bound to "agent did this" (mint in E2/E3) [DEMO·G-01, G-02].
  - A "held-back" climax colour [DEMO B-31].
  - At most 5 active hues, each with a meaning [DEMO B-29].
- **Defaults conflict** [CONFLICT]:
  - HeyGen's launch film is "light by default", with a rule that muted is fine but flat is not [DOC B-08].
  - Nate's reference philosophy (deconstructed from an "Infinite — Global Payments" spot) is "black is the canvas, ~90% of every frame" [DEMO B-29].
  - [REC] Treat both as selectable house styles chosen per brief.

##### 4.5 Motion and transitions

- **Camera always moving:** a canvas drift (E1) [DOC B-08]; "camera never sleeps" [DEMO B-29]; subtle motion reads static at 30 fps [DOC B-08].
- **Signature transitions:**
  - Smash cuts for montages [DOC B-08].
  - Cut-the-curve vertical whip with matched blur: exit about 0.33 s power2.in, entry about 1.0 s power2.out, same direction both sides [DEMO B-29; DOC B-12].
  - Light-streak whip, hiding the cut at peak brightness [DEMO B-29].
  - Thumbnail-to-fullscreen context zoom [DEMO·G-03].
  - Object-to-object morphs [DEMO B-31; DEMO·G-04].
- **Simulated UI as protagonist:** typed prompts, cursor paths with click ripples, timeline blocks snapping, freehand annotation drawn with a stroke-dash reveal [DEMO·G-01–G-05].
- **Transforms only:** tween transforms and opacity, never `left/top/width/height` [DEMO B-30, B-31].
- **One driver:** use a per-frame driver as a pure function of time for canvas effects and shared layers [DEMO B-31].
- **Heavy looks:** pre-render iridescent/3D looks as MP4 rather than live WebGL [DEMO B-29].

##### 4.6 Audio and sync

**Mix levels used by practitioners:**

| Layer | HeyGen launch | HeyGen timeline launch | Nate (philosophy / playbook) | Jake |
|---|---|---|---|---|
| Voice | 1.0 | — | 1.0 | — |
| Music/underscore | 0.15 | 0.15 (WAV) | 0.15 pad; bed ~11 dB under voice (9–14) | ~10% of voice |
| SFX | 0.2 | bell 0.3, click 0.8 | 0.2 | — |
| Master | — | — | −14 LUFS, TP ≤ −1.5 dBTP (playbook); −1.2 dBTP (showreel mix) [CONFLICT] | — |

Sources: [DOC B-10, B-12; DEMO B-29, B-30, B-31; DEMO·G-07]. The HeyGen launch underscore value comes from the handoff; the README says the render has no continuous music [CONFLICT B-10 vs B-07]. [REC] For reference, linear 0.15 ≈ −16.5 dB and 10% ≈ −20 dB.

**SFX follow visible actions, not every cut.** Use soft taps, clicks, paper, and air. Avoid laser zaps and whooshes on every cut, and vary samples across list items [DEMO B-30]. The official films tie SFX to on-screen acts: keystrokes, insertion "plinks", completion chimes [DEMO·G-02, G-03].

**Anchor every cue to the clock.**
- Voice-led films re-transcribe after any VO change (HeyGen used `npx hyperframes transcribe`) [DOC B-10].
- Narrated explainers put the whole timeline on one beat-grid clock and never hard-code word times [DEMO B-30].
- Music-led montages use `hyperframes beats` output with the `music-to-video` skill [DOC B-19].

##### 4.7 Endings

Hold the brand or CTA: 2 s wordmark (E1), about 2.5–4 s (E3, E6), about 8 s CTA with a command line (E5), and 4+ s outro in Nate's philosophy [DOC B-08; DEMO·G-02, G-04, G-05; DEMO B-29]. Never fade the last spoken word [DEMO B-30].
