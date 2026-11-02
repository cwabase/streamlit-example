# KB-11 — Worked Examples: one per mode

*PROMPT and DIRECT examples derive from source A (§4.4) and source B (§4.4); FIX, COACH and AUDIT are new syntheses.*

## 1. PROMPT — "FSY in December, youth, Reels" (French, 30 s, 9:16 + 16:9 cut-down)

**Intake table (excerpt).** Mode PROMPT (stated) · Objective: registration (inferred from "promo") · Audience: 14–18, Abidjan, phone, in-feed, sound-off likely (inferred from Reels) · Message: *"Cette vidéo dit aux jeunes de 14 à 18 ans que FSY est l'endroit où l'on marche avec le Sauveur et avec des amis qui marchent dans la même direction"* (derived from the 2026 theme; confirm) · Destination → 1080×1920 (+1920×1080 variant) · Length 30 s ±0.5 (route band) · Type: promo → `/general-video` with variables (date, venue, URL) · Formed (the theme shapes the telling) · Visual system: light canvas made cinematic — cream #F6EFE4, ink #1B1F3B, one gold accent #F2B134; Archivo Black 400 display + Montserrat 700/400 text; headline 96 px, body 36 px, captions 64 px; 4-column grid, 72 px padding; safe box x 120–780 / y 380–1248; key light top-left; gold path line as signature move · Audio: narration FR, young adult female, warm, 2.2 w/s (≈ 66 words); music = sells/inspires → scored (cinematic-pop build 116 BPM, piano under the hook, drums at 5 s, −24 dB and 1 s of silence before the scripture line, peak on the date, button at 29.2 s); SFX 9 cues (3 whooshes, 2 soft impacts, 1 shimmer, 3 UI pops); −14 LUFS, ≤ −1 dBTP; captions 3–5 words per group · Culture: Church standards; official-music terms; no lyrics under voice.

**Questions (≤ 3).** 1 "Date and venue — or shall I keep them as labelled placeholders? (recommended: placeholders now, variables later)". 2 "CTA words and URL?" No third question.

**Prompt set.** META (KB-03 §4.3.1 verbatim) → SYSTEM (KB-03 §4.3.2) → MASTER filled: PROJECT (title, message, CTA placeholder, audience, platform, 1080×1920 @30, 30 s, tone "chaleureux, lumineux, cinétique", references "Marche avec moi" for energy and theme line, the typical direction rejected: a slideshow of stock photos with a pop track) · SOURCE AND FACTS (theme line Moses 6:34; logo resolved never redrawn; dates/venue placeholders) · STRUCTURE (Hook → Promise → Proof → Invitation → CTA; 6 beats; rhythm PUNCH-breathe-fast-fast-HOLD-button; hook = contrast "Seul, c'est dur. Ensemble, on avance." over a split frame closing into one path) · VISUAL SYSTEM (tokens above; images treated; no banned tells) · MOTION (headline SLAMS 0.28 s `expo.out`; path DRAWS 0.6 s `power2.inOut`; panels SLIDE alternating 0.4 s `power3.out` + Ken Burns 1→1.04; date card LOCKS IN 0.3 s `back.out(1.5)` — the one playful overshoot; exits 0.2 s `power2.in`; hard cuts on the beat in the proof run; `sdf-iris` 0.6 s into the CTA) · AUDIO (as above) · TECHNICAL (probe version/skills/usage; sub-composition per scene; caption track; variables for date/venue/URL) · OUTPUTS (MP4 9:16 + 16:9 from one source; SRT; stems; assumptions list; HANDOFF.md) · GATES (storyboard → board → final look; lint 0 → check 0 → snapshots → ffprobe → ebur128; 35 items + 12 dimensions). STAGE prompts attached; EVALUATOR prompt attached.

**Tips and angles.** The theme line is both message and button; frame 0 is the thumbnail (two silhouettes, one path); the music's silence before scripture is the spectacle of restraint; French VO slower (2.2 w/s) with captions mandatory; verify dates before build — a labelled placeholder is the honest fallback.

## 2. DIRECT — "Ledgerly" 30-second product promo (English, 16:9) — beat table from source B

"This video tells freelancers that invoices can be sent and paid in three taps."

| # | Time | Job (why) | Element | Verb | Copy | VO | SFX | Out |
|---|---|---|---|---|---|---|---|---|
| 1 | 0.0–3.0 | Hook: show the payoff first | Invoice plane | Folds, launches | "Paid. / Already." | "Already paid?" | Paper flick at 0.5 s | Cut on motion |
| 2 | 3.0–8.0 | Problem: the chase | Overdue stack | Piles up, wilts | "Chasing payments?" | "Still chasing clients?" | Soft thud | Push-slide up |
| 3 | 8.0–19.0 | Proof: three taps | Phone UI (HTML rebuild) | Taps, fills, sends | "Create · Send · Paid" | "Three taps. Done." | Clicks on contact frames | Push-slide up |
| 4 | 19.0–25.0 | Value: the number | "2× faster" stat | Counts up, holds | "Invoices sent 2× faster" | "Twice as fast." | Chime on landing | Context zoom |
| 5 | 25.0–30.0 | CTA, callback | The plane | Lands on the CTA | "Start free — ledgerly.app" | "Start free today." | Stamp | End hold ≥ 2.5 s |

Gates: plan approved → sketch board → lint 0 → check 0 (audits ran) → strips across every cut → preview → render `--quality delivery` → `qa_render.py` → scorecard and rubric. Rhythm: PUNCH-build-build-HOLD-button. Music: light bed 108 BPM, carved; silence 0.5 s before "Twice as fast." A's second DIRECT example (the 60 s audit-team data explainer with a beatless bed out under the figures) is in KB-03 §4.4.2.

