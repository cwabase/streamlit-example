# KB-07 — Audio Direction

*Composite. Part I is Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026) §3.6: the layers and the one rule, narration, the music decision rule, the theme guide, audience adjustments (faith/FSY, West Africa, EN/FR, youth, executives), paste-ready music briefs, synchronisation, SFX in numbers, mix and delivery. Part II is Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229) §3.7: strategy first, narration, music, SFX, silence, mix targets, balance and ducking, sync, captions, measurement.*

*Section numbers inside each part keep the numbering of the source they came from (A = §2–§7 and appendices of the Skillgraph document; B = Parts 3–8 of the Claude Code document). Where the two parts disagree, the preface and KB-14 govern; where either disagrees with the installed CLI, the CLI wins.*

## 0. Reconciled levels (VO = 0 dB)

bed −14…−20 dB under speech (≥ 10 LU floor; ≥ 15 LU dense; ≥ 20 dB accessibility-critical), −6…−10 in gaps · SFX accents −8…−14 during speech, −6…−10 in gaps · hero hits −3…−6 in gaps · ambience −20…−30 · carve 0.8 against the voice group (lower if the bed is notched) · `truepeak` limiter last at −3 dBTP · targets −14 LUFS web, −16 voice-led, −23 R128, −24 A/85; ≤ −1 dBTP (−2 shared/broadcast) · measure the delivered file (`ffmpeg -af ebur128` or `qa_render.py`) · `data-volume` is linear: 0.5 ≈ −6 dB, 0.25 ≈ −12, 0.1 = −20, 0.6 ≈ −4.5 · SFX never generated — retrieved or bundled · one sound per stagger · transients at 0 to +1 frame, never early · silence 0.3–1 s before the key line; −24 dB or silence under scripture.

## Part I — Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026)

#### 3.6 Audio architecture

##### 3.6.1 The layers and the one rule

| Layer | Job | Rule | Tag |
|---|---|---|---|
| Narration (VO) | Carries meaning | Always intelligible; everything else yields to it | [Recommended] |
| Music bed | Emotion and pace | **Carved** around the voice (not merely ducked); edited on bar lines | [Documented] production-loop.md: "when BGM plays under a voice, the bed is carved … a duck alone is not a finished mix"; `data-fx-carve` (R1) |
| SFX accents | Punctuate motion | On the frame; in VO gaps when possible | [Recommended] |
| Hero SFX (risers, impacts) | Mark the 2–5 biggest moments | Rare, or they stop meaning anything | [Recommended] |
| Ambience / room tone | Glue and sense of place | Continuous, low, J-cut across scene changes | [Recommended] |
| Designed silence | Contrast | A music drop before the biggest reveal; at least one per 60 s in story pieces | [Recommended] |

**One lead at a time**: while the voice speaks, music and SFX step back; between phrases they come forward. HyperFrames' audio model [Documented, R1]: four attributes — `data-fx-chain` (effect nodes in signal order; on the root it is the master bus), `data-automation` (volume or `fx.<node>.<param>` lanes, up to 512 points), `data-fx-carve` (voiceover carve/sidechain on a bed) and `data-audio-group` (membership in an `<hf-audio-group>` bus); sixteen effects including `compressor`, `limiter` and `truepeak`; 22 presets. Until v0.8.228 nothing limited the summed mix; from v0.8.228 only over-ceiling peaks are brought down on export. Lint flags ungrouped carve sources and doubled volume automation.

##### 3.6.2 Narration

