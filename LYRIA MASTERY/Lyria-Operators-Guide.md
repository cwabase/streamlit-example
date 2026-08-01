# Lyria — Operator's Prompting Guide

**Compiled:** 1 August 2026 · **Built from:** Google-published (Tier 1) documentation only, except where a Tier 2 gap is marked inline. No Tier 2 source was needed; nothing below is Tier 3.

---

## Step 0 — Version confirmation

**The current official model is Lyria 3.5, launched 29 July 2026 in Google Flow Music — your "Lyria 3.5" is correct, but it does not name anything you can call from an API.** The developer surface is still the **Lyria 3** family: `lyria-3-clip-preview` and `lyria-3-pro-preview` (public preview), plus the experimental `lyria-realtime-exp` and the legacy `lyria-002` (Lyria 2). Google's own SDK ships no 3.5 model ID. So: prompt-craft guidance for 3.5 comes from the DeepMind/Flow surface; every parameter in this guide is a Lyria 3 / RealTime / Lyria 2 parameter.

### A note on how this was retrieved

Google's documentation hosts (`ai.google.dev`, `deepmind.google`, `docs.cloud.google.com`, `blog.google`) are blocked by this environment's egress policy. Everything below is still Tier 1, but by two different routes, and each claim is marked:

- **[T1-direct]** — retrieved in full: `cloud.google.com/blog` posts, Google's official GitHub notebooks, and the published `google-genai` Python SDK (v2.16.0) source. Parameter names, ranges and enums come from the SDK itself, which is authoritative.
- **[T1-index]** — the page is Google's, but reachable here only through the search index. Accurate to the doc's wording; not verified against the live page.

---

## 1. What the model is and where it runs

Lyria is Google DeepMind's music generation family — latent diffusion over temporal audio latents, generating high-fidelity stereo audio from text, images or PDF **[T1-index, Lyria 3.5 model card]**. It runs on: the **Gemini app** (Lyria 3 / 3 Pro), **Google Flow Music** (Lyria 3.5), the **Gemini API / AI Studio**, **Vertex AI / Gemini Enterprise Agent Platform** (API + Media Studio), and **Google Vids** for Workspace **[T1-direct]**. Developers reach it three ways: the Interactions API, legacy `generate_content`, and a WebSocket streaming API for RealTime. Output is 44.1 kHz stereo for Lyria 3; 48 kHz for RealTime and Lyria 2.

> **MusicFX:** you named it as a possible surface. I found no current Google documentation tying MusicFX to the Lyria 3 line, and I could not verify its status from this environment. Treated as a gap rather than guessed at.

---

## 2. Model lineup

| Model ID | Surface | Length | Audio | Vocals | Source |
|---|---|---|---|---|---|
| `lyria-3-pro-preview` | Gemini API, Vertex | up to ~3 min | 44.1 kHz stereo | yes | [T1-direct] |
| `lyria-3-clip-preview` | Gemini API, Vertex | always 30 s | 44.1 kHz stereo | yes | [T1-direct] |
| `lyria-realtime-exp` | Gemini API (`v1alpha`) | continuous stream | 48 kHz stereo | instrumental only | [T1-direct] |
| `lyria-002` (Lyria 2) | Vertex AI | 30 s WAV | 48 kHz | instrumental only | [T1-index] |

Google's own SDK describes the two Lyria 3 models verbatim as **[T1-direct]**:

> `lyria-3-clip-preview` — "Our low-latency, music generation model optimized for high-fidelity audio clips and precise rhythmic control."
> `lyria-3-pro-preview` — "Our advanced, full-song generative model with deep compositional understanding, optimized for precise structural control and complex transitions across diverse musical styles."

**Vocal languages (both Lyria 3 models):** English, German, Spanish, French, Hindi, Japanese, Korean, Portuguese — "more languages coming soon" **[T1-direct]**.

---

## 3. Prompt anatomy

### The core framework — reproduced verbatim

Google publishes exactly one prompt framework for Lyria 3, in the *Ultimate prompting guide for Lyria 3 models* (Google Cloud Blog, 7 April 2026) **[T1-direct]**:

```
[Genre and style] + [Mood] + [Instrumentation] + [Tempo and rhythm] + [Vocal style & language] + [Lyrics]
```

Field definitions, verbatim:

- **Genre and style:** Define the primary category, for example, "cinematic orchestral fantasy".
- **Mood:** Describe the emotional intent, for example, "tense and suspenseful".
- **Instrumentation:** Name the specific instruments, for example, "guitar", "piano".
- **Tempo and rhythm:** Set the speed, pace, and groove using descriptive terms, such as, "a fast, energetic pace with a driving beat".
- **Instrumental vs. vocal:** Specify "instrumental" to exclude vocals.
- **Vocal style & language:** Specify gender, tone (e.g., raspy, smooth), delivery (e.g. rapping), and language.
- **Lyrics:** Either provide a theme for Lyria to generate the words (e.g., "song about a cross-cultural connection"), or provide your exact lyrics in quotes for the model to perform.

The Vertex prompt guide uses the same six components with slightly different labels — Genre & style, Mood & emotion, Instrumentation, Tempo & rhythm, Vocal style & language, Lyrics **[T1-index]**.

### Best practices, verbatim [T1-direct]

- **Be descriptive and specific:** Use adjectives to create a clear description. The more detail you provide, the better Lyria understands your prompt.
- **Reference genres and eras:** Clearly state the musical category (for example, Rock or Pop) and stylistic timeframe (e.g. the 1950s, early 90s).
- **Specify key instruments:** Mention the important instruments driving the track, or Lyria chooses defaults based on the genre.
- **Iterate:** If the first result isn't perfect, refine your prompt by adjusting keywords.

### Parameter table — Lyria 3 (Interactions API / `generate_content`)

Lyria 3 has **no musical parameters**. Musical control is entirely in the prompt text; the API surface is a general content-generation surface **[T1-direct, from the official notebook]**.

| Parameter | Type / values | Default | Effect |
|---|---|---|---|
| `model` | `lyria-3-clip-preview`, `lyria-3-pro-preview` | — | Selects 30 s clip vs. up-to-3-min track |
| `contents` / `input` | text, image bytes, PDF | — | Prompt. Up to **10 images** per request |
| `response_modalities` | `["AUDIO","TEXT"]` | — | Must include both to receive lyrics/structure text alongside audio |
| `stream` | bool | `False` | Interactions API only; streams lyrics/description deltas as produced |

Response shape: text parts carry generated lyrics and song-structure information; audio arrives in `inline_data` (`generate_content`) or as `type: "audio"` base64 outputs (Interactions API) **[T1-direct]**.

**Negative prompts:** the `negative_prompt` parameter belongs to Lyria 2. Google's documentation states negative prompts are **not supported for Lyria 3 models** **[T1-index]**. I saw both a `negative_prompt` description and that non-support statement across Google's music docs; the non-support statement is the one that names Lyria 3 explicitly, so treat `negative_prompt` as Lyria-2-only and express exclusions in prose ("instrumental", "no drums") for Lyria 3.

### Parameter table — Lyria RealTime (`LiveMusicGenerationConfig`)

Names, ranges and enum members below are copied from the `google-genai` v2.16.0 SDK source — authoritative **[T1-direct]**. Defaults marked [T1-index] come from the RealTime doc via search.

| Parameter | Type | Range | Default | Effect (verbatim where quoted) |
|---|---|---|---|---|
| `temperature` | float | `[0.0, 3.0]` | `1.1` [T1-index] | "Controls the variance in audio generation. Higher values produce higher variance." |
| `top_k` | int | `[1, 1000]` | `40` [T1-index] | "Samples the topK tokens with the highest probabilities." |
| `seed` | int | — | random | "Seeds audio generation. If not set, the request uses a randomly generated seed." |
| `guidance` | float | `[0.0, 6.0]` | not stated in retrieved docs | "Controls how closely the model follows prompts. Higher guidance follows more closely, but will make transitions more abrupt." |
| `bpm` | int | `[60, 200]` | model decides | Beats per minute. **Changing it requires `reset_context()`** |
| `density` | float | `[0.0, 1.0]` | model decides | "Density of sounds." |
| `brightness` | float | `[0.0, 1.0]` | model decides | "Brightness of the music." |
| `scale` | enum | 13 members (below) | model decides | Key and mode. **Changing it requires `reset_context()`** |
| `mute_bass` | bool | — | `False` | "Whether the audio output should contain bass." |
| `mute_drums` | bool | — | `False` | "Whether the audio output should contain drums." |
| `only_bass_and_drums` | bool | — | `False` | "Whether the audio output should contain only bass and drums." |
| `music_generation_mode` | enum | `QUALITY`, `DIVERSITY`, `VOCALIZATION` | `QUALITY` | See below |

