# KB-06 — Format and Niche Playbooks

*Composite. §1 and §2 are HyperVideo Man's quick maps (formats and niches) — the defaults he applies before opening a playbook. Part I is Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026): seven format playbooks, the cross-format adaptation matrix and capability limits. Part II is Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229): how to use the playbooks, seven playbooks, the platform delivery reference and the limits table. Audio by theme and audience is in KB-07; culture rules in the persona's LANGUAGE & CULTURE PROTOCOL and KB-01.*

*Section numbers inside each part keep the numbering of the source they came from (A = §2–§7 and appendices of the Skillgraph document; B = Parts 3–8 of the Claude Code document). Where the two parts disagree, the preface and KB-14 govern; where either disagrees with the installed CLI, the CLI wins.*

## 1. Format quick map

| Format | Direction |
|---|---|
| **Brand film 45–90 s** | 16:9 (+9:16) · journey or five-act · luxe transitions, 1–2 shaders · music scored, one silence · SFX 2–8/min · VO 2.0–2.3 |
| **Product demo 30–90 s** | capture → promo or tour · hook → 3 feature beats → end card · UI rebuilt as HTML, cursor, punch-ins · light bed −18…−22, real UI clicks only |
| **Explainer 30–90 s (cap ~3 min)** | hook → problem → mechanism → proof → CTA · one idea per frame, source metaphor · light bed or none; music off during the mechanism for learners · captions on |
| **Education 2–10 min** | chapters every 1.5–3 min, interrupt every 30–60 s · orientation → demonstration → recap · VO 1.8–2.2 · music none or ≥ 20 dB under · sidecar captions |
| **Promo 15–60 s** | hook → promise → proof → invitation → CTA · variables for date/venue/URL · 1–2 shaders · music-led build → drop on reveal → button · SFX 16–32/min |
| **Social 7–30 s** | 9:16/1:1 · hook in 1 s, frame 0 = thumbnail · headline ≥ 90 px, body ≥ 32 · safe box · captions burned in · works muted |
| **Data story 30–90 s** | question → pattern → mechanism → before/after → action · ≤ 3 metrics per frame, zero baselines, staged ~1 s changes, object constancy, no pies/legends · beatless bed or none; music out under figures |
| **Music-led 15–60 s** | beat grid drives cuts (audiomap) · lyric/montage/visualizer · no narration |
| **Talking-head packaging any length** | footage untouched · transcript-synced lower-thirds, callouts, captions · safe zones |
| **Long-form chaptered 3–10 min** | `/general-video` · locked script · render in spans · HANDOFF. |

## 2. Niche quick map (global, EN/FR, West Africa)

| Niche / audience | Direction |
|---|---|
| **Faith/FSY/YSA** | reverent warmth; cinematic-pop build 100–120 BPM for promos, hymn-like 60–80 for devotionals; silence under scripture; Church standards and official-music terms; captions; dates and venues verified or placeholdered |
| **Finance/audit/data reporting** | calm cream or deep navy; one accent; numbers with units, sources and visual weight; beatless bed −20…−24 or none, out under findings; no red alarms, no drama on losses |
| **SaaS/tech** | capture tokens; UI rebuilt as HTML; modern electronic 100–124 BPM; soft UI sounds; value by beat 2 |
| **Nonprofit/social cause** | real field ambience; sparse piano/cello 60–85; silence on the hardest images; dignity over triumph |
| **Events/hype** | music-led 115–130 BPM (Afro-pop/Afrobeats-inspired 100–115 for West African youth where it fits); one big drop per 30 s; date card locks in; cut-downs from variables |
| **News/analysis** | tension bed without melody; out under key facts; teleprinter ticks; no music under tragedy |
| **Education/training** | learners' pace; one motif per section; music off during content |
| **Gaming/esports** | driving 120–150 BPM; glitch palette; drops never under VO; licensed audio only |
| **Luxury/real estate** | 55–60 % negative space; 300/900 weights; foley over whooshes; deep house or neo-classical 90–118 |
| **Health/wellness** | light canvas made cinematic; soft pads 60–85 or beatless; no sudden hits |
| **Kids/family** | bright major-key 110–130; soft pops; VO 1.8–2.2; repetition; no scary drones |
| **Executives/leaders** | voice first; bed ≤ −20 or none; half the effects; no hype hits. |