- Natural pace 2.5 words/s (15 s ≈ 37 words, 30 s ≈ 75, 60 s ≈ 150); the script should feel *shorter* than the video. [Documented] narration.md. Genre bands [Recommended]: 2.3–2.5 w/s explainers and promos; 2.0–2.3 documentary, premium, second-language; 2.6–3.0 hype social; 1.8–2.2 children, older viewers, learning.
- Pauses 0.3–0.6 s between sentences, 0.8–1.5 s between beats. "Silence between sentences is a feature" (launch storyboard) [Demonstrated].
- Write like a person: contractions, varied sentence length, read aloud. Write numbers as the voice should say them ("nearly two trillion dollars", "A P I", "stripe dot com") — the visual shows the exact figure while the voice rounds it. [Documented] narration.md. Verify acronyms by transcribing the TTS back: "text to speech reads 'ID' as a word. Write 'I.D.'" (OneWave) [Demonstrated].
- Lock the narration in `SCRIPT.md`; produce TTS with **word timestamps** so captions and on-word animation hit exactly; real voice duration trues the scene durations and synced values are never hand-edited. [Documented] script-format.md; production-loop.md § Duration sync.
- Transcription defaults to Parakeet (6.05 % WER vs 7.44 % for whisper.cpp, 5–10× faster) with whisper.cpp fallback. [Documented] media-use audio.md. Voice sources in real pipelines: HeyGen voices, ElevenLabs, edge-tts, local Kokoro; a synthetic-voice "on set" chain of room tone, roll-off above 7 kHz, light compression and a short room reverb reads less robotic (Anfloy) [Demonstrated].

##### 3.6.3 Music — does this video need it?

Ask in order; the first "yes" decides [Recommended, carried forward]:

1. **Is the subject grave** (tragedy, grief, a diagnosis, an apology, a crisis, testimony, a legal statement)? → **No music.** Room tone or a very low drone. Silence is respect.
2. **Is there no narration** (motion graphic, montage, sting, loop)? → **Music required** — it is the voice, and the cut follows its grid.
3. **Is it step-by-step instruction** (software tutorial, training, compliance)? → **None or a near-silent bed** (−24 to −30 dB under the VO, no melody), music only on intro, outro and section cards.
4. **Is it news, analysis, findings or figures?** → **A tension or ambient bed with no melody**, −18 to −24 dB, pulled out entirely under key facts.
5. **Does it sell, inspire or tell a story?** → **Music, scored to the arc**: sparse under the hook, a lift at the value claim, a peak at the hero moment, resolution on the CTA.
6. **Mute test.** Mute the music. If the film gets slower or flatter, keep it; if the narration gets clearer and nothing is lost, cut it or swap in ambience.

Always: instrumental only under a voice; one bed per video (or per chapter), changing only at structural boundaries. A music map — entry, build, reduction, silence, resolution — is part of the storyboard. The official prompting guide's Linear.app example sets a BGM ceiling of −18 dB in the prompt itself [Documented, R2].

##### 3.6.4 Theme guide

Levels are relative to the voice (VO = 0 dB). BPM and instrumentation are creative starting directions, not rules about groups of people — check the actual audience's expectations. [Recommended]