`music_generation_mode` values, verbatim from the SDK **[T1-direct]**:
- `QUALITY` — "Steer text prompts to regions of latent space with higher quality music."
- `DIVERSITY` — "Steer text prompts to regions of latent space with a larger diversity of music."
- `VOCALIZATION` — "Steer text prompts to regions of latent space more likely to generate music with vocals."

`Scale` enum members **[T1-direct]**: `SCALE_UNSPECIFIED`, `C_MAJOR_A_MINOR`, `D_FLAT_MAJOR_B_FLAT_MINOR`, `D_MAJOR_B_MINOR`, `E_FLAT_MAJOR_C_MINOR`, `E_MAJOR_D_FLAT_MINOR`, `F_MAJOR_D_MINOR`, `G_FLAT_MAJOR_E_FLAT_MINOR`, `G_MAJOR_E_MINOR`, `A_FLAT_MAJOR_F_MINOR`, `A_MAJOR_G_FLAT_MINOR`, `B_FLAT_MAJOR_G_MINOR`, `B_MAJOR_A_FLAT_MINOR`.

**`WeightedPrompt`** **[T1-direct]**:

| Field | Type | Constraint | Effect |
|---|---|---|---|
| `text` | string | — | "Text prompt." |
| `weight` | float | **must not be 0** | "Used to control the relative importance of the prompt… Weights of all weighted_prompts in this message will be normalized." |

Google's own cookbook adds that weights "can be any values, including negative, except 0" **[T1-direct]**.

### Parameter table — Lyria 2 (`lyria-002`, Vertex) [T1-index]

| Parameter | Type | Notes |
|---|---|---|
| `prompt` | string | "A text prompt in US English that describes the music to generate." |
| `negative_prompt` | string | Elements to exclude, e.g. `"vocals, excessive cymbal crashes, distorted guitar"` |
| `seed` | int | Reproducible output. **Cannot be used with `sample_count`** |
| `sample_count` | int | Number of samples. **Mutually exclusive with `seed`** |

Output: 30-second WAV, 48 kHz, instrumental only.

---

## 4. Documented workflows

### 4.1 Text-to-music

The baseline call, verbatim from Google's official notebook **[T1-direct]**:

```python
prompt = """
Sophisticated, rhythmic, and aspirational track with crisp 808 percussion, digital plucks,
and muted electric guitar rhythmic strums. Include breathy, airy Alto female vocal textures
with melodic, minimalist oohs and aahs with heavy reverb and rhythmic delay.
"""

response = client.models.generate_content(
    model="lyria-3-pro-preview",
    contents=prompt,
    config=types.GenerateContentConfig(response_modalities=["AUDIO", "TEXT"]),
)
```

Interactions API equivalent **[T1-direct]**:

```python
interaction = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Genera un tema pop",
)
```

### 4.2 Instrumental-only

Write `instrumental` in the prompt — that is the entire documented mechanism for Lyria 3 **[T1-direct]**.

### 4.3 Lyrics

- **Your own lyrics:** write `Lyrics:` before the lines you want sung **[T1-direct]**.
- **Backing vocals:** in the Gemini app, put echoed words in parentheses — `"Lyrics: Let's go (go)."` For the API guide, "mention where you want the backing vocals in the prompt" **[T1-direct]**.
- **Model-written lyrics:** describe the theme instead ("a love song", "a new happy birthday song") **[T1-direct]**.
- **Clip-length caution:** "since tracks are 30 seconds, try keeping your lyrics short and sweet" **[T1-index, Gemini app tips]**.

### 4.4 Vocal control