Adaptation rules that hold across every niche: recompose rather than crop for each aspect; halve UI density for square and vertical; captions mandatory for feeds and for every West African or accessibility-critical audience; nothing meaningful carried by hue alone; instrumental only under voice; stems separated for dubbing; verify or placeholder every date, venue, price and claim.

## Part I — Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026)

### 7. Format playbooks — adapting the system to each video type

Each playbook states what the format is for, which HyperFrames route it takes, how the prompt, visual language, pacing, audio and workflow adapt, and where the capability limits sit. All values are expert starting defaults unless tagged.

#### 7.1 Brand film

| Dimension | Direction |
|---|---|
| Goal | Feeling and memory: who the brand is, in 45–90 s |
| Route | `/general-video` (companion or automation with storyboard); borrow the product-launch genre lens for taste |
| Structure | Journey or Before–After–Bridge; the value claim is emotional, still by beat 2; one hero moment; ending on the lock-up |
| Visual language | Strict `frame.md`; one accent; luxe transitions (0.6–0.7 s); light and depth do the talking; typography as imagery; 55–60 % negative space |
| Pacing | Slow-build-PEAK-resolve; slowest scene ≥ 3× slowest; holds of 1.5–2 s on hero frames |
| Audio | Music-led or voice-led by brief; music scored to the arc with one designed silence; SFX sparse (2–8/min), foley over whooshes; −14 LUFS web |
| Prompt deltas | References with the quality to borrow are mandatory; the anti-pattern (generic "inspiring" corporate) named; signature move required |
| Limits | Live-action footage must be supplied or generated externally (HeyGen avatar/video generation via media-use); HyperFrames composes and grades it but does not shoot it |

#### 7.2 Product demonstration / UI walkthrough

| Dimension | Direction |
|---|---|
| Goal | Show it working; build confidence in 30–90 s |
| Route | `/product-launch-video` (capture a site → promo or "show it as-is" tour); UI rebuilt as HTML for marketing, real screenshots for training |
| Structure | Hook (outcome) → 3 feature beats with UI captures and one-line captions → end card [Documented] official prompting guide |
| Visual language | Device frames; animated cursor; punch-ins 10–20 % on the control being used; one accent on the active element; real UI colours from capture tokens |
| Pacing | 2–4 s per feature state; "something changes on every beat"; cursor and scroll leave through the frame edge |
| Audio | Light bed (−18 to −22 dB, no lead melody); real UI clicks on actual interactions only; narration 2.3–2.5 w/s |
| Prompt deltas | Name the 3–5 real screens in order; VO_MODE (verbatim vs restructured) when a script is supplied; sell-or-show decided first [Documented] route |
| Limits | Dynamic or protected pages capture partially; IPv6-only sites unsupported [Documented]; never iframes; a screen recording can be placed as footage but not "edited" inside the browser beyond cuts, trims and reframes |

#### 7.3 Explainer

| Dimension | Direction |
|---|---|
| Goal | Make a mechanism or concept understood in 30–90 s (hard cap ~3 min) |
| Route | `/faceless-explainer` (angle: concept / how-to / listicle / narrative) [Documented] |
| Structure | Hook → Problem → Mechanism → Proof → CTA; one idea per frame; a running metaphor mined from the source |
| Visual language | Invented typography, abstract graphics, diagrams, data; light canvas made cinematic for learning content; connector lines only with a start, an end and a job |
| Pacing | 3–5 s per beat; hold ≥ words ÷ 2.5 + 0.5 s; one hold on the key diagram |
| Audio | Light bed or none (−18 to −24 dB), music off during the mechanism for learning audiences; SFX 8–16/min: pops, soft clicks, one "aha" chime; captions on |
| Prompt deltas | The source text's own phrases become the visual vocabulary; `VO_MODE` for pasted scripts; destination → aspect |
| Limits | Specialised route caps at about 3 minutes; longer educational pieces go to `/general-video` with chapters |