| Theme | Music? | Style · BPM | Bed vs VO | Palette of SFX/ambience | Avoid |
|---|---|---|---|---|---|
| Tech / SaaS / AI launch | Yes | Modern electronic, warm pads, muted plucks, tight drums · 100–124 | −14 to −18 dB | soft UI clicks, data blips, airy whooshes | "inspiring corporate" ukulele; EDM drops under VO |
| Product demo / UI walkthrough | Light | Minimal lo-fi, steady pulse, no lead melody · 95–115 | −18 to −22 dB | real UI clicks, keystrokes, swipes | music fighting the UI sounds |
| Finance / audit / data reporting | Optional; none under findings | Restrained ambient pad, subtle piano or strings · beatless–95 | −20 to −24 dB | paper and ledger foley, soft ticks | tension cues on numbers, upbeat music over losses, sensational hits |
| News / analysis | Minimal | Tension bed: drones, ticking hats, muted stabs · beatless–120 | −18 to −24 dB, out under key facts | teleprinter ticks, stingers | melody, drops, music under tragedy |
| Documentary / history / science | Yes, dynamic | Ambient piano, cello, string pads · free time–90 | −16 to −22 dB | place soundscapes, archival crackle | wall-to-wall music, "epic" from minute one |
| Explainer / education | Light or none | Lo-fi or soft electronic loop · 85–110 | −18 to −24 dB (≥ 20 dB if accessibility-critical) | pops, soft clicks, pencil, "aha" chimes | vocals; busy melodies in the 1–4 kHz voice band |
| Faith, devotional and youth events (FSY, YSA) | Promos yes · devotionals optional | Promos: uplifting cinematic-pop build with piano, strings, soft drums · 100–120, rising and warm. Devotionals: gentle piano and strings or a hymn-based instrumental · 60–80 | about −18 dB; −24 dB or silence under scripture | warm whooshes, soft impacts on title and date, a shimmer on the logo | worldly lyrics, aggressive drops, anything outside the Church's standards and its terms for official music |
| Event promos and hype reels | Yes, music-led | Cinematic-electronic with big drums; for West African youth, Afro-pop / Afrobeats-inspired instrumentals (about 100–115) where they fit · 115–130; hook → build → drop on the reveal → button | full level without voice; −12 to −15 dB under short tags | risers, impacts, glitches | off-beat cuts, drops mid-sentence, more than one big drop per 30 s |
| Motivational / sport | Yes, building | Piano → strings → big drums, half-time · 80–100 | −14 to −18 dB, up to −8 in gaps | breaths, crowd swells, impacts on key lines | full intensity from second one |
| Luxury / fashion / real estate | Yes, minimal | Deep house, neo-classical piano, jazz trio · 90–118 | often no VO; else −16 to −20 dB | tactile foley: fabric, glass, water | busy stock tracks, cartoon whooshes |
| Health / wellness | Yes, soft | Ambient pads, felt piano, gentle guitar · 60–85 or beatless | −18 to −24 dB | breath, water, birds | heavy percussion, sudden hits |
| Kids / family | Yes, bright | Ukulele, glockenspiel, marimba, claps, major key · 110–130 | −14 to −18 dB | soft boings, pops, sparkles | harsh highs, loud booms, scary drones |
| Gaming / esports | Yes, driving | Trap, EDM, synthwave, DnB · 120–150 (DnB 160–175) | −12 to −16 dB | glitches, zaps, bass drops | drops masking VO; copyrighted OSTs |
| Corporate / HR / training | Light or none | Light modern corporate, soft piano, plucks · 95–115 | −18 to −24 dB | soft clicks, chimes | emotional manipulation |
| Nonprofit / social cause | Yes, sparing | Sparse piano, solo cello, strings · 60–85 | −16 to −22 dB; silence on the hardest images | real field ambience | uplifting cues over suffering |
| Exhibition / silent autoplay / loop | Designed loop, sparse ambience or no audio | — | — | — | information that exists only in sound |

##### 3.6.5 Audience adjustments [Recommended]

| Audience | Adjust |
|---|---|
| Youth (14–18) / short-form feeds | Hook in 1 s; a new visual every 1.5–3 s; more energy (110–128 BPM), contemporary sounds; bed −12 to −16 dB; captions mandatory; licensed or original music only |
| Young adults (18–30) | Authentic over salesy: indie, lo-fi, Afro-pop instrumentals at 95–120 BPM; no over-produced hype |
| Executives and leaders | Voice first; minimal bed at about −20 dB or none; half the effects; no hype hits or long intros |
| Professionals / peers / B2B / LinkedIn | Bed −18 to −24 dB or none; ≤ 10 SFX per minute; music off under data and findings; captions mandatory (muted autoplay) |
| Learners | Music off during content; a short, consistent 1–2 s motif marks each new section (sound as navigation) |
| Children | VO 1.8–2.2 w/s; bright melodic music; soft SFX; no sudden peaks; repetition |
| Older adults (60+) | VO about 2.0 w/s; bed ≥ 20 dB under speech; fewer high-frequency sparkles; larger type |
| Faith communities | Reverent, warm, acoustic or orchestral for celebration; quiet for scripture and teaching |
| French-speaking and bilingual (EN/FR), incl. West Africa | Duck music about 3 dB deeper for second-language listeners and AI French voices; local colour (kora, balafon, djembe-inspired textures, Afro-pop rhythms) where it fits and never as cliché — do not infer a genre from nationality alone; mix for phone speakers; no lyrics in any language under the voice |
| Global / multilingual | Instrumental only; separate VO, music and SFX stems for dubbing (HeyGen `video-translate` dubbing exists [Documented] capability-menu.md) |
| Accessibility-critical | Background ≥ 20 dB below speech or none (WCAG 1.4.7 [Standard]); full captions; nothing conveyed by audio alone |
| Sound-off viewers | Design without it: burned-in captions; visual rhythm carries the beat; the first frame works in silence |

