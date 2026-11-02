# KB-08 — HyperFrames Technical Reference

*Composite. Part I is Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229): the technical operating reference with [TESTED] rows (which source wins, environment, project layout, composition contract, command map, lint rules observed, render facts, troubleshooting). Part II is Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026) §2.2–2.7: the documented architecture, workflows and routes, capability menu, tooling, limitations and troubleshooting, plus Appendix C's command quick reference. Part III is B's hands-on lab (pass/fail summary, command and flag reference from `--help`, gotchas, conflicts between skill docs and CLI behaviour). Part IV is the raw `--help` index captured in the lab. The installed CLI's `--help` always wins over any line here.*

*Section numbers inside each part keep the numbering of the source they came from (A = §2–§7 and appendices of the Skillgraph document; B = Parts 3–8 of the Claude Code document). Where the two parts disagree, the preface and KB-14 govern; where either disagrees with the installed CLI, the CLI wins.*

## 0. The contract HyperVideo Man restates every build turn

root `data-composition-id`, `data-start="0"`, `data-width/height`, `data-duration` = runtime (read before scripts; variables cannot change it) · every timed element `data-start` (+ `data-duration` for divs/sub-comps) + `class="clip"`; half-open window — land end states before the end · one paused GSAP timeline per composition at `window.__timelines["<id>"]`, registered after the build; host id = template id = timeline key · sub-comps in `<template>` with `<style>`/`<script>` inside, scene root styled as `#root`; one scene per file · `fromTo` with explicit values, absolute times, ambient on the timeline, never tween a `.clip`'s visibility, never pair a CSS transform with a GSAP tween on the same property (lint catches `.to()`, not `.from()`), never tween width/height/top/left/fontSize/letterSpacing · no `Date.now()`, rAF loops, timers, CSS `transition`, unseeded `Math.random()` or `stagger:{from:"random"}`; `repeat:-1` only under a finite root duration · every `<audio>` has an id (silent otherwise); `data-has-audio="true"` or `muted` on every timed video; no `crossorigin`; no `play()`; no video inside a timed wrapper; no base64 media; asset paths without a leading slash · fonts: bundled family or `@font-face` (Google fetch fails closed in cloud renders) · relative `data-start` needs spaces and fails silently to 0 — snapshot it · `data-track-index` is a Studio lane, `z-index` paints · a lint error silently disables `check`'s layout and contrast audits ("0 samples") · registry first (`catalog --query` → `add`) · GSAP and auto-resolved fonts are fetched at compile time by default — vendor them for offline or cloud builds · sub-comps hold their last frame; pad a short timeline only if a black flash appears · distributed renders accept 24/25/30/60 fps and disable HDR/HLS/motion blur · 4K supersampling adds no detail to raster media · `check` fails a 3 s+ static sweep; `*.motion.json` sidecars assert appearsBy / before / staysInFrame / keepsMoving.

## Part I — Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229) — technical operating reference

### HyperFrames technical operating reference

This reference is the operational core of the platform research: what to run, what the composition contract demands, what lint and `check` catch, how renders behave, and how to fix common failures. Rows tagged [TESTED] were reproduced on Windows 11 with `hyperframes@0.8.229`, Node 24.22.1 and FFmpeg 8.1.1 on 2026-11-01 [E-01]. The platform ships several releases a day, so always confirm against the installed CLI: `npx hyperframes --version`, `npx hyperframes <command> --help`, and `npx hyperframes docs <topic>`. When this file and the installed CLI disagree, the CLI wins.

#### Which source wins

Three generations of official skill text circulate: early copies vendored in third-party kits (written before `check` existed), the 21-skill generation of 2026-10-21, and the 7-skill upstream generation published from v0.8.185 onward, which retired the workflow skills [DOC] [A1-37]. When they disagree, use this order [REC]:

1. `--help` and `docs` output of the CLI version that will actually render.
2. Upstream docs at `main` (HTML schema, lint rules, rendering guide).
3. Upstream skills at `main`.
4. Locally installed official skills.
5. Vendored copies in third-party kits. Several of their rules are now rejected by lint: `crossorigin` on media, always-muted video with separate audio, no async timeline builds, `Math.ceil` repeat counts, `data-volume` capped at 1, `validate` as the gate [DOC] [A1-92] [A1-45].

Projects pin their CLI version in `package.json`; a pinned older CLI lacks newer commands and flags (for example 0.7.109 has no `timeline`, `history`, `usage`, `looks` quality or HLS output) [TESTED] [A1-81].

#### Environment checklist

| Item | Requirement | Evidence |
|---|---|---|
| Node.js | 22 or later (`engines.node >= 22`) | [TESTED] [E-01] |
| FFmpeg + FFprobe | On PATH | [TESTED] [E-01] |
| Browser | The CLI's pinned `chrome-headless-shell`; `npx hyperframes browser ensure` fetches it | [TESTED] [E-01] |
| Health check | `npx hyperframes doctor --json` always exits 0; gate on the Node, FFmpeg, FFprobe and Chrome checks, because `ok` is false on most desktops (optional AI tools absent, Docker stopped, low *available* RAM) | [TESTED] [E-01] |
| Network at render | Needed by default: the compiler inlines GSAP from jsDelivr and fetches auto-resolved fonts (Inter) from Google Fonts; registry `add` downloads items | [TESTED] [E-01] |
| Telemetry | `HYPERFRAMES_NO_TELEMETRY=1` disables it; `npx hyperframes telemetry status` reports the source | [TESTED] [E-01] |

#### Project layout created by `init`

`npx hyperframes init <name> --non-interactive` (add `--resolution portrait` for 1080×1920) writes [TESTED] [E-01]:

- `index.html`: the root composition, fixed 1920×1080 `html, body`, a root element with `data-composition-id="main"` and `data-duration`, GSAP loaded from a CDN, and `window.__timelines["main"] = tl`.
- `hyperframes.json`: registry URL and paths (`compositions`, `compositions/components`, `assets`), `media.autoProxy: true`.
- `package.json`: `dev`, `check`, `render`, `publish` scripts pinned as `npx --yes hyperframes@<version>`.
- `AGENTS.md` and `CLAUDE.md`, which point agents to the `/hyperframes*` skills; `meta.json`.

No `assets/` folder is created; add one for fonts, images and audio.

#### The composition contract

A composition is an HTML file whose DOM declares timing with `data-*` attributes, whose animation runtime is seekable, and whose media playback the framework owns [DOC] [S-09]. The rules that matter most:

1. **Timing lives in attributes.** The root needs `data-composition-id`, `data-width`, `data-height` and a duration source; its `data-duration` is read at compile time, before scripts run, so variables and scripts cannot change the render length [DOC] [A1-04] [A1-44]. Timed elements carry `data-start` and `data-duration` (seconds) and are visible over the half-open window `[start, start + duration)`, so land final poses slightly before the end [DOC] [A1-04]. Write `class="clip"` on timed visual elements (a convention the scaffold CSS and Studio rely on) [DOC] [A1-04]. Media adds `data-media-start`, `data-volume` (0 to 3.98, i.e. up to +12 dB) and `data-playback-rate`; `data-track-index` is a Studio display lane only and does not set paint order (use `z-index`) [DOC] [A1-04] [A1-44]. Sub-compositions mount with `data-composition-src` and are identified by `data-composition-id` [DOC] [S-09] [TESTED] [E-01].
2. **One paused timeline per composition**, registered on `window.__timelines["<composition-id>"]` after the build completes. Never call `play()`; never autoplay; never register before an async build finishes (lint `gsap_timeline_registered_before_async_build`) [DOC] [A2-10] [TESTED] [E-01].
3. **State is a pure function of time.** `fromTo` with explicit start values; absolute values, no relative `+=`; no `Math.random()` or `Date.now()`; finite repeats (`repeat: -1` only under a finite root `data-duration`; lint `gsap_infinite_repeat`) [DOC] [A2-03] [TESTED] [E-01]. GSAP's `stagger: { from: "random" }` uses `Math.random` and must not be used [TESTED] [A2-89].
4. **Animate wrappers, not timed clips.** Tweening a `.clip` element directly fails lint (`gsap_animates_clip_element`); animate an inner wrapper [TESTED] [E-01].
5. **Transforms and paint-only properties.** Never tween `width`, `height`, `top`, `left`, `fontSize` or `letterSpacing`; use `x`, `y`, `scale`, `rotation`, `opacity` [DOC] [A2-13] [A2-03].
6. **Do not fight CSS transforms.** A CSS `transform` plus a GSAP tween on the same axis is overwritten; lint `gsap_css_transform_conflict` catches `.to()` but missed `.from()` in testing [TESTED] [E-01].
7. **Sub-compositions hold their last frame**; current core guidance forbids padding timelines to the slot length (older kits padded them) [DOC] [A2-25] [CONFLICT] [A2-70].
8. **Media rules.** Every `<audio>`/`<video>` needs an `id` (otherwise it is silent in renders); `crossorigin` breaks preview; missing files fail lint (`audio_src_not_found`) [TESTED] [E-01]. Audio volume moves use `data-automation` lanes, never GSAP volume tweens [DOC] [A2-57].
9. **Fonts.** Unknown families without `@font-face` fail lint; auto-resolved families (Inter tested) are fetched at compile time; generic `sans-serif` is mapped to Inter [TESTED] [E-01]. Embed `@font-face` for every brand face [DOC] [A2-31].
10. **Structure.** In 0.8.229, inline scenes with child elements produce a `nested_structure_needs_subcomposition` warning: the root should be built from sub-compositions, one per scene [TESTED] [E-01] [CONFLICT] (the core skill's own minimal example triggers it).
11. **Two root forms.** A standalone `index.html` root sits directly in `<body>`; a sub-composition file wraps everything, including its `<style>` and `<script>`, in `<template>`, because only the template's contents are cloned into the host. Style the scene root as `#root`. The host's `data-composition-id`, the scene's id and the `window.__timelines` key must be identical, or every render waits 45 s per scene and shows static frames [DOC] [A1-07] [A1-33].
12. **More media rules.** A timed `<video>` needs `data-has-audio="true"` (keep its sound) or `muted`; never call `play()`, `pause()` or set `currentTime`; never time both a video and its wrapper; no base64 media [DOC] [A1-08] [A1-45].
13. **No browser clocks.** `requestAnimationFrame` loops, timers as clocks and CSS `transition` for visual change all run on the browser clock (lint `requestanimationframe_in_composition`, `css_transition_used`); seeded pseudo-random generators are allowed [DOC] [A1-05] [A1-45].
14. **Relative timing fails silently.** References such as `data-start="intro + 0.5"` need spaces; a typo or missing target resolves to 0 without an error, so snapshot every reference-timed clip [DOC] [A1-06].
15. **Asset paths** are written `assets/...` with no leading `/`, including inside sub-compositions [DOC] [A1-32].

#### Command map

| Job | Command | Notes |
|---|---|---|
| Check environment | `npx hyperframes doctor --json` | Gate on specific checks [TESTED] |
| Scaffold | `npx hyperframes init <name> --non-interactive [--resolution portrait]` | [TESTED] |
| Fast static feedback | `npx hyperframes lint [--json] [file.html]` | Exit 1 on errors, 0 on warnings only [TESTED] |
| Final gate | `npx hyperframes check [--json] [--snapshots] [--strict]` | Lint, runtime errors, failed requests, layout, motion sidecars, WCAG contrast, craft and audio sections in one browser session [TESTED] [S-11] |
| Stills and crops | `npx hyperframes snapshot --at 1.2,3.4` · `--frames 8` · `--range 3:5` · `--zoom "#cta"` | [DOC] [S-11] |
| Timeline facts | `npx hyperframes timeline --json` | Also edits: `move`, `trim`, `split`, `delete`, `set`, `duplicate` [TESTED] |
| Preview (Studio) | `npx hyperframes preview --background --no-open --port 3017`; `--status`, `--stop` | Injects `data-hf-id` attributes into source [TESTED] |
| Render | `npx hyperframes render --output renders/out.mp4 [--format webm|mov|gif|hls] [--fps N] [--quality draft|standard|…] [--workers N]` | See render facts below [TESTED] |
| Registry | `npx hyperframes catalog --query "<words>" --json`; `npx hyperframes add <name>` | Network-dependent; one item timed out twice [TESTED] |
| Version | `npx hyperframes@latest upgrade --project . --check` | [TESTED] |
| Skills | `npx hyperframes skills update <workflow>` | [DOC] [S-09] |
| Audio tools | `npx hyperframes normalize-audio --reference <id> --target <id>`; `audio`; `beats` | [DOC] [A2-61] [TESTED help] |
| Media | `npx hyperframes tts`, `transcribe --model <m>`, `remove-background` | [DOC] [A2-46] [A2-48] [A2-54] |
| Scale out | `cloud`, `lambda`, `cloudrun`, `--batch`, `--variables` | Not tested (cost and account side effects) [E-01] |

For flag-level detail run `npx hyperframes <command> --help`; the research dossier (Part 2 §2.5) records the 0.8.229 help output for all 51 commands.

#### Lint rules observed

| Rule | Severity | Trigger |
|---|---|---|
| `nested_structure_needs_subcomposition` | warning | Inline scene with children in the root |
| `gsap_css_transform_conflict` | error | CSS transform plus GSAP `.to()` on the same property (not `.from()`) |
| `gsap_animates_clip_element` | error | Tween targets a timed `.clip` |
| `gsap_timeline_registered_before_async_build` | error | Registration before an async build completes |
| `gsap_infinite_repeat` | error | `repeat: -1` without a finite root duration |
| `missing_timeline_registry`, `missing_gsap_script` | error | No registered timeline / no GSAP |
| `standalone_composition_wrapped_in_template` | error | File begins with `<template>` |
| `media_missing_id`, `media_crossorigin_breaks_preview`, `audio_src_not_found` | error | Media without id, with `crossorigin`, or missing file |
| `font_family_without_font_face` | error | Unknown font family with no `@font-face` |
| `clip_ends_past_root_duration` | warning | A clip ends after the root |
| `studio_missing_editable_id` | warning | Element lacks a Studio-editable id |

All rows [TESTED] [E-01]. The full rule set has 141 documented codes [DOC] [A1-45]. Two behaviours matter most:

- **Lint errors silently skip `check`'s layout and contrast audits.** A `check` report with "0 samples" means nothing was audited; fix lint errors first [DOC] [A1-02] [A1-35].
- **`check` thresholds and assertions.** Contrast is sampled at 5 points against 4.5:1 (3:1 for large text) and findings carry a suggested color; optional `<name>.motion.json` sidecars assert `appearsBy`, `before`, `staysInFrame` and `keepsMoving`; a composition of 3 s or more with no visible change fails `sweep_static`; `--strict` gates warnings [DOC] [A1-14].

`check` added a false-positive layout warning `rotation_pivot_drift` for a simultaneous translate-and-rotate tween, and a craft warning `first_frame_empty` when frame 0 shows only background [TESTED] [E-01].

#### Render facts

| Fact | Value | Evidence |
|---|---|---|
| Default MP4 | H.264 High, yuv420p, BT.709 tags, AAC-LC 48 kHz stereo; CRF 16 ("looks") | [TESTED] |
| Frame accuracy | 6 s at 30 fps rendered exactly 180 frames and 6.000 s | [TESTED] |
| `data-volume="0.6"` | −4.5 dB measured (expected −4.44 dB) | [TESTED] |
| Repeat renders | Byte-identical file, frames and audio with the same settings | [TESTED] |
| Worker count | Changes the capture path; visually identical (PSNR ≈ 60 dB), not bit-identical. Pin `--workers` when bit-identity matters | [TESTED] |
| Auto workers | ~8 s calibration; `--workers 1` was faster for a 6 s piece | [TESTED] |
| `--fps 60` | 1.28× the 30 fps wall time on 6 s (docs say 2×; setup dominates short renders) | [TESTED] [CONFLICT] |
| `--quality draft` | CRF 28, faster, but a larger file than default on flat graphics | [TESTED] |
| WebM | VP9 with `ALPHA_MODE=1`, Opus audio; ffprobe shows `yuv420p`, so decode with `libvpx-vp9` to see alpha; container 6.024 s | [TESTED] |
| MOV | ProRes 4444 `yuva444p12le` with alpha; about 40× the MP4 size | [TESTED] |
| Other formats | GIF, HLS, PNG sequence listed in `render --help` | [TESTED help] |
| Wall vs reported time | CLI "rendered in" omits 5–7 s of startup and teardown | [TESTED] |

All rows [E-01]. Further documented limits [DOC] [A1-46] [A1-48] [A1-49] [A1-52]:

- `--resolution` supersampling (for example 4K from a 1080p layout) is MP4-only, cannot combine with HDR, and adds no detail to raster images, video or canvas buffers; 4K is about 4× slower per frame.
- HDR10 output is MP4 only and driven by HDR source media; not available with alpha formats, `--resolution`, Lambda or Cloud Run.
- GIF is capped at 30 fps with 1-bit alpha and no audio; HLS is SDR only and not available on distributed renders.
- Distributed renders (Lambda, Cloud Run) accept only 24, 25, 30 or 60 fps and disable HDR, HLS and motion blur.
- **Privacy caution for HeyGen cloud renders:** the archive limit is 200 MB, and media files of 5 MB or more are uploaded as assets referenced by public, unsigned URLs. Do not cloud-render confidential footage without the owner's consent.

#### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Element visible in preview, missing in render | Tween not on the registered timeline (bare `gsap.to`), or a callback that seeking skips | Put every tween on the paused timeline; use `tl.set` for state changes [DOC] [A2-28] [A2-44] |
| Different frames between renders | Unseeded randomness, wall-clock time, or different `--workers` | Index-derived hashes; pin workers [TESTED] [E-01] [A2-89] |
| Silent audio in render | `<audio>` without `id`, or file path wrong | Add an id; fix the path (lint flags both) [TESTED] [E-01] |
| Element jumps or ignores centering | CSS transform overwritten by GSAP | Center with a wrapper or flex; animate the inner element [TESTED] [E-01] |
| Wrong font in render | Family not embedded; generic family mapped to Inter | Embed `@font-face`; verify with a snapshot [TESTED] [E-01] |
| Black or frozen video panel | Animating the `<video>` element itself, or media not timed as a clip | Animate a wrapper; place media as a timed clip; snapshot each video scene [DOC] [S-11] [DEMO] [A2-77] |
| Descenders clipped in masked text | Clip-path mask too tight | Pad the mask about 0.2 em [DOC] [A2-02] |
| Banding in gradients | Long dark linear gradients under H.264 | Radial or solid fills plus local glow; add grain [DOC] [A2-29] |
| Render fails on a registry block | Download timeout | Retry or choose another block [TESTED] [E-01] |
| Unexpected diff noise in `index.html` | `preview` stamped `data-hf-id` attributes | Expected; commit or ignore [TESTED] [E-01] |
| Lint warns on inline scenes | 0.8.x expects sub-compositions | Move each scene into `compositions/<scene>.html` [TESTED] [E-01] |
| `doctor` reports `ok: false` | Optional tools missing, Docker stopped, low free RAM | Check the required rows only [TESTED] [E-01] |
| Every render ~45 s slower; static scenes | Host id, scene id and timeline key differ, or a root never registers a timeline | Make the three ids identical; add `data-no-timeline` to timeline-free roots [DOC] [A1-07] [A1-56] |
| Scene renders as tiny unstyled text | `<style>`/`<script>` outside the sub-composition's `<template>` | Move them inside; style the root as `#root` [DOC] [A1-07] |
| `check` passes with "0 samples" | A lint error skipped the browser audits | Fix lint errors, rerun `check` [DOC] [A1-35] |
| Clip starts at 0 unexpectedly | Relative timing reference typo or missing spaces | Fix the reference; snapshot to confirm [DOC] [A1-06] |
| Changing root duration with a variable does nothing | Root `data-duration` is locked at compile time | Edit the root attribute directly [DOC] [A1-56] |
| Black flash at the end of a scene | Scene timeline shorter than its slot (seen on older versions) | Current core says slots hold the last frame; if it appears, pad the timeline (`tl.to({}, { duration: SLOT }, 0)`), which is harmless [CONFLICT] [A1-07] [B-10] |
| Blur flicker bands, white bars, Chrome out of memory in final renders | Multi-worker capture on heavy compositions | `--workers 1` (or 3 on out-of-memory) for blur- or video-heavy finals [DEMO] [B-38] [DOC] [B-12] |
| A fix is missing from the render | `npx` used a stale cached CLI version | Pin the version and print it before rendering [DOC] [B-12] |
| Video stuck on frame 0 inside a scene | Video placed inside a timed sub-composition clip | Keep video at the root or animate an untimed wrapper [DOC] [B-12] [UNVERIFIED on 0.8.229] |
| Choppy music in render | MP3 bed re-encoded | Keep music beds as WAV [DOC] [B-12] |

## Part II — Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026) — documented facts

#### 2.2 Architecture and authoring contract

The composition model [Documented] HF-15–HF-19 and the local core skill files:

- **A composition is an HTML file.** The outer element carries `data-composition-id`; every timed element carries `data-start` (which is what makes it a clip) and, by convention, `class="clip"`; `index.html` is the top-level composition and can host other compositions. 30 fps is the default. The top-level root also declares `data-start="0"`, `data-width`/`data-height`, and normally `data-duration`, which is **read once at compile time** before scripts run — a script or `--variables` value cannot change render length. Timeline-free compositions declare `data-no-timeline` or wait out a 45-second player-ready timeout.
- **Clips.** `data-duration` is required for `<div>` and sub-composition hosts; an `<img>` defaults to 3 s; video and audio default to source length. The visibility window is half-open `[start, start + duration)`. `data-track-index` is a Studio lane only; paint order is CSS `z-index` (a negative z-index needs `isolation: isolate` on the parent). Relative timing (`data-start="intro + 0.5"`) works only inside one composition, needs spaces, and resolves silently to 0 on a typo, a cycle or a target without a resolvable duration.
- **Media.** `data-media-start` offsets into a `<video>`/`<audio>` source; `data-playback-start` is the equivalent for nested compositions (authoring a `<video>` with only `data-playback-start` trims the picture over untrimmed audio). `data-playback-rate` 0.1–10 (a `rate` lane in `data-automation` overrides it — speed ramps). `data-volume` (1 = 0 dB, up to 3.98 = +12 dB), `data-fade-in`/`data-fade-out`, `data-has-audio="true"` or `muted` on every timed video. The framework owns playback: never `play()`, `pause()` or set `currentTime`. Render decodes via FFmpeg, so HEVC assets render everywhere; preview auto-proxies browser-hostile codecs.
- **Sub-compositions** load through `data-composition-src` (file content wrapped in `<template>`; `<style>`/`<script>` must sit inside the template or the assembler drops them) or inline; nested timelines are seeked independently — never nest a child timeline into the parent GSAP timeline by hand. A shorter inner timeline holds its final state.
- **Variables.** `data-composition-variables` declares `{id, type, label, default}` with types `string, number, color, boolean, enum, font, image`; `data-variable-values` per instance; `data-var-text`, `data-var-src` and CSS `var(--id)` bind declaratively; `--variables`, `--variables-file`, `--strict-variables` and `--batch rows.json` drive renders. Variables cannot change viewport, root duration, fps or format.
- **Determinism.** "Rendering never plays your video. It asks for one frame at a time… time = floor(frame) / fps." Frame clock → seek → capture (`HeadlessExperimental.beginFrame`) → encode (FFmpeg mixes `<audio>`/`<video>`). No `Date.now()`, `requestAnimationFrame` or timers; no unseeded `Math.random()`; no fetching mid-render; fixed size; finite length. Docker pins Chromium, fonts and FFmpeg for cross-machine parity.
- **Animation runtimes.** GSAP, CSS, Anime.js, Lottie, Three.js, Web Animations and TypeGPU are seeked through the browser runtime; custom runtimes implement the experimental `FrameAdapter` (`getDurationFrames`, `seekFrame`). GSAP contract: one finite `{ paused: true }` timeline registered on `window.__timelines[<data-composition-id>]` after tweens are added.
- **Audio model.** Four attributes — `data-fx-chain` (effect nodes in signal order; on the root it is the master bus), `data-automation` (volume or `fx.<node>.<param>` lanes, ≤ 512 points), `data-fx-carve` (voiceover carve/sidechain on a bed), `data-audio-group` (membership in an `<hf-audio-group>` bus). Sixteen effects (highpass, lowpass, peaking, lowshelf, highshelf, gain, compressor, limiter, truepeak, gate, saturate, bitcrush, delay, reverb, chorus, phaser, pitchshift), 22 presets, one-knob profiles; worklet effects cannot be automated; no static validation of fx chains ("one typo on the root blocks every export") [Documented] HF-20.
- **Captions and transcription.** `init --video/--audio` auto-transcribes and patches captions in; `transcribe` yields word-level `transcript.json`, imports SRT/VTT/OpenAI JSON and exports `--to srt|vtt`; Parakeet TDT 0.6B v3 (25 languages) or whisper.cpp run locally; 74 text-and-caption catalog items [Documented] HF-21, HF-13, HF-28.
- **Fonts and assets.** Put the font file in the project and declare it with `@font-face`; an undeclared font can fall back and lint reports it. Eighteen families are pre-bundled (local skill `typography.md`). Keep everything required for the final result inside the project; remote media fails for permissions, expiring URLs and cross-origin reasons; engine downloads refuse private addresses [Documented] HF-13, HF-22.
- **Colour grading.** `data-color-grading` JSON on `<img>`/`<video>` (presets, adjust, details, effects, colour space); `media-treatment` CLI; grade groups; LUT baking [Documented] HF-19, HF-30.

#### 2.3 Workflows, routes and the intent layer

The local skill files describe a two-layer process [Documented] (hyperframes `SKILL.md`, `intent-interview.md`, `pitch-round.md`, `brief-contract.md`, `brief-format.md`, `review-loop.md`, `production-loop.md`, `storyboard-format.md`, `script-format.md`, `routes/*`):

1. **Project state first** (explicit Remotion port → specific operation → question/hold → new film in an existing project → specific edit → `BRIEF.md` exists → project exists without brief → fresh creation).
2. **Fresh creation runs the intent layer once** — memory and recipes, triage (formed vs unformed), the pitch round for unformed requests, must-have questions one field at a time, run shape (`flow` automation/companion × `storyboard` yes/no → derived `mode`), hand-off — and ends by writing `BRIEF.md`, "the only routing artifact the workflow reads".
3. **Routing by deliverable**, first match wins: remotion-to-hyperframes · slideshow · embedded-captions · talking-head-recut · music-to-video · motion-graphics (short, unnarrated, under ~10 s; alpha WebM/MOV overlays possible) · pr-to-video · product-launch-video · faceless-explainer · general-video (everything else, and every companion run). Narrative routes support up to about 3 minutes and are strongest at 30–90 s.
4. **Four project layers**: `BRIEF.md` (why, for whom) → `STORYBOARD.md` (what, frame by frame) → `frame.md` (how it looks) → `compositions/` (the thing itself). An optional `SCRIPT.md` locks narration for TTS.
5. **The review loop** (plan in chat → sketch pass as posed stills on `boards/storyboard.html` → build on confirmed layouts → final look in the Studio preview) and **the production loop** (blocks & assets → audio in the background → frames → duration sync → assembly → transitions → captions → verify → deliver), written as dependencies, not numbered steps.
6. **Gate behaviour** differs by mode (collaborative waits, autonomous posts and continues) but rendering is user-gated in both.

**Skill-set conflict [Documented, R1].** The live README on 2026-11-01 says HyperFrames ships **seven** skills — core `/hyperframes`, `/hyperframes-cli`, `/hyperframes-registry`, `/media-use`; on demand `/figma`, `/slideshow`, `/remotion-to-hyperframes` — after a mid-October 2026 consolidation ("publish seven knowledge skills aligned with Studio"), with a `reverse-any-video` skill also present in the repository. Earlier snapshots and the local workspace copy carry the 21-skill set (hyperframes-core, -creative, -animation, -keyframes, -audio, -studio and the ten workflow skills). The former workflow names persist as documentation guide pages. **Consequence for this skill:** doctrine from the creative, core and workflow files remains valid as craft knowledge; an agent must read the *installed* skill set (`npx hyperframes skills check`) and route by the names it finds rather than by the names in any guide, including this one.

#### 2.4 Capabilities and integrations (the capability menu)

[Documented] `capability-menu.md`, HF-13, HF-27–29, HF-33–35:

| Capability | What you get | Entry |
|---|---|---|
| Design spec (`frame.md`) | One file that locks palette, type and layout feel; shipped presets with `frame-showcase.html` | `/hyperframes-creative` → `design-spec.md`; presets; `build-frame.mjs` |
| Website capture | Headless-Chrome crawl: screenshots, brand tokens, text, assets; strict public-IPv4 proxy | `npx hyperframes capture <URL> -o ./capture` |
| Beat analysis & audio-reactive motion | Deterministic beat/energy map (`audiomap.json`); elements pulse with the music | `analyze-beatgrid.py`; `audio-reactive.md`; CLI `beats` / `audio` |
| Motion blueprints and rules | Proven scene shapes (reveals, counters, charts, dioramas) cited per beat | `/hyperframes-animation` blueprints and rules indexes |
| Voice, music, SFX, images, logos, treatments | One `resolve` verb; HeyGen catalog (10 k+ tracks, 75 k+ vectors), Openverse SFX (CC0/CC BY) with a bundled 21-file library; TTS (HeyGen → ElevenLabs → Kokoro); music (HeyGen → Lyria → MusicGen) | `/media-use` |
| Generative video | AI presenter reads the script; photo → talking clip; dubbing into another language (`video-translate`) | `/media-use` → `operations.md` § Generate |
| Transcription & captions | Word-timed transcripts; styled caption skins; cut footage by picking sentences (`transcript-cut.mjs`) | `transcribe.mjs`, `captions.mjs` |
| Designed overlays on footage | Kinetic titles, lower-thirds, data callouts synced to speech | `/talking-head-recut`; animation blueprints |
| Real map scenes | Genuine basemap with located pins, routes, flight paths | `/motion-graphics` maps category |
| Figma import | Assets, brand tokens, components, storyboard frames as motion states; Motion → GSAP timelines | `hyperframes figma asset|tokens|component`; `/figma` |
| Registry / catalog | ~450 items: 3D (11), Carousels (25), Text & captions (74), Code (12), Transitions (31), Data & charts (18), Scenes & demos (93), Cursors (14), Motion & effects (97), Surfaces (26, experimental), Blocks (47); `catalog --query` plain-English search | `npx hyperframes add <block>` |
| Scene transitions | 30+ CSS patterns in 13 categories; 14 WebGL shader transitions with duration ranges; custom GLSL | `/hyperframes-animation` → `transitions/` |
| Publish | Hosted URL, private by default; `--public`, `--update` | `npx hyperframes publish` |
| Remotion port | `useCurrentFrame`/`interpolate` → tweens, `Sequence` → clips; refuses React state machines; compares renders frame by frame | `/remotion-to-hyperframes` |
| Agents and hosts | Claude Code plugin, Codex plugin, Cursor, Copilot CLI, Gemini CLI, Antigravity, IBM Bob, OpenCode; hosted MCP connector (beta) for Claude.ai, ChatGPT, Grok | HF-33, HF-34 |
| Deploy | HeyGen cloud render, AWS Lambda (SAM/CDK, S3 CAS), Google Cloud Run, Docker, hosted templates (Vercel/Cloudflare/Modal) | HF-36–38 |

#### 2.5 Tooling: CLI, Studio and the desktop app

**CLI command map [Documented] HF-11, HF-12:** start a project — `init`, `add`, `catalog`; bring in material — `capture`, `media-use`, `transcribe`, `tts` (local Kokoro-82M), `remove-background` (VP9-alpha WebM / ProRes 4444 / PNG), `media-treatment`, `beats`, `audio` (moments, onsets, LUFS, beats, sections), `normalize-audio`, `models`; look at it or share it — `preview` (Studio, port 3002, `--background/--stop`), `present`, `play`, `publish`, `open`, `catch-up`; find problems — `lint`, `check` (runtime, layout, motion, media, contrast), `snapshot --at`, `keyframes`, `compare`, `grade-compare`; edit from the terminal — `timeline` (list; `move`, `trim`, `split`, `delete` with `--plan`), `history`; make a file — `render`, `benchmark`; render elsewhere — `cloud`, `lambda`, `cloudrun`; fix setup — `doctor`, `browser`, `upgrade --check`, `docs`, `info`, `compositions`, `clean`; connect — `auth`, `skills update|check`, `usage`, `figma`, `events`, `telemetry`, `feedback`. `validate`, `inspect` and `layout` are deprecated in favour of `check`. Every command takes `--json`; runs are unattended under CI or inside a coding agent (`HYPERFRAMES_AGENT=1`).

**Studio (browser editor) [Documented] HF-13, HF-14, HF-24:** opens from `preview`; layers, inspector, timeline with snapping and beats, auto-keyframing, variables UI, renders panel (GIF export, loop count, ≤ 30 fps, no audio), code editor with autosave, asset import; every edit saves to the project files. Its "Ask agent" copies a prompt back to the conversation — Studio does not talk (local `hyperframes` SKILL.md § 6).

**Desktop app and Framey [Documented] HF-25–HF-27, HF-39:** free for Mac (Apple Silicon/Intel), Windows x64 and Linux (.deb/AppImage); Windows on Arm not yet; sign-in with a free HeyGen account. "You describe the video, an agent on your computer builds it, and you change it by typing, pointing at the picture, drawing, or commenting… Framey, the small green guide, points you to the next step." Agents inside the app: Claude Code, Codex, OpenCode (free models), Grok, Antigravity. Tools: Select (V), Draw (D), Comment (C); right-click "Ask Framey, Hide, Bring to front, Replace with, Cut out object here"; batch up to 10 pending edits; `@` attaches moments/media. Export: "This Mac" (free, any shape or length) or "Cloud" (paid per minute from the HeyGen balance; 16:9, 9:16, 1:1; 24/25/30/60 fps; project ≤ 200 MB; 4K about twice the price of 1080p). The app changelog (builds b271–b524, Oct 2026) adds brand kits from a website, "Reference any video", lip-sync, podcast multi-camera edits, GPU and cloud export, storyboard play/step.

**Outputs and performance [Documented] HF-22, HF-23:** MP4 (H.264 default; HDR10 H.265 10-bit when sources are HDR, MP4 only, not on Lambda), MOV (ProRes 4444 with alpha by default; `hq|422|lt|proxy` without alpha), WebM (VP9 with alpha), GIF (no audio, ≤ 30 fps), PNG sequence (RGBA), HLS VOD (SDR, no `--gpu`, not on cloud). Default 1920×1080 at 30 fps; `--resolution` presets including 4K supersampling ("roughly 4× slower per frame and 3–5× larger file"; not combinable with HDR). GPU encode via `--gpu` (NVENC/VideoToolbox/VAAPI/QSV). Quality: the rendering guide names tiers "draft / looks (CRF 16, visually lossless at 1080p) / delivery" and flags `--crf`, `--video-bitrate`, `--keyframe-interval`, `--max-bitrate`; the CLI skill reference, cloud docs and FAQ use `--quality draft|standard|high` — both vocabularies appear in official sources on the research date. Measured examples: a 300-frame 1080p composition rendered in 9.8 s (25 s with one expensive CSS declaration left in); a 12-second Studio export "took about 16 seconds on a MacBook". `--workers` spawns one Chrome per worker (~256 MB each). Third-party timings: 6 s at 1080p in 8.7 s (1 worker) → 3.3 s (8 workers) on an M5 Pro; 10 s at 1080p in 16.18 s versus Remotion's 6.35 s at defaults; 30 s in 39.93 s versus 13.27 s [Demonstrated] P-21, P-23. Video-heavy compositions: drop to `--workers 1` [Demonstrated] P-2, P-9.

**Pricing and limits [Documented] HF-13, HF-36, HF-37:** the framework, CLI and skills are free; a HeyGen account is needed for HeyGen voices and music, avatars, cloud rendering, the hosted connector and the Studio app; cloud render bills 4K at 1.5× (the Studio export page says about 2×); cloud accepts only mp4/webm/mov, 16:9/9:16/1:1, a 200 MB archive; Lambda has no fixed maximum length but each plan/chunk/assemble step must finish within a 15-minute invocation, up to 256 chunks, SDR only, no webhook. A published pricing page for the "HyperFrames plan" was not found [Not found].

#### 2.6 Documented limitations and boundaries

[Documented] HF-13, HF-22, HF-34, HF-36–38, HF-20: HDR is MP4-only, not on Lambda, not with 4K; HLS is SDR-only without GPU and not on cloud; cloud renders cannot be stopped once started and may still charge; `capture` does not support IPv6-only sites and refuses private addresses; variables cannot change root duration, fps or format; audio fx chains have no static validation and worklet effects cannot be automated; the summed mix was unlimited before v0.8.228; the desktop app has no Windows-on-Arm build (and the FAQ's "Mac and Linux only" line is stale); the hosted MCP connector is in beta and "does not give you the same local project folder, browser editor surface, or debugging access"; `FrameAdapter` is an experimental v0 API; the paused-timeline and no-wall-clock rules "break quietly if you don't" follow them. Determinism is strongest on Linux (`beginFrame` capture); macOS and Windows fall back to screenshot heuristics, and the worker count can change pixels [Demonstrated] P-2, P-21. Specialised narrative workflows cap at about 3 minutes [Documented, local SKILL.md].

#### 2.7 Troubleshooting guidance (documented)

The single official troubleshooting page [Documented] HF-14 asks for `npx hyperframes doctor`, `lint` and `check` output first, then covers: FFmpeg not found; "No composition found"; black video in preview (codec the browser cannot decode — proxy); "Do not animate width, height, top, or left directly on a `<video>` element"; "Do not call play(), pause(), or set currentTime from composition scripts"; timed visible elements need `class="clip"`; static animation → the timeline is not paused or not registered under the exact id; every render ~45 s too long → add `data-no-timeline`; render differs from preview → `--docker`; slow under WSL2; HDR → SDR fallbacks; feedback via `npx hyperframes feedback --rating N --comment … [--file-issue]`; Studio-app sign-in and agent-usage limits ("your agent's own plan limit, not a HyperFrames one"). The local core skill adds the lint rules that catch first-build failures (`gsap_css_transform_conflict`, `media_crossorigin_breaks_preview`, `video_nested_in_timed_element`, `media_missing_id`, `gsap_animates_clip_element`, `font_family_without_font_face`, `gsap_timeline_registered_before_async_build`, `clip_ends_past_root_duration`, `nested_clip_never_visible`, `root_composition_missing_duration_source`) and the silent bugs lint misses (relative-timing zeros, invisible scaled spans, pulsing decoratives clipped at their peak, a lint error disabling the layout and contrast audits).

### Appendix C. HyperFrames command quick reference (verify flags on the installed version)

| Need | Command |
|---|---|
| Probe | `npx hyperframes --version` · `npx hyperframes skills check` · `npx hyperframes usage --json` · `npx hyperframes@latest upgrade --project . --check` |
| Scaffold | `npx hyperframes init` (`--resolution landscape|portrait|square|…-4k`, `--video`, `--audio`, `--tailwind`) |
| Registry | `npx hyperframes catalog --query "<move in plain English>"` · `npx hyperframes add <block>` |
| Capture a site | `npx hyperframes capture <URL> -o ./capture` |
| Media | `npx hyperframes media-use resolve --type <bgm|sfx|image|icon|logo|voice|grade|lut> --intent "…" --project .` · `transcribe` · `tts` · `remove-background` · `media-treatment` · `beats` · `audio` · `normalize-audio` |
| Audio engine | `node <media-use>/audio/scripts/audio.mjs --request ./audio_request.json --out ./audio_meta.json` · `wait-bgm.mjs` before render |
| Timeline | `npx hyperframes timeline [--json]` · `timeline move|trim|split|delete --plan` · `history show --diff` |
| Validate | `npx hyperframes lint` · `npx hyperframes check [--json]` · `npx hyperframes snapshot --at <t1,t2,…> -o boards/stills` · `keyframes` · `compare` |
| Preview | `npx hyperframes preview --background` · `preview --stop` · `play` · `present` |
| Render | `npx hyperframes render` (`--resolution`, `--fps`, `--workers`, `--gpu`, `--start/--end`, `--variables` / `--variables-file` / `--batch`, `--prores-profile`, quality flags per `--help`) |
| Measure | `ffprobe out.mp4` · `ffmpeg -i out.mp4 -af ebur128=peak=true -f null -` |
| Share | `npx hyperframes publish [--public] [--update]` · `npx hyperframes open` · `npx hyperframes catch-up` |
| Fix setup | `npx hyperframes doctor` · `browser` · `docs <topic>` · `info` · `feedback --rating N --comment "…"` |
| Memory | `node <media-use>/scripts/prefs.mjs get --hyperframes <root> --json` · `scripts/recipe.mjs freeze --name <name>` |

## Part III — Source B hands-on lab (Windows 11, hyperframes 0.8.229)

#### 2. PASS/FAIL summary

| # | Claim | Command (from project dir unless noted) | Result | Evidence |
|---|---|---|---|---|
| 1 | CLI runs on Node 24 / Windows 11 | `hyperframes --version` | **PASS** | `0.8.229`, 0.76 s |
| 2 | `doctor` checks Node, FFmpeg, FFprobe and Chrome; `--json` always exits 0 | `hyperframes doctor --json` | **PASS** | exit 0 while `ok:false`, because of the Memory check, optional whisper/Kokoro/MusicGen and Docker not running. Chrome, FFmpeg and FFprobe all `ok`. 14.9 s. `logs\doctor.json` |
| 3 | Every subcommand has `--help` | loop over 46 listed + 5 hidden commands | **PASS** | 51/51 exit 0. `help\<command>.txt` |
| 4 | Non-TTY `init` scaffolds the centered blank | `hyperframes init demo --non-interactive` | **PASS** | 6 files in 2.0 s. `index.html` is byte-identical to the bundled `dist/templates/blank/index.html` |
| 5 | `init --resolution portrait` sets 1080×1920 | `hyperframes init demo-vertical --non-interactive --resolution portrait` | **PASS** | viewport, `body`, `data-width` and `data-height` all 1080×1920 |
| 6 | A documented-syntax composition lints with 0 errors | `hyperframes lint` | **PASS** (2 warnings) | `nested_structure_needs_subcomposition` ×2, exit 0. See [CONFLICT] C1 |
| 7 | MP4 output matches root `data-duration`, fps and size | `hyperframes render --output renders/r1.mp4` | **PASS** | 6.000000 s; 30/1; 180 frames (counted); 1920×1080; H.264 High; yuv420p; tv range; BT.709 ×3; AAC-LC 48 kHz stereo |
| 8 | Default quality `looks` = CRF 16 | same | **PASS** | x264 SEI in file: `crf=16.0 bframes=0 keyint=250` |
| 9 | `data-volume` sets static gain | same, plus `ffmpeg volumedetect` | **PASS** | source mean −34.0 dB, output −38.5 dB. Δ −4.5 dB vs expected 20·log10(0.6) = −4.44 dB |
| 10 | `check` = lint + runtime + layout + contrast in one browser session | `hyperframes check --json` | **PASS** | `ok:true` in 9.96 s; contrast 4/4. One layout warning, a false positive (§T4) |
| 11 | Lint catches the documented mistakes | 16 mutated variants + the doc example | **all 9 documented rules fire; 4 deviations** | §T5 table; C1–C4 |
| 12 | Re-rendering the same command is deterministic | r1 vs r2 (and r3) | **PASS, byte-identical** | same sha256; 180/180 decoded frames identical; audio md5 identical |
| 13 | Output is identical across worker counts | r1 (auto = 6 workers) vs `--workers 1` | **FAIL (not bit-exact)** | 180/180 frames differ; PSNR 59.8 dB; SSIM 0.99986. Visually identical; different capture path |
| 14 | Vertical render | portrait project, `render` | **PASS** | 1080×1920, 30/1, 180 frames, 6.0 s, AAC |
| 15 | `--format webm` has transparency | `hyperframes render --format webm` | **PASS** | VP9 with `ALPHA_MODE=1`. Decoded alpha min 0, max 255 |
| 16 | `--format mov` = ProRes 4444 with alpha | `hyperframes render --format mov` | **PASS** | `prores` profile 4444, `yuva444p12le`. Alpha min 0, max 255 |
| 17 | "60fps doubles render time" | `render --fps 60` | **NOT REPRODUCED** | 49.0 s vs 38.3 s wall (1.28×); 360 frames at 60/1 |
| 18 | `--quality draft` is the fast option | `render --quality draft` | **PASS (speed); file larger** | 32.6 s vs 38.3 s wall. CRF 28, 713.5 KB vs 497.0 KB |
| 19 | `preview --background` serves Studio, and `--stop` stops it | `preview --background --no-open --port 3017` | **PASS** | `http://localhost:3017/#project/demo` returns HTTP 200. After `--stop`, the connection is refused |
| 20 | `preview` leaves source alone | same | **FAIL (side effect)** | preview injected `data-hf-id="hf-…"` into 10 elements of `index.html`. Renders are unaffected (r3 byte-identical to r1) |
| 21 | `add` installs registry items | `add staggered-fade-up`, `add hw-title` | **PASS** (one other block failed) | files written plus `hyperframes.lock.json`. `glass-shard-title` failed twice with a download timeout |
| 22 | `catalog --query --json` envelope | `catalog --query "fade a title in" --json` | **PASS** | `tier:"words"`, `total:448`, `shown:45`, `dropped:0`, `unindexed:0`, `report_gap` present |
| 23 | Fast capture defaults on only for macOS + hardware GPU (`--help`) | `render --workers 1` | **[CONFLICT] C6** | Windows render used `drawelement capture` with self-verify |

#### 4. CLI command and flag reference (hyperframes 0.8.229, from `--help`) [TESTED 0.8.229]

How the table was built:

- Generated by `hf-lab\help\_summarize.js` from `hf-lab\help\_squeezed\*.txt`. Raw help text is in `hf-lab\help\<command>.txt`.
- `play`, `layout`, `events`, `usage` and `figma` are hidden from the root help.
- `validate`, `inspect` and `layout` are deprecated aliases of `check`.
- Commands that take subcommands show them in **Usage**. Their sub-flags were not captured: `auth`, `cloud`, `figma`, `measure`, `skills`, `history`.

| Command | Description (from --help) | Usage | Arguments | Flags |
|---|---|---|---|---|
| `add` | Install a block or component from the registry into this project | `add [OPTIONS] <NAME>` | NAME  Registry item name or tag. Single items install directly (e.g. shader-wipe). If the name matches a tag instead, all blocks with that tag are installed (e.g. html-in-canvas, captions). Give several names to install each of them in one call. (Required) | `--dir=…` `--clipboard` `--no-clipboard` `--json` `--vars=…` `--force` |
| `audio` | Measure how sound moves in time: where it lands, its hits, loudness and silence | `audio [OPTIONS] [FILES]` | FILES  Audio or video files to analyze | `--dir=…` `--element=…` `--at=…` `--range=…` `--place-at=…` `--skip-file-seconds=…` `--only=…` `--quality=…` `--provider=…` `--onset-method=…` `--threshold=…` `--band=…` `--hop-ms=…` `--onset-ratio=…` `--tail-db=…` `--silence-db=…` `--full` `--read` `--transcript=…` `--json` |
| `auth` | Sign in to HeyGen and manage credentials | `auth login|status|logout|refresh` |  |  |
| `beats` | Detect beats in the project music track (writes beats/<audio>.json) or in one audio file | `beats [OPTIONS] [DIR]` | DIR  Project directory, or one audio or video file to analyse | `--json` |
| `benchmark` | Render with preset fps/quality/worker configs and compare speed and file size | `benchmark [OPTIONS] [DIR]` | DIR  Project directory | `--runs=…` `--json` |
| `billing` | Open the HyperFrames plans or credits page and wait until the person is done (subscribe / top-up) | `billing [OPTIONS] <ACTION>` | ACTION  subscribe / top-up (Required) | `--needed=…` `--tool=…` `--timeout=…` |
| `browser` | Manage the Chrome browser used for rendering | `browser [OPTIONS] [SUBCOMMAND]` | SUBCOMMAND  ensure = find or download Chrome, path = print executable path, clear = remove cached download | `--force` |
| `capture` | Capture a website as editable HyperFrames components | `capture [OPTIONS] [URL]` | URL  Website URL to capture (omit when using --local-file or --video) | `--local-file=…` `--local-root=…` `-o, --output=…` `--skip-assets` `--skip-vision` `--max-screenshots=…` `--timeout=…` `--capture-budget=…` `--json` `--video=…` `--index=…` `--video-url=…` `--list` |
| `catalog` | Browse and install blocks and components from the registry | `catalog [OPTIONS] [WORDS]` | WORDS  Search words, same as --query (e.g. `catalog crossfade`) | `--type=…` `--tag=…` `--json` `--human-friendly` `--query=…` `-y, --yes` `--on-device` |
| `catch-up` | See what was done in the desktop app since you last looked | `catch-up [OPTIONS] [DIR]` | DIR  Project directory (default: current) | `--json` |
| `check` | Run lint, runtime, layout, motion, and WCAG contrast verification in one browser session | `check [OPTIONS] [DIR]` | DIR  Project directory | `--json` `--samples=…` `--range=…` `--components=…` `--at=…` `--at-transitions` `--max-transition-samples=…` `--max-issues=…` `--collapse-static` `--no-collapse-static` `--tolerance=…` `--timeout=…` `--contrast` `--no-contrast` `--strict` `--prepare-media` `--proxy` `--browser-gpu` `--snapshots` `--caption-zone=…` `--frame-check=…` `--layout=…` |
| `clean` | Find and remove what HyperFrames left on disk | `clean [OPTIONS] [DIR]` | DIR  Project directory (default: current); its subfolders are not searched | `--dry-run` `--snapshots` `--json` |
| `cloud` | Render HyperFrames compositions on the HeyGen cloud | `cloud render|list|get|delete` |  |  |
| `cloudrun` | Deploy and drive renders on Google Cloud Run | `cloudrun [OPTIONS] [SUBCOMMAND] [TARGET] [EXTRA]` | SUBCOMMAND  deploy / sites / render / render-batch / progress / destroy; TARGET  Subcommand positional (project dir, execution name, sites verb); EXTRA  Extra positional (e.g. `sites create <projectDir>`) | `--project=…` `--region=…` `--image=…` `--repo=…` `--cpu=…` `--memory=…` `--max-instances=…` `--timeout=…` `--site-id=…` `--width=…` `--height=…` `--fps=…` `--format=…` `--codec=…` `--quality=…` `--chunk-size=…` `--max-parallel-chunks=…` `--target-chunk-frames=…` `--output-resolution=…` `--variables=…` `--variables-file=…` `--strict-variables` `--batch=…` `--max-concurrent=…` `--dry-run` `--render-id=…` `--output-key=…` `--wait` `--wait-interval-ms=…` `--json` |
| `compare` | Render independent composition variants into one labeled comparison sheet | `compare [OPTIONS] [PATH]` | PATH  Composition project directory or .html file (pass 2+ paths) | `--at=…` `--labels=…` `--out=…` `--cols=…` `--timeout=…` `--json` |
| `compositions` | List all compositions in a project | `compositions [OPTIONS] [DIR]` | DIR  Project directory | `--json` |
| `diff` | Score a render or a project against the original video frame by frame: SSIM, worst moments, cuts, segments | `diff [OPTIONS] <REFERENCE> <YOURS>` | REFERENCE  The original video (Required); YOURS  A rendered video, or a project folder (captured at the original's frame times, no render) (Required) | `--at=…` `--range=…` `--segments=…` `--ledger=…` `--project=…` `--min-mean=…` `--min-p05=…` `--min-cell=…` `--worst=…` `--sbs` `--out=…` `--timeout=…` `--drawn=…` `--json` |
| `docs` | View inline documentation in the terminal | `docs [OPTIONS] [TOPIC]` | TOPIC  Topic: data-attributes, examples, rendering, gsap, troubleshooting, compositions, motion-blur. Omit to list all.;  |  |
| `doctor` | Check system dependencies and environment | `doctor [OPTIONS]` |  | `--json` |
| `events` | Emit a skill-usage telemetry event (skills report their own invocation/outcome). Honors DO_NOT_TRACK / telemetry opt-out. | `events [OPTIONS]` |  | `--skill=…` `--event=…` `--outcome=…` |
| `feedback` | Submit feedback about your experience | `feedback [OPTIONS]` |  | `--rating=…` `--comment=…` `--source=…` `--search-miss=…` `--wanted=…` `--tier=…` `--file-issue` `--dir=…` `-y, --yes` |
| `figma` | Import figma assets, tokens, and components (REST) | `figma asset|tokens|component` |  |  |
| `grade-compare` | Render candidate color grades onto a reference frame as one comparison PNG | `grade-compare [OPTIONS] --for=<for>` |  | `--for=…` `--grades=…` `--luts=…` `--project=…` `--out=…` `--json` `--timeout=…` `--baseline` `--no-baseline` |
| `history` | List, undo and restore the project's recorded changes | `history [OPTIONS] show|undo|restore|peek|pin|begin|end` |  | `--dir=…` `--json` `--since=…` `--who=…` `--limit=…` |
| `info` | Print project metadata | `info [OPTIONS] [DIR]` | DIR  Project directory | `--json` |
| `init` | Scaffold a new composition project | `init [OPTIONS] [NAME]` | NAME  Project name | `-e, --example=…` `-t, --template=…` `-v, --video=…` `-V, --video-legacy=…` `-a, --audio=…` `--skip-transcribe` `--keep-original` `--model=…` `--language=…` `--non-interactive` `--agent` `--skip-skills` `--tailwind` `--resolution=…` `--skill=…` |
| `inspect` | Inspect rendered composition layout for text/container overflow, plus optional motion verification via a *.motion.json sidecar (deprecated, use check) | `inspect [OPTIONS] [DIR]` | DIR  Project directory | `--json` `--samples=…` `--at=…` `--at-transitions` `--max-transition-samples=…` `--tolerance=…` `--timeout=…` `--max-issues=…` `--collapse-static` `--no-collapse-static` `--strict` |
| `keyframes` | See, debug, and refine keyframes — surface GSAP, CSS @keyframes, Anime.js, paths, and onion-shot diagnostics | `keyframes [OPTIONS] [TARGET]` | TARGET  Project dir or composition .html | `--selector=…` `--runtime=…` `--json` `--shot=…` `--samples=…` `--layout=…` `--from=…` `--to=…` `--angle=…` `--fit` `--no-fit` `--ghost` |
| `lambda` | Deploy and drive renders on AWS Lambda | `lambda [OPTIONS] [SUBCOMMAND] [TARGET] [EXTRA]` | SUBCOMMAND  deploy / sites / render / progress / destroy / policies; TARGET  Subcommand-specific positional (project dir, render id, policies verb, etc.); EXTRA  Extra positional (e.g. `sites create <projectDir>` or `policies validate <policy.json>`) | `--stack-name=…` `--region=…` `--profile=…` `--concurrency=…` `--chrome-source=…` `--memory=…` `--video-arch=…` `--skip-build` `--warm` `--no-warm` `--site-id=…` `--width=…` `--height=…` `--output-resolution=…` `--fps=…` `--format=…` `--codec=…` `--quality=…` `--keyframe-interval=…` `--max-bitrate=…` `--buffer-size=…` `--prores-profile=…` `--chunk-size=…` `--max-parallel-chunks=…` `--target-chunk-frames=…` `--execution-name=…` `--output-key=…` `--variables=…` `--variables-file=…` `--strict-variables` `--batch=…` `--max-concurrent=…` `--dry-run` `--wait` `--wait-interval-ms=…` `--json` |
| `layout` | Inspect rendered composition layout for text/container overflow, plus optional motion verification via a *.motion.json sidecar (deprecated, use check) | `layout [OPTIONS] [DIR]` | DIR  Project directory | `--json` `--samples=…` `--at=…` `--at-transitions` `--max-transition-samples=…` `--tolerance=…` `--timeout=…` `--max-issues=…` `--collapse-static` `--no-collapse-static` `--strict` |
| `lint` | Validate a composition for common mistakes | `lint [OPTIONS] [DIR]` | DIR  Project directory, or one composition .html file | `--json` `--verbose` |
| `measure` | Measure a video file as JSON: clock, cuts, events, frames, crops, eases, motion energy, ink, look, faces, lip sync | `measure probe|cuts|events|frames|extract|curve|energy|ink|look|face|sync` |  |  |
| `media-treatment` | Discover, apply, or clear deterministic media treatments | `media-treatment [OPTIONS]` |  | `--capabilities` `--capability=…` `--all` `--project=…` `--file=…` `--selector=…` `--selector-index=…` `--grading=…` `--apply` `--analyze` `--clear` `--dry-run` `--json` |
| `models` | List or download on-device models (models list, models install parakeet) | `models [OPTIONS] <ACTION> [NAME]` | ACTION  list or install (Required); NAME  Model to install: parakeet | `--json` |
| `normalize-audio` | Normalize a clip with sound to an absolute LUFS target, or match it to another clip | `normalize-audio [OPTIONS] [DIR] --target=<target>` | DIR  Project directory | `--reference=…` `--target=…` `--lufs=…` `--write` `--tolerance=…` `--json` |
| `open` | Open a project in the HyperFrames desktop app | `open [OPTIONS] [DIR]` | DIR  Project directory (default: current) | `--json` |
| `play` | Play a composition in a lightweight browser player | `play [OPTIONS] [DIR]` | DIR  Project directory | `--port=…` `--open` `--no-open` `--browser-path=…` `--user-data-dir=…` `--remote-debugging-port=…` `--proxy` `--no-proxy` |
| `present` | Serve a slideshow deck and open it in presenter mode (with audience sync) | `present [OPTIONS] [DIR]` | DIR  Project directory | `--port=…` `--open` `--no-open` `--browser-path=…` `--user-data-dir=…` `--remote-debugging-port=…` |
| `preview` | Start the studio for previewing compositions | `preview [OPTIONS] [DIR]` | DIR  Project directory | `--port=…` `--force-new` `--background` `--foreground` `--status` `--stop` `--list` `--kill-all` `--lint-verbose` `--open` `--no-open` `--selection` `--json` `--context` `--context-fields=…` `--context-detail=…` `--browser-path=…` `--user-data-dir=…` `--remote-debugging-port=…` `--browser-no-gpu` `--browser-gpu` `--proxy` `--no-proxy` |
| `publish` | Upload the project to a stable URL (private by default) | `publish [OPTIONS] [DIR]` | DIR  Project directory | `-y, --yes` `--public` `--update=…` `--space=…` `--proxy` `--lint-verbose` |
| `remove-background` | Remove background from a video or image using a local AI model — outputs transparent WebM, ProRes 4444, or PNG | `remove-background [OPTIONS] [INPUT]` | INPUT  Source video (.mp4/.mov/.webm/.mkv) or image (.jpg/.png/.webp) | `-o, --output=…` `-b, --background-output=…` `--device=…` `--quality=…` `--info` `--json` |
| `render` | Render a composition to MP4, WebM, MOV, GIF, HLS, or a PNG sequence | `render [OPTIONS] [DIR]` | DIR  Project directory | `-c, --composition=…` `-o, --output=…` `-f, --fps=…` `-q, --quality=…` `--skill=…` `--format=…` `--gif-loop=…` `--hls-segment-seconds=…` `--video-frame-format=…` `--page-motion-blur=…` `-w, --workers=…` `--docker` `--hdr` `--sdr` `--crf=…` `--start=…` `--end=…` `--video-bitrate=…` `--keyframe-interval=…` `--max-bitrate=…` `--buffer-size=…` `--prores-profile=…` `--vp9-cpu-used=…` `--gpu` `--browser-gpu` `--quiet` `--lint-verbose` `--debug` `--best-effort` `--no-best-effort` `--strict` `--strict-all` `--max-concurrent-renders=…` `--variables=…` `--variables-file=…` `--strict-variables` `--batch=…` `--batch-concurrency=…` `--batch-fail-fast` `--json` `--resolution=…` `--page-side-compositing` `--no-page-side-compositing` `--browser-timeout=…` `--protocol-timeout=…` `--player-ready-timeout=…` `--resume` `--keep-segments` `--low-memory-mode` `--experimental-fast-capture` `--frames-cache-dir=…` |
| `skills` | Install, check, and update HyperFrames skills for AI coding tools | `skills check|update` |  |  |
| `snapshot` | Capture key frames from a composition as PNG screenshots for visual verification | `snapshot [OPTIONS] [DIR]` | DIR  Project directory | `--frames=…` `--at=…` `--range=…` `--composition=…` `--timeout=…` `--angle=…` `--end` `--no-end` `--keep` `--zoom=…` `--zoom-scale=…` `--against=…` `--review` `--json` `--describe=…` `--proxy` `--browser-gpu` |
| `telemetry` | Manage usage telemetry | `telemetry [OPTIONS] [SUBCOMMAND]` | SUBCOMMAND  Subcommand: enable, disable, status;  |  |
| `timeline` | Print and edit the project's tracks and clips | `timeline [OPTIONS] [DIR] move|trim|split|delete|set|duplicate|ids|apply|undo` | DIR  Project directory | `--component=…` `--at=…` `--range=…` `--boundary=…` `--generation=…` `--offset=…` `--json` |
| `transcribe` | Transcribe audio/video to word-level timestamps, or import an existing transcript | `transcribe [OPTIONS] <INPUT>` | INPUT  Audio/video file to transcribe, or transcript file to import (.json, .srt, .vtt) (Required) | `-d, --dir=…` `-e, --engine=…` `--speakers` `-m, --model=…` `-l, --language=…` `--json` `--to=…` `-o, --output=…` `--preserve-cues` `--runtime-install` `--no-runtime-install` `--optional` `--timeout=…` |
| `tts` | Generate speech audio from text using a local AI model (Kokoro-82M) | `tts [OPTIONS] [INPUT]` | INPUT  Text to speak, or path to a .txt file | `--text-file=…` `-v, --voice=…` `-s, --speed=…` `-l, --lang=…` `--list` `--json` |
| `upgrade` | Check for updates and show upgrade instructions | `upgrade [OPTIONS]` |  | `-y, --yes` `--check` `--json` `--project=…` |
| `usage` | Read remaining harness subscription usage without telemetry | `usage [OPTIONS]` |  | `--harness=…` `--json` |
| `validate` | Load a composition in headless Chrome and report console errors (deprecated, use check) | `validate [OPTIONS] [DIR]` | DIR  Project directory | `--json` `--contrast` `--no-contrast` `--timeout=…` |

#### 5. Observed gotchas [TESTED 0.8.229]

1. **`preview` edits your source.** It stamps `data-hf-id` on elements in `index.html`, which adds noise to diffs. Rendered output was unchanged.
2. **Compile-time network dependency.**
   - The compiler inlines GSAP fetched from jsdelivr ("Inlined CDN script").
   - It also maps the generic `sans-serif` to Inter, fetched from Google Fonts ("Fetched 11 font face(s) for 'Inter'"), and logs that line on every render.
   - Offline renders and an empty font cache are **[UNVERIFIED]**.
3. **Monolithic files always warn.** Any inline `<section class="clip">` that contains child elements triggers `nested_structure_needs_subcomposition`. That includes the skill's own minimal example. It is only a warning, and the render is fine.
4. **Capture path on Windows.** It was `screenshot` (auto workers) or `drawelement` (`--workers 1`), never `beginframe`. Worker count changes the pixels slightly (PSNR ≈ 60 dB), so pin `--workers` when you need bit-identical output.
5. **Auto workers costs ~8 s** of calibration. On short pieces, `--workers 1` was faster.
6. **First render on Windows** logged `[FrameCapture] Timed out closing browser; forcing browser process shutdown` ×4. It was harmless, and later renders did not log it.
7. **The CLI's "rendered in" time understates wall time** by about 5–7 s.
8. **`--quality draft` can make larger files** than `looks` on flat graphics (CRF 28 with an ultrafast-style preset).
9. **Checking WebM alpha.** VP9 alpha is invisible to ffprobe's `pix_fmt` (`yuv420p`). Decode with `libvpx-vp9`. WebM audio is Opus, and the container duration was 6.024 s, not 6.000 s.
10. **ProRes 4444 is heavy**: about 40× the MP4 size (19.9 MB for 6 s).
11. **`check` false positive.** Layout reports `rotation_pivot_drift` when an element translates and rotates in the same tween. Craft warns `first_frame_empty` when nothing is on screen at t = 0.
12. **Lint verifies media files exist** (`audio_src_not_found`). The skill does not list this rule.
13. **`doctor` `ok:false` is normal** on a desktop: Docker is stopped and optional AI tools are absent. The Memory check uses *available* RAM.
14. **Preview log path ignores `HOME`/`USERPROFILE`** and goes to `%LOCALAPPDATA%\hyperframes\previews\`. `~\.hyperframes` is derived from `os.homedir()`. `HYPERFRAMES_CONFIG_DIR` only moves credentials (`auth --help`).
15. **Registry items differ from the core skill's conventions.** They can bring assets (fonts), write `hyperframes.lock.json`, ship as full HTML documents (not `<template>`), and pin a different GSAP minor version (3.14.2) than the scaffold (3.15.0). Whether mixing the two GSAP versions in one assembled page matters is **[UNVERIFIED]**.
16. **One registry item failed reproducibly**: `glass-shard-title` hit a download timeout twice. Treat `add` as network-dependent and retry or choose an alternative.
17. **`info` and `compositions` disagree** on element counts (2 vs 3) for the same file.

#### 6. Conflicts between skill docs and CLI behaviour

- **C1 [CONFLICT]** `hyperframes-core\references\minimal-composition.md` calls its example "the smallest renderable composition", and `composition-patterns.md` presents inline `<section class="clip">` scenes as a valid "Monolithic" architecture. 0.8.229 lint warns on both with `nested_structure_needs_subcomposition`: "the root composition is built only from sub-compositions".
- **C2 [CONFLICT]** The core skill says wrapping a standalone root in `<template>` is rejected with `standalone_composition_wrapped_in_template`. That code fires only when the file **starts with** `<template`. A `<template>` inside `<body>` fails with `missing_timeline_registry` or `missing_gsap_script` instead.
- **C3 [CONFLICT]** The core skill says "A named CSS font-family needs an in-file `@font-face` … or lint fires `font_family_without_font_face`". Fonts on the CLI's auto-resolved list (Inter tested) are exempt: the compiler downloads them from Google Fonts. Only unknown families fail.
- **C4 [CONFLICT]** Core pitfall #1 says translate(-50%,-50%) centering combined with a GSAP x/y tween is caught by `gsap_css_transform_conflict`. Lint catches `.to()` but **not `.from()`** (N1c passes silently).
- **C5 [CONFLICT, UNVERIFIED which is right]** `init-and-scaffold.md` says `--skip-skills` is "temporarily ignored; use `HYPERFRAMES_SKIP_SKILLS=1`". `init --help` says "Skip installing missing core AI skills (also HYPERFRAMES_SKIP_SKILLS=1)". Only the environment variable was used.
- **C6 [CONFLICT]** `render --help` says `--experimental-fast-capture` is "Default: on where it can engage (macOS + hardware-GPU browser)". On Windows, `--workers 1` rendered with `drawelement capture` (the drawElementImage path) by default. The CLI SKILL also documents only `beginframe` vs `screenshot` as summary-line values.
- **C7 [CONFLICT]** `preview-render.md` says "60fps doubles render time". Measured 1.28× for a 6 s piece. The claim may hold only for long renders.
- **C8 [CONFLICT]** The CLI SKILL says `check --snapshots` writes "annotated overview frames + per-finding crops". `check --help` says "Save contrast-pass PNGs". Not exercised.
- **C9 [CONFLICT]**
  - `init-and-scaffold.md` documents `npx hyperframes skills` as an installer; the CLI exposes `skills check|update`, and init's next steps say `skills update`.
  - The skill's render table lists `--fps` 24/30/60; the CLI accepts 1–240 and rationals.
  - Root `--help` describes `render` as "MP4 or WebM", while `render --help` lists MP4/WebM/MOV/GIF/HLS/PNG-sequence.
- **C10 [CONFLICT]** `lint-validate-inspect.md` lists the `check --json` envelope as `{ok, browserSkipped, lint, runtime, layout, motion, contrast, hdr, snapshots}`. 0.8.229 also returns `strict`, `craft`, `audio`, `saved` and `_meta`.
- **C11 [minor]** GSAP version drift: the skill's minimal example uses 3.14.2, the bundled blank template 3.15.0, and the `hw-title` registry block 3.14.2.
- **Not a conflict, but worth stating.** The skill offers `--docker` for byte-identical output. Plain local renders with the same settings were byte-identical too. Docker's added value, cross-host reproducibility, is [UNVERIFIED].

#### 7. Not tested (time-boxed, about 45 min of tool time)

- `render --docker`: Docker daemon not running.
- `--gpu` (NVENC) encode, `--hdr` / `--sdr`.
- `--resolution` supersampling.
- `--format gif|png-sequence|hls`.
- `--start/--end`, `--crf`, `--video-bitrate`.
- `--batch` and `--variables` / `--strict-variables`.
- `check --snapshots`, a `*.motion.json` sidecar, `--at-transitions`.
- `snapshot`, `keyframes`, `beats`, `audio`, `normalize-audio`, `compare`, `grade-compare`, `diff`, `measure`, `media-treatment`.
- `history`, and the `timeline` edit verbs.
- `play`, `present`, `open`, `catch-up` (desktop app not installed).
- `publish`, `cloud`, `lambda`, `cloudrun`, `auth`, `billing`: account, cost or public side effects.
- `tts`, `transcribe`, `remove-background`, `models install`: model downloads.
- `skills check|update`: would touch global skill folders.
- `feedback`: public channel, not sent.
- `init --example <name>` for registry examples, and `capture <url>`.
- Whether `--skip-skills` works without the environment variable (C5).
- Offline rendering, and whether fonts are re-downloaded on every render.
- Cross-host or Docker determinism.
- Long-composition performance (the 60 fps scaling claim at length).
- Sub-composition (`data-composition-src`) rendering of the installed `hw-title` block: it was installed and linted but not mounted or rendered.

## Part IV — `--help` index captured in the lab

| Command | Description (from --help) | Usage | Arguments | Flags |
|---|---|---|---|---|
| `add` | Install a block or component from the registry into this project | `add [OPTIONS] <NAME>` | NAME  Registry item name or tag. Single items install directly (e.g. shader-wipe). If the name matches a tag instead, all blocks with that tag are installed (e.g. html-in-canvas, captions). Give several names to install each of them in one call. (Required) | `--dir=…` `--clipboard` `--no-clipboard` `--json` `--vars=…` `--force` |
| `audio` | Measure how sound moves in time: where it lands, its hits, loudness and silence | `audio [OPTIONS] [FILES]` | FILES  Audio or video files to analyze | `--dir=…` `--element=…` `--at=…` `--range=…` `--place-at=…` `--skip-file-seconds=…` `--only=…` `--quality=…` `--provider=…` `--onset-method=…` `--threshold=…` `--band=…` `--hop-ms=…` `--onset-ratio=…` `--tail-db=…` `--silence-db=…` `--full` `--read` `--transcript=…` `--json` |
| `auth` | Sign in to HeyGen and manage credentials | `auth login|status|logout|refresh` |  |  |
| `beats` | Detect beats in the project music track (writes beats/<audio>.json) or in one audio file | `beats [OPTIONS] [DIR]` | DIR  Project directory, or one audio or video file to analyse | `--json` |
| `benchmark` | Render with preset fps/quality/worker configs and compare speed and file size | `benchmark [OPTIONS] [DIR]` | DIR  Project directory | `--runs=…` `--json` |
| `billing` | Open the HyperFrames plans or credits page and wait until the person is done (subscribe / top-up) | `billing [OPTIONS] <ACTION>` | ACTION  subscribe / top-up (Required) | `--needed=…` `--tool=…` `--timeout=…` |
| `browser` | Manage the Chrome browser used for rendering | `browser [OPTIONS] [SUBCOMMAND]` | SUBCOMMAND  ensure = find or download Chrome, path = print executable path, clear = remove cached download | `--force` |
| `capture` | Capture a website as editable HyperFrames components | `capture [OPTIONS] [URL]` | URL  Website URL to capture (omit when using --local-file or --video) | `--local-file=…` `--local-root=…` `-o, --output=…` `--skip-assets` `--skip-vision` `--max-screenshots=…` `--timeout=…` `--capture-budget=…` `--json` `--video=…` `--index=…` `--video-url=…` `--list` |
| `catalog` | Browse and install blocks and components from the registry | `catalog [OPTIONS] [WORDS]` | WORDS  Search words, same as --query (e.g. `catalog crossfade`) | `--type=…` `--tag=…` `--json` `--human-friendly` `--query=…` `-y, --yes` `--on-device` |
| `catch-up` | See what was done in the desktop app since you last looked | `catch-up [OPTIONS] [DIR]` | DIR  Project directory (default: current) | `--json` |
| `check` | Run lint, runtime, layout, motion, and WCAG contrast verification in one browser session | `check [OPTIONS] [DIR]` | DIR  Project directory | `--json` `--samples=…` `--range=…` `--components=…` `--at=…` `--at-transitions` `--max-transition-samples=…` `--max-issues=…` `--collapse-static` `--no-collapse-static` `--tolerance=…` `--timeout=…` `--contrast` `--no-contrast` `--strict` `--prepare-media` `--proxy` `--browser-gpu` `--snapshots` `--caption-zone=…` `--frame-check=…` `--layout=…` |
| `clean` | Find and remove what HyperFrames left on disk | `clean [OPTIONS] [DIR]` | DIR  Project directory (default: current); its subfolders are not searched | `--dry-run` `--snapshots` `--json` |
| `cloud` | Render HyperFrames compositions on the HeyGen cloud | `cloud render|list|get|delete` |  |  |
| `cloudrun` | Deploy and drive renders on Google Cloud Run | `cloudrun [OPTIONS] [SUBCOMMAND] [TARGET] [EXTRA]` | SUBCOMMAND  deploy / sites / render / render-batch / progress / destroy; TARGET  Subcommand positional (project dir, execution name, sites verb); EXTRA  Extra positional (e.g. `sites create <projectDir>`) | `--project=…` `--region=…` `--image=…` `--repo=…` `--cpu=…` `--memory=…` `--max-instances=…` `--timeout=…` `--site-id=…` `--width=…` `--height=…` `--fps=…` `--format=…` `--codec=…` `--quality=…` `--chunk-size=…` `--max-parallel-chunks=…` `--target-chunk-frames=…` `--output-resolution=…` `--variables=…` `--variables-file=…` `--strict-variables` `--batch=…` `--max-concurrent=…` `--dry-run` `--render-id=…` `--output-key=…` `--wait` `--wait-interval-ms=…` `--json` |
| `compare` | Render independent composition variants into one labeled comparison sheet | `compare [OPTIONS] [PATH]` | PATH  Composition project directory or .html file (pass 2+ paths) | `--at=…` `--labels=…` `--out=…` `--cols=…` `--timeout=…` `--json` |
| `compositions` | List all compositions in a project | `compositions [OPTIONS] [DIR]` | DIR  Project directory | `--json` |
| `diff` | Score a render or a project against the original video frame by frame: SSIM, worst moments, cuts, segments | `diff [OPTIONS] <REFERENCE> <YOURS>` | REFERENCE  The original video (Required); YOURS  A rendered video, or a project folder (captured at the original's frame times, no render) (Required) | `--at=…` `--range=…` `--segments=…` `--ledger=…` `--project=…` `--min-mean=…` `--min-p05=…` `--min-cell=…` `--worst=…` `--sbs` `--out=…` `--timeout=…` `--drawn=…` `--json` |
| `docs` | View inline documentation in the terminal | `docs [OPTIONS] [TOPIC]` | TOPIC  Topic: data-attributes, examples, rendering, gsap, troubleshooting, compositions, motion-blur. Omit to list all.;  |  |
| `doctor` | Check system dependencies and environment | `doctor [OPTIONS]` |  | `--json` |
| `events` | Emit a skill-usage telemetry event (skills report their own invocation/outcome). Honors DO_NOT_TRACK / telemetry opt-out. | `events [OPTIONS]` |  | `--skill=…` `--event=…` `--outcome=…` |
| `feedback` | Submit feedback about your experience | `feedback [OPTIONS]` |  | `--rating=…` `--comment=…` `--source=…` `--search-miss=…` `--wanted=…` `--tier=…` `--file-issue` `--dir=…` `-y, --yes` |
| `figma` | Import figma assets, tokens, and components (REST) | `figma asset|tokens|component` |  |  |
| `grade-compare` | Render candidate color grades onto a reference frame as one comparison PNG | `grade-compare [OPTIONS] --for=<for>` |  | `--for=…` `--grades=…` `--luts=…` `--project=…` `--out=…` `--json` `--timeout=…` `--baseline` `--no-baseline` |
| `history` | List, undo and restore the project's recorded changes | `history [OPTIONS] show|undo|restore|peek|pin|begin|end` |  | `--dir=…` `--json` `--since=…` `--who=…` `--limit=…` |
| `info` | Print project metadata | `info [OPTIONS] [DIR]` | DIR  Project directory | `--json` |
| `init` | Scaffold a new composition project | `init [OPTIONS] [NAME]` | NAME  Project name | `-e, --example=…` `-t, --template=…` `-v, --video=…` `-V, --video-legacy=…` `-a, --audio=…` `--skip-transcribe` `--keep-original` `--model=…` `--language=…` `--non-interactive` `--agent` `--skip-skills` `--tailwind` `--resolution=…` `--skill=…` |
| `inspect` | Inspect rendered composition layout for text/container overflow, plus optional motion verification via a *.motion.json sidecar (deprecated, use check) | `inspect [OPTIONS] [DIR]` | DIR  Project directory | `--json` `--samples=…` `--at=…` `--at-transitions` `--max-transition-samples=…` `--tolerance=…` `--timeout=…` `--max-issues=…` `--collapse-static` `--no-collapse-static` `--strict` |
| `keyframes` | See, debug, and refine keyframes — surface GSAP, CSS @keyframes, Anime.js, paths, and onion-shot diagnostics | `keyframes [OPTIONS] [TARGET]` | TARGET  Project dir or composition .html | `--selector=…` `--runtime=…` `--json` `--shot=…` `--samples=…` `--layout=…` `--from=…` `--to=…` `--angle=…` `--fit` `--no-fit` `--ghost` |
| `lambda` | Deploy and drive renders on AWS Lambda | `lambda [OPTIONS] [SUBCOMMAND] [TARGET] [EXTRA]` | SUBCOMMAND  deploy / sites / render / progress / destroy / policies; TARGET  Subcommand-specific positional (project dir, render id, policies verb, etc.); EXTRA  Extra positional (e.g. `sites create <projectDir>` or `policies validate <policy.json>`) | `--stack-name=…` `--region=…` `--profile=…` `--concurrency=…` `--chrome-source=…` `--memory=…` `--video-arch=…` `--skip-build` `--warm` `--no-warm` `--site-id=…` `--width=…` `--height=…` `--output-resolution=…` `--fps=…` `--format=…` `--codec=…` `--quality=…` `--keyframe-interval=…` `--max-bitrate=…` `--buffer-size=…` `--prores-profile=…` `--chunk-size=…` `--max-parallel-chunks=…` `--target-chunk-frames=…` `--execution-name=…` `--output-key=…` `--variables=…` `--variables-file=…` `--strict-variables` `--batch=…` `--max-concurrent=…` `--dry-run` `--wait` `--wait-interval-ms=…` `--json` |
| `layout` | Inspect rendered composition layout for text/container overflow, plus optional motion verification via a *.motion.json sidecar (deprecated, use check) | `layout [OPTIONS] [DIR]` | DIR  Project directory | `--json` `--samples=…` `--at=…` `--at-transitions` `--max-transition-samples=…` `--tolerance=…` `--timeout=…` `--max-issues=…` `--collapse-static` `--no-collapse-static` `--strict` |
| `lint` | Validate a composition for common mistakes | `lint [OPTIONS] [DIR]` | DIR  Project directory, or one composition .html file | `--json` `--verbose` |
| `measure` | Measure a video file as JSON: clock, cuts, events, frames, crops, eases, motion energy, ink, look, faces, lip sync | `measure probe|cuts|events|frames|extract|curve|energy|ink|look|face|sync` |  |  |
| `media-treatment` | Discover, apply, or clear deterministic media treatments | `media-treatment [OPTIONS]` |  | `--capabilities` `--capability=…` `--all` `--project=…` `--file=…` `--selector=…` `--selector-index=…` `--grading=…` `--apply` `--analyze` `--clear` `--dry-run` `--json` |
| `models` | List or download on-device models (models list, models install parakeet) | `models [OPTIONS] <ACTION> [NAME]` | ACTION  list or install (Required); NAME  Model to install: parakeet | `--json` |
| `normalize-audio` | Normalize a clip with sound to an absolute LUFS target, or match it to another clip | `normalize-audio [OPTIONS] [DIR] --target=<target>` | DIR  Project directory | `--reference=…` `--target=…` `--lufs=…` `--write` `--tolerance=…` `--json` |
| `open` | Open a project in the HyperFrames desktop app | `open [OPTIONS] [DIR]` | DIR  Project directory (default: current) | `--json` |
| `play` | Play a composition in a lightweight browser player | `play [OPTIONS] [DIR]` | DIR  Project directory | `--port=…` `--open` `--no-open` `--browser-path=…` `--user-data-dir=…` `--remote-debugging-port=…` `--proxy` `--no-proxy` |
| `present` | Serve a slideshow deck and open it in presenter mode (with audience sync) | `present [OPTIONS] [DIR]` | DIR  Project directory | `--port=…` `--open` `--no-open` `--browser-path=…` `--user-data-dir=…` `--remote-debugging-port=…` |
| `preview` | Start the studio for previewing compositions | `preview [OPTIONS] [DIR]` | DIR  Project directory | `--port=…` `--force-new` `--background` `--foreground` `--status` `--stop` `--list` `--kill-all` `--lint-verbose` `--open` `--no-open` `--selection` `--json` `--context` `--context-fields=…` `--context-detail=…` `--browser-path=…` `--user-data-dir=…` `--remote-debugging-port=…` `--browser-no-gpu` `--browser-gpu` `--proxy` `--no-proxy` |
| `publish` | Upload the project to a stable URL (private by default) | `publish [OPTIONS] [DIR]` | DIR  Project directory | `-y, --yes` `--public` `--update=…` `--space=…` `--proxy` `--lint-verbose` |
| `remove-background` | Remove background from a video or image using a local AI model — outputs transparent WebM, ProRes 4444, or PNG | `remove-background [OPTIONS] [INPUT]` | INPUT  Source video (.mp4/.mov/.webm/.mkv) or image (.jpg/.png/.webp) | `-o, --output=…` `-b, --background-output=…` `--device=…` `--quality=…` `--info` `--json` |
| `render` | Render a composition to MP4, WebM, MOV, GIF, HLS, or a PNG sequence | `render [OPTIONS] [DIR]` | DIR  Project directory | `-c, --composition=…` `-o, --output=…` `-f, --fps=…` `-q, --quality=…` `--skill=…` `--format=…` `--gif-loop=…` `--hls-segment-seconds=…` `--video-frame-format=…` `--page-motion-blur=…` `-w, --workers=…` `--docker` `--hdr` `--sdr` `--crf=…` `--start=…` `--end=…` `--video-bitrate=…` `--keyframe-interval=…` `--max-bitrate=…` `--buffer-size=…` `--prores-profile=…` `--vp9-cpu-used=…` `--gpu` `--browser-gpu` `--quiet` `--lint-verbose` `--debug` `--best-effort` `--no-best-effort` `--strict` `--strict-all` `--max-concurrent-renders=…` `--variables=…` `--variables-file=…` `--strict-variables` `--batch=…` `--batch-concurrency=…` `--batch-fail-fast` `--json` `--resolution=…` `--page-side-compositing` `--no-page-side-compositing` `--browser-timeout=…` `--protocol-timeout=…` `--player-ready-timeout=…` `--resume` `--keep-segments` `--low-memory-mode` `--experimental-fast-capture` `--frames-cache-dir=…` |
| `skills` | Install, check, and update HyperFrames skills for AI coding tools | `skills check|update` |  |  |
| `snapshot` | Capture key frames from a composition as PNG screenshots for visual verification | `snapshot [OPTIONS] [DIR]` | DIR  Project directory | `--frames=…` `--at=…` `--range=…` `--composition=…` `--timeout=…` `--angle=…` `--end` `--no-end` `--keep` `--zoom=…` `--zoom-scale=…` `--against=…` `--review` `--json` `--describe=…` `--proxy` `--browser-gpu` |
| `telemetry` | Manage usage telemetry | `telemetry [OPTIONS] [SUBCOMMAND]` | SUBCOMMAND  Subcommand: enable, disable, status;  |  |
| `timeline` | Print and edit the project's tracks and clips | `timeline [OPTIONS] [DIR] move|trim|split|delete|set|duplicate|ids|apply|undo` | DIR  Project directory | `--component=…` `--at=…` `--range=…` `--boundary=…` `--generation=…` `--offset=…` `--json` |
| `transcribe` | Transcribe audio/video to word-level timestamps, or import an existing transcript | `transcribe [OPTIONS] <INPUT>` | INPUT  Audio/video file to transcribe, or transcript file to import (.json, .srt, .vtt) (Required) | `-d, --dir=…` `-e, --engine=…` `--speakers` `-m, --model=…` `-l, --language=…` `--json` `--to=…` `-o, --output=…` `--preserve-cues` `--runtime-install` `--no-runtime-install` `--optional` `--timeout=…` |
| `tts` | Generate speech audio from text using a local AI model (Kokoro-82M) | `tts [OPTIONS] [INPUT]` | INPUT  Text to speak, or path to a .txt file | `--text-file=…` `-v, --voice=…` `-s, --speed=…` `-l, --lang=…` `--list` `--json` |
| `upgrade` | Check for updates and show upgrade instructions | `upgrade [OPTIONS]` |  | `-y, --yes` `--check` `--json` `--project=…` |
| `usage` | Read remaining harness subscription usage without telemetry | `usage [OPTIONS]` |  | `--harness=…` `--json` |
| `validate` | Load a composition in headless Chrome and report console errors (deprecated, use check) | `validate [OPTIONS] [DIR]` | DIR  Project directory | `--json` `--contrast` `--no-contrast` `--timeout=…` |