#### 7.4 Educational / training video

| Dimension | Direction |
|---|---|
| Goal | Learning and retention; often 2–10 min |
| Route | `/general-video` with chapters (the genre routes cap at ~3 min); `/talking-head-recut` when an instructor's footage exists |
| Structure | Orientation → Demonstration → Recap per chapter; a chapter card every 1.5–3 min; a pattern interrupt every 30–60 s |
| Visual language | Consistent diagram grammar; one accent for "the thing to look at"; larger body text (≥ 32 px); no decorative motion during reading |
| Pacing | 1.8–2.2 w/s for learners; longer holds for complex reasoning; no cut-per-beat compulsion |
| Audio | Music none or ≥ 20 dB under speech (WCAG 1.4.7 [Standard]); a 1–2 s motif marks each new section (sound as navigation); full captions; nothing conveyed by audio alone |
| Prompt deltas | Learning objectives stated per chapter; accuracy of UI and figures prioritised over polish; sidecar captions required |
| Limits | Real interface screenshots are the bottleneck practitioners name [Demonstrated, Masset]; interactive branching belongs to `/slideshow` (a navigable deck, not an MP4) |

#### 7.5 Promotional content (events, launches, campaigns)

| Dimension | Direction |
|---|---|
| Goal | Desire and action in 15–60 s |
| Route | `/product-launch-video` or `/general-video`; `/music-to-video` when a track's beat grid drives the piece |
| Structure | Hook → Promise → Proof → Invitation → CTA; value by beat 2; date/venue/price as hero facts with visual weight |
| Visual language | Energetic palette with one accent still leading; 1–2 shader transitions (hero reveal + CTA); signature move tied to the brand mark |
| Pacing | 15 s: 3–5 beats; 30 s: 5–8; a new visual every 1.5–3 s; one hold on the date |
| Audio | Music yes, scored hook → build → drop on the reveal → button; SFX 16–32/min; hero hits ≥ 15 s apart (≥ 8 s in hype edits); no drops mid-sentence |
| Prompt deltas | Variables for date, venue, URL so cut-downs render from one source; multiple aspects briefed up front; FSY/faith events: Church standards and official-music terms stated explicitly |
| Limits | Rights: library, generated or original music only (Content ID); generated avatars/clips bill HeyGen credits [Documented] |

#### 7.6 Social media video (vertical and square)

| Dimension | Direction |
|---|---|
| Goal | Stop the scroll and deliver one idea in 7–30 s, sound-off first |
| Route | `/motion-graphics` for unnarrated units under ~10 s (stat hit, logo sting, kinetic title; alpha overlays possible); otherwise the subject's route at 1080×1920 or 1080×1080 |
| Structure | Hook in 1 s (frame 0 is the thumbnail) → one proof → CTA; often Hook + Proof + CTA only |
| Visual language | Headline ≥ 90 px, body ≥ 32 px, labels ≥ 24 px; vertical zones clear of platform UI (top 10–15 %, bottom 20–30 %, right strip); captions burned in, 2–3 words per group |
| Pacing | New visual every 1.5–3 s; transitions 0.15–0.2 s; VO 2.6–3.0 w/s if any |
| Audio | Designed to work muted; music at −12 to −16 dB when VO exists; trend energy from licensed or generated music only |
| Prompt deltas | Destination drives aspect [Documented]; "the first frame works in silence" is an acceptance item; text never in the corners |
| Limits | Platform recompression softens fine detail — avoid hairlines and 3–8 % decoratives; exact UI safe-zone pixels vary by app version (verify against the platform template) |