##### 3.6.6 Paste-ready music briefs

Keep library retrieval queries short (`bgm.query`: mood + genre + instruments); use the full line as `bgm.prompt` when generating; `bgm.mode` = `retrieve | generate | none`. Provider order for agent workflows: HeyGen catalog → Lyria → MusicGen. [Documented] media-use audio.md; authentication guide (R1). Examples [Recommended]:

- **Tech / SaaS**: "Instrumental modern electronic, 112 BPM, warm analog pads, muted pluck arpeggios, tight kick and clap, confident and optimistic, sparse 4-bar intro, lift at the value claim, clean ending hit, no vocals."
- **Finance / audit**: "Calm cinematic underscore, 92 BPM, soft strings, felt piano, light pulse percussion, trustworthy and steady, gradual build, resolved major ending, no vocals."
- **FSY youth promo (French, 16:9 and 9:16)**: "Uplifting cinematic-pop instrumental, 110–120 BPM, major key, piano intro, strings and soft drums entering with the first strong line, peak on the date and venue, clean button on the theme line, no vocals." Map: soft piano under the hook (0–8 s); drums with the first strong line; peak on the date and venue; button on the theme line. Levels: bed −18 dB; dips to −24 dB with 1 s of silence before the scripture.
- **Devotional**: "Gentle hymn-like piano and strings, 66 BPM, warm and reverent, long sustained phrases, no percussion, no vocals."
- **Explainer**: "Light lo-fi electronic, 96 BPM, mellow keys, soft kick, simple four-chord loop, curious and friendly, low density, no vocals."
- **Documentary**: "Reflective underscore, 72 BPM, ambient piano, solo cello, soft string pads, human and patient, long quiet passages with slow swells, no vocals."
- **Kids**: "Playful acoustic, 120 BPM, ukulele, glockenspiel, marimba, pizzicato strings, hand claps, bright major key, cheerful and curious, no vocals."
- **Nonprofit**: "Sparse emotional piano with solo cello, 72 BPM, intimate, hopeful resolution in the final 20 %, no vocals."

##### 3.6.7 Synchronisation

- SFX transients land on the exact frame: 0 to +1 frame late, never early. Viewers detect audio that leads the picture by more than about 45 ms or lags by more than about 125 ms (ITU-R BT.1359 detectability thresholds [Standard]); aim for ±1 frame.
- Whooshes peak at the fastest point of the move or on the cut — start the file early enough that its accent reaches the visual moment; placing the file start at the cut lands it late.
- A riser starts at the reveal minus its own length; an impact hits the landing frame and its tail J-cuts into the next scene; ambience and music may lead a scene change by 0.2–1 s.
- **Suck-out**: drop music and ambience 0.3–1.0 s before the biggest hit.
- Light ↔ sound: bloom and flash peak on the impact frame; glow pulses follow the kick (2–6 % scale or 10–20 % intensity); a riser gets a light ramp cresting on the reveal; a shimmer rides the light sweep.
- Cuts on beats, hero reveals on downbeats: at 120 BPM a beat is 0.5 s and a bar 2 s, so scenes cut to whole beats feel right even when nobody can say why. The beat grid comes from `analyze-beatgrid.py` → `audiomap.json` (beats, energy, sections) or the CLI `beats` / `audio` commands (moments, onsets, LUFS, beats, sections). [Documented] capability-menu.md; CLI reference (R1). Anfloy's rule for sound-off feeds: put scene boundaries on the beat grid "so cuts feel intentional even with the sound off" [Demonstrated].

All timing values above: [Recommended] unless tagged.

##### 3.6.8 SFX in numbers

**Palette** [Recommended; HyperFrames gain facts Documented]

