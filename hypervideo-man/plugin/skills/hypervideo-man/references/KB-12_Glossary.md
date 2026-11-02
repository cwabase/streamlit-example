# KB-12 — Glossary

*Part I is Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026) Appendix B; the additions table covers terms introduced by Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229) and by the merge.*

## Part I — Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026) — Appendix B

### Appendix B. Glossary

| Term | Meaning |
|---|---|
| Beat | One unit of the storyboard: a scene with a job, a duration and a hand-off |
| Bed | Background music under a voice |
| Button | A clean musical ending on a hit, as opposed to a fade |
| Carve | A voice-aware spectral and level cut in the bed (`data-fx-carve`), deeper than a plain duck |
| Clip | Any DOM element with `data-start` (and `class="clip"` by convention); the framework owns its visibility |
| Composition | An HTML file that describes a video; the root carries `data-composition-id` |
| Contact sheet | One image of many frame snapshots, used to review a film at a glance |
| Duck | A level reduction of the bed while the voice speaks |
| Expansion | The step that turns an approved plan into per-scene production specs (`.hyperframes/expanded-prompt.md`) |
| Frame worker | A sub-agent that builds one scene from the expanded prompt and the confirmed still |
| `frame.md` | The frame-scale design spec: frontmatter tokens (normative) plus prose (context) |
| Half-open window | A clip shows while start ≤ t < start + duration |
| Hero moment | One of the 2–5 biggest moments of a film: reveal, stat, lock-up |
| J-cut | Sound from the next scene (or an SFX tail) starting before the picture changes |
| LUFS / LKFS | Integrated loudness units (identical scales) |
| dBTP | True-peak level, accounting for inter-sample peaks |
| Pitch round | The intent layer's divergent step: five concepts, two below the median |
| Recipe | A frozen bundle of a proven run (design spec, storyboard skeleton, brief skeleton, confirmed values) |
| Reverse iceberg | Value before evidence; implementation is the footnote |
| Rhythm pattern | A named sequence of scene speeds (fast-fast-SLOW-fast-HERO-hold) declared before HTML |
| Run shape | `flow` (automation / companion) × `storyboard` (yes / no) → `mode` (collaborative / autonomous) |
| Signature move | One recurring brand motion that threads the film |
| Suck-out | Dropping music and ambience 0.3–1 s before the biggest hit |
| Velocity matching | Exit and entry eases whose fastest points meet at the cut |


## Additions from the merge

| Term | Meaning |
|---|---|
| 40-field brief schema | Source B's intake schema (identity, audience, message, creative direction, visual system, structure, motion, audio, technical, outputs, acceptance); canonical in HyperVideo Man; the twelve fields of source A map onto it |
| Carve | HyperFrames audio ducking of one group against another (`data-audio-carve`); default strength 0.8 against the voice group |
| `data-volume` | Linear gain on a media element: 0.5 ≈ −6 dB, 0.25 ≈ −12, 0.1 = −20, 0.6 ≈ −4.5, max 3.98 (+12) |
| Evaluator prompt | The fourth prompt layer: a separate judge that sees only evidence (stills, strips, measurements) and scores the twelve dimensions |
| Hard gate | A binary check that blocks release (lint 0, check 0 with audits run, ffprobe within one frame, loudness within ±1 LU, fonts embedded, claims matched) |
| Judge separation | The rule that the model that built a scene never scores it; scores without evidence default to 2 |
| Motion sidecar (`*.motion.json`) | Assertions evaluated by `check`: appearsBy, before, staysInFrame, keepsMoving |
| Quality tiers | `render --quality draft|standard|…`: default "looks" ≈ CRF 16; draft ≈ CRF 28; `delivery` for finals (verify names on the installed version) |
| Ship bar | Twelve-dimension rubric threshold: no dimension below 3 and an average ≥ 4.0; exceptional = none below 4, average ≥ 4.5 |
| Stage prompts | Per-stage instructions (plan · sketch · build · verify · refine · deliver) that carry the hard specs into each step |
| `sweep_static` | The `check` audit that fails a span of 3 s or more with no visual change |
| Surgical prompt set | HyperVideo Man's PROMPT-mode deliverable: META + SYSTEM + MASTER + STAGE + EVALUATOR, with the intake table, the pipeline, the tips and angles and the acceptance stack |
| Three-question rule | At most three clarifying questions per intake, one at a time, recommended option first; everything else defaulted with a logged reason |
| Twelve dimensions | Purpose & audience fit · story & structure · pacing & rhythm · composition & hierarchy · typography & legibility · colour, light & depth · asset quality & art direction · motion language · transitions & continuity · sound & sync · accessibility & safety · coherence & technical integrity |
| Watch three ways | FIX-mode first step: with sound, muted, sound only — then freeze three frames (first, weakest, last) |