#### 7.7 Data-driven storytelling

| Dimension | Direction |
|---|---|
| Goal | Make one quantitative insight land honestly in 30–90 s |
| Route | `/faceless-explainer` (concept angle) or `/general-video`; `nyt-graph` init template; `data-chart` registry block (the most-installed after `logo-outro` [Documented]) |
| Structure | Question → the pattern → the mechanism → the before/after → what to do; one chart per idea |
| Visual language | ≤ 3 metrics per frame; numbers with visual weight (bars, rings, fills); tabular figures; successive values in the same visual space; honest scales with units and sources; no pies, gridlines, legends, multi-axis or six-panel dashboards [Documented] data-in-motion.md |
| Pacing | Count-ups 0.8–1.2 s from one proxy value; a hold of ≥ 1.5 s on the key comparison; music out under the figures |
| Audio | Beatless ambient bed −20 to −24 dB or none; soft ticks on bars; one chime on the conclusion; no drama on numbers |
| Prompt deltas | Supply the dataset and its units; state rounding rules for the voice ("nearly two trillion") versus the visual (exact figure) |
| Limits | No chart-library output; build with GSAP + SVG/CSS; large datasets need pre-aggregation outside HyperFrames |

#### 7.8 Cross-format adaptation matrix

| Lever | Brand film | Product demo | Explainer | Education | Promo | Social | Data story |
|---|---|---|---|---|---|---|---|
| Runtime | 45–90 s | 30–90 s | 30–90 s | 2–10 min | 15–60 s | 7–30 s | 30–90 s |
| Hook deadline | 5 s | 2–5 s | 2–5 s | 5–8 s | 1–2 s | 1 s | 2–5 s |
| Beats | 8–14 | 5–12 | 6–14 | chapters | 3–8 | 2–5 | 6–10 |
| Transition palette | luxe/shader | CSS + cuts | CSS | CSS, cuts | shader + cuts | cuts | CSS |
| Music decision | scored | light | light/none | none/≥ 20 dB under | scored, music-led | muted-first | beatless/none |
| SFX density | 2–8/min | 8–16 | 8–16 | 2–8 | 16–32 | 16–32 | 2–8 |
| VO pace | 2.0–2.3 | 2.3–2.5 | 2.3–2.5 | 1.8–2.2 | 2.3–2.8 | 2.6–3.0 | 2.2–2.4 |
| Type scale | full-screen | full-screen | full-screen | full-screen + | in-feed | in-feed | full-screen |
| Captions | optional | on | on | required | on | burned-in | on |
| Loudness | −14 | −14 | −14/−16 | −16 | −14 | −14 | −16 |

#### 7.9 Capability limits and when other tools are required