| SFX type | Typical played length | Sync point | Level vs VO peak |
|---|---|---|---|
| UI click / tap / key | 30–150 ms | exact press frame | −8 to −14 dB |
| Pop / blip (element in) | 80–250 ms | appear frame or overshoot peak | −8 to −12 dB |
| Short whoosh / swipe | 250–700 ms | fastest frame of the move, or the cut | −6 to −12 dB |
| Cinematic whoosh build | 1.5–5.5 s | swell peaks on the cut | −6 to −10 dB |
| Riser | 2–4 s short-form · 4–10 s long-form | crests on the reveal | −8 to −12 dB, rising |
| Impact / bass hit | 50–150 ms hit + 1–2.5 s tail | landing frame of the hero element | −3 to −6 dB, in a VO gap |
| Chime / success | 0.8–2.5 s | element entering / success state | −8 to −12 dB |
| Glitch | 0.2–1 s accent | the cut or the distortion frame | −8 to −14 dB |
| Shimmer / sparkle | 0.8–1.8 s | rides the light sweep | −10 to −14 dB |
| Typing burst | matches the typing; cap 4–6 ticks per phrase | first character | −12 to −16 dB |
| Ambience / room tone | continuous | J-cut 0.3–1 s before the picture | −20 to −30 dB |

HyperFrames gain is **linear**: `data-volume` default 1 (0 dB), 0.5 ≈ −6 dB, 0.25 ≈ −12 dB, 0.1 = −20 dB, up to 3.98 (+12 dB); clip-edge fades use `data-fade-in` / `data-fade-out`; ducks and automation use the `data-automation` volume lane, and a timeline `volume` tween is ignored when a lane is present. [Documented] data-attributes.md; html-schema (R1). Played length is a trim decision, not the file's length. SFX resolve from Openverse (CC0 / CC BY, no account) with a bundled 21-file offline library; credit CC BY sounds wherever the video is published [Documented] media-use SKILL.md.

**Density** — merged from the earlier runtime table and style budgets **(revised: one matrix replaces two tables)** [Recommended]

| Style | Per minute | 15 s | 30 s | 60 s | 90 s | 3 min | 10 min |
|---|---|---|---|---|---|---|---|
| Sparse / reflective / luxury / documentary | 2–8 | 0–2 | 1–4 | 2–7 | 3–10 | 5–15 | 10–30 |
| Clear branded explainer with VO | 8–16 | 2–5 | 4–9 | 7–14 | 10–20 | 20–35 | 40–70 |
| Energetic promo / hype / kids / gaming | 16–32 | 5–10 | 8–14 | 12–20 | 16–28 | 30–45 | 60–90 |

Ratios [Recommended]: SFX per cut 0.3–0.6 narrated · 0.6–1.0 music-led promo · 0.1–0.3 documentary or luxury; hero : accent about 1 : 5 to 1 : 8; hero hits ≥ 15–20 s apart (≥ 8 s in hype edits); ≥ 0.5 s between accents unless a deliberate rhythmic run; a staggered group gets **one** sound; 2–4 variants per recurring type, never the same sample three times in a row, levels varied ±1–3 dB; at most two overlapping SFX layers (one low body + one high transient); 20–25 % of the timeline free of transients. A cue is one perceptual event even if built from two layers. Worked example: a 30 s explainer can be complete with two interaction clicks, one directional whoosh, one reveal impact and one closing chime — five cues; the official agent-built comparison film added "a music bed and five sound effects it chose" [Documented, R2].

**Level stack (VO = 0 dB)** [Recommended] **(revised: speech-time bands tightened by 2 dB to protect consonants on phone speakers)**: bed −14 to −20 dB under speech (−12 to −18 in the earlier standard), −6 to −10 dB in gaps · accents −8 to −14 dB under speech (−6 to −14 earlier), −6 to −10 in gaps · hero hits −3 to −6 dB in gaps · ambience −20 to −30 dB · SFX under speech always ≥ 8 dB under the voice.

##### 3.6.9 Mix and delivery

