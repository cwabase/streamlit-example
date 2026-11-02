# KB-09 — Fix-and-Coach Protocol: from a weak result to the expected one, and from a fix to a lesson

*New synthesis: merges source A's troubleshooting ladder (§8.4) and source B's diagnosis table (§3.5), prompt-level failure modes (§4.7) and validation loop, and adds the coaching method.*

## 1. Diagnosis protocol (FIX mode)

1. **Watch three ways** — with sound, muted, sound only. One sentence per pass on what failed.
2. **Freeze three frames** — the opening, the densest frame, the ending. One visual system? Reading order obvious? Safe areas respected?
3. **Scrub every cut.** Note each jump, flash, clip, unsettled element, double exit, teleport — with its timestamp.
4. **Read the evidence** — `npx hyperframes lint`, `npx hyperframes check --json --snapshots` (did the audits run, or "0 samples"?), the render summary's second line (`beginframe` vs `screenshot`, GPU mode), 6-frame strips across each cut, the animation map, `ffprobe`, `ffmpeg -af ebur128=peak=true`, `scripts/qa_render.py` (spec, loudness, black/frozen/silent spans, flash risk, contact sheet).
5. **Build the diagnosis table**: timestamp · symptom · likely cause · owning skill (D#.C#) · fix · evidence.
6. **Rank by impact on the message**; name the weakest scene and the single change that lifts it most.
7. **Write revisions** as *time · symptom · desired result · scope*. One variable per edit with an absolute target. Freeze what works. Re-render only the affected span (`render --start/--end`). Compare before/after stills.
8. **Re-run the failed gate and every gate after it.** Stop after three judge rounds; keep the best version, not the last; record why you stopped.
9. **Coach**: say what caused it and how to prevent it in the next brief or prompt.

Revision syntax: "At **00:12.4**, the statistic reveal lands before the spoken number. Move the reveal to the word 'quarante', hold it 0.7 s longer and remove the competing click. Keep the surrounding scene structure. Re-snapshot 11.8–14.0 s."

## 2. Symptom → cause → fix (merged table; owning skill in the unified skillgraph)

| Symptom | Likely cause | Fix | Owner |
|---|---|---|---|
| Viewers would leave in the first seconds | Logo-first, slow build, no tension | Visual change ≤ 0.5 s; outcome readable sound-off by 1–3 s; frame 0 = thumbnail | D2.2 |
| "Looks like a slideshow" | Everything enters at scene start, then nothing moves | Reveal on voice cues across the scene; one primary motion at a time; one ambient motion on decoratives | D6.3 |
| "Looks generic / AI-made" | Defaults: gradient text, cyan-on-dark, centred card grids, monoculture fonts, bounce everywhere, template look; delegated choices | Sampling gate; concept from the subject's own vocabulary; tokens from brand truth; name the rejected typical direction; pin screens, hex, font, tempo, avoid-list, ending | D1.4, D3.1, D8.2 |
| Everything moves at once; nothing reads | DOM-order staggers; no build/breathe/resolve; same ease everywhere | Stagger by importance (< 500 ms); build 0–30 / breathe 30–70 / resolve 70–100; vary eases; text lands and holds while read | D6.3 |
| Flat, web-page frames | Web sizes and opacities; single focal point; centred-and-floating | Headline 64–120 px, decoratives 12–25 %; three layers; two focal points; edge-anchored zones | D3.3, D3.4 |
| Text cannot be read | Too small, too brief, too thin, low contrast | Size floors; hold ≥ max(1.5 s, 0.5 + 0.4 s × words); medium weight; scrim; contrast on the worst frame | D3.2 |
| Feels rushed | Too many words for the time | Cut copy — never speed up the voice; add holds after payoffs | D2.3, D6.2 |
| Feels slow | Long eases, dead air, late slow pans | Use the energy band; remove back-half pans; tighten non-payoff holds; animation map for dead zones > 2 s | D6.2, D3.5 |
| Transitions feel random | Too many types; no relation logic | One primary (60–70 % of cuts) + ≤ 2 accents by meaning; velocity-matched seams; the transition owns the exit | D6.5 |
| Scenes look unrelated | No shared tokens | One `frame.md`; review the contact sheet as one film | D3.1 |
| Still frame, no motion in render | Timeline not registered under the root id, or registered before the async build finished; ambient on bare `gsap.to()` | Register `window.__timelines["<id>"]` after the build; ids identical (host = template = key); move ambient tweens onto `tl` | D6.1, D5.3 |
| Element invisible / flashes at frame 0 / skips entrance | `from()` immediateRender; overlapping transform tweens; relative tweens; counter text set on load | `fromTo` with explicit values; split parent/child transforms; absolute times; set text only from the tween | D6.1, D6.4 |
| Black flash between beats | Scene timeline shorter than its slot (older versions) | Current core: slots hold the last frame; if the flash appears, pad the timeline `tl.to({}, {duration: SLOT}, 0)` — harmless | D6.1 |
| Captions in preview, absent in render | Implicit start/end values; wall-clock timing | Explicit start and end values; captions driven by word timings on the timeline | D6.1, D2.5 |
| Clip starts at 0 unexpectedly | Relative `data-start` without spaces, typo, target without duration, cycle | Fix the reference; snapshot to confirm | D5.2 |
| Last frame never shows | End state landed exactly at `data-duration` (half-open window) | Land end states slightly before the end | D5.2 |
| Silent render / missing bed | `<audio>` without `id`; BGM still generating; volume lane conflict | Add ids; `wait-bgm` before render; automation lane, not a volume tween | D5.4, D7.5 |
| Voice buried / music fights speech | Bed only ducked; vocals or melody in the voice band; mixed to preview volume | Carve against the voice group (0.8; lower if notched); bed −14 to −20 dB under speech; instrumental; measure the delivered file | D7.2, D7.5 |
| SFX constant, loud, cartoonish | Whoosh per cut; same sample repeated; hits every few seconds; early onsets | Budget by style; one sound per stagger; 2–4 variants; hero hits ≥ 15 s apart; on the contact frame or +1, never early | D7.3 |
| Music feels wrong | Chosen by default; genre stereotype; wrong BPM for the cut | Re-run the decision rule; paste-ready brief with emotion and listening context; cut on bars; compare against ambience-only | D7.2 |
| Quiet or distorted after upload | Mix not targeted; premix measured instead of the file | −14 LUFS ±1 (social), ≤ −1 dBTP; measure the delivered file | D7.5 |
| Captions drift or cover things | Stale captions; wrong zone | Re-transcribe the final audio; place inside the safe box | D2.5, D3.4 |
| Data looks misleading | Truncated bars, rescaling, overshoot, too many series | Zero baselines; staged ~1 s changes; no overshoot on marks; ≤ 5–7 series, one highlighted; object constancy | D6.6 |
| Banding on dark backgrounds | Full-screen linear gradient; low-quality encode | Radial or solid + local glow; 2–4 % grain; CRF ≤ 18 masters | D3.3 |
| `check` says "0 samples" / 0/0 text checks | A lint error disabled the audits | Clear lint errors first, then trust the numbers | D5.6 |
| Render ~45 s slower per scene; static scenes | Host id, scene id and timeline key differ; root never registers a timeline | Make the three ids identical; `data-no-timeline` for timeline-free roots | D5.3 |
| Sub-comp renders as tiny unstyled text | `<style>`/`<script>` outside the `<template>` | Move them inside; style the root as `#root` | D5.3 |
| Tiny output file | GSAP (CDN) failed to load | Serve GSAP locally; check the file size before judging the film | D5.1 |
| Render differs from preview | Capture path; worker count; fonts | `--docker` for parity; pin `--workers`; embed fonts | D5.5 |
| Blur flicker, white bars, Chrome out of memory | Multi-worker capture on heavy compositions | `--workers 1` (or 3) for blur- or video-heavy finals | D5.5 |
| Wrong font in render | Family not embedded; generic family mapped to Inter; cloud fetch refused | `@font-face` for every brand face; verify with a snapshot | D4.5 |
| Video stuck on frame 0 inside a scene | Video inside a timed wrapper; animating the `<video>` itself | Time the wrapper **or** the video, never both; animate a wrapper; snapshot each video scene | D5.4 |
| Choppy music in render | MP3 bed re-encoded | Keep beds as WAV | D7.2 |
| Hosted agent ignored hard specs | Spec drift across turns | Restate aspect, length, voice, avoid-list, acceptance in full at every turn; open the file and verify | D8.2 |
| Things nobody asked for appear | Agent initiative | Scope lock: propose additions before adding scenes, narration, music, captions or transitions | D8.2 |
| "What was the point?" | No single objective; competing messages | Re-brief: one message, one action | D1.1 |
| Slow renders, heavy effects | WebGL/3D for simple motion; blur and filters everywhere | CSS and GSAP first; budget effects to hero beats; `--workers 1` | D6.6, D5.5 |

## 3. Prompt-level failure modes (when the fix is in the prompt, not the file)

| Failure | Prompt-level fix | Verify with |
|---|---|---|
| Web-page look | Video-scale type, planes, edge anchoring; read the house style first | Judge: visual |
| Slide-deck feel | Carry one element across each cut; cut mid-motion; transitions caused on screen | Transition strips |
| Everything appears at once | Stagger by importance; time entrances to the voice | `before` assertions |
| Titles drift or "breathe" | Land and hold; only live elements move | Strips; judge |
| Bounce on text, UI or counters | Overshoot only on physical objects; counters never exceed their final value | Strips |
| Dead or frozen scene | Real activity: data, footage, camera travel with intent | `keepsMoving` |
| Jump at a cut | Match position and speed; name the timestamp | Strips |
| Collisions or overflow | Write overlaps out ("A gone by 4.2 s; B at 4.2 s") | `check` layout |
| Paraphrased copy | Quote all copy with "/" for line breaks | Text diff |
| Invented facts or fake UI | Claim ledger; asset paths; labelled placeholders | Gate |
| Generic look | Named bans plus tokens, or a pitch round | Judge: originality |
| Brand drift | Design spec as law | Adherence report |
| Music fights the voice | Measure levels, then carve against the voice group | Audio-only pass |
| Effects on everything | Budget in events; sound the cause; leave part effect-free | Count |
| "No narration" read as silence | Name present and absent audio layers | Brief |
| Script and length mismatch | "~N s"; duration follows the voice | ffprobe |
| Correction oscillation | Absolute targets; one variable; freeze what works | Score change |
| Premature "done" | Checklist, completion condition, continuation cap, evidence | Report |
| Gaming the gates | Never loosen gates; never add motion to pass | Diff of gate files |

## 4. Improvement ladder (nothing is broken, but it is not exceptional)

1. Sharpen the **message**; cut any beat whose *why* does not trace to it.
2. Replace the **hook** with a different type; make frame 0 a thumbnail; visual change ≤ 0.5 s.
3. Lock the **system**: one accent, two voices, one light, one shadow recipe, one signature move.
4. Re-choreograph the **weakest scene**: verbs, stagger order, one ambient motion, a hold.
5. Re-cut to the **grid**: beats on bars, hero on a downbeat, one designed silence before the key line.
6. Re-mix: carve, level stack, limiter at −3 dBTP, measured loudness; phone and mono check.
7. Re-verify with the scorecard and the rubric; record the lift in `HANDOFF.md`.

## 5. Coaching method (COACH mode)

For every lesson: **principle** (what and why, with its evidence tag and source) → **the number** (the default and when to break it) → **an example** from the exemplar library (KB-10) → **a ten-minute exercise** ("take your weakest scene; give every element a verb; re-time the first motion to +0.2 s; re-snapshot") → **what to watch for** in the learner's next film. Adapt depth to the learner: a client needs the outcome and the decision; a marketer needs the brief fields and the hook rules; a designer needs the type, colour, motion and transition numbers; an engineer needs the contract, lint rules and render facts. Teach in the learner's language (English or French). Never lecture where a table will do; never give a rule without its reason; end with the one habit that would have prevented the problem.

### Coaching quick-cards (the ten lessons most often needed)

1. The message line and the delete tests. 2. Why the first frame is the thumbnail and why the hook speaks the viewer's language. 3. Build / breathe / resolve and "the transition owns the exit". 4. Easing is emotion: `.out` in, `.in` out, `.inOut` move; vary. 5. Video scale is not web scale (sizes, opacities, padding). 6. One accent, one light, one shadow recipe, one signature move. 7. The music decision rule and the mute test. 8. SFX on the frame, never early; one sound per stagger; silence before the key line. 9. The HyperFrames contract's silent killers (ids, `fromTo`, ambient on the timeline, half-open window, relative timing). 10. Measure, don't guess: lint → check (audits ran) → strips → ffprobe → ebur128 → separate judge.