Four documented axes **[T1-direct]**:

1. **Singer demographics and range** — "commanding baritone vocals", "clear and high soprano range".
2. **Voice texture (timbre)** — "gravelly", "soulful", "breathy".
3. **Vocal patterns and styles** — "fast-paced" or "laid-back" groove; layer styles; change dynamically, e.g. getting "calmer and quieter as the track progresses".
4. **Language** — one of the eight supported.

### 4.5 Timestamp prompting (structural control)

"Ideal for creating dynamic genre shifts or scoring video content by assigning actions to timed segments" **[T1-direct]**. Format is `[mm:ss]` at line start. Full published example in §5.

### 4.6 Multimodal conditioning

Upload **reference images (up to 10) or PDFs** "to establish the emotional baseline for the track" **[T1-direct]**:

```python
response = client.models.generate_content(
    model="lyria-3-clip-preview",
    contents=[
        types.Part.from_bytes(data=image, mime_type="image/png"),
        "Generate an instrumental clip based on this input image that starts slowly and builds in intensity.",
    ],
    config=types.GenerateContentConfig(response_modalities=["TEXT", "AUDIO"]),
)
```

### 4.7 Streaming (Interactions API)

Set `stream=True` to receive lyrics and descriptions as deltas rather than waiting for completion **[T1-direct]**:

```python
stream = client.interactions.create(
    model="lyria-3-pro-preview",
    input="Generate a song about spending a day in Seoul in Korean.",
    stream=True,
)
for event in stream:
    if event.event_type == "content.delta":
        ...
```

### 4.8 RealTime session steering

WebSocket, `v1alpha`, model string `models/lyria-realtime-exp`, output 48 kHz stereo PCM **[T1-direct]**.

Session lifecycle **[T1-direct]**:

| Call | Behaviour (verbatim from SDK) |
|---|---|
| `set_weighted_prompts(prompts)` | Sends blended prompts; can be called mid-stream to steer |
| `set_music_generation_config(config)` | Updates config mid-stream |
| `play()` | "Start generating the music." |
| `pause()` | "Hold the music generation. Use PLAY to resume from the current position." |
| `stop()` | "Stop the music generation and reset the context (prompts retained). Use PLAY to restart." |
| `reset_context()` | "Reset the context (prompts retained) without stopping the music generation." |
| `close()` | "Closes the bi-directional stream and terminates the session." |

Steering rules Google states explicitly:
- "Iterate and steer gradually. Rather than completely changing the prompt, try adding or modifying elements to morph the music more smoothly." **[T1-index]**
- "Since updating the bpm or the scale is a drastic change for the model you'll also need to tell it to reset its context using `reset_context()` to take the new config into account. It won't stop the stream, but it will be a hard transition." **[T1-index]**
- Keep prompts short: "the model will better understand things like 'meditation', 'eerie', 'harp' than 'An eerie and relaxing music illustrating the verdoyant forests of Scotland using string instruments'." **[T1-direct, cookbook]**

Server messages carry `setup_complete`, `server_content.audio_chunks[]` (each with `data`, `mime_type`, and `source_metadata` echoing the prompts/config that produced it), or `filtered_prompt` **[T1-direct]**.

### 4.9 Seeding

Two places only: `seed` on Lyria 2 (reproducible output, mutually exclusive with `sample_count`) and `seed` in `LiveMusicGenerationConfig` for RealTime. **No seed parameter is documented for Lyria 3** **[T1-direct — absent from the SDK and from the official notebook]**.

### 4.10 Cross-model workflows [T1-direct]

- **Lyria + Veo:** "Generate video assets using Veo, and then dictate the exact structural timing in Lyria 3 Pro to score a custom soundtrack that matches every scene transition."
- **Lyria + Nano Banana:** "Generate images of a storyboard or vibe, and let Lyria create a song based on those images."
- **Lyria + Gemini:** "use Gemini to analyze your creative brief and output a highly descriptive prompt to feed into Lyria 3 models."

### Workflows Google does not document

Stated plainly rather than invented:

- **Continuation / extension of an existing track** — no endpoint, parameter or documented workflow found in any Tier 1 source.
- **Stems / multitrack export** — nothing. RealTime's `mute_bass` / `mute_drums` / `only_bass_and_drums` steer *generation*; they are not stem separation.
- **Audio-input style conditioning** — documented conditioning inputs are text, images and PDF only.
- **Explicit duration parameter for Lyria 3 Pro** — duration is influenced through the prompt (asking for a length, or timestamps), not a numeric field.

---

## 5. Worked examples Google publishes

Each is reproduced verbatim with the result Google states for it.

**1. Six-component framework, full stack** — *stated result: a romantic Bossa Nova/R&B fusion with a bilingual vocal duet* **[T1-direct]**

> "A romantic fusion of classic Bossa Nova and modern R&B. The mood is intimate, warm, and deeply affectionate. Features a gentle acoustic nylon-string guitar, warm electric piano chords, and a crisp, laid-back modern hip-hop drum beat. A slow, swaying tempo. Featuring a vocal duet: a smooth male vocalist singing in English, and a soft, breathy female vocalist singing in French. The lyrics are a beautiful love song about an undeniable, cross-cultural connection"

**2. Instrumental** — *stated result: instrumental lofi, no vocals* **[T1-direct]**

> "A warm, modern lofi hip-hop beat for studying, featuring a muffled drum break and dusty jazz piano samples. Instrumental."

**3. Vocal-arc control** — *stated result: vocals that start confident and become calmer/quieter across the track* **[T1-direct]**

> "A smooth, moody jazz ballad featuring piano and upright bass. The vocals should be a female singer with a breathy, soulful soprano range. The vocal pattern should start out confident but get calmer and quieter as the track progresses. Song lyrics about meeting the love of her life in New York."

**4. Non-English vocal** — *stated result: J-pop with Japanese male tenor vocal* **[T1-direct]**

> "An upbeat, high-energy J-pop track with bright, sparkling synths, electric guitar, and a driving bassline. Featuring a clear, expressive male tenor vocal singing in Japanese. The vocal style should be fast-paced and melodic, with a sweet and highly polished texture."

**5. Timestamp prompting** — *stated result: a timed arrangement with genre shifts at the marked points* **[T1-direct]**

> ```
> [00:00] Begin immediately with a massive gospel choir singing a powerful, uplifting harmony about being kind to yourself.
> [00:15] A heavy, modern hip-hop drum beat and a deep 808 bassline drop in, matching the energy of the choir.
> [00:30] A male lead vocalist begins rapping a confident verse about overcoming life's challenges, while the large choir punctuates his lines in the background.
> [01:10] Transition into a huge, triumphant chorus celebrating victory and winning. The gospel choir sings at full volume, layering rich, soulful harmonies over the driving hip-hop beat and triumphant brass horns.
> [01:50] The beat strips back to just a gentle Hammond B3 organ. The rapper delivers a quiet, emotional bridge about giving yourself grace, supported by soft, warm hums from the massive choir.
> [02:10] The full hip-hop beat and the giant choir return at maximum energy for an uplifting final chorus, before ending on a resonant, sustained choir chord at [03:00].
> ```

**6. Multimodal** — *stated result: track whose lyrics and mood match the attached images* **[T1-direct]**

> "A deeply emotional, modern Bollywood song in English. The lyrics and mood should match the story in the images attached."

**7. Genre + lyrics block** — from the official notebook, paired with a dog-bed advertising image **[T1-direct]**

> ```
> Genre: Upbeat, acoustic Folk-Pop with a warm and cuddly vibe. Bright acoustic guitars, a soft shaker rhythm, and a friendly, melodic vocal.
>
> Lyrics:
> Tail wags and a heavy head,
> Time to curl up in your favorite bed.
> Soft as a cloud, a dream come true,
> The perfect spot for a dog like you.
> ```

**8. Vertex prompt guide, instrumental with explicit BPM** **[T1-index]**

> "A 60-second instrumental track at 80 BPM. The feeling is nostalgic, introspective, and atmospheric — a warm, comforting melancholy with a soft, minor-key feel. The sound should be centered around a warm, slightly overdriven Fender Rhodes and soft, ethereal synth pads. The rhythm is a minimalist, laid-back drum beat with a relaxed, human feel."