| Destination | Integrated loudness | True peak | Tag |
|---|---|---|---|
| YouTube, web, most social | −14 LUFS (±1) | ≤ −1 dBTP | [Standard] YouTube normalisation reference; [Recommended] |
| Voice-led, e-learning, podcast-style | −16 LUFS (±1) | ≤ −1 dBTP (consider −2 for codec headroom) | [Recommended] |
| Broadcast, Europe (EBU R 128) | −23 LUFS (±0.5) | ≤ −1 dBTP | [Standard] |
| Broadcast, US (ATSC A/85) | −24 LKFS (±2) | ≤ −2 dBTP | [Standard] |

- Carve the bed against the voice group before Verify (`data-fx-carve`, sources grouped in an `<hf-audio-group>` [Documented]); the earlier standard records the carve default as strength 0.8 ≈ −7 dB across 250 Hz–2.5 kHz — treat those exact numbers as **unverified against the current CLI** (§2.10) and set strength 0.25–0.5 when the music is the point.
- Ducking envelope (where automation is hand-built): 80–150 ms anticipation, 250–600 ms recovery; release slowly so the bed does not pump. [Recommended]
- Voice bus: compressor about −18 dB threshold, 3:1; +2 dB clarity at 3 kHz; hold VO short-term loudness within ±2 LU. Master: a `truepeak` limiter last in the root `data-fx-chain`, ceiling at least 2 dB under the delivery spec (−3 dBTP for a −1 dBTP delivery) because estimators overshoot on noisy material; from v0.8.228 the export also pulls down over-ceiling peaks, which is a safety net, not a mix. Loudness range 5–10 LU web, up to 15 LU cinematic. [Recommended; attribute names Documented]
- **Phone test**: phone speakers reproduce little below about 200 Hz — give impacts a 1–4 kHz "crack"; check the mix summed to mono. [Recommended]
- **Measure, don't guess**: `npx hyperframes audio --read` reports LUFS on a recording [Documented, R1]; on the export, `ffmpeg -i out.mp4 -af ebur128=peak=true -f null -` gives integrated LUFS, LRA and true peak; `ffprobe` confirms duration, fps and the presence of an audio stream. Inspect the encoded final mix, not only the stems. [Recommended]
- Keep voiceover, music and SFX in separate groups so stems, remixes and dubs stay possible. The documented effect list has no panner: bake left-right movement into the SFX asset. [Documented effect list, R1]
- Units discipline: LUFS = loudness, dBFS = digital level, dBTP = true peak, relative dB = a difference; name the measurement, reference and window — never judge a 100 ms click by the integrated LUFS of a minute. Gain in dB = 20·log10(multiplier).

## Part II — Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229)

### 3.7 Audio direction

Sound carries much of the meaning and most of the perceived production value. The official model treats the mix as "a set of relationships, not a stack of processors" [DOC] [A2-57].

#### Choose the sound strategy first

| Context | Strategy | Why |
|---|---|---|
| Social feeds (often muted) | Text-led picture, burned-in captions, music and effects as enhancement | 41 % of studied ads lacked meaning without sound; captions added 12 % view time [STD] [C-14] |
| Explainer or tutorial | Voice-led; low or no music under dense explanation | Coherence principle [RES] [C-23] |
| Brand film | Voice or music-led with planned silences | Emotion through tempo and contrast [RES] [C-65] [C-64] |
| Music-led montage or showreel | Music sets the grid; cuts on beats | Beat-locked edits read as one gesture [DEMO] [B-31] |
| Product demo | Voice plus UI micro-sounds; light bed | Effects make actions physical [DEMO] [G-02] |

#### Narration

- **Rate.** Average English speech is about 150 wpm; ~140 wpm improves clarity [DEMO] [C-66]. The official narration guide uses about 2.5 words per second (15 s ≈ 37 words) [DOC] [A2-32]. Working rates: explainer 140–160 wpm; social ad 160–190; technical or educational 120–140 with pauses at segment boundaries [REC] [C-66] [C-21]. Fast talking-head reels run 4.0–4.7 words per second [DEMO] [B-30].
- **Script length.** Words ≈ seconds × 2.5. When the script overruns, cut words; do not speed up the voice.
- **Voice.** Natural voices outperform machine-like ones (voice principle) [RES] [C-23]. Pin the provider and voice so retakes match; run the official sign-in preflight (`npx hyperframes auth status`) before generating voice or music, and stop for the user's choice when no credential exists [DOC] [A2-45]. Write numbers and acronyms as spoken [DOC] [A2-32]; check brand names by ear [DEMO] [B-43].
- **Timing data.** Extract word timestamps from the final voice; re-transcribe after any change [DOC] [B-10]. For non-English audio always pass a transcription model explicitly, because English-only models translate [DOC] [A2-48].
- **Clarity.** High-pass the voice around 80–100 Hz; keep it centred and mono-compatible; avoid music with vocals under narration [REC] [C-66].