## 3. FIX — "The render feels generic and the voice is buried" (60 s explainer, 16:9)

**Watch three ways.** With sound: the bed masks consonants from 0:08 to 0:41. Muted: the message survives but every scene enters from the bottom with the same ease. Sound only: narration intelligible alone; music has a lead melody in the voice band.

**Freeze three frames.** 0:00 — a gradient-text title centred on a dark linear gradient (banding visible); 0:27 — a four-metric card grid, identical cards, 14 px labels; 0:58 — logo fades to black before the CTA is readable.

**Evidence.** `lint`: 0 errors. `check --json`: contrast finding on 0:27 labels (3.1:1). Strips: double exit at 0:18 (element fades, then the crossfade fades it again). `ebur128`: integrated −11.8 LUFS, true peak +0.3 dBTP. Animation map: dead zone 0:44–0:47.

**Diagnosis table.**

| Time | Symptom | Cause | Owner | Fix | Evidence after |
|---|---|---|---|---|---|
| 0:00 | Banding + gradient text; centred floating title | Full-screen linear gradient; AI tells | D3.3, D3.1 | Solid ink canvas + radial accent glow 18 %; solid-colour display type; anchor to the left third; 3 % grain | snapshot 0:00 |
| 0:08–0:41 | Voice buried | Bed with melody at −9 dB, duck only | D7.2 | Instrumental bed; carve 0.8 against the voice group; bed −16 dB under speech, −8 in gaps | ebur128 + listening pass |
| 0:18 | Double exit | Element exit tween + crossfade | D6.5 | Remove the element exit; the transition owns the scene exit | strips 0:17.5–0:18.5 |
| 0:27 | Four identical cards; labels 14 px at 3.1:1 | Web pattern; web sizes | D3.4, D3.2 | Three metrics max, one per moment with proportional bars; labels 22 px; contrast ≥ 4.5:1 (target 7:1) | check contrast = 0 findings |
| all | Same entrance everywhere | `y: 30, opacity: 0` on every element | D6.2 | Vary direction and ease per scene; ≤ 2 shared eases; first motion +0.2 s | strips |
| 0:44–0:47 | Dead zone | Nothing moves 3 s | D3.5 | One ambient motion on the decoratives; hold is 1.5 s, not 3 | animation map |
| 0:58 | CTA unreadable | Fade to black before the hold | D2.1e | Lock-up on the final hit; hold ≥ 2.5 s; no fade before it is read | snapshot 0:58–1:00 |
| master | −11.8 LUFS, +0.3 dBTP | No limiter; mixed to preview volume | D7.5 | `truepeak` last at −3 dBTP; target −14 LUFS; measure the delivered file | ebur128 |

**Ranked revisions.** 1 Voice/bed (message intelligibility). 2 CTA hold. 3 Title frame. 4 Card grid → three metrics. 5 Entrance variety. 6 Double exit. 7 Dead zone. 8 Master. Each written as time · symptom · result · scope; one variable per edit; freeze scenes 2 and 4 (already strong); re-render spans only; before/after stills.

**Coach line.** "The brief never named the bed level or the banned list — add the level stack and the avoid-list to the SYSTEM prompt and this cannot recur."

## 4. COACH — "Why do my transitions feel random?"

**Principle.** Transitions carry meaning: a hard cut says *wake up*, a crossfade says *this continues*, a slow dissolve says *drift with me* [Documented, motion-principles]. A new effect per cut tells the viewer nothing. **Number.** One primary transition for 60–70 % of cuts plus at most two accents; 1–2 shader heroes per 5–7 beats; presets 0.15 / 0.2 / 0.4 / 0.5 / 0.6 / 0.7 s; velocity-match seams within ~5 %; blur on at most three beats; the transition owns the scene exit. **Example.** HeyGen's launch film: one calm house style for most cuts, and a deliberate hard-smash-cut montage *because* the variety is the argument. **Exercise.** Take your storyboard; write the relation between each pair of beats (continues / contrasts / reveals / lists); assign cut, CSS or shader by relation; delete every separate exit animation; re-time two seams to velocity-match. **Watch for.** Double exits in the strips; a shader used as connective tissue; a cut that is not on a beat.

## 5. AUDIT — a 15-second social sting (9:16), scored

**Gates.** lint 0 ✔ · check 0 findings, audits ran ✔ · motion assertions ✔ · ffprobe 1080×1920 @30, 15.00 s, AAC ✔ · fonts embedded ✔ · claims: n/a ✔ · flashes ≤ 3/s ✔ · loudness −14.4 LUFS, −1.2 dBTP ✔ · final look approved ✔.

**35-item checklist.** 33 PASS; 1 FAIL (item 9: caption group at 0:11 enters the bottom 25 % UI zone); 1 NOT VERIFIABLE (item 23: phone-speaker listening not performed — measurement only).

**Rubric (separate judge, evidence first).** Purpose 5 · Story 4 · Pacing 5 · Composition 3 (caption zone) · Typography 4 · Colour/light 4 · Assets 5 · Motion 5 · Transitions 4 · Sound 4 · Accessibility 3 (caption zone) · Coherence 5 → average 4.25, minimum 3 → **ships**; not yet *exceptional* (two dimensions below 4). **Freeze list:** scenes 1 and 3. **Ranked fixes:** move captions into the safe box (y ≤ 1248); re-snapshot 0:10–0:12; re-score composition and accessibility.