**9. RealTime weighted blend** — Google's cookbook default configuration **[T1-direct]**

> Prompts: `Indie Pop` @ 0.6, `Sitar` @ 2.0, `Danceable` @ 1.4
> Config: `bpm=140`, `scale=F_MAJOR_D_MINOR`, `density=0.2`, `brightness=0.7`, `guidance=4.0`, `music_generation_mode=QUALITY`

### Published prompt vocabulary

Google's cookbook ships these as its sampled dropdown values **[T1-direct]**:

- **Genres:** Hard Rock, Latin Jazz, Polka, Baroque, Chiptune, Indie Pop, Bluegrass, Heavy Metal, Contemporary R&B, Reggaeton
- **Instruments:** Piano, Guitar, Bagpipes, Harpsichord, 808 Hip Hop Beat, Sitar, Harmonica, Didgeridoo, Woodwinds, Organ
- **Moods:** Chill, Emotional, Danceable, Psychedelic, Acoustic Instruments, Glitchy Effects, Ominous Drone, Upbeat

The RealTime doc carries a longer non-exhaustive list — instruments including *303 Acid Bass, 808 Hip Hop Beat, Accordion, Alto Saxophone, Trumpet*, and genres including *Acid Jazz, Afrobeat, Alternative Country, Baroque, Bhangra, Bluegrass, Blues Rock, Bossa Nova* **[T1-index]**. I could not retrieve the complete list from this environment; it is on the RealTime page linked in §7.

---

## 6. Limits, safety, licensing

### Length and format

| | Lyria 3 Clip | Lyria 3 Pro | RealTime | Lyria 2 |
|---|---|---|---|---|
| Length | 30 s fixed | up to ~3 min | continuous | 30 s fixed |
| Sample rate | 44.1 kHz | 44.1 kHz | 48 kHz | 48 kHz |
| Channels | stereo | stereo | stereo | — |
| Vocals | yes | yes | **no** | **no** |

Images per request: **up to 10** (Lyria 3) **[T1-direct]**.

### Safety filters

- Prompts can be rejected. RealTime returns a `filtered_prompt` message carrying the offending `text` and a `filtered_reason` string; the official sample handles this as a distinct branch from audio **[T1-direct]**.
- Google "employ[s] filters to check outputs against existing content" **[T1-direct]**.
- Lyria 3.5 "was developed in partnership with internal safety and responsibility teams. A range of evaluations and red-teaming activities were conducted" **[T1-index, model card]**.

### Watermarking and provenance

All Lyria 3 and Lyria 3 Pro outputs are embedded with **SynthID** watermarking and support **C2PA** cryptographically signed metadata **[T1-direct]**. SynthID "embeds a watermark into AI-generated audio content that's inaudible to the human ear and doesn't compromise the listening experience" **[T1-index]**. This is not optional and there is no documented way to disable it.

### Training data

"Lyria 3.5 was trained on audio data. Audio datasets were annotated with text captions at different levels of detail. Data filtering and preprocessing included techniques such as deduplication, safety filtering… and quality filtering" **[T1-index, model card]**. Google states the models are trained "using materials that YouTube and Google has a right to use under our terms of service, partner agreements, and applicable law" **[T1-direct]**.

### Licensing and commercial use

- **Ownership:** "Generated Output is Customer Data. As between Customer and Google, Google does not assert any ownership rights in any new intellectual property created in the Generated Output." **[T1-index, Service Specific Terms]**
- **Commercial use in preview:** for Generative AI Preview offerings, customers "may elect to use it for production or commercial purposes or disclose generated output to third parties" subject to the governing agreement **[T1-index]**.
- **Indemnification:** Google's generated-output indemnity covers third-party IP claims including copyright, but "only applies if you didn't try to intentionally create or use generated output to infringe the rights of others" **[T1-index]**.
- Users must adhere to the Terms of Service and Gen AI prohibited use policies, "which prohibit violating others' intellectual property and privacy rights" **[T1-direct]**.

Consumer surfaces (Gemini app, Flow Music) run under their own consumer terms, not the Cloud terms above. Confirm before commercial release.

### Pricing and rate limits