#### Music: when and what

| Tone / format | Tempo | Character | Level |
|---|---|---|---|
| Energetic product launch, social | 110–130 BPM | Major, punchy, clear downbeats | Bed under voice; full only in music-only beats |
| Premium brand film | 70–100 BPM | Sparse arrangement, room to breathe | Low under voice; rises in silent beats |
| Explainer, tutorial | Low tempo or none | Instrumental, no lead melody | ≥ 15 LU under voice, or no music |
| Finance, enterprise, data story | ~90–100 BPM | Calm, cinematic | Low and steady |
| Creative, playful | ~115 BPM | Playful electronic | Bed |
| Default SaaS | ~108 BPM | Uplifting corporate tech | Bed |

Sources: tempo and mode effects [RES] [C-65]; platform guidance that tracks above 120 BPM often lift view-through on TikTok [STD] [C-15]; official mood inference for the last three rows [DOC] [A2-53]. **Leave music out** when explanation is dense, when content is sensitive or accessibility-critical, or when the brief's tone is better served by silence [REC] [C-23]. Edit music to picture: cuts on bars, reveals on downbeats, an ending that resolves [REC] [C-65]. Keep beds as WAV; MP3 beds played choppy in one production [DOC] [B-12]. Confirm the licence for the target platform.

#### Sound effects

- Effects follow visible actions, not every cut; vary samples for repeated items; avoid laser zaps and comic plops [DEMO] [B-30].
- Place an effect on the exact frame of contact or one frame late, never early; whooshes 2–6 frames before a fast move peaks; risers 0.5–2 s before reveals [REC] [C-62]. The official riser in the bundled library is 10.03 s long and must be triggered that far before the reveal so it crests on time [DOC] [A2-56].
- Keep effects 6–12 dB below voice peaks [REC] [C-62]; the official default effect level is about 0.35 under narration and music [DOC] [A2-52]. Official policy uses retrieval or the bundled Pixabay-licensed library and never generates effects [DOC] [A2-52] [A2-56].

#### Silence

Cutting to silence just before crucial information improved its recall compared with continuous music [RES] [C-64]. Drop the bed 0.3–1 s before the key line or number, keep the silence under 3 s, and bring the music back on the payoff [REC] [C-64] [C-95].

#### Mix targets

| Deliverable | Integrated loudness | True-peak ceiling | Source |
|---|---|---|---|
| Social and web (default) | −14 LUFS ±1 | ≤ −1 dBTP (−2 for low-bitrate AAC or masters louder than −14) | [REC] [C-57] [C-53] |
| YouTube | Not officially documented; ~−14 LUFS reported by practitioners | ≤ −1 dBTP | [UNVERIFIED] [C-57] |
| TikTok, Instagram, X, LinkedIn | No published target found; use the social default | ≤ −1 dBTP | [UNVERIFIED] |
| EU broadcast (EBU R 128 v5) | −23.0 LUFS | ≤ −1 dBTP | [STD] [C-53] |
| US broadcast (ATSC A/85) | −24 LKFS ±2 | ≤ −2 dBTP | [STD] [C-55] |
| Podcast / Apple | −16 LKFS ±1 | ≤ −1 dBTP | [STD] [C-58] |
| Netflix | −27 LKFS ±2, dialogue-gated | ≤ −2 dBTP | [STD] [C-59] |

HyperFrames has no official loudness target [DOC] [A2-61]; practitioner targets differ (−14 or −16 LUFS; −1, −1.2 or −1.5 dBTP) [CONFLICT] [B-30] [B-31] [A2-80]. Keep an unlimited archival master and derive platform versions from it [REC] [C-55].