| Need | HyperFrames position | What to use instead or alongside |
|---|---|---|
| Live-action shooting, actors, locations | Out of scope — HyperFrames composes and renders what a browser can show | Real footage; HeyGen avatar/video generation and dubbing via `media-use` (credits); third-party generators (Seedance, Wan via fal, as practitioners report) |
| Photoreal generative video at length | Limited to provider hooks; costly and reroll-heavy ("expect 5–25 % of AI shots to be usable" [Demonstrated, Anfloy]) | Generate externally, adopt into `assets/` |
| Complex NLE editing of long footage (multicam, colour-matching dozens of clips) | Cuts, trims, reorders, speed ramps, crossfades and treatments are documented; the desktop app adds podcast multi-camera edits [Documented, app changelog] | Final Cut / Premiere for heavy footage work; HyperFrames for graphics and finishing |
| Interactive presentations | `/slideshow` produces a navigable deck, not an MP4 [Documented] | Record the deck or author a video route separately |
| Audio mastering beyond the 16 effects (multiband, de-essing, panning) | Not documented; no panner in the effect list | Pre-process stems in a DAW; bake movement into assets |
| HDR on distributed renders, HLS with GPU, 4K + HDR together | Documented limits [R1] | Render locally for HDR; choose one of 4K or HDR |
| Very long renders on one machine | Possible; slow on software GPU ("~2.5 s/frame" internally observed; third-party 10 s 1080p in ~16 s at defaults) | `render --start/--end` spans, Lambda chunks (15-min invocation ceiling), cloud render on a paid plan |
| Exact platform safe zones | Not provided by HyperFrames | The platform's own templates |
| Rights-cleared commercial music | Not provided; catalogue retrieval via HeyGen needs sign-in | Licensed libraries; generated music; original composition; the Church's terms for official music |
| Fonts with no local file and no Google listing | Falls back to a default face (lint warns) | Obtain the font file and embed with `@font-face` |
| Determinism guarantees on macOS/Windows | Linux `beginFrame` capture is the deterministic path; other platforms fall back to screenshot heuristics; worker count can change pixels [Demonstrated, R2] | `--docker` for cross-machine parity; pin worker counts when hash-comparing |

## Part II — Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229)

### 6.1 How to use the playbooks

Pick the playbook from the deliverable, not from the words in the request: "make a video about our site" is a product demo or promo; "explain how X works" is an explainer [DOC] [S-09]. Each playbook gives the goal, structure, pacing, visual and motion language, audio, what the prompt must emphasise, the workflow adaptation, the matching official route, and the usual failure. Numbers come from Part 3 (`quality-framework.md`, `audio-direction.md`); this file only states what changes per format.

| Format | Typical length | Default aspect | Pace (average shot) | Sound default | Official route (generation B) |
|---|---|---|---|---|---|
| Brand film | 30–90 s | 16:9 (+ 9:16 cut-down) | 2–5 s, with deliberate holds | Music-led or VO + music; planned silence | general-video |
| Product demo / launch | 30–75 s | 16:9; 1:1 or 9:16 variants | 2.2–5.2 s | VO + UI micro-sounds + light bed | product-launch-video |
| Explainer | 45 s–3 min | 16:9 | 4–10 s per visual idea | VO-led; little or no music under dense parts | faceless-explainer |
| Educational / tutorial | 2–6 min per unit | 16:9 | 4–10 s; chapters every 45–90 s | VO-led, no music under explanation | general-video / faceless-explainer |
| Promo / ad | 6–30 s | 9:16, 1:1, 16:9 | 1–2.5 s | Music + VO; captions burned in | motion-graphics / product-launch-video |
| Social organic | 7–60 s | 9:16 | 1.1–2.5 s | Captions first; music and effects as enhancement | general-video / embedded-captions |
| Data story | 30–120 s | 16:9 (1:1 for social) | ~1 s per change stage; long holds on results | VO-led; calm bed or none | general-video |

Lengths and paces combine official route guidance, platform guidance and practitioner measurements [DOC] [S-09] [STD] [C-16] [C-20] [RES] [C-21] [DEMO] [G-01] [B-29] [B-30]. Upstream retired the route skills in v0.8.185; the same format guidance now lives in `/hyperframes` references [DOC] [A1-37].

### 6.2 Brand film

- **Goal.** Make the audience feel something about the brand and remember one idea.
- **Structure.** Five-act shape: set-up 10–15 %, rising tension 35–40 %, turn at 60–70 %, resolution and brand in the last 20 % [REC] [C-28]. Or a motif transformation: one object becomes every chapter and returns as the lockup [DEMO] [B-31].
- **Visual language.** A strong art direction from the brand system; one held-back color for the climax; value flips (light ↔ dark) at structural boundaries [DEMO] [B-31] [G-01].
- **Motion.** Slower bands (0.5–0.8 s gravity, 0.8–2.0 s cinematic moments); camera journeys with dwell; velocity-matched seams; at most one or two shader transitions, at the hero reveal and the CTA [DOC] [A2-28] [A2-30].
- **Audio.** 70–100 BPM sparse score or VO plus score; silence before the key line; music edited to bars [REC] [C-65] [C-64].
- **Prompt emphasis.** Tone words translated into tokens; the motif and its payoff; the one spectacle beat; reference films with the quality to borrow.
- **Workflow.** Animatic before build is mandatory; music chosen before motion so cuts can land on bars.
- **Usual failure.** Beautiful frames without an idea; trend styles that clash with the brand.

