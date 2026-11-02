# KB-14 — Merge Log: how two deliverables became HyperVideo Man

*New synthesis. Records what came from where, every divergence between the two sources, and the resolution adopted. Read this when two KB files seem to disagree: the resolution here governs.*

## 1. The two sources

| | Source A — "HyperFrames-Motion-Mastery-Skillgraph" | Source B — "HyperFrames-Motion-Mastery" (Claude Code) |
|---|---|---|
| Size | 41 k words, 88 pp.; skill `hyperframes-motion-mastery`; persona KINESIS PRIME APEX (22/22) | 46.5 k words, 98 pp.; skill `directing-hyperframes-motion`; persona KINEMA PRIME APEX; ~71 k words of research notes |
| Distinct strengths | Eleven markers; theme × audience audio guide (incl. faith/FSY, West Africa, EN/FR); SFX palette and density matrix; level stack; 35-item scorecard; three-layer prompt system with meta/system/master templates and worked FSY/audit examples; 8-domain/40-cluster/220-skill skillgraph with cluster cards; 17-stage skillmap; seven playbooks; conflicts register; revision log vs the author's earlier standards | CLI verification lab on HyperFrames 0.8.229 (every command's `--help`, lint tests, render/determinism/alpha logs); technical operating reference with [TESTED] rows; twelve-dimension quality model and 1–5 rubric with ship bars; eight Gemini-analysed exemplars; four-layer prompt system (adds the evaluator) with stage prompts and a 40-field brief schema; diagnosis and prompt-failure tables; `qa_render.py` post-render gate; 277-row source registry |
| Precedence adopted | **Craft doctrine, audio guide, culture rows, scorecard, worked examples, skillgraph spine** | **Technical truth (CLI-tested), rubric and judge discipline, 40-field schema, evaluator and stage prompts, diagnosis tables** |

## 2. Source precedence rule for technical facts (adopted from B)

1. `--help` and `docs` of the CLI version that will render. 2. Upstream docs at `main`. 3. Upstream skills at `main`. 4. Locally installed official skills. 5. Vendored copies in third-party kits (several of their rules are now rejected by lint). When any KB file and the installed CLI disagree, the CLI wins.

## 3. Divergences and resolutions