#### Balance and ducking

- Keep narration at least 10 LU above music and 15 LU above ambience; non-experts prefer about 4 LU more separation [RES] [C-61]. Push to ≥ 15 LU for dense or accessibility-critical content [REC] [C-61].
- Ease ducks with 150–300 ms attack and 300–800 ms release so the bed does not pump [REC] [C-61].
- In HyperFrames, apply the official voice-over carve whenever music plays under any voice (default strength 0.8); it follows the voice envelope and should let the bed return between phrases; if it sounds notched, lower the strength [DOC] [A2-57]. Volume moves use `data-automation` lanes, never GSAP volume tweens [DOC] [A2-57] [A1-04].
- Practitioner starting levels: voice `data-volume` 1.0, bed about 0.15 (≈ −16.5 dB), effects 0.2–0.35; then measure [DOC] [B-10] [DEMO] [B-30] [A2-52].
- Put the `truepeak` effect last on the master with its ceiling at least 2 dB under the hard limit (−3 dBTP for a −1 dBTP spec), because its 4× estimate can overshoot [DOC] [A2-60]. Export applies peak limiting since 0.8.228 [DOC] [A1-38]; one practitioner reports renders slightly quieter than the premix [UNVERIFIED] [B-31]. Always measure the delivered file.

#### Sync

- Audio–video offsets become detectable at about +45 ms (audio early) and −125 ms (audio late), and acceptable up to +90 / −185 ms [STD] [C-62].
- Captions appear about 2 frames before the word [DEMO] [B-30]; music-locked cuts land within 2 frames (~35 ms) of the beat [DEMO] [B-31]; graphic reveals land on or slightly before the anchor word (practitioners lead by 0.15–0.6 s; the official doctrine reveals on the cue) [DOC] [A2-24] [DEMO] [A2-83] [CONFLICT].
- HyperFrames has no automatic waveform sync or drift correction; retime by hand from timestamps [DOC] [A1-10].

#### Captions

| Parameter | Working rule | Source |
|---|---|---|
| Rate | General adult 160–180 wpm (BBC); streaming ≤ 20 cps (Netflix); education ≤ 130–160 wpm (DCMP) | [STD] [C-67] [C-69] [DEMO] [C-72] |
| Lines | ≤ 2 (16:9, 1:1); ≤ 3 (9:16) | [STD] [C-67] |
| Length | ≤ 37–42 characters (16:9); ≤ 20–25 (9:16) | [STD] [C-67] [C-69] |
| Duration | ≥ 0.3 s per word; ≤ 6–7 s per caption; ≥ 2-frame gaps | [STD] [C-67] [C-70] [DEMO] [C-72] |
| Size | Line height 7–8 % of frame height (16:9); 3.9–4.5 % (9:16) | [STD] [C-67] |
| Style | Bold sans, white with a 2–4 px dark stroke or translucent box; never over faces or key text | [REC] [C-67] [C-72] [STD] [C-71] |
| Content | Speaker identity and meaningful non-speech sound, not only dialogue | [STD] [C-73] |
| Breaks | Break after punctuation and before conjunctions; never split article–noun or name pairs | [STD] [C-68] |
| Highlighting | Active-word changes ≥ 150 ms apart; never flash the whole line | [REC] [C-76] |

Official caption authoring adds tone-based styles (hype, corporate, tutorial, storytelling, social), grouping of 2–6 words by energy, one group visible at a time, a hard exit at each group's end, and a karaoke baseline with emphasis words that break the pattern [DOC] [A2-49] [A2-50]. For 9:16 social, burn styled captions into the safe box and also upload sidecar captions where supported, without enabling two caption layers at once [REC] [C-14] [C-67].

#### Measure, don't guess

- `python scripts/qa_render.py final.mp4 --lufs -14 --true-peak -1` measures integrated loudness and true peak on the delivered file and flags silent spans.
- `npx hyperframes normalize-audio --reference <id> --target <id>` matches clip loudness inside the project [DOC] [A2-61].
- `ffmpeg -i final.mp4 -af ebur128=peak=true -f null -` gives the raw meter readout [DOC] [A2-61].