### 6.3 Product demo and launch film

- **Goal.** Show the product doing the job the viewer cares about, and make them try it.
- **Structure.** Hook (the result or a human stake) → problem → product in use → proof (number, delta or testimonial) → CTA; or problem act versus solution act paced faster in the problem [DEMO] [G-01] [G-02]. The official blueprints map shots to roles (hook, problem, product intro, feature showcase, benefits, social proof, CTA, brand outro) [DOC] [A2-04].
- **Visual language.** Real UI, rebuilt or captured cleanly with real (anonymised) data; light app shells framing dark previews; one accent bound to "the product did this" [DEMO] [G-01] [G-05].
- **Motion.** Cursor-driven UI choreography (the input is the star); context zooms from thumbnail to full screen; typing at 8–12 characters per second for natural reads [DOC] [A2-23] [A2-22] [DEMO] [G-03].
- **Audio.** Voice at 140–160 wpm; dry clicks and taps on contact frames; a light bed carved under the voice [REC] [C-66] [C-62] [DOC] [A2-57].
- **Prompt emphasis.** The exact UI states and copy; which feature carries the value; capture source (`npx hyperframes capture <url>`) and brand tokens [DOC] [A1-15].
- **Workflow.** Capture or rebuild UI first; lock the script; time UI actions to word timestamps.
- **Usual failure.** Feature tours; UI text too small for phones; lists scrolling too fast to read [DEMO] [G-02].

### 6.4 Explainer

- **Goal.** Make a mechanism understood and remembered.
- **Structure.** Hook 0–3 s → problem ≈ 10 % → pre-training of 2–3 terms ≈ 5–10 % → mechanism in 2–4 signalled segments ≈ 50 % → proof ≈ 10–15 % → CTA in the last 3–5 s [REC] [C-23] [C-17]. The "sandwich" (fast proofs, slow explanation, recap) also works [DEMO] [G-04].
- **Visual language.** Diagrams with labels on the objects; one travelling subject that never teleports; a persistent world with altitude changes for long pieces [RES] [C-23] [DEMO] [A2-83].
- **Motion.** Reveal on the voice; staged changes; end each segment on a static summary frame [DOC] [A2-24] [RES] [C-45].
- **Audio.** Voice-led; music low or absent under dense explanation (coherence principle) [RES] [C-23].
- **Prompt emphasis.** The single mechanism; vocabulary to pre-train; the "first, second, third" signals; what is said versus shown versus written.
- **Workflow.** Script and diagram plan before any styling; check that every drawn element is named by the voice ("if it doesn't get a word, it doesn't get drawn") [DEMO] [A2-83].
- **Usual failure.** Decorative motion competing with explanation; narration duplicated verbatim on screen.

### 6.5 Educational and tutorial

- **Goal.** Durable learning and the ability to perform a task.
- **Structure.** Units under 6 minutes; chapter every 45–90 s; objective → demonstration → practice cue → recap [RES] [C-21] [C-22] [REC].
- **Visual language.** High legibility; code or UI at readable sizes with zoom-ins; consistent callout grammar.
- **Motion.** Slow, predictable, slow-in/slow-out; no spectacle beats; procedural animation where motion itself is the content (animation helps most for procedural knowledge) [RES] [C-26] [C-27].
- **Audio.** 120–140 wpm with pauses at boundaries; no music under explanation; captions with sidecar files [REC] [C-66] [STD] [C-37].
- **Prompt emphasis.** Learning objective; prerequisite knowledge; exact steps; reading levels for captions.
- **Workflow.** Segment the script first; one sub-composition per chapter; caption accuracy check on every chapter.
- **Usual failure.** Pacing tuned for social; text and voice saying different things at once.