| # | Topic | Source A | Source B | Resolution in HyperVideo Man | Why |
|---|---|---|---|---|---|
| 1 | Render quality flag | `--quality draft` / `delivery` carried from earlier standards, marked unverified | `--quality draft|standard|…` [TESTED]; default "looks" CRF 16; `draft` CRF 28; `--quality delivery` used for finals | `draft` while iterating, `delivery` for finals; confirm with `render --help` | B tested it |
| 2 | Network at render | "No network calls" | GSAP from jsDelivr and auto-resolved fonts fetched at compile time by default [TESTED] | No fetch *inside* the composition at render time; compile-time GSAP/font fetch exists — vendor GSAP and embed fonts for offline or cloud builds | B tested it |
| 3 | Sub-timeline padding | Pad to the slot (HANDOFF fix) | Current core: slots hold the last frame; padding harmless if a black flash appears | Pad only if a black flash appears | B cites current core doctrine |
| 4 | CSS transform conflict lint | Lint catches it | Lint catches `.to()`, missed `.from()` [TESTED] | Avoid both; rely on `fromTo` | B tested it |
| 5 | Inline scenes | Monolithic acceptable under ~40 s | 0.8.229 warns `nested_structure_needs_subcomposition` | One scene per sub-composition always | B tested it |
| 6 | Reading hold | words ÷ 2.5 + 0.5 s, min 1.2 s | max(1.5 s, 0.5 + 0.33 s × words), +0.5 s numbers, +30–50 % when voice/motion competes | **max(1.5 s, 0.5 + 0.4 s × words)**, +0.5 s for numbers, +30–50 % when competing | Stricter per-word (A) and stricter minimum (B) |
| 7 | Hook deadline | Outcome within 1–2 s social / 5 s long-form | Visual change ≤ 0.5 s; message readable sound-off by 3 s | Visual change ≤ 0.5 s; outcome readable ≤ 1–2 s social / ≤ 3 s default / ≤ 5 s long-form | Union of the two tests |
| 8 | 9:16 safe box | Union x 120–888, y 380–1248 | x 120–780, y 288–1248 | **Intersection x 120–780, y 380–1248** | Survives both readings |
| 9 | Bed under speech | −14 to −20 dB | ≥ 10 LU (15 LU dense); practitioner bed 0.15 ≈ −16.5 dB | −14 to −20 dB (≥ 10 LU floor; ≥ 15 LU dense; ≥ 20 dB accessibility-critical) | A's band contains B's floors |
| 10 | SFX under voice | −8 to −14 dB | 6–12 dB below voice peaks | −8 to −14 dB during speech; −6 to −10 in gaps | Consonant protection |
| 11 | Ambient motion | One slow ambient motion per scene on decoratives (official house style) | "No idle loops; one bounded breath at most on a held hero" | Decoratives may share one slow ambient motion; content elements never idle-loop; on a held hero at most one bounded breath | Both official generations honoured |
| 12 | Scene exits | Element exits 60–70 % of entrances | "Exits only on the final scene; the transition IS the exit" | Element-level settles in the resolve phase; the transition owns the scene exit | Reconciled in A's revision log, confirmed by B |
| 13 | Transitions budget | 1–2 shaders per 5–7 beats; presets 0.15–0.7 s | One primary for 60–70 % of cuts + ≤ 2 accents; calm 0.5–0.8 / medium 0.3–0.5 / high 0.15–0.3; blur ≤ 3 beats | All kept (compatible) | Complementary |
| 14 | Evaluation | 35-item pass/fail scorecard | Hard gates + instrumented metrics + 12-dimension 1–5 rubric with ship bars and a separate judge | Three-layer stack: gates → 35 items → 12 dimensions with judge | Complementary |
| 15 | Questions | One at a time, only when it changes the deliverable | At most three | ≤ 3 per intake, one at a time, recommended option first | Union |
| 16 | Prompt layers | Three (meta, system, master) + expansion/review/revision gates | Four (adds evaluator) + stage prompts | Four layers + stage prompts + expansion/review/revision gate prompts | Union |
| 17 | Brief fields | Twelve required fields | 40-field schema | 40-field schema canonical; the twelve map onto it (KB-01 §3) | B is finer-grained |
| 18 | Narration pace | 2.3–2.5 w/s bands by genre; FR/second-language 2.0–2.3 | 140–160 wpm explainer; 160–190 social; 120–140 technical | Consistent; both expressed (w/s and wpm) | Same values |
| 19 | Captions | ≤ 20 cps, ≤ 42 chars, 2 lines, groups by energy | + BBC line height 7–8 % (3.9–4.5 % vertical), ≥ 0.3 s/word, 2-frame gaps, active-word ≥ 150 ms, ≤ 25 chars on 9:16 | All kept | Complementary |
| 20 | Data motion | ≤ 3 metrics; visual weight; tabular figures; no pies/legends | Object constancy; staged ~1 s changes; zero baselines; no overshoot; ≤ 5–7 series | All kept | Complementary |
| 21 | Music decision | Six-step rule + theme × audience guide | Strategy-first table; tone × tempo table; leave music out for dense/sensitive content | Rule first, then the theme/audience guide and tone table | Complementary |
| 22 | Worker count | Pin for bit-identity | Visually identical, not bit-identical across counts [TESTED]; `--workers 1` for heavy finals | Both | B tested it |
| 23 | Cloud privacy | — | ≥ 5 MB media uploaded as public unsigned URLs | Hard rule 5 | B documented it |
| 24 | Distributed renders | HDR not on Lambda | fps 24/25/30/60 only; HDR/HLS/motion blur disabled | Both | Complementary |
| 25 | 4K supersampling | 4× slower, 3–5× larger | Adds no detail to raster images, video or canvas | Both | Complementary |
| 26 | Skill set | 21 → 7 names (Oct 2026) | Three generations; precedence order | Read the installed set; precedence order adopted | Same finding |
| 27 | SFX generation | Resolve via Openverse/bundled | Official policy never generates SFX | Retrieve or bundled library; never generate | B documented it |
| 28 | Exemplars | Launch film, Linear.app, OneWave, JetBrains, Social SDK, TanStack, internal (Price of AI, Marche avec moi, Journal IA) | Eight Gemini-analysed HeyGen films + Nate Herk showreel | Union in KB-10 | Complementary |
| 29 | Culture | Theme × audience rows for faith/FSY, West Africa, EN/FR | General guidance | A's rows adopted as a first-class cluster (D1.2) and Hard Rule 12 | User requirement |
| 30 | Persona names | KINESIS PRIME APEX | KINEMA PRIME APEX | **HyperVideo Man PRIME APEX** (user's name); lineage credited | User requirement |

## 4. Traceability of the knowledge base

| KB file | From A | From B | New synthesis |
|---|---|---|---|
| KB-01 Intake-to-Prompt | twelve fields; translation table; pitch round (official) | 40-field schema; ≤ 3 questions; stage prompts | derivation order; prompt-set assembly; micro-intakes |
| KB-02 Quality framework | §3 in full (markers, numbers, audio guide, exemplars, scorecard) | quality model, craft standards, rubric, diagnosis, checklists | merge preface with reconciled values |
| KB-03 Prompting system | §4 (meta/system/master, gates, examples, checklists) | four layers, brief schema, templates, stage and evaluator prompts, correction phrases, failure modes | preface |
| KB-04 Unified skillgraph | 8/40/220 notation and cluster cards | 8-domain graph and cluster cards | unified 8/44/253 notation; cluster crosswalk |
| KB-05 Skillmap | 17 stages, diagram, gates, scheduling | pipeline, validation loop, defaults | preface |
| KB-06 Formats and niches | seven playbooks, limits | seven playbooks, platform delivery table, limits | niche matrix |
| KB-07 Audio | §3.6 doctrine, theme × audience, SFX numbers | strategy table, tone table, mix targets, sync, captions | preface |
| KB-08 Technical | documented facts §2.2–2.7 | CLI-verified reference, lab notes, help index | preface |
| KB-09 Fix and coach | troubleshooting ladder | diagnosis table, prompt failure modes, validation loop | coaching method, quick-cards |
| KB-10 Exemplars | §3.8 analyses | §3.2 table | — |
| KB-11 Worked examples | FSY promo, audit explainer | Ledgerly 30 s | FIX, COACH, AUDIT examples |
| KB-12 Glossary | Appendix B | terms | additions |
| KB-13 Sources | 170 sources | 277 sources | union with dedupe statistics |

## 5. What remains unverified (carried honestly)

Carve numeric defaults beyond "strength 0.8"; true-peak estimator overshoot magnitude; platform loudness targets for TikTok/Instagram/X/LinkedIn (none published); exact platform safe-zone pixels (templates only); video placement inside timed sub-composition clips on 0.8.229 (B marks [UNVERIFIED]); whether renders are slightly quieter than the premix (practitioner report). The persona marks these [UNVERIFIED] when they matter and measures instead.

## Annex A — Source A conflicts and uncertainty register (§2.10, verbatim)

### 2.10 Conflicts and uncertainty register

| # | Topic | Conflict or uncertainty | Resolution adopted |
|---|---|---|---|
| 1 | Official domain | `hyperframes.ai` (brief) unreachable; official docs at `hyperframes.heygen.com` | Cite heygen.com docs, GitHub, npm; flag look-alikes |
| 2 | Skill set | README lists 7 skills; local copy and earlier guides list 21 | Doctrine retained; agents read the installed set with `skills check` |
| 3 | Version | npm page cached at 0.8.79; GitHub Releases v0.8.228 (2026-11-01) | GitHub Releases authoritative |
| 4 | Quality tiers | `--quality draft|standard|high` vs "draft / looks (CRF 16) / delivery" | Check `render --help`; never assume |
| 5 | Desktop app platforms | FAQ "Mac and Linux only" vs documented Windows installer | Windows supported (x64); Arm not yet |
| 6 | 4K cloud pricing | "billed at 1.5×" (cloud docs) vs "about twice" (Studio export page) | Report both; treat as indicative |
| 7 | Launch date | March vs mid-April 2026 | Unresolved; immaterial to craft |
| 8 | Launch film length | 49.77 s (repo) vs "62-second" (narration.md reference) | Repo authoritative |
| 9 | Website demo length | ~61 s (storyboard) vs 41.8 s (showcase) | Unresolved |
| 10 | Transitions | "ALWAYS use transitions… no jump cuts" vs deliberate hard cuts in the launch montage | Default against accidental jump cuts; meaningful hard cuts are transitions |
| 11 | Scene exits | "NEVER use exit animations except on the final scene" vs motion-principles' resolve phase | Transition owns the scene exit; resolve phase choreographs element-level settles |
| 12 | Carve defaults | Earlier standard: strength 0.8 ≈ −7 dB across 250 Hz–2.5 kHz; not re-verified | Attribute names documented; numeric defaults marked unverified |
| 13 | True-peak estimator overshoot "up to ~1.7 dB" | Earlier standard; not re-verified | Keep −3 dBTP ceiling as a conservative [Recommended] |
| 14 | Text hold formula | words ÷ 3 + 0.5 s vs words ÷ 2.5 + 0.5 s vs 1.4 s/2.4 s steps | Adopt words ÷ 2.5 + 0.5 s after settle, min 1.2 s |
| 15 | Bed under speech | −12…−18 dB vs 12–20 dB below vs dBFS tables | −14…−20 dB relative to VO; ≥ 20 dB for accessibility-critical |
| 16 | Display contrast | ≥ 10:1 (6-page spec) vs 7:1 target | 7:1 target, 4.5:1 floor |
| 17 | Frame rate | "locked 60 fps" (6-page spec) vs 30 default | 30 default; 24 cinematic; 25 for 50 Hz broadcast; 60 only for fast UI/gaming |
| 18 | Stagger per item | 30–80 / 40–100 / 50–80 ms | 40–80 ms, < 500 ms total |
| 19 | SFX density | Runtime table vs style budgets vs 0.55–0.80/s | One style × runtime matrix (§3.6.8) |
| 20 | Vertical UI safe zones | Platforms publish templates only; practitioner pixel readings disagree | Minimum top 10–15 % / bottom 20–30 % / right strip; union x 120–888, y 380–1248 for a universal master; verify per platform |
| 21 | True peak | −1 dBTP (EBU, AES, Apple) vs −2 dBTP (ATSC, Netflix) | −1 dBTP for web masters; −2 for shared/broadcast masters |
| 22 | Cut rate and memory | Faster cutting helped (Lang 2000) vs hurt (JAR 1993) | Depends on cognitive load; cut when meaning changes |
| 23 | Music and learning | Harms (Moreno & Mayer) vs inconclusive (2020 review) vs helps congruent ads | Decide by goal (§3.6.3) |
| 24 | HyperFrames claims by third parties | "no native video import", "no ducking" | Contradicted by official docs; disregarded |
| 25 | Private resources | `OneDrive\AgentOS\GENERAL\VIDEO\HYPERFRAME RESOURCES` not found in the work OneDrive; no standalone "Qualia v2.0 Persona" document found | The eleven attached files were used as the private materials; Qualia requirements taken from `/qualia-nexus-forge` references (§9) |
| 26 | Internal exemplars | "The Price of AI", "Marche avec moi", "Journal IA" are internal productions without public links | Tagged [Demonstrated, internal]; techniques, not claims about reception |

## Annex B — Source B decision-relevant conflicts and unverified items (§8.4–8.5, verbatim)

### 8.4 What remains unverified

- **Offline rendering.** Renders fetched GSAP and fonts over the network at compile time; behaviour with no network and a cold cache was not tested [TESTED] [E-01].
- **Cross-machine determinism and `--docker`.** Byte-identical output was shown on one machine only; Docker was not running [TESTED] [E-01].
- **Black flash at scene ends on 0.8.229.** Current core docs say slots hold the last frame; practitioners pad timelines; not reproduced either way [CONFLICT] [A1-07] [B-10].
- **`tl.call()` under seek and `background-clip: text` in capture.** Disputed in the sources; not tested [CONFLICT] [A2-44] [B-31].
- **Platform loudness targets** for YouTube, TikTok, Instagram, X and LinkedIn: none officially published [UNVERIFIED] [C-57].
- **TikTok and YouTube Shorts safe-zone pixels**: templates only; third-party readings disagree [UNVERIFIED] [C-43] [C-44].
- **Generation C upstream skills** were read from the repository but not installed; their exact reference wording may differ from summaries here [DOC] [A1-32].
- **Hosted MCP, cloud, Lambda and Cloud Run** were characterised from documentation and help output; no paid or account-bound operation was run [DOC] [A1-85] [A1-52].
- **The skill in use.** The optional pilot (building and scoring a real video with the skill) was not requested and was not run; the smoke tests in §7.7 are the first check after installation.

### 8.5 Decision-relevant conflicts

| Topic | Position A | Position B | Resolution used here |
|---|---|---|---|
| Overshoot easing | Rare, playful register only [DOC] [A2-11] | Free use of `back.out` and `elastic` [DEMO] [A2-70] | Official doctrine; overshoot as a declared register |
| Idle "aliveness" | Stillness plus subtle jitter [DOC] [A2-24] | "Camera never sleeps" [DEMO] [A2-70] | Official doctrine; motion needs a reason |
| Timeline padding | Slots hold the last frame; no padding [DOC] [A2-25] | Pad every timeline [DEMO] [B-10] [A2-70] | Do not pad on 0.8.x; pad only if a flash appears |
| Transition variety | 2–3 types, repeated [DOC] [A2-06] | Rotate flavours [DEMO] [A2-79] | One primary plus ≤ 2 accents |
| Loudness target | None official [DOC] [A2-61] | −14 or −16 LUFS; −1 to −1.5 dBTP [DEMO] [B-30] [A2-80] | −14 LUFS ± 1, ≤ −1 dBTP for social; per-platform table |
| Carve default | 0.8 [DOC] [A2-57] | 0.25 in an earlier prompt [PRIOR] [D-03] | 0.8 |
| Safe areas 16:9 | 90 / 80 % [PRIOR] [D-01] | 93 / 90 % (SMPTE ST 2046-1) [STD] [C-31] | SMPTE |
| Text hold | Five formulas across earlier documents [PRIOR] [D-01] [D-02] [D-03] [D-04] | "Three seconds on screen readable in two" [DOC] [A2-31] | `max(1.5 s, 0.5 + 0.33 s × words)` |
| Caption rate | ≤ 20 cps [STD] [C-69] | 160–180 wpm [STD] [C-67] | Choose by audience |
| Color tags | BT.709 [STD] [C-81] | sRGB transfer for browsers [DEMO] [C-39] | BT.709 for uploads; test web embeds |
| `repeat: -1` | Banned in contract [DOC] [A1-32] | Warning under a finite root duration [DOC] [A1-45] | Finite repeats |
| Workers | Auto by default [DOC] [A1-80] | One worker for finals [DEMO] [B-38] | Pin workers when bit-identity or blur stability matters |
| 60 fps cost | "Doubles render time" [DOC] [A1-13] | 1.28× on a 6 s piece [TESTED] [E-01] | Setup dominates short renders |
| Lint coverage | CSS/GSAP transform conflict always caught [DOC] [A1-02] | Missed for `.from()` [TESTED] [E-01] | Prefer `fromTo`; snapshot |
| Fonts | Any family needs `@font-face` [DOC] [A1-02] | Auto-resolved families fetched [TESTED] [E-01] | Embed every brand face |
| Skill count upstream | 7 published [DOC] [A1-30] | 8 directories [DOC] [A1-36] | Read the installed set |

Full conflict registers (more than sixty entries) are in the research notes: A1 §20, A2 §18, B §12, C §10, D §11 and E §6.