- **Lyria 2:** $0.06 per 30 seconds of output **[T1-index]**.
- **Lyria 3 / 3 Pro:** pricing not retrieved. Check the Vertex AI / Gemini API pricing page.
- **RealTime:** "a preview feature. It is free to use for now with quota limitations, but is subject to change." **[T1-direct, cookbook]**
- **Numeric rate limits and quotas:** not documented in anything I could retrieve. Gap.

### Other gaps

`guidance` default value; maximum RealTime session duration; exact Lyria 3 concurrency limits. Google's docs are silent or unreachable on these from here.

---

## 7. Sources

### Tier 1 — retrieved directly and in full

- [Ultimate prompting guide for Lyria 3 models](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-lyria-3-pro) — Google Cloud Blog, 7 Apr 2026. *The core framework, best practices, vocal guidance, timestamp and multimodal workflows, examples 1–6.*
- [Build music generation into your apps with Lyria 3 models on Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/lyria-3-and-lyria-3-pro-on-vertex-ai) — Google Cloud Blog, 7 Apr 2026. *Model split, SynthID/C2PA, training-data and ToS statements.*
- [`lyria3_music_generation.ipynb`](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/music/getting-started/lyria3_music_generation.ipynb) — GoogleCloudPlatform/generative-ai. *All Lyria 3 code, image and lyrics conditioning, Interactions API, streaming.*
- [`Get_started_LyriaRealTime.py` / `.ipynb`](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_LyriaRealTime.ipynb) — google-gemini/cookbook. *RealTime session handling, weighted-prompt format, vocabulary lists, preview/quota note.*
- `google-genai` Python SDK v2.16.0 (PyPI) — `google/genai/types.py`, `google/genai/live_music.py`. *Authoritative source for every RealTime parameter name, range, enum member and playback-control semantic; the two Lyria 3 model IDs and their descriptions.*

### Tier 1 — Google-published, retrieved via search index only (hosts blocked from this environment)

- [Generate music with Lyria 3 — Gemini API](https://ai.google.dev/gemini-api/docs/music-generation)
- [Generate music with Lyria 3 — Interactions API](https://ai.google.dev/gemini-api/docs/interactions/music-generation)
- [Real-time music generation using Lyria RealTime](https://ai.google.dev/gemini-api/docs/realtime-music-generation) — *full instrument/genre list, temperature and top_k defaults*
- [Live Music API — WebSockets API reference](https://ai.google.dev/api/live_music)
- [Lyria 3 Pro Preview](https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview) · [Lyria 3 Clip Preview](https://ai.google.dev/gemini-api/docs/models/lyria-3-clip-preview) · [Lyria RealTime experimental](https://ai.google.dev/gemini-api/docs/models/lyria-realtime-exp)
- [Lyria music generation prompt guide — Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/music/music-gen-prompt-guide)
- [Lyria API reference — Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/lyria-music-generation) · [Generate music with Lyria](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/music/generate-music) · [Lyria 2 (`lyria-002`)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-002)
- [Lyria 3.5 — Google DeepMind](https://deepmind.google/models/lyria/) · [Lyria 3.5 model card](https://deepmind.google/models/model-cards/lyria-3-5/) · [Lyria 3 model card](https://deepmind.google/models/model-cards/lyria-3/)
- [How to create effective prompts with Lyria — DeepMind](https://deepmind.google/models/lyria/prompt-guide/) · [Lyria RealTime — DeepMind](https://deepmind.google/models/lyria/lyria-realtime/)
- [6 tips for prompting Lyria 3 in the Gemini app](https://blog.google/products-and-platforms/products/gemini/tips-prompting-lyria-3/) — *backing-vocals parentheses syntax, 30 s lyrics advice*
- [Launching Lyria 3.5 in Google Flow Music](https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/) · [How developers can use Lyria 3](https://blog.google/innovation-and-ai/technology/developers-tools/lyria-3-developers/)
- [Service Specific Terms — Google Cloud](https://cloud.google.com/terms/service-terms) · [Generative AI indemnification](https://cloud.google.com/blog/products/ai-machine-learning/protecting-customers-with-generative-ai-indemnification)

### Tier 2

None used.