### 6.6 Promo and ad

- **Goal.** A specific action (click, install, buy) from a cold audience.
- **Structure.** Hook in 3 s with the product or message (over 63 % of top-CTR TikTok ads show it within 3 s) → 1–2 benefit beats → proof → CTA with brand inside the action [STD] [C-15] [C-17]. ABCD: attention, branding, connection, direction [STD] [C-17].
- **Visual language.** Bright, high-contrast visuals for small screens; brand present early [STD] [C-17].
- **Motion.** High-energy band (0.15–0.3 s transitions, `power4`/`expo`), kinetic type beats spaced 1.2–1.8 s [DOC] [A2-06] [A2-22].
- **Audio.** 110–130 BPM; sound linked to more conversions in Shorts ads; captions burned in [STD] [C-15] [C-20].
- **Length.** TikTok In-Feed 21–34 s recommended; Shorts action ads 10–30 s [STD] [C-16] [C-20].
- **Prompt emphasis.** One offer, one CTA; safe zones per placement; variants per aspect.
- **Workflow.** Build three materially different openings and test them before polishing [DEMO] [A2-80].
- **Usual failure.** Logo build first; text inside platform UI zones.

### 6.7 Social organic

- **Goal.** Stop the scroll and hold attention to the end.
- **Structure.** Payoff or tension in the first second; one main open loop closed before the end [DEMO] [A2-80].
- **Visual language.** 9:16 composed for the safe box (x 120–780, y 288–1248 on 1080×1920); half the UI density of 16:9 [REC] [C-41] [DEMO] [G-05].
- **Motion.** Fast but varied rhythm (burst, anticipation, payoff); every extended graphic beat has an action with an outcome [DEMO] [A2-80].
- **Audio.** Design for sound off; captions 1–3 lines, ≤ 20–25 characters per line, just above the bottom UI band [STD] [C-14] [REC] [C-67].
- **Prompt emphasis.** First-frame design; caption style; loop closure.
- **Workflow.** Talking-head footage routes to the official caption or recut workflows; graphics-only pieces to general video [DOC] [S-09].
- **Usual failure.** A 16:9 master cropped to 9:16; captions under platform UI.

### 6.8 Data story

- **Goal.** Make a quantitative insight believed and remembered.
- **Structure.** Question → context → the change (staged) → the insight held on a static summary → implication.
- **Visual language.** One hero metric per beat; labels on marks; common scales; zero baselines for bars [RES] [C-45] [C-50] [DOC] [A2-36].
- **Motion.** Object constancy; each change stage about 1 s; count-ups 0.8–1.5 s then hold ≥ 1.5 s plus reading time; no overshoot on marks [RES] [C-45] [C-48] [REC].
- **Audio.** Say the number as it lands; calm bed or none [REC] [C-45].
- **Prompt emphasis.** Data source and claim ledger; units and time frame on screen; which series to highlight.
- **Workflow.** Lock the data file first and bind it with variables so numbers are never retyped [DOC] [A1-08].
- **Usual failure.** Truncated axes, rescaling mid-story, too many series, animated chart-library defaults.

### 6.9 Platform delivery reference

| Platform | Container / codec | Aspect / size | Duration | Notes |
|---|---|---|---|---|
| YouTube | MP4, H.264 High, 4:2:0, closed GOP of half the frame rate, AAC-LC 48 kHz | 16:9; SDR 1080p at 8 Mbps (30 fps) / 12 Mbps (60 fps) | Up to 12 h / 256 GB | BT.709 tags; untagged is assumed BT.709 [STD] [C-81] [C-82] |
| YouTube Shorts | As YouTube | Vertical or square | Up to 3 min | Ads: first 60 s play in the feed; action ads 10–30 s [STD] [C-83] [C-20] |
| TikTok (organic via API) | MP4 (H.264 recommended) | 360–4096 px; 23–60 fps | 3 min for all creators; some 5 or 10 | ≤ 4 GB [STD] [C-85] |
| TikTok In-Feed ads | MP4, MOV and others | 9:16 ≥ 540×960 | ≤ 10 min; 21–34 s recommended | ≤ 500 MB; safe zones via templates [STD] [C-44] [C-16] |
| Instagram Reels ads | MP4/MOV, H.264, AAC ≥ 128 kbps | 9:16, 1440×2560 | Up to 15 min | Keep top 14 %, bottom 35 %, sides 6 % clear [STD] [C-41] |
| LinkedIn | MP4, MOV and others | 1:2.4 to 2.4:1; 10–60 fps | 3 s–15 min | 75 KB–5 GB [STD] [C-86] |
| X | H.264 High, AAC-LC | Recommended 1280×720, 720×1280, 720×720 | 20 min via API; app limits differ | [STD] [C-87] [C-88] [CONFLICT] |

Platform specifications change frequently; re-check the platform's own page before a paid campaign. HeyGen's cloud render supports only 16:9, 9:16 and 1:1 [DOC] [A1-52].

### 6.10 Capabilities, limits and when to use other tools

| Need | HyperFrames fit | Limit | Use alongside |
|---|---|---|---|
| Typography, UI, diagrams, data, illustration, compositing | Excellent: any web layout, SVG, canvas, WebGL [DOC] [A1-05] | Fixed viewport; no input events; no wall clock | — |
| Video footage, trims, speed ramps, fades | Good: media at any depth, rate 0.1–10, automation lanes [DOC] [A1-08] [A1-10] | No mid-source freeze; no automatic waveform sync; not an NLE replacement [DOC] [A1-10] [B-13] | A non-linear editor for long-form cutting |
| Characters and character animation | Lottie playback, sprites, 3D via Three.js [DOC] [A1-34] | No rigging or acting tools in HTML | After Effects/Lottie, Rive, Blender, or generative video |
| Photoreal 3D, product renders | Three.js scenes; pre-rendered video plates [DOC] [A2-15] [DEMO] [A2-70] | Live WebGL can stall renders; canvas buffers gain no detail from supersampling [DOC] [A1-48] | Blender or another 3D renderer, imported as video |
| Live action, people, lip sync | Composite footage; background removal locally [DOC] [A1-08] [A2-54] | No capture, no generation of real people in the framework | A camera shoot, avatar or generative-video service with consent |
| Voice | Local Kokoro TTS; HeyGen voices with an account [TESTED] [A1-80] [DOC] [A1-57] | Local voice quality and range limited | A professional voice actor or premium TTS |
| Music | Retrieval and generation fallbacks through the official media skill [DOC] [A2-53] | Licensing remains your responsibility | A licensed library or composer |
| HDR | HDR10 MP4 driven by HDR sources [DOC] [A1-49] | MP4 only; local only | A color-managed finishing tool for mastering |
| Scale (thousands of variants) | Variables and batch; Lambda and Cloud Run [DOC] [A1-21] [A1-19] | Distributed renders are SDR, 24/25/30/60 fps, no motion blur | — |
| Interactive or responsive output | `<hyperframes-player>` and `publish` for playback [DOC] [A1-30] [A1-13] | Output is linear video, not responsive UI | A web build for true interactivity |

**Hybrid pattern.** When a brief needs live action, photoreal 3D or character acting, make those plates in the right tool, import them as video, and let HyperFrames do what it does best: typography, interface, data, layout, transitions and the final assembly with sound [REC].
