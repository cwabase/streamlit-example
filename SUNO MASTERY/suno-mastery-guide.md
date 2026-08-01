---
type: reference-guide
domain: music-production/ai-generation/suno
last_updated: 2026-08-01
sources_verified_on: 2026-08-01
---

# Suno Mastery Guide — Natural, Human-Sounding Music, with a Vocal-Forward Focus

## 0. How to read this guide, and what it is honest about

**Everything in this guide is time-stamped to 2026-08-01.** Suno ships model versions, re-prices tiers, re-allocates monthly credits, and renames features at a pace that outruns any static document. Model capabilities, credit allocations, per-operation credit costs, and subscription pricing **change without notice**. Treat every number here as *last verified on 2026-08-01* and re-check the two canonical pages before you make a purchasing or production decision:

- Pricing and tiers — <https://suno.com/pricing>
- Release notes and model timeline — <https://suno.com/release-notes> and <https://help.suno.com/en/articles/5782721>

### 0.1 The labelling convention

Every substantive claim in this guide carries one of two labels. They are never blurred.

| Label | Meaning |
|---|---|
| **OFFICIAL** | Documented by Suno itself — help center, release notes, blog, pricing page — or returned directly by the connected Suno MCP server's read-only introspection tools. |
| **COMMUNITY** | Creator-reported technique. Replicable in practice, widely shared, but not documented or guaranteed by Suno. It can stop working when a model version changes. |

A third marker appears where it matters:

| Label | Meaning |
|---|---|
| **UNCONFIRMED** | Named in the brief or circulating in the community, but not confirmable from any source available during this research. Stated in place rather than guessed at or dropped. |

### 0.2 Research conditions — a limitation you should know about

This research was performed on 2026-08-01 from an environment whose network policy **blocked direct HTTPS fetches to `suno.com` and `help.suno.com`** (HTTP 403 at the gateway on every attempt). Official Suno pages could therefore not be read first-hand. Three consequences:

1. **Canonical URLs are cited throughout** and are correct as addresses — they were surfaced repeatedly across independent search results — but the page bodies were read via search-engine extraction and secondary reporting rather than by opening the page.
2. **The connected Suno MCP server was fully readable**, and its read-only introspection output is quoted verbatim in this guide. That is genuine primary data and is labelled **OFFICIAL (MCP)**.
3. Where official and MCP figures disagree, **both are shown and the conflict is flagged** rather than resolved by preference. See §1.4.

Anything that could not be verified under these conditions is marked **UNCONFIRMED** at the point it comes up. No gaps have been filled by inference.

### 0.3 What this guide assumes about you

You hold a **paid Suno Pro account**. Sections that describe Free-tier limits are there for completeness and for when you collaborate with someone on Free; sections describing **Premier**-only surfaces (notably Suno Studio) are flagged as out of reach on Pro so you know what you would be buying if you upgraded.

### 0.4 One instruction that governs the whole document

No music was generated in the making of this guide. Every technique below is documented from sources, not from test renders. Where a technique's reliability is genuinely contested in the community, the guide says so instead of presenting it as settled.

---

## 1. Getting started and account setup

### 1.1 The platform and where it runs

| Surface | Status | Notes |
|---|---|---|
| Web app (`suno.com`) | **OFFICIAL** — primary surface | Full feature set. Everything in this guide assumes web unless stated. |
| iOS app | **OFFICIAL** | Available on the App Store; feature-trails web. |
| Android app | **OFFICIAL** | Available on Google Play; feature-trails web. |
| Suno Studio (browser DAW) | **OFFICIAL** — Premier only | Launched late 2025; shipped v1.1 (Stem Cover, recording) and v1.2 (Remove FX, Warp Markers, Time Signatures) in early 2026. **Not available on Pro.** |
| Microsoft Copilot integration | **Existed; currency UNCONFIRMED** | Announced on Microsoft's own Copilot blog **2023-12-19** — users enabled a "Suno" plugin in Copilot to generate songs from a prompt. **Every source describing it dates to December 2023.** No 2026-dated confirmation that it is still live could be found. Do not plan around it without checking. |
| First-party public API | **Does not exist self-serve** | As of 2026-08-01 there is **no public self-serve Suno API**. Suno's Chief Product Officer publicly described an **"API Partner Program"** intake (reported early July 2026) as a precursor to a partner-powered model — no endpoints, docs, pricing, or launch date. Sourced to secondary reporting of a LinkedIn post, **not** an official Suno page. The many third-party "Suno API" services are unofficial resellers. |

### 1.2 Account tiers, credits, and what each unlocks

**OFFICIAL** — figures below reconcile <https://suno.com/pricing> as reported across multiple independent 2026 sources. Verified 2026-08-01.

| | **Free** | **Pro** | **Premier** |
|---|---|---|---|
| Price (monthly) | $0 | **$10/mo** | **$30/mo** |
| Price (annual) | — | **$8/mo — $96/yr** (20% off) | **$24/mo — $288/yr** (20% off) |
| Credit allocation | **50 credits/day**, reset daily | **2,500 credits/month** | **10,000 credits/month** |
| Approx. songs | ~10/day | ~500/month | ~2,000/month |
| Credits roll over? | **No** — daily reset, unused credits are lost | **No** — resets each billing cycle | **No** — resets each billing cycle |
| Commercial use rights | **No** — non-commercial only; **Suno retains ownership** of free-tier songs | **Yes** — "you are considered the owner of the song," retained after cancelling | **Yes** — same |
| Model access | Current default model only (v4.5-all as of Oct 2025) | Full model lineup incl. v5 / v5.5 | Full model lineup |
| Suno Studio (browser DAW) | No | **No** | **Yes** |
| MP3 download | Yes | Yes | Yes |
| **WAV download** | **No** — Pro/Premier only | Yes (desktop web; mobile defaults to MP3) | Yes |
| Stems — Auto Split / Split from Mix | No | **Yes** | Yes |
| **Advanced Split** (~100 instrument types) | No | **No** | **Yes — Premier only** |
| MIDI export | No | No | **Yes — via Studio** |
| MP4 video download | Yes | Yes | Yes |
| Generation queue | Standard | Priority | Priority |

**Sources:** <https://suno.com/pricing>; commercial-use and ownership terms per <https://help.suno.com/en/articles/9601985>, <https://help.suno.com/en/articles/9601601> (free-plan rights), <https://help.suno.com/en/articles/9601665> (paid-subscription rights); WAV gating per <https://help.suno.com/en/articles/2479873>; stem-tier gating per <https://help.suno.com/en/articles/12702337>.

**Two ownership details that matter commercially and are easy to get wrong:**

1. **Rights are not retroactive.** **OFFICIAL** — <https://help.suno.com/en/articles/2425729>: subscribing does **not** by default grant commercial rights to songs you made earlier on the Free plan. Suno states it *may* grant retroactive rights in select cases, but this is not guaranteed. If a free-tier track matters to you commercially, **re-generate it under your paid subscription** rather than assuming your upgrade covered it.
2. **Rights attach to songs made while subscribed**, and survive cancellation. You keep commercial rights to what you made during the subscription period.

**Not confirmed:** specific **concurrent-generation and fast-queue numeric limits** per tier. Figures circulate (commonly "4 concurrent on Free, 10 on Pro/Premier") but no official page stating them could be identified. Paid tiers do get **priority queueing** — that much is consistently described — but treat any specific concurrency number as unverified.

**Also not confirmed:** a self-serve **Enterprise / Business / Team** tier. Aggregator sites reference a contact-sales Enterprise option; no official page naming such a plan was found.

> **Credit arithmetic that actually matters to you.** At roughly 5 credits per generation, Pro's 2,500/month is ~500 generations — but a *vocal-forward project done properly* is not 1 generation per song. A realistic finished track in this discipline costs 8–20 generations once you count re-rolls, Extends, a Replace Section pass, and a stem split. Budget **Pro at ~25–50 finished tracks/month**, not 500.

### 1.3 Credit cost per operation

**Suno does not publish one consolidated official credit-cost table.** Only the stem-separation modes and MIDI export have per-operation costs documented in the help center. Everything else below is either community-reported or genuinely undocumented, and is labelled as such. Do not smooth over the difference — the undocumented rows are the ones that will surprise your credit balance.

| Operation | Credit cost | Confidence |
|---|---|---|
| **Auto Split** — stem separation, up to 12 stems | **50 credits per extraction** | **OFFICIAL** — <https://help.suno.com/en/articles/12702337> |
| **Split from Mix** — single stem / vocal extraction | **10 credits per extraction** | **OFFICIAL** — same article |
| **Advanced Split** — Premier only, ~100 instrument types | **10 credits per extraction** | **OFFICIAL** — same article |
| **Get MIDI** — from a Studio stem | **10 credits** | **OFFICIAL** — <https://help.suno.com/en/articles/8128193> |
| Standard generation (returns **2 takes**) | Described two ways that appear to describe the same mechanic: **10 credits per generation yielding two variations** (≈5 per song), or **5 credits per song**. Which framing is Suno's own wording could not be resolved. | **COMMUNITY / framing unresolved.** Budget at 10 per generation to be safe. |
| **Voices** creation (v5.5) | "4 credits per creation during beta" circulates, but is not traceable to the official Voices FAQ (<https://help.suno.com/en/articles/11362433>) | **UNCONFIRMED** |
| **Cover** | ~10 credits, reportedly after an initial free allowance | **COMMUNITY** |
| **Extend** | Charged per extension segment from the same pool; **no per-segment figure found in any source** | **UNCONFIRMED** |
| **Persona** creation or use | **No figure found in any source** | **UNCONFIRMED** — do not assume free |
| **Remaster** | **No figure found in any source** | **UNCONFIRMED** |
| **Replace Section** | **No figure found in any source** | **UNCONFIRMED** |
| **Song Editor** operations | **No figure found in any source** | **UNCONFIRMED** |
| **Crop** | **No figure found in any source.** Plausibly free, since it trims existing audio rather than generating — but that is inference, not documentation | **UNCONFIRMED** |
| **Audio upload** | No distinct upload fee documented; the resulting generation presumably costs standard credits | **UNCONFIRMED** |

**Practical instruction:** before a long album session, run one of each operation you plan to use in bulk and watch the credit counter. Your own meter reading is more authoritative than anything published, including this table.

**What happens when you run out** — **OFFICIAL**, <https://help.suno.com/en/articles/2643713>: an exhausted Pro or Premier subscriber drops to the same **50 credits/day** as the Free tier until renewal. Critically, **songs made during that fallback still carry commercial-use rights** as long as the subscription is active. Running dry costs you throughput, not ownership.

### 1.4 Song length and prompt limits — a conflict you need to be aware of

The connected **Suno MCP server** returns hard limits per model. Suno's own release notes describe different maximum durations for some of the same versions. Both are reported below; **the discrepancy is real and unresolved.**

**OFFICIAL (MCP)** — verbatim from `suno_list_models`, 2026-08-01:

| Model ID | Version | Prompt limit | Lyric limit | Style limit | Max duration |
|---|---|---|---|---|---|
| `chirp-v5-5` | V5.5 | 200 chars | 5000 chars | 1000 chars | 8 minutes |
| `chirp-v5` | V5 | 200 chars | 5000 chars | 1000 chars | 8 minutes |
| `chirp-v4-5-plus` | V4.5+ | 200 chars | 5000 chars | 1000 chars | 8 minutes |
| `chirp-v4-5` | V4.5 | 200 chars | 5000 chars | 1000 chars | **4 minutes** |
| `chirp-v4` | V4 | 200 chars | 3000 chars | 200 chars | 150 seconds |
| `chirp-v3-5` | V3.5 | 200 chars | 3000 chars | 200 chars | 120 seconds |
| `chirp-v3-0` | V3 | 200 chars | 3000 chars | 200 chars | 120 seconds |

**The conflict:** Suno's v4.5 announcement (<https://suno.com/blog/introducing-v4-5>, <https://help.suno.com/en/articles/5782593>) describes v4.5 as raising the **first generation** ceiling to **8 minutes**. The MCP reports v4.5 at **4 minutes**.

**Most likely explanation, stated as inference and labelled as such:** the connected MCP server is a **third-party API bridge**, not Suno's first-party interface — the `chirp-*` model identifiers are internal API names used by resale API providers. Third-party bridges frequently expose more conservative limits than the consumer web app. **Trust the web app's own UI over both tables** for what you can actually render in your browser session.

**Two limits worth internalising regardless of which table is right:**

- **The style box is character-limited.** 200 characters on v3/v3.5/v4; **1,000 characters** on v4.5 and later. This is the single most important constraint on style-prompt craft, and §6 is built around it.
- **The lyric box is character-limited.** 3,000 characters on v3–v4; **5,000 characters** on v4.5 and later. Long-form a cappella and choral pieces will hit this. Plan to Extend rather than to cram.

**Important caveat on those character limits.** They are **OFFICIAL (MCP)** — returned directly by `suno_list_models` — but **Suno itself does not publish a limits table** on any help-center page that could be identified. App-side numbers can shift between UI releases without announcement. Treat the figures as accurate for the API surface and approximately right for the web app; if the box stops accepting text before you expect, believe the box.

### 1.5 A note on the connected MCP server

This project has a Suno MCP server connected. Its read-only introspection tools (`suno_list_models`, `suno_list_actions`, `suno_get_lyric_format_guide`, `suno_list_personas`) are cited throughout this guide as **OFFICIAL (MCP)**.

**Read this carefully:** the MCP exposes job-starting tools (`suno_generate_music`, `suno_cover_music`, `suno_extend_music`, `suno_create_persona`, and others) that **consume credits from your account**. Introspection is free; generation is not. The full action surface is catalogued in §2.6.

**One live data point from your own account.** `suno_list_personas` returned exactly **one** saved persona as of 2026-08-01:

```json
{
  "persona_id": "31e86491-68f8-4655-9a77-eb47a2a2f3f7",
  "name": "DigiDjo Lead Voice v1",
  "description": "Charismatic gritty-warm male lead vocal in French with West African accent, chant-leader phrasing, festive triumphant energy, gang-vocal call-and-response style — the DigiDjo house voice for coupé-décalé × afrobeats releases",
  "source_type": "persona",
  "source_audio_id": "fd5dddd7-3ff0-46a2-9b61-92d84ecbfe9d",
  "created_at": 1784711542
}
```

Two things this tells you, and they shape §9 and §12:

1. **The persona object is anchored to a `source_audio_id`.** A persona is not a text description that Suno interprets — it is a *reference to one specific rendered audio clip* whose vocal character gets carried forward. The `description` field is a human-readable label for your own benefit; the vocal identity lives in the source audio. This is the single most misunderstood thing about Personas and it changes how you should seed them (§9.2).
2. You already have a West-African-accented, French-language, call-and-response chant-leader voice captured. That persona is directly reusable for the Afro-fusion, Afro-gospel, and coupé-décalé × Afrobeats work in §8, and it is a ready-made spine for the album workflow in §12.

### 1.6 Setup checklist before you make anything serious

1. **Confirm your plan and model access.** On Pro you should see v4, v4.5, v4.5+, v5, and v5.5 selectable. If v5.5 is missing, your subscription state has not propagated.
2. **Set your default model to v5.5** for vocal work. §1.7 explains why in one line: it is the only model whose release notes specifically claim improvements in *phrasing nuance, vocal emotional depth, and instrument separation* — the three axes that decide whether vocal-forward output sounds human.
3. **Turn off any "surprise me" style randomisation** if your UI offers it. For consistent-identity work (§12) you want determinism in every field you control.
4. **Create a workspace per project, not per song.** §2.3.
5. **Decide your download format policy now.** WAV for anything you will master or stem; MP3 only for reference listening. Re-downloading later is free but re-generating is not.

### 1.7 Which model to actually use

**OFFICIAL** — model timeline per <https://help.suno.com/en/articles/5782721> and <https://suno.com/release-notes>.

| Version | Released | Max first-gen length | Vocal realism | Harmony / multi-voice | Prompt adherence | Use it for |
|---|---|---|---|---|---|---|
| **v3** | 2024-03-21 | ~2 min initially, then 120 s | Baseline; audibly synthetic | Not addressed in release material | Baseline | Nothing today. **Deprecated for free users** as of 2025-09-11 |
| **v3.5** | Summer 2024 | 4 min (Extend +2 min/pass) | Marginal | Not addressed | Baseline | Nothing today. Legacy only |
| **v4** | Nov 2024 | 4 min | **Step-change** — "completely changed the robotic tone of earlier models." Introduced **Extend, Cover, Persona** | Persona arrives here — first identity-consistency tool | Improved | Legacy project compatibility |
| **v4.5** | **2025-05-01** | **8 min in one shot** (no Extend needed) | Enhanced depth, emotion, range — "whispers to full-on power hooks" | Not separately claimed | **Major focus.** Expanded genres, smarter mashups, "Enhance" prompt helper | Reliable fallback; genre blends |
| **v4.5+** | Jul 2025 | 8 min | Same as v4.5 | **Add Vocals / Add Instrumental** — layer vocals onto an instrumental or vice versa | Same | Layering work; the vocal-onto-instrumental path |
| **v5** | Sept 2025 (~09-23) | 8 min | **Authentic vocals** — breathiness, vibrato, dynamic expression. Cleaner mixes | **Improved instrument separation**; consistent voice/instrument signature across a project; multi-stem export workflow | Improved | Strong general choice |
| **v5.5** | **2026-03-26** | 8 min | **Best available.** Nuanced phrasing, vocal emotional depth, dynamic range | **Best instrument separation.** Powers **Voices**, **Custom Models**, **My Taste** | Best | **Default for all vocal-forward and a cappella work** |

**Sources:** <https://help.suno.com/en/articles/5782721> (Model Timeline), <https://help.suno.com/en/articles/5782593> (What's new in V4.5), <https://help.suno.com/en/articles/8105153> (Introducing v5), <https://help.suno.com/en/articles/11362305> (What's New in v5.5), <https://help.suno.com/en/articles/7986753> (Sept 2025 model availability update).

**Every version named in the brief is real.** v3, v3.5, v4, v4.5, v4.5+, v5 all exist and are confirmed. Three clarifications:

- **v5.5 is the current flagship** as of 2026-08-01 and the brief did not name it. Use it.
- **v6 does not exist.** No v6 has shipped, been named, dated, or priced as of 2026-08-01. Secondary reporting indicates Suno has signalled new licensed models later in 2026, but nothing is confirmed. If you see a "v6 prompt guide" anywhere, it is fabricated.
- **v4.5+'s taxonomic status is slightly ambiguous.** It is real and separately named in the Model Timeline, but whether Suno treats it as a distinct top-level model or an incremental update folded under the v4.5 help category could not be resolved. It appears as a selectable model, which is what matters practically.
- **v4.5-all** (2025-10-21) is the model served to the Free tier. Not a separate capability tier for you.
- **Deprecations, 2025-09-11** (**OFFICIAL** — <https://help.suno.com/en/articles/7986753>): v2 and v3 deprecated for free users; **Remaster v4 deprecated for all users**.

**On vocal isolation quality specifically** — the per-version axis the brief asks about: **v5 introduced improved instrument separation and v5.5 improved it further.** Nothing before v5 has any separation claim attached. This matters directly for §7's stems-as-fallback workflow: a v5.5 render stem-splits more cleanly than a v4.x render of the same song, because the sources were less entangled in the mix to begin with. **If you intend to stem-split, generate on v5.5 even if you prefer another model's musical character.**

**A v5.5 regression you should know about before you commit to it.** **COMMUNITY**, reported independently across multiple source clusters: v5.5 has a **mid-track degradation** failure mode — a track starts clean and then turns hissy, robotic, or structurally incoherent partway through. It is described as common on v5.5 and less common on v5 and v4.5.

The community workaround is worth having in your pocket: **generate on v4.5 or v5, then run the result through Cover on v5.5.** You inherit v5.5's improved timbre without exposing a full generation to the degradation bug. This is unverified by Suno and may be fixed by the time you read this — but if a long v5.5 vocal take falls apart at the three-minute mark, this is why, and that is the route around it.

This does not change the recommendation to default to v5.5. It changes what you do when v5.5 misbehaves on a long take: shorten the generation and Extend (§10.2), or fall back to generate-on-v5-then-Cover.

**A documented conflict on vocal gender control.** The MCP's `suno_list_models` output lists, under "Features by Version," that **v4.5+ has vocal gender control ('f' for female, 'm' for male)**. No official Suno help-center article describing a vocal-gender toggle could be identified. Most likely reading — labelled as inference: this is an **API-level parameter** exposed by the third-party bridge (§1.4), not a documented consumer UI feature. In the web app, specify gender in the style box (§6.4) rather than looking for a switch.

### 1.8 The three v5.5 features that change how a vocal project is run

**OFFICIAL** — <https://suno.com/release-notes/introducing-v5-5-voices-custom-models-and-my-taste>, 2026-03-26.

| Feature | What it does | Why it matters for vocal-forward work |
|---|---|---|
| **Voices** | Record or upload your own audio; Suno verifies it by asking you to sing a randomised phrase, then generates songs in your own vocal identity | This is the strongest available answer to "make it sound like a real human singer" — because it is one. Supersedes Persona for *your own* voice. Personas remain the tool for a synthetic-but-consistent identity. |
| **Custom Models** | Upload **≥6 tracks** from your catalogue to train a private personalised version of v5.5. **Up to three** models; they stay private | The album-cohesion tool (§12). A custom model biases *everything* toward your sound — not just the voice, but arrangement and production habits. |
| **My Taste** | Learns your recurring genres, moods, and references; applies them via the Magic Wand | Convenience, and a mild hazard for this discipline — it pulls output toward your averages, which is the opposite of what you want when deliberately breaking pattern. Know it is on. |

**A UI change you will run into immediately.** **OFFICIAL** — in the v5.5 interface, the **"Voices" button replaced "Personas"** in the Create menu. Personas were not removed: **"Style Personas" remain accessible inside the Voices menu.** Suno frames Voices as an evolution of Personas that additionally captures your own singing voice. If you go looking for a Personas button and cannot find one, look inside Voices.

**On "Personas v2":** the brief refers to this. **No official Suno feature, article, or term called "Personas v2" could be found.** The name appears to be community or press shorthand for the Personas→Voices transition described above, or a conflation with Custom Models. Stated here rather than dropped, and rather than described as if it were real.

> **A judgement call, stated plainly:** if your goal is one believable singer across a body of work and that singer can be *you*, **Voices is a better tool than Personas** and you should evaluate it first. §9 covers Personas thoroughly because the brief asks for it and because Personas remain correct when the voice must be synthetic, must not be legally tied to a real performer, or must be a character rather than a person.

---

## 2. Interface walkthrough

### 2.1 The Create page

The Create page is where every generation starts. It has two modes, and the toggle between them is the most consequential switch on the platform.

| Control | Simple / prompt mode | Custom Mode |
|---|---|---|
| Song description | One free-text box — subject *and* style together | Absent — split into separate fields |
| Lyrics | Written for you | **Your field.** Paste your own, or generate then edit |
| Style | Inferred from the description | **Your field.** Genre, instrumentation, tempo, vocal type, production |
| Title | Auto | Yours |
| Instrumental toggle | Yes | Yes |
| Exclude styles | Yes | Yes |
| Model selector | Yes | Yes |
| Persona / Voice selector | Yes | Yes |

**For everything this guide is about, you will live in Custom Mode.** Simple mode is covered properly in §3 because it is genuinely the right tool for a specific job — finding a direction you cannot yet describe — but it cannot deliver controlled vocal work.

Official references: Simple Mode — <https://help.suno.com/en/articles/2462273>; using your own lyrics — <https://help.suno.com/en/articles/2415873>; V4.5-era prompt guidance — <https://help.suno.com/en/articles/5782977> ("Better Prompts in Lyrics") and <https://help.suno.com/en/articles/5782849> ("Detailed Style Instructions").

### 2.2 The Exclude field

**OFFICIAL** — this is a documented feature with its own help article: <https://help.suno.com/en/articles/3161921>, "How do I exclude elements of a song?" **Suno's own name for it is "Exclude," not "negative prompt."** It covers omitting unwanted genres, instruments, and vocal styles from a generation.

This is Suno's negative-prompting surface, and it is drastically under-used. Community consensus is that Exclude works by removing *conflicting* elements — it is a suppressor, not an absolute prohibition. It cannot guarantee the absence of something, but it measurably shifts probability.

For vocal-forward work these are the three exclusions that earn their place most often:

```
autotune, pitch correction, vocoder
```

```
drums, percussion, bass, synth, guitar, piano
```

```
lo-fi, distorted, tape hiss, vinyl crackle
```

§6.6 and §7.3 develop this properly.

### 2.2b Advanced Options — the three sliders

**OFFICIAL** that these controls exist in the Create page's Advanced Options; **COMMUNITY** as to how the ranges behave in practice.

| Slider | Range | What it does |
|---|---|---|
| **Weirdness** | 0–100%, default ~50% | Low = simpler, more predictable, steadier vocals. High = more experimental, more distinctive vocal processing |
| **Style Influence** | 0–100% | How tightly the output adheres to your style box |
| **Audio Influence** | 0–100% | How strongly an uploaded/reference audio steers the result |

**Community-reported working bands for Weirdness:** 10–30% for safe, commercial, predictable output; 40–60% balanced; 70–100% experimental.

**For vocal-forward work, keep Weirdness low — 10–30%.** "Distinctive vocal processing" is precisely what you are trying to avoid; it is the mechanism behind several of the artefacts in §6.7. High Weirdness and a request for a natural, unprocessed voice are working against each other.

**One counterintuitive tip that recurs across sources:** a *vague* style box benefits from **high** Style Influence (70–90%), not low. If all you have written is `pop`, pushing influence up makes the model commit to that thin instruction rather than wandering. A detailed style box does not need it.

**The caveat every source repeats:** higher influence is not higher quality. The sliders cannot rescue unclear lyrics, contradictory style directions, or poor source audio. They are not a quality knob.

### 2.3 Library and Workspaces

- **Library** — every song you have generated, chronological, searchable, filterable. Your default destination.
- **Workspaces** — **OFFICIAL**, <https://help.suno.com/en/articles/4326849>. Distinct from the Library, found **above the Create button**. Groups related generations — notably a chain of Extends — into a named container. Move songs in from the Library via multi-select → More Actions → **Move to Workspace**.

Create one workspace **per project, not per song**. For the album workflow in §12 the workspace *is* the album: it is where you keep the seed track, the persona reference, the style-box variants, and the ordered tracklist together. Working out of a raw Library on a 12-track album is how sonic identity drifts without anyone noticing.

**Practical convention that pays for itself on album work:** name tracks `NN — Title — vN` (`03 — Ìmọ́lẹ̀ — v4`). Suno's default titles are unstable across re-rolls and you will lose track of which take was the good one.

### 2.4 The editing surface

Selecting a finished song exposes the operations catalogued in §10, reached via **More Actions (…) → Edit**. This includes **Get Stems**, Replace Section, and Crop. The **Song Editor** (**OFFICIAL** — <https://help.suno.com/en/articles/6141505>) lets you reorder, rewrite, and remake a track **section by section directly from the waveform**.

### 2.5 Suno Studio — Premier only

**OFFICIAL** — <https://help.suno.com/en/articles/7940161> ("Introduction to Studio") and <https://help.suno.com/en/articles/8128193> ("Exporting from Studio").

Suno describes Studio as a **"web-based Generative Audio Workstation (GAW)"** — a DAW with AI generation built into it. Launched late 2025, **Premier only**. What it does:

- Multitrack layering, arranging, and editing
- **In-place AI stem generation** — generate a bass, percussion, or melody part directly into the arrangement
- Auto-saved, versioned projects
- Export as **Full Song**, **Selected Time Range**, or **Multitracks**; **MIDI extraction** from stems (10 credits)
- Shipped **v1.1** (Stem Cover, recording) and **v1.2** (Remove FX, Warp Markers, Time Signatures) in early 2026

**On Pro, you do not have this.** Your equivalent is: generate on v5.5 → Get Stems → finish in your own DAW. That path is not worse, and for anyone who already owns a DAW it is arguably better. §11 assumes it.

> **The one genuine reason to consider Premier for this discipline** is not Studio — it is **Advanced Split**, the Premier-exclusive stem separation across roughly 100 instrument types (**OFFICIAL** — <https://help.suno.com/en/articles/12702337>). For vocal isolation work specifically, finer separation is worth more than a browser DAW you may already own a better version of.

### 2.6 WavTool — status, confirmed

Earlier drafts of this guide flagged this as unconfirmable. **It is confirmable, from Suno's own blog.**

**OFFICIAL** — <https://suno.com/blog/suno-acquires-wavtool>: Suno acquired **WavTool**, a browser-based AI-accelerated DAW, "bringing WavTool's advanced editing capabilities and core team into Suno," with WavTool leadership taking product and engineering roles at Suno. Suno subsequently introduced **Suno Studio**, explicitly positioned as *"the next chapter for the evolution of the DAW,"* built on the acquired technology.

**What this means practically:** Suno Studio *is* the productised successor to WavTool. Do not plan a workflow around WavTool as a separate surface — Studio is where that technology lives now. Whether wavtool.com remains independently accessible as a legacy product was not confirmed, but it is not the right place to build.

### 2.7 The full action surface

**OFFICIAL (MCP)** — verbatim from `suno_list_actions`, 2026-08-01. This is the most complete enumeration of Suno's operation set available in this guide, and several of these operations have no obvious entry point in the consumer web UI.

| Category | Action | What it does |
|---|---|---|
| **Generation** | `suno_generate_music` | Simple/Inspiration mode — text prompt in, song out |
| | `suno_generate_custom_music` | Custom Mode — separate lyrics and style |
| | `suno_extend_music` | Continue a song from a chosen timestamp |
| | `suno_cover_music` | Cover/remix an existing song |
| | `suno_concat_music` | Merge extended segments into one continuous audio file |
| | `suno_remaster_music` | Re-render a song at improved audio quality |
| | `suno_replace_section` | Replace a specific time range with new content |
| | `suno_mashup_music` | Blend multiple songs musically |
| **Upload-based** | `suno_upload_audio` | Bring external audio into Suno |
| | `suno_upload_extend` | Extend uploaded audio with AI content |
| | `suno_upload_cover` | AI cover of uploaded audio |
| | **`suno_underpainting`** | **Add AI accompaniment to uploaded *vocal* audio** |
| | **`suno_overpainting`** | **Add AI vocals to uploaded *instrumental* audio** |
| | `suno_samples_music` | Add AI-generated samples to uploaded audio |
| **Stems** | `suno_stems_music` | Two-way split: vocal + instrumental |
| | `suno_all_stems_music` | Full multi-stem split: vocals, bass, drums, etc. |
| | `suno_extract_vocals` | **Vocal track only** |
| **Media** | `suno_get_mp4` / `suno_get_wav` / `suno_get_midi` / `suno_get_timing` | Video, lossless audio, MIDI, word-level timing data |
| **Persona** | `suno_create_persona` | Save a voice style from Suno-generated audio |
| | `suno_create_voice` | Create a voice persona from an **external** audio URL |
| | `suno_list_personas` / `suno_delete_persona` | Manage saved personas |
| | `suno_generate_with_persona` | Generate using a saved voice |
| | **`suno_generate_with_persona_vox`** | **Generate using a saved voice in "VOX consistency mode"** |
| **Lyrics** | `suno_generate_lyrics` | Lyrics from a prompt |
| | `suno_optimize_style` | **Optimise a style description for better results** |
| | `suno_mashup_lyrics` | Combine two lyric sets |
| **Info** | `suno_list_models` / `suno_list_actions` / `suno_get_lyric_format_guide` | Read-only introspection (free) |

**Five of these deserve your specific attention because they are directly load-bearing for vocal-forward work and are easy to miss:**

1. **`suno_extract_vocals`** — a dedicated vocals-only extraction, distinct from the two-way stem split. This is the cleanest documented path to an a cappella from an existing track (§7.5).
2. **`suno_underpainting`** — upload a dry vocal, get AI accompaniment built underneath it. **This inverts the whole problem.** If you have a real recorded vocal, or a stem-extracted one, you are no longer asking Suno to sing convincingly — you are asking it to arrange. That is a much easier ask and it is the single highest-leverage technique in this guide for "human-sounding" results.
3. **`suno_overpainting`** — the mirror: upload an instrumental, get AI vocals on top. Corresponds to v4.5+'s **Add Vocals**.
4. **`suno_generate_with_persona_vox`** — a distinct "VOX consistency mode" for persona generation. The MCP documents that it exists and that it is a consistency mode; **what VOX mode does differently from standard persona generation is not documented in the MCP output and could not be confirmed elsewhere — UNCONFIRMED.** Worth testing empirically for album work (§12.4), because if it does what its name implies it is exactly the album-cohesion tool.
5. **`suno_optimize_style`** — an official style-description optimiser. If your style box is not landing, this is a documented first move before you start hand-tuning.

---

## 3. Your first song in Simple mode

### 3.1 What Simple mode is actually good at

Simple mode takes one free-text description and writes the lyrics, the style, and the title for you. It is a **direction-finding tool**, not a production tool. Use it in exactly two situations:

1. **You cannot yet describe what you want.** Type the feeling, listen to four takes, and steal the vocabulary from whichever one is closest. This is the fastest way to build the style vocabulary you will need in Custom Mode.
2. **You need a persona seed and do not care about the lyric.** A persona is captured from rendered audio (§1.5), so a throwaway Simple-mode render can be a perfectly good voice source.

Do not use it for finished work. You cannot control structure, you cannot place vocal metatags, and you cannot separate "what the song is about" from "how it should sound" — which is the entire discipline of §5 and §6.

### 3.2 Writing a Simple-mode prompt that returns something useful

The failure mode is describing a *subject* and getting a genre cliché back. Give it a **subject, a sonic frame, and a vocal instruction** in one breath:

```
A grandmother's kitchen at dawn, sung by a warm mid-range male voice with
audible breath and no autotune, over sparse acoustic guitar and hand percussion.
Afro-soul, unhurried, 92 BPM.
```

Compare with what most people type — `a song about my grandmother` — which will return a generic sentimental ballad every time.

**Three habits from that example, carried forward into every prompt in this guide:**

- **Name the vocal explicitly.** Voice type, register, texture. Suno defaults to a genre-typical voice if you do not, and genre-typical is exactly the "AI sameness" problem (§6.7).
- **Name the tempo.** A BPM number constrains groove more reliably than an adjective.
- **Name one thing you do not want.** `no autotune` in the description works even before you reach the Exclude field.

### 3.3 Reading the two takes

Every generation returns **two takes** from the same prompt. They are not ranked. Judge them on **the vocal first** — for this discipline, a take with a great arrangement and a plasticky voice is a dead end, whereas a take with a compelling voice and a mediocre arrangement is salvageable via stems, Replace Section, and Extend. Vocal character is the hardest thing to fix downstream; everything else is negotiable.

---

## 4. Switching to Custom Mode

### 4.1 What changes, and why it is the whole game

Custom Mode splits one box into four independent controls: **Lyrics**, **Style**, **Title**, and **Exclude Styles**, plus the instrumental toggle, model selector, and persona/voice selector.

The reason this matters is not convenience. It is **separation of concerns**. In Simple mode, your subject matter and your sonic intent compete for the model's attention in a single string, and subject matter usually wins — which is why Simple-mode output drifts toward genre defaults. In Custom Mode:

- **The lyric box controls what is sung and how it is performed** — words, structure, and vocal metatags (§5).
- **The style box controls what it sounds like** — genre, instrumentation, tempo, vocal type, mix, era (§6).

Cross-contaminating these is the most common Custom Mode error. **Do not put genre words in the lyric box. Do not put narrative in the style box.**

### 4.2 The field-by-field discipline

| Field | Belongs here | Never here |
|---|---|---|
| **Lyrics** | Words to be sung; `[Section]` tags; performance metatags; phonetic respellings | Genre names, BPM, instrument lists, mix instructions |
| **Style** | Genre stack, sub-genre, region, BPM, instrumentation, vocal type and mix prominence, production era, mix reference | Lyric content, story, song title, section structure |
| **Title** | The title | Style hints (it does not read as style) |
| **Exclude Styles** | Instruments and treatments to suppress | Anything you actually want |

### 4.3 Own lyrics vs AI-assisted lyrics

You have three routes, and they are not equal for vocal-forward work.

| Route | How | When it is right |
|---|---|---|
| **Write your own** | Paste into the lyric box | **Default for this discipline.** Only route that gives you syllable-level control over phrasing (§5.5), and the only one where phonetic spelling for accent (§8.5) survives intact. |
| **AI-generate, then edit** | Suno's lyric generator or `suno_generate_lyrics`, then rewrite | Good compromise. Generate for structure and rhyme scaffolding, then **rewrite every line for singability**. AI lyrics are consistently over-syllabled — they scan on the page and choke in the mouth. |
| **AI-generate, use as-is** | Accept the output | Only for throwaway seeds and demos. |

**The edit pass that matters most, whatever route you take:** read every line **out loud at the target tempo**. If you cannot sing it comfortably, the model cannot either — it will compress syllables, swallow consonants, and produce exactly the mumbled diction complained about in §7.8.

### 4.4 The instrumental toggle

Turning **Instrumental** on suppresses vocals entirely and ignores the lyric box. Relevant here for two reasons: it is how you make backing tracks (§10.6), and it is the thing you must **not** accidentally leave on when chasing an a cappella — an easy and infuriating mistake, since "no instruments" and "no vocals" are opposite intentions and only one of them has a toggle.

### 4.5 A Custom Mode starting template

Copy this, fill the three brackets, and you have a correctly-separated first attempt:

```
STYLE BOX:
[genre stack], [BPM] BPM, [instrumentation, 3-5 items],
[vocal type + register + texture], vocals mixed forward and dry,
[production era / mix reference]

LYRIC BOX:
[Intro]
...
[Verse 1]
...
[Pre-Chorus]
...
[Chorus]
...
[Outro]

EXCLUDE STYLES:
autotune, pitch correction, over-compressed
```

---

## 5. Writing and formatting lyrics and vocal metatags

### 5.1 The official baseline

**OFFICIAL (MCP)** — verbatim guidance from `suno_get_lyric_format_guide`, 2026-08-01. This is the only lyric-formatting guidance in this guide that carries an official label, and it is deliberately minimal:

> **Section markers (square brackets):** `[Verse]` or `[Verse 1]`, `[Verse 2]` · `[Chorus]` · `[Pre-Chorus]` · `[Bridge]` · `[Outro]` · `[Intro]`
>
> **Tips for best results:**
> - Keep lines concise (**4–8 words**) for better singing flow
> - Use simple, clear language that's easy to sing
> - Include rhymes for catchiness (especially in the chorus)
> - Leave some creative freedom for the AI
> - Use consistent line lengths within sections
> - End verses with a lead-in to the chorus

**That is the entire officially-documented tag vocabulary: six structural tags.** Everything else in this section — every performance tag, every vocal-direction tag — is **COMMUNITY**.

### 5.2 The OFFICIAL / COMMUNITY split on metatags, stated without hedging

**Suno does not publish a formal specification for bracket metatag syntax.** This is the most important negative finding in the guide, and it is worth being precise about what was and was not found:

- **Suno's help center has no metatag syntax spec.** There is no official article documenting `[Verse]`, `[Chorus]`, `[Instrumental]` etc. as an input format.
- **Suno does publish a "Music Glossary for Suno"** — **OFFICIAL**, <https://help.suno.com/en/articles/9010177> — which defines song-structure vocabulary (Verse, Chorus, Bridge, Pre-Chorus, Intro/Outro) alongside sections on Tempo & Rhythm, Melody & Harmony, Genres & Styles, Instrumentation & Texture, **Vocal Techniques**, and Production & Effects. But it presents these as **musical concepts to inspire prompt-writing**, not as bracket syntax. It is a vocabulary source, not a spec — and as a vocabulary source for §6 it is genuinely useful.
- **Suno does publish V4.5-era prompt guidance** — <https://help.suno.com/en/articles/5782977> ("Better Prompts in Lyrics") and <https://help.suno.com/en/articles/5782849> ("Detailed Style Instructions").
- **The six structural tags in §5.1 are officially documented via the MCP's `suno_get_lyric_format_guide`.** That is a real official source and it is why they carry an OFFICIAL label here.
- **Everything beyond those six comes from third-party sites.** The community has catalogued hundreds of bracket tags through trial and error. Sites advertising "1,000+ Suno metatags" are documenting *observed behaviour*, not a specification. The model empirically responds to many of them; Suno has never ratified any of them.

What follows from that, and you should hold it firmly:

- **The six structural tags in §5.1 are reliable.** They are documented and the model is trained to respond to them.
- **Performance tags are probabilistic.** They shift output; they do not command it. A `[Whispered]` tag makes a whispered delivery more likely, not certain.
- **Tag behaviour can change between model versions without notice.** A tag that reliably worked on v4.5 may be inert on v5.5. Re-test your key tags after any model change.
- **Unrecognised bracket text is a real hazard.** Community consensus is that Suno may **sing the contents of a bracket it does not recognise**. Invent a clever tag and you may hear it performed as a lyric. Keep to conventional vocabulary.

| Tag class | Examples | Status |
|---|---|---|
| **Core structural** | `[Intro]` `[Verse]` `[Verse 1]` `[Pre-Chorus]` `[Chorus]` `[Bridge]` `[Outro]` | **OFFICIAL** |
| **Extended structural** | `[Hook]` `[Refrain]` `[Interlude]` `[Breakdown]` `[Drop]` `[Build]` `[Instrumental Break]` `[Solo]` `[Coda]` `[Fade Out]` | **COMMUNITY** — widely replicated |
| **Vocal arrangement** | `[Harmony]` `[Choir]` `[Backing Vocals]` `[Call and Response]` `[A Cappella]` `[Duet]` `[Unison]` | **COMMUNITY** — reasonably reliable |
| **Vocal performance** | `[Belted]` `[Whispered]` `[Falsetto]` `[Vocal Run]` `[Melisma]` `[Ad-lib]` `[Spoken Word]` `[Shouted]` `[Breathy]` `[Vibrato]` | **COMMUNITY** — variable; effect is a nudge |
| **Non-lexical vocal** | `[Humming]` `[Vocalize]` `[Chanting]` `[Ululation]` `[Beatbox]` `[Vocal Percussion]` `[Scat]` | **COMMUNITY** — least reliable class; see §7.6 |
| **Dynamic / mix** | `[Soft]` `[Loud]` `[Building]` `[Crescendo]` `[Sparse]` `[Full Band]` | **COMMUNITY** — treat as weak hints |

### 5.3 Where tags go, and the one placement rule that matters

The lyric box holds **structure tags and lyrics only**. The style box holds genre, mood, instrumentation, tempo, key, and production. Putting genre in the lyric box is a recognised error that produces genre drift, and putting structure in the style box does nothing at all.

**The placement rule:** a performance tag applies from where it appears **forward**, until the next section tag resets it. So this:

```
[Chorus]
[Belted]
Hold the line, hold the line
```

...belts the chorus. Whereas an inline tag placed mid-line is far less predictable and frequently ends up sung.

**A refinement with solid community backing:** performance cues are most reliable **on their own line, immediately preceding the section tag** — not embedded next to the lyric. Cues placed inline with a lyric line are widely reported as ignored. The pattern that works:

```
(whispered)
[Verse 1]
I been waiting for the morning to arrive

(belted)
[Chorus]
Nothing left to lose
```

**One v5.5-specific gotcha worth knowing:** **stray blank lines can be read as a pause or instrumental-break cue.** If your song is inserting gaps you did not ask for, strip the extra blank lines from your lyric box.

**Number your repeated sections.** `[Verse 1]` / `[Verse 2]` rather than two bare `[Verse]` tags — it helps the model treat them as parallel-but-distinct rather than as a repeat.

### 5.4 Combining tags — stacking, and its limit

Tags stack, and stacking is how you get specificity:

```
[Chorus]
[Choir] [Harmony] [Belted]
Ìmọ́lẹ̀ dé, ìmọ́lẹ̀ dé
```

**COMMUNITY consensus on the limit: two to three tags per section.** Beyond that, adherence collapses and the risk of a tag being sung rises. If you find yourself stacking five tags, the instruction belongs in the style box instead.

### 5.5 Lyric craft for singable phrasing

This is the part of the discipline that separates output that sounds performed from output that sounds recited, and almost none of it is Suno-specific — it is songwriting.

**Syllable and meter control.** The official guidance says 4–8 words per line. The more useful unit is **syllables**: aim for **6–10 syllables** in a verse line and **4–8** in a hook line. Keep syllable counts *consistent between parallel lines* — if verse 1 line 1 is 8 syllables and verse 2 line 1 is 14, the model has to compress the second one, and compression is what produces the machine-gun diction and swallowed word endings people describe as robotic.

**Stress placement.** Put your stressed syllables where the beat is. English lyrics that fight the meter get *re-stressed* by the model — `beCAUSE` becomes `BEcause` — and that single artefact reads as inhuman faster than almost anything else.

**Line length as a phrasing instruction.** A short line leaves air. Air is where breath goes, and breath is the strongest single cue of a human performance. Deliberately vary line lengths across a verse so the singer has somewhere to breathe:

```
[Verse 1]
I left the door open
Just in case
The rain came in instead
```

**Punctuation as phrasing.** These are **COMMUNITY** conventions with reasonably broad agreement:

| Mark | Reported effect |
|---|---|
| Comma | Short internal pause |
| Period / full stop | Full phrase end, breath likely |
| Ellipsis `...` | Trailing, unresolved delivery; hang |
| Em dash `—` | Abrupt cut-off |
| Line break | The primary phrasing unit — stronger than any punctuation |
| ALL CAPS | Emphasis, increased intensity |
| *Asterisks* / (parentheses) | Frequently rendered as **backing vocals or ad-libs** |

Parentheses are the highest-value item in that table. This is the single most reliable community technique for backing vocals, and it needs no bracket tag at all:

```
[Chorus]
We were never gonna stay here (never gonna stay)
Burning down the summer (burning, burning)
```

**Rhyme.** Perfect rhyme in the hook, slant rhyme in the verse. Wall-to-wall perfect rhyme is one of the loudest tells of AI-written lyrics.

**Repetition.** Real songs repeat far more than writers expect. A hook that appears four times with one word changed on the last pass will feel more like a record than four distinct clever lines.

### 5.6 Phonetic spelling to steer pronunciation, accent, and delivery

**COMMUNITY**, but consistently reported and central to §8.

Suno pronounces what it reads. If a word is being mangled — a name, a non-English word, a regional pronunciation — **respell it phonetically in the lyric box**. The lyric box is an instruction to a performer, not a document for a reader; it does not need to be orthographically correct.

| Intent | Written as | Notes |
|---|---|---|
| Yoruba `ìmọ́lẹ̀` (light) | `ee-MOH-leh` | Tone marks are generally not interpreted; syllabify and capitalise the stress |
| Swahili `nakupenda` | `nah-koo-PEN-dah` | |
| Zulu `sawubona` | `sah-woo-BOH-nah` | |
| Twi `medaase` | `meh-DAA-seh` | Doubled vowel to lengthen |
| Nigerian Pidgin `abeg` | `ah-beg` | |
| Dropped-g English | `runnin'`, `nothin'` | Apostrophe reliably drops the g |
| Drawn-out vowel | `sooooo`, `yeahhh` | Repeated letters lengthen the note |
| Southern US `right` | `rahht` | |
| Clipped British `water` | `wa-tuh` | |

**Three working rules:**

1. **Hyphenate syllables** and **capitalise the stressed one**. `nah-koo-PEN-dah` is far more reliable than `nakupenda`.
2. **Strip diacritics.** Tone marks and accents are unreliable and can trigger odd pronunciation. Encode tone through capitalisation and vowel doubling instead.
3. **Keep a clean copy.** Your published lyric sheet should have correct orthography. The phonetic version is a *studio script* for Suno only. Maintain both — this matters for multilingual releases where the printed lyric carries cultural weight.

### 5.7 Structure templates

**Standard pop / Afrobeats (3:00–3:30)**

```
[Intro]
[Verse 1]
[Pre-Chorus]
[Chorus]
[Verse 2]
[Pre-Chorus]
[Chorus]
[Bridge]
[Chorus]
[Outro]
```

**Hook-first, for short-form and streaming (2:20–2:50)**

```
[Intro]
[Chorus]
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
[Outro]
```

**Vocal-forward ballad with a dynamic arc**

```
[Intro]
[Whispered]
[Verse 1]
[Pre-Chorus]
[Building]
[Chorus]
[Belted]
[Verse 2]
[Chorus]
[Bridge]
[A Cappella]
[Chorus]
[Full Band]
[Outro]
```

That bridge is the important move: dropping to a bare vocal before the final chorus is the oldest dynamic trick in vocal music and it is the most effective single instruction for making a Suno track feel arranged by a person.

### 5.8 The ending problem

Abrupt endings are among the most-complained-about Suno failure modes. Three mitigations, all **COMMUNITY**:

1. **Always write an explicit `[Outro]`** with actual content — even two lines. Songs that end on a final `[Chorus]` are the ones that cut off mid-word.
2. **Add a terminal instruction**: `[Fade Out]` or `[End]` as the last line.
3. **Leave headroom.** If your target is 3:00, aim the arrangement at 2:45. Suno truncating a song that hits the duration ceiling is the actual mechanism behind most abrupt endings — and where Extend then Crop (§10) becomes the reliable fix.

---

## 6. Crafting the style prompt for a natural, vocal-forward human sound

### 6.1 The style box is a budget

**OFFICIAL (MCP):** 200 characters on v3/v3.5/v4, **1,000 characters on v4.5 and later**. On v5.5 you have room — but not unlimited room, and **every word competes with every other word for attention**. A 900-character style box is not four times as controlled as a 220-character one; past a point, adding descriptors dilutes the ones that matter.

**Target 150–350 characters for most work.** Go longer only when you are deliberately stacking a hybrid genre.

**Two budget facts that cost people real time:**

- **Suno truncates silently past the character cap.** No error, no warning — the tail of your style box is simply discarded. This is a common and hard-to-diagnose beginner failure. If your last few descriptors seem to have no effect, count your characters.
- **Tag-count sweet spot is roughly 8–15 descriptors.** Below 4–5 the prompt is too vague to steer anything. Above 15–20 the model starts dropping tags — and community reporting specifically claims it drops them **from the middle**, not just the end, which makes over-long prompts fail in ways that are hard to attribute. Put your must-haves first and last.

### 6.2 The slot framework

Write the style box as **ordered slots**. Order matters — earlier terms carry more weight (**COMMUNITY** consensus, widely replicated):

```
1. GENRE STACK      — primary genre, then modifier genre
2. REGION/ERA       — where and when it is from
3. TEMPO            — a BPM number
4. INSTRUMENTATION  — 3-5 named instruments, no more
5. VOCAL            — type, register, texture, accent
6. VOCAL MIX        — how forward, how dry
7. PRODUCTION       — mix character, era, reference
```

Worked example, 268 characters:

```
Afro-soul with gospel harmony, contemporary Lagos, 92 BPM, fingerpicked
nylon guitar, upright bass, brushed kit, hand percussion. Warm mid-range
male lead, slight rasp, Nigerian English accent. Lead vocal loud, dry,
close-mic'd, front of mix. Analog warmth, minimal compression.
```

Every slot is doing work. Delete the vocal-mix slot and the voice sinks into the band. Delete the accent and you get generic international pop-soul.

### 6.3 The vocal-forward instruction specifically

This is the crux of the brief and it deserves being spelled out. **Suno's default mix places vocals inside the band.** To get them forward you must say so explicitly, and the terms that community reporting consistently finds effective are mixing terms, not adjectives:

| Goal | Style-box phrasing |
|---|---|
| Vocal loud in the mix | `lead vocal loud in the mix`, `vocals front and centre`, `vocal-forward mix` |
| Vocal dry and close | `dry vocal`, `close-mic'd`, `intimate vocal`, `minimal reverb on lead` |
| Sparse backing | `sparse instrumentation`, `minimal arrangement`, `stripped-back`, `let the voice carry it` |
| Vocal as the focus | `vocal-led`, `voice is the lead instrument` |

**Stack three of these, not one.** `vocal-forward mix, dry close-mic'd lead, sparse arrangement` is materially more effective than any single phrase.

The reason sparseness matters as much as level: a vocal is forward *relative to* what surrounds it. Thinning the arrangement raises the voice more reliably than asking for the voice to be louder.

### 6.4 Naming the voice

Never leave the voice to the genre default. Specify along **five axes** — and pick at most three per prompt, or they compete:

| Axis | Vocabulary |
|---|---|
| **Type / register** | male / female / androgynous; tenor, baritone, bass, alto, soprano, mezzo; low, mid-range, high |
| **Texture** | warm, raspy, gritty, smoky, breathy, clear, nasal, rich, thin, husky, gravelly, silky |
| **Delivery** | conversational, declamatory, soulful, restrained, urgent, laid-back, percussive, melismatic |
| **Accent / origin** | Nigerian English, Ghanaian English, South African English, Southern American, London, Jamaican Patois, Parisian French |
| **Age / character** | young, mature, weathered, childlike, elder |

Worked: `weathered baritone, smoky and conversational, Ghanaian English accent`.

### 6.5 Production and era

Era references are among the most efficient tokens in the whole box — one word carries an entire production aesthetic:

| Phrasing | What it buys you |
|---|---|
| `1970s analog warmth`, `tape saturation` | Softer transients, less clinical top end |
| `late-90s R&B production` | Specific era of vocal stacking and drum programming |
| `modern streaming master`, `loud contemporary mix` | Bright, compressed, current |
| `live room recording`, `single-take feel`, `room mics` | Ambience and bleed — reads as human |
| `lo-fi`, `bedroom recording` | Deliberate imperfection |
| `minimal compression`, `wide dynamic range` | **The most useful for vocal realism** — see §6.7 |

### 6.6 Negative prompting

**OFFICIAL** that the Exclude Styles field exists; **COMMUNITY** as to what to put in it.

Exclude works as a suppressor. It measurably shifts output without guaranteeing absence.

**Keep it short — 2 to 3 exclusions.** This is repeated near-identically across independent community sources and it is the opposite of most people's instinct. A long exclusion list dilutes the same way a long style box does; you get weaker suppression of everything instead of strong suppression of the thing that was actually bothering you. **Exclude the specific problem you heard in the last take, not every problem you can imagine.**

The three highest-value exclusion sets in vocal-forward work — pick one, occasionally two:

```
autotune, pitch correction, vocoder
```

```
heavy compression, over-produced
```

```
choir pad, synth choir
```

That third one matters more than it looks: asking for a choir frequently returns a *synthetic choir pad* rather than stacked human voices. Excluding the pad pushes the model toward actual layered vocals (§7.6).

**The one place to break the short-list rule** is true a cappella (§7.2), where you are fighting the model's core instinct to generate accompaniment and stacked redundant negation is reported to genuinely help. Everywhere else, keep it to three.

**A trap worth naming.** Words like `anthemic chorus`, `festival hook`, `gospel emotion`, and `crowd energy` are reported to **invite extra voices** — choirs, crowds, gang vocals — even when you asked for a solo singer. If unrequested backing vocals keep appearing, look for one of these words in your style box before you start adding exclusions.

### 6.7 The natural / human dimension — the core section

**This section is the reference point for the entire guide.** Every output type in §10.6 and every genre playbook in §13 points back here rather than repeating it. If you read one section, read this one.

"AI-sounding" is not one flaw. It is six, and each has a different fix.

---

**1. Excessive smoothness — no error, no grit, no variation.**

Human singing is full of small failures: a slightly flat note pulled back into tune, a consonant that lands late, a breath taken in the wrong place. Suno's default is to render none of these.

*Fix, in the style box:* `slightly imperfect vocal`, `raw take`, `unpolished`, `first-take feel`, `human imperfection`, `live vocal take`.
*Fix, in the lyric box:* vary your line lengths and syllable counts so the phrasing cannot settle into a grid.
*Fix, in Exclude:* `pitch correction, autotune, quantised`.

---

**2. Dynamic flatness — every line at the same intensity.**

The single most reliable tell. Real performances have an arc; Suno defaults to a plateau.

*Fix, in the style box:* `wide dynamic range`, `minimal compression`, `builds from quiet to powerful`.
*Fix, in the lyric box:* stage the dynamics explicitly with tags — `[Whispered]` on verse 1, plain on verse 2, `[Belted]` on the final chorus. Do not ask for dynamics; **schedule** them.
*Fix, structurally:* the bare-vocal bridge before the last chorus (§5.7).

---

**3. Absent breath.**

Breath is the cheapest and strongest humanity cue available.

*Fix, in the style box:* `audible breaths`, `breathy delivery`, `you can hear them breathing`, `close-mic'd intimate vocal` — close-mic'ing implies breath by implication and is often more effective than asking for breath directly.
*Fix, in the lyric box:* **write in the gaps.** A line that runs to the end of the bar leaves nowhere to breathe. Shorten every fourth line.
*Note:* `[Breath]` as a bracket tag is **COMMUNITY and unreliable** — it is reported as often ignored, and occasionally sung. Prefer style-box phrasing and lyric spacing.

---

**4. Autotuned / pitch-perfect tone.**

*Fix, in Exclude:* `autotune, pitch correction, vocoder, melodyne` — the highest-value single exclusion in this guide.
*Fix, in the style box:* `natural pitch`, `unprocessed vocal`, `no autotune`, `raw untuned vocal`.
*Caveat worth stating:* in genres where autotune is a *stylistic feature* — much of Afrobeats, all of trap and drill — excluding it entirely will make the track read as dated rather than human. §8 and §13 flag this per genre. Autotune is not automatically the enemy; **unintentional** autotune is.

---

**5. Instrumental sameness — plausible but characterless backing.**

*Fix:* name **specific** instruments rather than sections. `fingerpicked nylon-string guitar` beats `guitar`. `brushed snare` beats `drums`. Three named instruments outperform seven generic ones.
*Fix:* add a performance descriptor — `loose timing`, `live band feel`, `slightly behind the beat`, `played not programmed`.

---

**6. Emotional flatness — technically correct, expressively empty.**

*Fix, in the style box:* name the emotion *and its physical correlate*. `grieving` is weak; `grieving, voice catching, holding back tears` gives the model something to render.
*Fix, in the lyric box:* specificity in the words. A lyric with a concrete image produces a more committed vocal than a lyric of abstractions. This is not mysticism — the model conditions on the text it is singing.
*Fix:* stage a moment of restraint. A held-back verse makes the released chorus land.

---

**The compressed version — a checklist to run against every vocal-forward prompt:**

```
□ Vocal type, texture, and accent explicitly named
□ Vocal mix position stated (forward / dry / close)
□ Arrangement sparseness stated
□ Dynamic range requested AND scheduled with section tags
□ At least one imperfection descriptor present
□ Breath cue present (style box or lyric spacing)
□ Autotune excluded — unless the genre requires it
□ Instruments named specifically, 3-5 maximum
□ Emotion named with a physical correlate
□ BPM stated as a number
```

---

## 7. A cappella and voice-only tracks (and stems as fallback)

### 7.1 The honest position first

**True a cappella is the least reliable thing you can ask Suno to do.** This is well-documented in community reporting: even with explicit prompts like `a cappella` or `only vocal`, results frequently contain residual instrumentation, pads, or background tone. Nothing in v5 or v5.5's release notes claims to have fixed this.

Plan accordingly. **The professional workflow is a two-stage one** — generate a vocal-dominant track deliberately designed to stem-split cleanly, then extract the vocal — and it is described in §7.5. Direct a cappella generation (§7.2–7.4) is worth attempting first because when it lands it is better, but you should not build a deadline around it.

**Why it fails, mechanically.** The best available explanation from community analysis: **negative instructions are processed as soft hints, not hard constraints.** "No instruments" competes against a model whose entire training pushes it to generate melody, rhythm, and harmony together — and the training usually wins. Understanding this changes your strategy: **stop negating, and start describing a format that has no instruments in it.**

**The reframing technique — the most useful single idea in this section.** Instead of subtracting instruments from a song, ask for a *kind of recording* that inherently contains only a voice:

| Instead of | Ask for |
|---|---|
| `no instruments` | `isolated vocal take` |
| `a cappella, no backing` | `vocal-only demo`, `raw acoustic capture` |
| `just singing` | `field recording of unaccompanied singing` |
| `remove the band` | `solo voice memo, single microphone` |

These give the model a coherent target to hit rather than a prohibition to resist. Combine reframing *with* the Exclude field — they work on different mechanisms.

### 7.2 Direct generation — the prompt stack

Four controls have to agree, and most failed attempts are missing at least one:

**1. Style box.** Stack multiple redundant phrasings — redundancy is doing real work here:

```
A cappella, unaccompanied solo voice, no instruments whatsoever, pure vocal
performance, close-mic'd dry vocal, natural room, layered vocal harmonies only
```

**2. Exclude Styles.** Name the instruments, do not just negate abstractly:

```
drums, percussion, bass, guitar, piano, synth, strings, pads, beat,
instrumental, backing track, orchestration
```

**3. Lyric box.** Open with the tag and re-assert it at each section:

```
[A Cappella]
[Intro]
[Vocalize]
Mmm...

[Verse 1]
[A Cappella]
...
```

**4. Instrumental toggle: OFF.** Stated because getting this wrong is common — the toggle removes *vocals*, which is the opposite of your intent (§4.4).

### 7.3 Why direct a cappella fails, and what to do about each failure

| Failure | Cause | Fix |
|---|---|---|
| Faint pad or drone under the voice | Model treats "a cappella" as a *texture* rather than a constraint | Add `pads, drone, ambient texture, reverb wash` to Exclude; add `completely dry` to style |
| Percussion creeps in | Rhythmic lyric implies a groove | Add `no beat, no percussion, no rhythm section` to Exclude; slow the implied tempo |
| Starts a cappella, band enters at the chorus | Tag applied only at the top | **Re-assert `[A Cappella]` at every section header** |
| Voice sounds thin and exposed | No arrangement to hide behind | This is correct behaviour. Fix it with **layered harmony** (§7.6), not with instruments |
| Sounds like an isolated stem, not a performance | No room, no ensemble | Add `natural room ambience`, `choir in a small church`, `voices in one room` |

### 7.4 The a cappella style boxes, copy-paste

**Solo a cappella — intimate, singer-songwriter**

```
Solo a cappella, unaccompanied single female voice, no instruments, 72 BPM
implied, warm alto with audible breath and slight rasp, close-mic'd and dry,
small natural room, wide dynamic range, minimal compression, raw first-take
feel, occasional pitch imperfection
```
Exclude: `instruments, drums, bass, guitar, piano, synth, pads, reverb wash, autotune`

**Layered harmony a cappella — modern choral-pop**

```
Layered a cappella, stacked vocal harmonies, four-part arrangement, no
instruments, 88 BPM, lead voice plus three-part backing stack, warm blended
tone, close harmony, natural room, vocal bass line, breath audible between
phrases
```
Exclude: `instruments, synth choir, choir pad, orchestration, drums, bass guitar`

**Gospel choir stack**

```
A cappella gospel choir, full SATB stack with soloist, no instruments, 76 BPM,
powerful belted lead over rich harmony, hand claps only, church room ambience,
call and response, tight harmonic movement, wide dynamics from hush to full
voice
```
Exclude: `organ, piano, drums, bass, synth choir, choir pad, orchestral strings`
> Note: `hand claps only` is a deliberate, controlled exception — a single percussive element that is idiomatically vocal-adjacent and will not read as a band.

**Vocal percussion / beatbox-driven**

```
A cappella with vocal percussion, beatboxed rhythm section, no instruments,
100 BPM, lead vocal over mouth-drum groove, vocal bass line, layered harmony
stabs, tight and dry, close-mic'd, contemporary a cappella group
```
Exclude: `drums, drum machine, real percussion, bass guitar, synth`

**Traditional / chant — unmetered**

```
Unaccompanied traditional chant, solo voice with group response, no
instruments, free rhythm no fixed tempo, call and response, open-throated
natural singing, outdoor ambience, ululation, no vibrato, modal melody
```
Exclude: `instruments, drums, harmony pad, western harmony, autotune, reverb`

### 7.5 Stems as the fallback — the workflow that actually ships

When direct generation will not behave, invert the problem: **generate a track engineered to split cleanly, then split it.**

**Step 1 — generate on v5.5.** Non-negotiable. v5.5 is the only version with an official claim to improved **instrument separation**, and separation quality at generation time determines stem quality at extraction time.

**Step 2 — write the style box for separability, not for a mix you like.** You are making a *source*, not a record:

```
Vocal-forward acoustic soul, 84 BPM, single fingerpicked nylon guitar only,
sparse arrangement, warm male tenor with breath and rasp, lead vocal loud dry
and close-mic'd at the front of the mix, minimal reverb, wide dynamic range,
clean separation between voice and guitar
```
Exclude: `pads, synth, strings, reverb wash, double-tracked vocals, heavy compression`

Four choices there are all in service of the split:
- **One instrument, not five.** Every additional instrument is more spectral overlap with the voice.
- **Minimal reverb.** Reverb tails smear across the split and are the main source of the watery artefacts in extracted vocals.
- **No double-tracking.** Doubled vocals confuse separation.
- **Loud, dry, forward vocal.** Higher vocal-to-instrument ratio, cleaner extraction.

**Step 3 — extract.** Three documented paths, in order of preference:

| Path | Tool | Notes |
|---|---|---|
| Dedicated vocal extraction | `suno_extract_vocals` — **OFFICIAL (MCP)** | Purpose-built for vocals only. First choice. |
| Two-way split | `suno_stems_music`, or **Get Stems** in the web UI's Edit menu | Vocal + instrumental. ~10 credits (**COMMUNITY**) |
| Full multi-stem | `suno_all_stems_music` | Vocals, bass, drums, etc. ~50 credits (**COMMUNITY**). Use when you also want the backing parts |

**OFFICIAL:** Suno's 2026 stems improvements are described as producing stems that are "cleaner, crisper, free from artifacts," accessible via **Get Stems** in the Edit menu.

**Step 3b — clean up residual bleed with UVR if needed.** **COMMUNITY**, near-universal: **Ultimate Vocal Remover (UVR)** is the free tool the community reaches for when Suno's own extraction leaves instrumental bleed. Run the Suno-extracted vocal through UVR as a second pass. It is consistently named across independent sources as the go-to.

**Step 4 — repair in your DAW.** An extracted vocal usually needs: a high-pass around 80–100 Hz to remove bleed, gentle de-essing, and a light transient-shaping pass. Do not over-clean it — the artefacts you are chasing are less audible than the lifelessness that aggressive restoration creates.

> **One note on how Advanced Split works.** Community analysis of the 2026 stem improvements suggests Advanced Split **regenerates** parts via frequency analysis rather than simply cutting the finished mix apart. If accurate — and this is **COMMUNITY**, not documented by Suno — it explains both why the stems sound cleaner than a conventional split and why they are sometimes subtly different from what you heard in the mix. Check the extracted vocal against the original before you build on it.

**Step 5 — optional: rebuild underneath it.** With a clean vocal, **`suno_underpainting`** (**OFFICIAL (MCP)** — "add AI-generated accompaniment to uploaded vocal audio") lets you upload it and have Suno build a new arrangement beneath. This is the strongest quality path on the whole platform for vocal-forward work, because the vocal is fixed and known-good before any arranging happens.

### 7.6 Multiple voices — harmony, backing, duets, choirs

Four distinct problems, four distinct techniques.

**Harmony stacks.** Ask in the style box, and ask in intervals: `three-part close harmony`, `stacked thirds and fifths`, `SATB four-part harmony`, `octave doubling`. The tag `[Harmony]` supports this but does not substitute for it.

*The thin-harmony fix:* thin harmonies are usually a **synth pad standing in for voices**. Put `synth choir, choir pad, vocal synth, ahh pad` in Exclude and specify `stacked human voices, individually recorded, slight timing variation between parts`. That last phrase — asking for imperfect alignment — is what makes a stack sound like people rather than a chord.

**Backing vocals.** Parentheses in the lyric box, per §5.5. More reliable than any tag:

```
[Chorus]
Carry me home (carry me, carry me)
Before the morning comes (before the morning)
```

**Duets.** The most fragile of the four. Suno has no reliable way to assign parts. What community reporting supports:

```
[Verse 1]
(male vocal)
I never said I'd wait

[Verse 2]
(female vocal)
And I never asked you to

[Chorus]
(both, harmony)
So we let the winter take it
```
Combine with a style box that names both voices: `duet, male tenor and female alto trading verses, distinct voices, harmonised chorus`. **Expect to re-roll.** If part assignment matters, the reliable route is two separate generations — one per voice — combined in your DAW.

**Choirs.** State the ensemble concretely: `gospel choir, twenty voices, SATB, church room` beats `choir`. Always exclude `synth choir, choir pad`. For call-and-response, write it as an actual exchange:

```
[Call and Response]
Lead: Who will carry the water
Choir: We will carry the water
Lead: Who will carry the fire
Choir: We will carry the fire
```
**COMMUNITY**, and the `Lead:` / `Choir:` prefixes are reported as sometimes sung — if that happens, strip them and rely on line alternation plus the tag.

**Vocal percussion, humming, chanting.** The least reliable tag class on the platform. `[Beatbox]`, `[Humming]`, `[Vocalize]`, `[Ululation]` all shift output but frequently do nothing. Reinforce every one of them in the style box (`beatboxed rhythm section`, `wordless humming`, `ululation`) and write the sound into the lyric where you can — `mmm mmm mmm`, `oh-oh-oh-oh`, `boots and cats`, `lu-lu-lu-lu-lu` — since **written syllables are more reliable than tags asking for those syllables.**

### 7.7 Realistic vocal phrasing — the technique index

Cross-reference to §6.7, which covers the *why*. This is the *how*, per technique.

| Effect | Style box | Lyric box | Reliability |
|---|---|---|---|
| **Breaths** | `audible breaths`, `close-mic'd intimate` | Short lines; gaps between phrases | Good via style; `[Breath]` tag unreliable |
| **Runs / melisma** | `melismatic`, `gospel runs`, `ornamented` | Hold a vowel: `oh-oh-oh-ohh`; `[Vocal Run]` | Moderate |
| **Vibrato** | `natural vibrato`, `sustained notes with vibrato` | Long held vowels at line ends | Moderate |
| **Belting** | `powerful belted chorus`, `full-voice` | `[Belted]` at section head; ALL CAPS | Good |
| **Falsetto** | `falsetto`, `head voice`, `high register` | `[Falsetto]` at section head | Good |
| **Whispers** | `whispered intimate delivery` | `[Whispered]`; lower-case, short lines | Good |
| **Ad-libs** | `ad-libs and vocal fills` | Parentheses: `(yeah)`, `(come on)` | Very good via parentheses |
| **Dynamics** | `wide dynamic range`, `minimal compression` | Schedule with section tags | Good — see §6.7 item 2 |
| **Emotional delivery** | Emotion + physical correlate | Concrete, specific imagery | Good |
| **Rasp / grit** | `raspy`, `gritty`, `smoky`, `weathered` | — | Very good |
| **Spoken passages** | `spoken word section` | `[Spoken Word]`; write as prose, no rhyme | Good |

### 7.8 Vocal failure-mode troubleshooting

| Symptom | Most likely cause | Fix, in order |
|---|---|---|
| **Mumbled diction** | Too many syllables per line; tempo too high for the lyric | 1. Cut syllables. 2. Lower BPM. 3. Add `clear diction, articulate` to style. 4. Shorten lines. |
| **Wrong accent** | Accent not specified, or contradicted by genre default | 1. Name the accent explicitly. 2. **Phonetically respell key words** (§5.6). 3. Add a regional marker to the genre stack (`contemporary Lagos`, not just `Afrobeats`). 4. Use a Persona captured from a take with the right accent (§9). |
| **Thin harmonies** | Synth pad substituting for voices | 1. Exclude `synth choir, choir pad, vocal synth`. 2. Specify part count and intervals. 3. Add `slight timing variation between parts`. |
| **Autotuned tone** | Genre default | 1. Exclude `autotune, pitch correction, vocoder`. 2. Add `natural pitch, unprocessed`. 3. Add `raw take, slight imperfection`. 4. If the genre implies autotune, accept it or change genre. |
| **Pitch drift over long songs** | Long generation, weak harmonic anchor | 1. Shorten the generation and **Extend** instead of generating 8 minutes at once. 2. Name a key in the style box. 3. Add a sustained harmonic instrument — a hard trade-off against a cappella, which is part of why long a cappella is difficult. |
| **Robotic tone** | Every item in §6.7 at once | Run the §6.7 checklist. |
| **Voice changes between sections** | Long generation, no identity anchor | 1. Use a **Persona** (§9). 2. Shorten segments and Extend. 3. Keep the vocal description identical across every related generation. |
| **Genre drift mid-song** | Style box overloaded or internally contradictory | 1. Cut the style box to its three strongest terms. 2. Remove contradictions (`sparse` + `wall of sound`). 3. Re-assert genre in the lyric box **only** as a last resort — it violates §5.3 and may be sung. |
| **Muddy mix** | Too many instruments in the 200–500 Hz range | 1. Cut instrument count to 3–4. 2. Add `clean separation, clear midrange, uncluttered arrangement`. 3. Exclude `wall of sound, dense arrangement, heavy layering`. |
| **Abrupt ending** | Duration ceiling hit | §5.8: explicit `[Outro]`, `[Fade Out]`, and target under the ceiling. |

---

## 8. Authentic Afrobeats and African vocal-forward styles

### 8.1 The core problem this section solves

Prompting `Afrobeats` alone returns **generic tropical pop**: a marimba-ish synth, a four-on-the-floor-adjacent kick, and an accent-free voice. It is recognisably nothing. Everything in this section is aimed at the gap between that and a track that a Lagos or Johannesburg listener would accept.

Four levers close that gap, and they work in this order of impact:

1. **Region and city, not just genre.** `contemporary Lagos Afrobeats` and `Accra highlife-pop` produce materially different output from `Afrobeats`. Geography is the highest-leverage single token in African style prompting, and it is the strongest consensus finding in the community corpus. Generic `African music`, `tropical`, or `world music` tags produce what one source aptly called *djembe over a generic pop structure that sounds like a tourism ad*.
2. **Named indigenous instruments — the specific one, not the category.** `log drum` ≠ `kick`. `talking drum` ≠ `percussion`. `palm-wine guitar` ≠ `guitar`. This is the highest-leverage authenticity move after region.
3. **Accent, stated explicitly.** `Nigerian English accent`, `Ghanaian English accent`, `South African accent`, `Nigerian Pidgin delivery`.
4. **Language handled phonetically** (§5.6, §8.5).

**Which African instruments Suno actually reproduces reliably.** This distinction is worth having before you write a template:

| Reliability | Instruments |
|---|---|
| **Reported most reliable** | **talking drum**, **djembe** — named explicitly as the two most dependably reproduced |
| **Reported working** | log drum, shekere, kora, mbira / kalimba, balafon, dundun, congas |
| **NOT confirmed** | **agogo, gyil, udu** — no source found confirms Suno reproduces these reliably. Treat them as a risk, not an assumption. If you want a gyil sound, describe it (`wooden xylophone with buzzing resonators`) rather than naming it |

**And name only two or three.** Over-listing percussion muddies the result rather than enriching it — this is the same dilution principle as §6.1, and it bites hardest in exactly the genres people most want to load up with percussion.

**One tempo rule specific to this section:** give a **single BPM number, not a range**. Suno picks unpredictably from a stated range. `107 BPM` steers; `100-115 BPM` does not.

### 8.2 One correction before the templates

There is a naming confusion worth being precise about, because it affects what you get.

**Afrobeat** (no *s*) — singular — is Fela Kuti's genre: long-form, horn-driven, polyrhythmic, politically declamatory, typically 8–15 minutes, built on a repeating groove with extended instrumental sections.

**Afrobeats** (with *s*) — plural — is the contemporary West African pop genre: Burna Boy, Wizkid, Rema, Tems. Song-length, hook-driven, mid-tempo, sparse.

They are not the same music and Suno responds to them differently. **Use `Afrobeats` for contemporary pop and `Afrobeat` (or `Afrobeat, Fela Kuti style horn-driven`) for the 1970s genre.** Getting this wrong is the most common single error in African prompting.

### 8.3 BPM — the reference table

Tempo is where authenticity is won or lost, and it is the most frequently mis-stated parameter in circulating prompt libraries. Community prompt guides commonly quote "Afrobeats 90–110 BPM"; the genre's actual centre of gravity is higher. Both framings appear below so you can hear the difference yourself.

| Genre | Working BPM | Pick this number | Notes |
|---|---|---|---|
| **Afrobeats / Afropop** | 95–115 | **107** | Modern sweet spot reported as 100–110. Guides quoting 90–110 are aiming low; the bottom of that range reads as sluggish |
| **Afro-fusion** | 95–110 | **98** | Slower, more spacious than mainstream Afrobeats |
| **Amapiano** | **108–115** | **112** | Remarkably narrow, and 112 is the near-universally cited centre. Do not stray |
| **Afro-house** | 118–126 | **122** | |
| **Highlife** | **105–118** | **112** | Sub-split: traditional guitar-band ~105–110; modern Afropop-influenced ~112–118 |
| **Afro-soul** | 80–100 | **88** | |
| **Afro-gospel** | 90–100 worship / higher for praise | **96** worship | Broader gospel range is 68–118 depending on ballad vs up-tempo. **An authoritative BPM for up-tempo Afro-gospel specifically could not be found — treat 120–130 as a working guess, not a sourced figure** |
| **Afrobeat (Fela)** | 100–120 | **112** | Feel is driven by polyrhythm, not tempo |
| **Coupé-décalé** | 120–135 | **128** | Ivorian; relevant to your existing persona |
| **Traditional / choral** | Often unmetered | — | Use `free rhythm, no fixed tempo` |

### 8.4 The style boxes

**Afrobeats — Nigerian, contemporary**

```
Contemporary Nigerian Afrobeats, Lagos sound, 107 BPM, log drum bass,
talking drum accents, shekere, syncopated shaker pattern, clipped kick,
melodic guitar highlife lick. Smooth male tenor, laid-back behind-the-beat
phrasing, Nigerian English and Pidgin, light rhythmic ad-libs. Vocal forward,
warm, subtle autotune as texture. Spacious modern mix, deep sub-bass.
```
Exclude: `generic tropical house, EDM drop, marimba synth, four-on-the-floor`

> The `subtle autotune as texture` is deliberate and it is the §6.7 caveat in action. Afrobeats vocals are *conventionally* lightly tuned; stripping it entirely reads as folk, not as Afrobeats. Tune-as-texture is authentic; tune-as-correction is the problem.

**Afrobeats — Ghanaian**

```
Ghanaian Afrobeats with highlife DNA, Accra sound, 104 BPM, palm-wine guitar
lick, talking drum, shaker, warm rounded bass. Male lead with Ghanaian English
and Twi phrases, melodic conversational delivery, group response vocals on the
hook. Vocal-forward, warm analog mix.
```
Exclude: `EDM, generic tropical pop`

> Ghanaian Afrobeats is **more melodic and more guitar-led** than Nigerian; the highlife lineage is audible in it. **`palm-wine guitar` is the signature and must be named** — generic `guitar` under-specifies badly here and will return a neutral pop lick. Note that this template deliberately omits `gyil` despite its being idiomatic to Ghanaian music: it is in the unconfirmed-instrument list above. If you want it, describe it rather than name it.

**Amapiano — South African**

```
South African Amapiano, Johannesburg sound, 112 BPM, deep log drum groove,
jazzy Rhodes piano chords, sub-heavy bass, shaker and rim percussion, airy
pads. Soulful female vocal with Zulu and English, spoken ad-libs and
conversational interjections, layered vocal chants. Vocal present but sitting
in the groove. Wide spacious mix, long percussive builds.
```
Exclude: `fast tempo, EDM drop, aggressive drums, four-on-the-floor house kick`

> **The single most-reported mistake in Amapiano prompting, near-verbatim across independent sources: writing "kick drum" instead of naming "log drum."** Say `kick` and Suno gives you a standard four-on-the-floor kick. The log drum is a *distinct, pitched, sliding* element and it is the genre. Always name it explicitly, and ask for glide and swing so it bounces rather than thuds.
>
> Three things make Amapiano read as Amapiano rather than as deep house: the **log drum**, the **112 BPM lock**, and the **spoken ad-lib layer** — conversational interjections riding over the sung vocal. Ask for all three by name. Extended jazz voicings (maj9, 13) on the piano are the fourth thing, and they are what separate Amapiano from Afro-house.

**Afro-fusion**

```
Afro-fusion, contemporary West African, 98 BPM, blend of Afrobeats percussion
with R&B chord movement, live bass, muted guitar, talking drum, atmospheric
pads. Warm husky male vocal, melodic and unhurried, Nigerian English with
melismatic runs, doubled hook. Vocal-forward, intimate, wide dynamic range.
```
Exclude: `hard EDM, dense percussion, autotune-heavy, generic pop`

**Afro-soul**

```
Afro-soul, 88 BPM, fingerpicked nylon guitar, upright bass, brushed kit, hand
percussion, subtle kora arpeggio. Rich alto female voice, warm with slight
rasp, gospel-inflected runs, Yoruba and English, audible breath. Lead vocal
loud dry and close-mic'd, sparse arrangement, analog warmth, minimal
compression, wide dynamics.
```
Exclude: `autotune, pitch correction, synth pad, heavy drums, dense arrangement`

> This is the strongest African template for **vocal-forward** work specifically. Sparse arrangement, dry forward vocal, acoustic instrumentation, no tuning — every §6.3 lever is engaged.

**Highlife — classic**

```
Classic Ghanaian highlife, 1970s, 112 BPM, interlocking clean electric guitar
lines, horn section stabs, congas and cowbell, walking bass, brass swells.
Warm male lead with call-and-response group chorus, Twi and English,
conversational storytelling delivery. Live band feel, slightly behind the
beat, analog tape warmth, room mics.
```
Exclude: `modern production, autotune, programmed drums, synth bass`

> `live band feel, slightly behind the beat, room mics` is doing the heavy lifting. Highlife dies when it is quantised.

**Afro-gospel**

```
Afro-gospel praise, contemporary Nigerian, 128 BPM, driving talking drum and
congas, bright organ, bass guitar, brass stabs, hand claps. Powerful belted
female lead over full SATB choir, call and response, Yoruba and English,
gospel runs and shouts, ululation on the peaks. Lead vocal forward over rich
live choir, church room ambience, wide dynamics from hush to full voice.
```
Exclude: `synth choir, choir pad, autotune, programmed drums, thin mix`

**Traditional / choral African vocal**

```
Traditional West African choral singing, unaccompanied, free rhythm no fixed
tempo, call and response between lead and group, polyrhythmic handclaps only,
open-throated natural chest voice, ululation, dense overlapping vocal layers,
outdoor communal ambience, modal melody, no western harmony, no vibrato.
```
Exclude: `instruments, piano, drums, synth choir, choir pad, western four-part harmony, reverb wash, autotune`

> `no western harmony` and `no vibrato` are the two most important terms. Suno's default choral behaviour is Western SATB with vibrato; both are wrong for most traditional African vocal music, which is built on parallel motion, overlapping call-and-response entries, and a straighter tone.

**Coupé-décalé × Afrobeats** — matched to the persona already in your account (§1.5)

```
Coupé-décalé meets Afrobeats, Abidjan sound, 128 BPM, driving atalaku
percussion, log drum, brass stabs, sliding synth bass, handclaps. Charismatic
gritty-warm male chant-leader in French with West African accent, gang-vocal
call and response, festive triumphant energy, spoken shout-outs. Vocal loud
and forward over the crowd, live party ambience, punchy mix.
```
Exclude: `slow tempo, sparse arrangement, autotune-heavy, ambient pads`

### 8.5 Language and lyric handling

Suno handles African languages inconsistently, and how you write them matters more than which one you pick.

| Language | Behaviour | Handling |
|---|---|---|
| **English** | Reliable | Specify the **accent**, or you get neutral international English |
| **Yoruba** | **Among the best-supported** African languages | **Strip tone marks, respell phonetically.** `ee-MOH-leh` not `ìmọ́lẹ̀` |
| **Swahili** | **Among the best-supported** | Standard orthography often works; respell anything mangled |
| **Zulu** | **Among the best-supported** | Respell phonetically. Click consonants are unreliable — avoid or substitute |
| **Nigerian Pidgin** | Works well **mixed with English**; standalone reliability unconfirmed | Write it naturally (`I no fit lie`, `abeg`, `wetin dey`). Add `Nigerian Pidgin delivery` to the style box. Note that broader research on generative models flags Naija Pidgin as underrepresented in training data — treat as an inferred risk, not a tested Suno finding |
| **Twi** | Works mixed with English; standalone reliability unconfirmed | Respell phonetically; keep phrases short; anchor with English around them |
| **French (West African)** | Good | Specify `West African French accent` — default is metropolitan French |

**Yoruba, Swahili, and Zulu are repeatedly named as the African languages with the most Suno training data and the best reliability.** If you have a choice of language for a hook, those three are the safest bets.

**One technique that outperforms either half alone:** write the lyrics **directly in the target language** in Custom Mode *and separately* name the language in the style box (`singing in Yoruba`). The combination is reported as more reliable than doing either on its own.

**Code-mixing works well.** Mixing English and an African language within one song is explicitly reported to work — which is fortunate, since it is how these genres are actually written.

**The five working rules for multilingual African lyrics:**

1. **Anchor in one language, garnish with the other.** A verse in English with a Yoruba hook works far better than alternating languages line by line. The model's pronunciation stability degrades sharply at every switch.
2. **Phonetically respell every non-English word** (§5.6). Hyphenate syllables, capitalise stress, strip diacritics.
3. **Repeat the non-English phrase.** A Yoruba hook sung four times will be pronounced better on the later passes than a phrase appearing once — and repetition is idiomatic in these genres anyway.
4. **Keep non-English lines short.** Four to six syllables. Long phrases in a weakly-supported language are where diction collapses.
5. **Maintain two lyric documents.** The Suno script (phonetic, for the machine) and the published lyric (correct orthography, with tone marks, for humans). Do not let the phonetic version escape into your release metadata — in these traditions the written language carries cultural weight and mangled orthography reads as carelessness.

**Worked example — Yoruba hook in an Afro-soul track:**

```
[Chorus]
ee-MOH-leh deh, ee-MOH-leh deh
(light has come, light has come)
ee-MOH-leh deh, oh-oh
ah-way ah-way, ee-MOH-leh deh
```
Published as: `Ìmọ́lẹ̀ dé, ìmọ́lẹ̀ dé / Ìmọ́lẹ̀ dé, oh-oh / Àwa, àwa, ìmọ́lẹ̀ dé`

Note the parenthesised English translation on line 2 — it will be rendered as a **backing vocal** (§5.5), which is both a practical translation device and an idiomatic gospel/Afro-soul arrangement move.

### 8.6 Keeping the delivery rhythmically natural

The tell that separates authentic African vocal delivery from a Western pop vocal over African percussion is **where the voice sits against the beat**.

| Style | Vocal placement | Style-box phrasing |
|---|---|---|
| Afrobeats | **Behind the beat** — laid-back, unhurried | `laid-back behind-the-beat phrasing`, `relaxed unhurried delivery` |
| Amapiano | **In the pocket**, conversational, half-spoken | `conversational half-spoken delivery`, `sitting in the groove` |
| Highlife | **On top of the beat**, buoyant | `buoyant forward-leaning delivery` |
| Afro-gospel | **Rhythmically aggressive**, percussive attack | `percussive rhythmic delivery`, `punching the downbeats` |
| Traditional | **Free against the pulse** | `free rhythmic phrasing over steady pulse` |
| Coupé-décalé | **Ahead, urgent**, shouted | `urgent shouted chant-leader delivery` |

**Two structural habits that matter as much as any descriptor:**

- **Write call-and-response into the lyric, do not just tag it.** Communal response is structural in most of these traditions, not decorative. §7.6 has the format.
- **Leave space.** Afrobeats and Amapiano arrangements are *sparse*. The single most common way Western-authored African prompts fail is over-instrumentation — six percussion elements where the real records use three. Name **three to five** instruments and stop.

### 8.7 Authentic versus generic — the diagnostic

Play your output against this list. If two or more are true, it is generic:

```
□ You could not name the city or country from the sound alone
□ The vocal has no identifiable accent
□ The percussion is a generic shaker loop with no talking drum, log drum, or hand drum
□ The groove is straight rather than syncopated
□ The vocal sits dead on the grid rather than behind or around it
□ There is no call-and-response anywhere in the arrangement
□ Every instrument enters at bar 1 and never leaves
□ The tempo is outside the reference range in §8.3
□ It would work equally well as a generic summer pop record
```

---

## 9. Creating and applying a Persona for a consistent singer

### 9.1 What a Persona actually is

**OFFICIAL** — <https://help.suno.com/en/articles/3484161>: a Persona captures the **"essence"** of a song — its vocals, style, and vibe — for reuse in new generations. Created from an existing song via the **"…" menu → Create → Make a Persona**. There is a **Public/Private toggle**; Public Personas can be used by others and link back to your profile.

**The mechanical detail that changes how you use it** comes from the MCP's own persona object (§1.5): a persona is anchored to a **`source_audio_id`**. It is a reference to *one specific rendered clip*, not a text description the model interprets. The `description` field is a label for you.

Three consequences, and they are the whole discipline of this section:

1. **Persona quality is capped by seed quality.** A persona made from a mediocre vocal will reproduce a mediocre vocal indefinitely. There is no prompt that rescues a bad seed.
2. **A persona carries more than the voice.** It captures style and vibe too. This is useful for album cohesion and a nuisance when you want the same singer over a different genre — see §9.5.
3. **You cannot edit a persona.** You can only make a new one from a better seed. Treat seed selection as the high-stakes step it is.

**Where to find it in the v5.5 UI:** the **Voices** button replaced Personas in the Create menu; **Style Personas live inside the Voices menu** (§1.8).

### 9.2 Seeding a persona properly

This is the highest-leverage twenty minutes in any album project. Do not rush it.

**Step 1 — write a seed-specific style box.** You are not making a song; you are making a *voice specimen*. Optimise for vocal clarity, not for a great arrangement:

```
Afro-soul, 88 BPM, sparse arrangement, single fingerpicked nylon guitar and
light hand percussion only. Warm male tenor, slight rasp, Nigerian English
accent, audible breath, conversational phrasing with gospel-inflected runs.
Lead vocal loud, dry, close-mic'd, front of mix. Minimal compression, wide
dynamic range, raw first-take feel.
```
Exclude: `autotune, pitch correction, dense arrangement, synth pad, heavy reverb, double-tracked vocals`

Why sparse: the persona is captured from the audio, so **anything crowding the voice in the seed gets captured with it.**

**Step 2 — write seed lyrics that exercise the full range.** Your seed should contain every delivery you will need later. A seed that only ever sings mid-range, mid-volume gives you a persona that only does that.

```
[Verse 1]
[Whispered]
I came in from the rain
Nobody heard the door

[Chorus]
[Belted]
BUT I AM STILL HERE
Still standing in the doorway

[Bridge]
[Falsetto]
Ohh-oh, oh-oh
(still here, still here)

[Outro]
[Spoken Word]
And that was the whole of it.
```

**Step 3 — generate 6–10 takes.** More than feels necessary. You are auditioning a singer, and you will use this voice on every track you make for months.

**Step 4 — select on voice alone.** Ignore the arrangement entirely. Ask only: is this a person I would want to hear sing twelve songs? Judge timbre, accent accuracy, breath, and whether the belted section actually belts.

**Step 5 — capture, and name it descriptively.** Follow the convention already in your account: genre, register, texture, language, accent, delivery character, and intended use, all in the description field. The existing `DigiDjo Lead Voice v1` entry is a good model for this — it names the texture, the language, the accent, the phrasing style, the energy, and the project it belongs to.

**Step 6 — version it.** `v1`, `v2`. When you re-seed a better take in three months you want to know which tracks used which voice.

### 9.3 Applying a persona

Select the persona in the Create menu, then write your style box **omitting everything the persona already carries**. This is the part people get wrong: a persona plus a full vocal description means two sources of truth competing, and the result is usually worse than either alone.

| Slot | With a persona applied |
|---|---|
| Genre stack | **Keep** — you may want a different genre |
| BPM | **Keep** |
| Instrumentation | **Keep** |
| Vocal type / texture / accent | **Drop** — the persona carries it |
| Vocal mix position | **Keep** — mix placement is not part of vocal identity |
| Production / era | **Keep** |

A persona-applied style box, 141 characters:

```
Afro-soul with gospel harmony, 92 BPM, fingerpicked nylon guitar, upright
bass, hand percussion. Lead vocal forward and dry. Analog warmth.
```

Note what is absent: no voice description at all. The persona is doing that job.

### 9.4 Personas vs Voices vs Custom Models

Three overlapping tools; choosing wrong wastes real time.

| | **Persona** | **Voices** (v5.5) | **Custom Model** (v5.5) |
|---|---|---|---|
| Source | One Suno-generated clip | **Your own recorded voice**, identity-verified by singing a randomised phrase | **≥6 tracks** from your catalogue |
| Captures | Vocal + style + vibe | Your actual vocal identity | Your whole sonic signature — arrangement and production too |
| Best for | A **synthetic character** singer, consistent across a project | Releasing music **in your own voice** | **Album-wide cohesion** beyond the voice |
| Limit | Capped by seed quality | Requires you to be able to sing it | Up to **3** models; they stay private |
| Availability | All paid tiers | v5.5 | Pro / Premier |

**Choosing, in one line each:**
- The singer should be **you** → **Voices**.
- The singer is **a character** you invented → **Persona**.
- You want the whole *record* to sound like your catalogue, not just the voice → **Custom Model**, layered on top of either of the above.

### 9.5 Persona limitations you will hit

- **Genre bleed.** Because a persona captures style as well as voice, using an Afro-soul persona on a drill track will drag the arrangement toward Afro-soul. **Mitigation:** seed personas on the *sparsest, most genre-neutral* arrangement you can — the acoustic seed in §9.2 travels much better than a fully-produced one would.
- **Consistency is strong, not absolute.** Personas reduce drift; they do not eliminate it. Long generations still wander. **Mitigation:** shorter generations plus Extend (§10.2).
- **`suno_generate_with_persona_vox`** — the MCP documents a distinct **"VOX consistency mode"** for persona generation. **What it does differently is not documented anywhere and could not be confirmed — UNCONFIRMED.** If album-wide vocal consistency is your central problem, this is the single most worthwhile undocumented feature to test empirically; the name suggests exactly the tool you want.
- **No editing.** Re-seed, do not repair.

---

## 10. Editing — Extend, Replace Section, Crop, stems

### 10.1 The operation map

| Operation | What it does | Official reference |
|---|---|---|
| **Extend** | Continue a song from a chosen point via a drag-selectable window | <https://help.suno.com/en/articles/2409601> |
| **Replace Section** | Add, remove, or change **middle** sections and their lyrics. **Pro/Premier** | <https://help.suno.com/en/articles/3271873> |
| **Crop** | Trim the **start or end** of a song; adjust displayed lyrics. **Pro/Premier** | <https://help.suno.com/en/articles/3166529> |
| **Song Editor** | Reorder, rewrite, and remake sections directly from the waveform | <https://help.suno.com/en/articles/6141505> |
| **Stem separation** | Auto Split (≤12 stems, 50cr) · Split from Mix (single stem, 10cr) · Advanced Split (Premier, ~100 types, 10cr) | <https://help.suno.com/en/articles/12702337> |
| **Remaster** | Improve audio quality, rebalance mix, sharpen vocal clarity — **without** changing structure, lyrics, or performance | <https://help.suno.com/en/articles/8105281>, <https://help.suno.com/en/articles/3591617> |
| **Cover** | Transform the style of a song while preserving its melody. **Beta, Pro/Premier** | <https://help.suno.com/en/articles/2872257> |
| **Audio Upload** | Bring external audio in as a generation input | <https://help.suno.com/en/articles/2477633>, <https://help.suno.com/en/articles/6141569> |

> **Terminology correction.** The brief refers to "Replace Section / Inpainting." **Suno's own documentation calls this "Replace Section" and never uses the word "inpainting."** Inpainting is the community/press analogy borrowed from image models. Use Suno's term when searching their docs or you will find nothing.

### 10.2 Extend

Extend continues from a point you select. Two uses:

**Building past the ceiling.** Generate 3 minutes, Extend twice, then merge — `suno_concat_music` (**OFFICIAL (MCP)**) merges extended segments into one continuous file.

**Fixing an abrupt ending** (§5.8). Extend from just before the cut-off with an `[Outro]` in the lyric box, then **Crop** back to where you want it to land. Extend-then-Crop is the standard repair and it is more reliable than re-rolling the whole song.

**The single most important rule about Extend, and the most-repeated piece of advice in the entire community corpus:**

> **Suno does not remember your previous generation. Every Extend is a fresh instruction.**

If you Extend with an empty or abbreviated style box, the model has no idea what the first three minutes sounded like. This is the root cause of nearly all reported genre drift — the section that suddenly changes key, tempo, instrumentation, or singer halfway through a track.

**What to do, every single time:**

```
□ Paste the FULL original style string into every extension — verbatim, not paraphrased
□ Keep the BPM number in every extension
□ Keep the vocal descriptors in every extension
□ Apply the Persona to every extension
□ Review each segment BEFORE extending again — do not chain blind
```

**On vocal consistency across Extends** specifically: because each pass is a fresh generation, **voice drift accumulates multiplicatively**. Persona on every pass plus a byte-identical style box is the only thing that holds it. Do not retype your style box between passes; copy it.

### 10.3 Replace Section

The precision tool. Highlight a section, edit its lyrics, hit **Recreate Section**, confirm — you get **two tagged outputs: "Section" and "Full Song."**

Use it for: one mumbled line, one flat chorus, one wrong-language verse, one weak bridge.

**The technique that makes it work for vocal repair:** when replacing a section for vocal reasons, **change the lyric slightly even if you liked it**. Re-rolling identical text tends to return a similar performance. Shortening the line by two syllables, or breaking it into two lines, changes the phrasing problem rather than re-rolling the same dice.

### 10.4 Crop

Trims the start or end and adjusts displayed lyrics. Cannot touch the middle — that is Replace Section. Its main jobs: removing the dead air or false start at the top, and landing the end after an Extend.

### 10.5 Stems — the three modes

**OFFICIAL** — <https://help.suno.com/en/articles/12702337>. Access via **Edit → Get Stems**. 2026 improvements are described as producing stems that are "cleaner, crisper, free from artifacts."

| Mode | Output | Cost | Tier | Use for |
|---|---|---|---|---|
| **Split from Mix** | A single stem — e.g. vocals only | **10 credits** | Pro+ | **A cappella extraction (§7.5).** Your default. |
| **Auto Split** | Up to **12 stems** | **50 credits** | Pro+ | Full remix work; when you want the backing parts too |
| **Advanced Split** | ~**100 instrument types** | **10 credits** per extraction | **Premier only** | Surgical isolation |

The MCP exposes equivalents: `suno_stems_music` (two-way), `suno_all_stems_music` (full), and **`suno_extract_vocals`** (vocals only).

**Stem quality is decided before you press the button.** Everything in §7.5 step 2 — one instrument, minimal reverb, no double-tracking, loud dry forward vocal, generated on v5.5 — determines what you get out. A dense, reverb-soaked mix will not split cleanly no matter which mode you pay for.

### 10.6 Covers, uploads, and the two painting operations

**Cover** — **OFFICIAL**, <https://help.suno.com/en/articles/2872257>. **Beta, Pro/Premier only.** Transforms the *style* of a song while **preserving its melody**. Works on your own songs, or others' if they enabled Remix. Always references the original source audio.

For vocal work, Cover is how you keep a melody and topline you like while changing everything around it — the fastest route to "same song, different genre" for a deluxe edition or a regional remix.

**Audio Upload** — **OFFICIAL**, <https://help.suno.com/en/articles/2477633> and <https://help.suno.com/en/articles/6141569>. Turns recorded or imported sound into music. **Note a documented inconsistency:** the two official articles give different length limits — one states 6–60 seconds free / up to 120 seconds Pro–Premier for a recorded clip; the other states up to 60 seconds free / **up to 8 minutes** Pro/Premier for a full song upload. These probably describe two different actions (record-a-clip vs upload-a-file), but **the discrepancy is real and unreconciled.** Check in-app before planning around a specific duration.

**The two highest-value operations on the platform for this discipline**, both **OFFICIAL (MCP)**:

| Operation | What it does | Why it matters |
|---|---|---|
| **`suno_underpainting`** | Add AI accompaniment **under uploaded vocal audio** | **Inverts the hard problem.** With a real or stem-extracted vocal, Suno is no longer being asked to sing convincingly — only to arrange. Arranging is something it is reliably good at. |
| **`suno_overpainting`** | Add AI vocals **over uploaded instrumental audio** | The mirror. Corresponds to v4.5+'s **Add Vocals**. |

**Underpainting deserves emphasis.** If you can sing at all, or if you can get one clean stem-extracted vocal you believe in, the underpainting route produces the most human-sounding results available on the platform — because the human part is actually human. Every technique in §6.7 is an attempt to *simulate* what underpainting lets you simply *supply*.

### 10.7 Remaster

**OFFICIAL** — <https://help.suno.com/en/articles/8105281>, <https://help.suno.com/en/articles/3591617>. Produces subtle sonic variations of an existing clip: improves overall sound quality, **rebalances the mix between instruments and vocals**, and can **sharpen vocal clarity and pronunciation** — **without** changing structure, lyrics, or performance.

Two things follow:

- **Remaster is a legitimate fix for mumbled diction** (§7.8) when the performance is otherwise good. It is the only operation that improves pronunciation without re-rolling the take.
- **Remaster can push the vocal forward** in an otherwise good track whose mix buries it. Worth trying before you re-generate.

**Deprecation note** (**OFFICIAL** — <https://help.suno.com/en/articles/7986753>): **Remaster v4 was deprecated for all users on 2025-09-11.**

### 10.8 The iteration workflow

The standard loop, in order:

```
1. GENERATE   — v5.5, Custom Mode, 6-10 takes on the seed idea
2. SELECT     — judge on vocal first; arrangement is fixable, voice is not
3. EXTEND     — build length in segments, persona applied to each
4. REPLACE    — surgically fix weak sections; alter the lyric slightly when you do
5. CROP       — trim the head, land the ending
6. REMASTER   — rebalance the mix, sharpen diction
7. STEM-SPLIT — extract what you need
8. FINISH     — master in your own DAW (§11)
```

**Two rules that save the most credits:**

- **Do not re-generate to fix something Replace Section can fix.** A full re-roll costs a generation and throws away everything that was working.
- **Do not Extend a take whose voice you are not sure about.** Fix identity first, then build length. Extending a drifting voice multiplies the drift.

---

## 11. Mastering, finalizing, exporting

### 11.1 Download formats

| Format | Availability | Use for |
|---|---|---|
| **MP3** | All tiers | Reference listening, sharing, social |
| **WAV** | **Pro/Premier only** (<https://help.suno.com/en/articles/2479873>). **Desktop web only** — mobile downloads default to MP3 | **Everything you will master, stem, or release** |
| **Stems** | Pro+ (Advanced Split: Premier) | Post-production, a cappella extraction |
| **MP4 video** | Available (<https://help.suno.com/en/articles/2409921>) | Social and streaming visualisers |
| **MIDI** | **Premier**, via Studio, 10 credits | Re-scoring, replacing parts with real instruments |

**Always download WAV, always on desktop.** Re-downloading is free; re-generating is not. An MP3 you later want to master is a mistake that costs a generation to undo.

### 11.2 What Suno's own tools can and cannot do

**Remaster** (§10.7) is Suno's only mastering-adjacent tool, and it is a *re-render*, not a mastering chain. It rebalances and cleans; it does not give you level control, EQ, or limiting.

**On Pro you finish outside Suno.** That is not a limitation to work around — it is the correct workflow for anything you intend to release.

### 11.3 A minimal finishing chain for vocal-forward material

Assumes WAV in, your own DAW, aimed at streaming.

```
1. HIGH-PASS      80-100 Hz on the full mix (or on the vocal stem, if split)
2. SUBTRACTIVE EQ Narrow cuts for resonances — Suno mixes commonly
                  build up around 200-400 Hz
3. DE-ESS         Gentle. Generated vocals often carry bright sibilance
4. COMPRESSION    Slow attack, low ratio (2:1), 2-3 dB gain reduction MAX.
                  You spent §6.7 asking for dynamics — do not now flatten them
5. SATURATION     Light tape or tube. Reintroduces the harmonic irregularity
                  that reads as "recorded"
6. LIMIT          -14 LUFS integrated for streaming; -1 dBTP ceiling
```

**Step 4 is the one people get wrong.** Heavy compression is exactly the flattening you spent your prompting effort avoiding. If your track needs heavy compression to feel loud, fix it at the arrangement stage.

**If you split stems, do the vocal work on the vocal stem, not on the mix.** De-essing a full mix damages the cymbals; compressing a full mix to control a vocal pumps the whole band. This is the practical payoff of §7.5 even when you never wanted an a cappella.

### 11.4 Release checklist

```
□ WAV downloaded from desktop web, not MP3, not mobile
□ Track generated while your paid subscription was active (§1.2 — rights are NOT retroactive)
□ Lyrics: publish the correct-orthography version, not the phonetic Suno script (§5.6)
□ Loudness: -14 LUFS integrated, -1 dBTP
□ Dynamic range preserved — check LRA is not flattened
□ Ending lands deliberately; no truncation (§5.8)
□ Title and metadata consistent with the album identity (§12)
□ Stems archived alongside the master — you will want them for edits and sync
```

---

## 12. Assembling a full album with one vocal identity

### 12.1 What "one identity" actually requires

Cohesion is four separate things, and personas only deliver one of them:

| Layer | Tool |
|---|---|
| **Vocal identity** | Persona, or Voices |
| **Sonic identity** | A locked style-box **core** reused verbatim across tracks (§12.3) |
| **Production identity** | Same model version, same mix language, same mastering chain |
| **Structural identity** | Recurring motifs, tempo family, key relationships |

An album where only the voice is consistent still sounds like a compilation. All four layers or none.

### 12.2 The album workflow, end to end

**Phase 1 — Identity (do this once, properly)**

1. Create a **Workspace** for the album (§2.3).
2. **Seed and capture the persona** per §9.2. Budget 6–10 generations. Do not proceed until the voice is right — everything downstream inherits it.
3. **Write the album style core** — the 100–150 characters that will appear in *every* track's style box, unchanged (§12.3).
4. **Fix the parameters:** model version (v5.5), tempo family, key family, mastering chain.
5. **Optional but strongly recommended if you have the catalogue:** train a **Custom Model** on ≥6 finished tracks. This is the only tool that locks production identity as well as vocal identity.

**Phase 2 — Track production (repeat per track)**

6. Write lyrics per §5, in the album's language(s).
7. Style box = **album core + per-track variation** (§12.3).
8. Apply the persona. Omit all vocal description from the style box (§9.3).
9. Generate 4–6 takes. Select on voice consistency *with the other tracks*, not just on quality in isolation.
10. Extend / Replace / Crop per §10.
11. Download WAV. Do **not** master yet.

**Phase 3 — Album finishing**

12. Sequence the tracks.
13. **Master the whole album in one session, with one chain.** This is what turns twelve files into a record. Per-track mastering on different days is the single most common way a coherent album falls apart at the last step.
14. Check level and tonal consistency across the sequence — listen to the transitions, not the tracks.

### 12.3 The style-box core technique

Split every style box into a **fixed core** and a **per-track variable**.

**Album core — identical in every track, never edited:**

```
Afro-soul with gospel harmony, contemporary Lagos, fingerpicked nylon guitar,
upright bass, hand percussion. Lead vocal loud, dry, close-mic'd, front of
mix. Analog warmth, minimal compression, wide dynamic range.
```

**Per-track variable — appended:**

```
Track 1:  92 BPM, bright and open, major key, full band from the top
Track 2:  78 BPM, sparse, one guitar only, intimate and restrained
Track 3:  104 BPM, driving, congas and shaker added, communal call and response
Track 4:  86 BPM, minor key, sustained melancholy, brushed kit
```

Every track is recognisably the same record; every track is a different song. **Copy-paste the core — do not retype it.** Paraphrasing your own core is how albums drift, and it happens without anyone noticing until the sequence is assembled.

### 12.4 Consistency troubleshooting across a body of work

| Symptom | Fix |
|---|---|
| Voice differs between tracks | Persona not applied to every generation — **including every Extend**. Check each segment. |
| Voice drifts *within* a long track | Shorter generations + Extend, persona on each pass (§10.2). Test `suno_generate_with_persona_vox` (§9.5). |
| Tracks feel unrelated despite one voice | Style-box core not reused verbatim (§12.3). |
| Album sounds inconsistent in level or tone | Mastered per-track instead of as one session. Re-master from the WAVs together. |
| One track is obviously better | Usually a v5.5 track sitting among v4.5 tracks. Regenerate the outliers on the same model. |
| Language or accent slips on some tracks | Phonetic respellings not carried across (§5.6). Keep one master phonetic glossary for the album and reuse it. |

### 12.5 A concrete album spec — worked

A 10-track Afro-soul / Afro-gospel album, one female lead, English and Yoruba.

```
IDENTITY
  Model:        v5.5, every track, no exceptions
  Persona:      "Album Lead v2" — warm alto, slight rasp, Nigerian English,
                gospel-inflected runs, audible breath
  Seed:         Sparse acoustic, 88 BPM, one nylon guitar, dry forward vocal
  Custom Model: Trained on tracks 1-6 once they are finished, then used
                for tracks 7-10

STYLE CORE (verbatim in all 10)
  Afro-soul with gospel harmony, contemporary Lagos, fingerpicked nylon
  guitar, upright bass, hand percussion. Lead vocal loud, dry, close-mic'd,
  front of mix. Analog warmth, minimal compression, wide dynamic range.

EXCLUDE (verbatim in all 10)
  autotune, pitch correction, synth pad, choir pad, heavy compression,
  dense arrangement

TEMPO FAMILY   78-108 BPM
KEY FAMILY     A minor / C major and relatives
LANGUAGE       English verses, Yoruba hooks, phonetic glossary maintained
               once for the whole album

SEQUENCE
  01  96 BPM   full band          English         opener, bright
  02  88 BPM   core               Eng + Yor hook  first single
  03  78 BPM   guitar only        English         intimate
  04 104 BPM   + congas, shaker   Yoruba lead     call and response
  05  92 BPM   core               English         mid-album ballad
  06  86 BPM   brushed kit        Eng + Yor       minor key
  07 108 BPM   + brass            Yoruba lead     uptempo praise
  08  82 BPM   A CAPPELLA (§7)    Yoruba          the centrepiece
  09  94 BPM   core               English         penultimate
  10  90 BPM   full band + choir  Eng + Yor       closer

FINISHING
  All 10 WAVs downloaded desktop-only, mastered in ONE session,
  -14 LUFS / -1 dBTP, stems archived
```

Track 08 is placed deliberately. **An a cappella track lands hardest when it arrives late on a record that has established a full arrangement** — and it is also the track most likely to need the §7.5 stems fallback, so schedule extra time for it.

---

## 13. Prompt-writing best practices and reusable templates

### 13.1 The formula

Everything in this guide compresses to one ordered formula. **Order matters — earlier tokens carry more weight**, and this is the most-replicated structural claim in the community corpus:

```
GENRE + SUBGENRE + ERA/REGION → MOOD/ENERGY → VOCAL STYLE/CHARACTER
→ KEY INSTRUMENTS (3-5) + PRODUCTION QUALITY → BPM (single number)
```

**Genre always goes first. If vocal quality is your priority, front-load the vocal descriptors too** — deliberately overriding the default order. This is the whole point for vocal-forward work: what you put in the first five tokens is what you get.

**Budget:** 8–15 descriptors, 150–350 characters, 2–3 exclusions.

### 13.2 The genre playbooks

Each playbook gives the style box, vocal treatment, structure notes, and the one thing that makes it read as **current rather than dated**. The natural/human dimension is not repeated per genre — it lives in **§6.7** and applies to all of them.

---

#### Pop

```
Contemporary pop, 2020s production, 102 BPM, bright and open, clean female
alto with breathy texture and conversational phrasing, layered vocal stack
on the chorus, punchy programmed drums, warm sub bass, plucked synth,
occasional live guitar. Lead vocal loud and forward, polished but not
over-compressed.
```
Exclude: `dated 2010s EDM drop, over-autotuned`

**Vocal:** conversational verse, stacked chorus. The verse/chorus *density* contrast is the arrangement.
**Structure:** hook-first (§5.7) for streaming.
**Current vs dated:** 2026 pop reads current through **vocal realism**, not production tricks. The dated tell is a big-room EDM drop where a chorus should be. The current tell is a chorus that arrives through *added vocal layers* rather than added synths.

---

#### Afrobeats

See **§8.4** for the full Nigerian and Ghanaian templates. Condensed:

```
Contemporary Nigerian Afrobeats, Lagos sound, 107 BPM, log drum bass, talking
drum accents, shekere, clipped kick. Smooth male tenor, laid-back
behind-the-beat phrasing, Nigerian English and Pidgin, light rhythmic ad-libs.
Vocal forward and warm, subtle autotune as texture. Spacious modern mix.
```
Exclude: `generic tropical house, marimba synth`

**Current vs dated:** space. Contemporary Afrobeats is *sparse* — three or four elements with air between them. Dense percussion reads as 2016.

---

#### Amapiano

See **§8.4**. The non-negotiables: **112 BPM**, **log drum named explicitly** (not "kick"), extended jazz piano voicings, spoken ad-lib layer.

**Current vs dated:** the log drum must **glide and swing**, not thud on the grid. A quantised log drum is the single clearest tell of a non-South African production.

---

#### Hip-Hop / Rap — Boom Bap

```
Boom bap hip-hop, 1990s New York, 90 BPM, dusty vinyl-sampled jazz loop,
snappy snare, deep sub bass, crisp hi-hats, MPC-chopped drums. Confident
male rapper, laid-back conversational flow, clear diction, no melody.
Warm analog sampling character, tape saturation.
```
Exclude: `modern trap, autotune`

**Vocal:** clarity over aggression. Boom bap flows sit *on* the beat.
**Current vs dated:** here "dated" is the goal. **Suno defaults to modern hip-hop unless you aggressively anchor the era** — the year and the city are load-bearing, not decorative.

---

#### Hip-Hop / Rap — Trap

```
Trap, modern Atlanta sound, 140 BPM half-time feel, gliding 808 bass, rapid
hi-hat rolls and triplets, sparse dark piano, cinematic pad. Male rapper,
melodic autotuned delivery, sparse ad-libs panned wide. Dark and spacious,
heavy low end.
```
Exclude: `boom bap, live drums`

**Vocal:** autotune is **correct here** — it is the genre's texture, not a flaw (§6.7 item 4).
**Current vs dated:** name the **808 glide** and the **hi-hat rolls** explicitly. Without both you get "plain trap" — the drum pattern without the genre.

---

#### Drill

```
UK drill, London, 141 BPM, sliding 808 bass, dark eerie piano melody,
syncopated skippy hi-hats, sparse menacing arrangement. Male rapper,
aggressive triplet flow, London accent, deadpan delivery. Cold and
claustrophobic mix, heavy sub.
```
Exclude: `melodic trap, bright synths`

**Vocal:** deadpan and rhythmic, not shouted.
**The one thing that matters most:** **the geographic anchor is non-negotiable.** UK / New York / Chicago drill are three different genres, and without naming one, Suno averages all three into something generic. UK ≈ 140–142 BPM with grime-inflected triplet flow; **NY drill** shares the sliding 808 but is more sample-driven with faster hats and melodic vocal samples. Chicago drill is the third pole; the research found no reliable detail on prompting it specifically — **treat Chicago drill as unmapped and test it yourself.**
**Universal to all three:** the **sliding 808**. Name the glide.

---

#### R&B / Neo-Soul

```
90s neo-soul, 92 BPM, D minor, Rhodes electric piano with extended jazz
voicings, fretless bass guitar, loose live drum machine, muted guitar.
Warm female alto, melismatic with runs and ad-libs, intimate and
conversational, audible breath. Lead vocal close-mic'd, dry, front of mix.
Live-feel production, minimal compression, wide dynamics.
```
Exclude: `autotune, over-compressed`

**Vocal:** this is a **vocal-forward genre by default** — the closest mainstream match to §6 and §7. Runs and melisma need explicit request plus genre framing to land.
**Current vs dated:** the era anchor does the work. Small changes to the **vocal wording** matter more than instrumental changes in this genre specifically — worth knowing when you iterate.

---

#### K-Pop

```
K-pop, bright synth-pop with hip-hop bridge, 120 BPM, layered youthful
vocals, polished maximalist production, punchy synth bass, plucked synth
lead, trap-influenced percussion in the bridge. Mixed male vocal group,
clean tight harmonies, emotional pre-chorus, rapped bridge section.
Glossy contemporary mix.
```
Exclude: `lo-fi, sparse arrangement`

**Structure — the thing that decides success:** K-pop is a **mosaic** that switches style aggressively within a track, which fights Suno's tendency to average. **Tag every section, and label the rap section explicitly as `[Rap Verse]`** — it will not happen reliably unlabelled.

```
[Intro]
[Verse 1]
[Pre-Chorus]
[Chorus]
[Verse 2]
[Pre-Chorus]
[Chorus]
[Rap Verse]
[Bridge]
[Final Chorus]
[Outro]
```

**Approach that works:** build one structural skeleton and reuse it, swapping only lyrics and concept. **Aegyo** (the cute-voice convention) is a real K-pop device but **was not confirmed as a working Suno technique** — untested.

---

#### Latin — Reggaeton

```
Reggaeton, 94 BPM, dembow rhythm, heavy sub bass, synth stabs, sharp
percussion. Male Spanish vocal, rhythmic melodic delivery, Puerto Rican
accent, call-and-response ad-libs. Punchy contemporary mix, vocal forward.
```
Exclude: `generic latin pop, English vocals`

**The two non-negotiables:**
1. **Name the dembow rhythm.** Without it you get generic Latin pop.
2. **Spanish is a genre parameter, not a lyric choice.** Community reporting is explicit: **English vocals change the genre entirely.** If you want reggaeton, write in Spanish.

**Sub-styles:** dembow/perreo (aggressive) · reggaetón romántico (sensual) · reggaeton pop (radio).

---

#### Latin — Bachata

```
Bachata, 124 BPM, requinto lead guitar with reverb, bongos, güira, bass
guitar, syncopated guitar arpeggios. Romantic male Spanish vocal, warm and
emotive, Dominican phrasing. Warm intimate mix, vocal forward.
```
Exclude: `salsa, electronic production`

**Note on instrument names:** Spanish instrument names such as `güiro`/`güira` and `bongos` are reported as only **partially** recognised. If the percussion sounds wrong, describe it (`scraped gourd percussion`) instead of naming it. The **requinto** is the signature and must be present.

---

#### Gospel

```
Traditional black gospel, 6/8 time, 72 BPM, Hammond B3 organ, acoustic
piano, tambourine, live syncopated drums, bass. Powerful female lead with
gospel runs and shouts, full SATB choir stacks, call and response between
lead and choir, hand claps. Church hall reverb, live room, wide dynamics
from hush to full voice.
```
Exclude: `synth choir, autotune`

**The traditional/contemporary split is real and they need different stacks:**

| | Traditional | Contemporary worship |
|---|---|---|
| Signature | **Hammond B3 organ** | Ambient shimmering pads |
| Rhythm | Live syncopated drums, 6/8 | Straight 4/4, programmed |
| Strings | None | Orchestral, "cinematic worship" |
| Guitar | Minimal | Electric with delay, "stadium worship" |
| Tempo | 68–100 | 70–90 ballad, 110–130 praise |

**Vocal:** the most demanding vocal genre on this list. Everything in §7.6 about choir stacks and call-and-response applies directly.
**Common errors** (repeated near-verbatim across sources): forgetting the vocal-style descriptor, conflicting energy tags, 15+ tag overload, and skipping production-quality tags.

---

#### Country

```
Modern country, 110 BPM, pedal steel guitar, fiddle, acoustic guitar,
brushed drums, upright bass. Warm male baritone, conversational
storytelling delivery, slight Southern American drawl, audible breath.
Lead vocal loud, dry, front of mix. Live room, analog warmth, minimal
compression.
```
Exclude: `pop production, autotune`

**Two genre-specific rules:**
1. **Name `pedal steel` and `fiddle` explicitly.** Vague `twang` returns a regular electric guitar.
2. **Write your own lyrics.** Country depends on concrete storytelling specificity more than any other genre here, and AI-generated country lyrics reliably come out generic. This is the one playbook where the lyric route from §4.3 is not a preference but a requirement.

**Sub-styles:** classic/Bakersfield (honky-tonk piano, twangy male) · pop-country · red-dirt (dusty, acoustic and fiddle, Texas roadhouse) · storytelling country.

---

#### EDM / House

```
Big room festival EDM, 128 BPM, euphoric and massive, supersaw leads, sub
bass, sidechained pads, layered kick, sweeping risers. Female vocal, soaring
belted topline in the chorus, processed and wide. Loud modern festival
master, huge build into the drop.
```
Exclude: `lo-fi, acoustic`

**Structure — an important exception to §5.3.** EDM is the one genre where **structural cueing in the style box matters as much as in the lyric box.** State `builds into a drop` in the style box **and** tag it in the structure, or the energy curve stays flat:

```
[Intro]
[Verse]
[Build]
[Drop]
[Breakdown]
[Build]
[Drop]
[Outro]
```

**House benchmarks:** house ~120 BPM · big room / progressive ~128 · Afro house 118–126.

---

#### Lo-fi

```
Lo-fi hip-hop, 78 BPM, rainy afternoon in a dorm room, detuned muted jazz
piano, warm Wurlitzer chords, boom-bap drums, subtle sidechained bass,
vinyl crackle, tape hiss, warm analog saturation. Instrumental, hazy and
nostalgic, narrow lo-fi mix.
```
Exclude: `clean modern production, loud master`

**Authenticity here is textural, not melodic.** `vinyl crackle, tape hiss, warm analog` reportedly does most of the work — stack multiple imperfection layers rather than relying on one.
**Scene-setting phrases** (`rainy afternoon in a dorm room`) meaningfully shift character despite not being literal audio instructions. Use them.
**Usually instrumental** — see §7.2's inverse case below for suppressing vocals reliably.

---

#### Viral short-form hooks

```
Contemporary pop hook, 105 BPM, immediate and catchy, bright plucked synth,
punchy drums, warm bass. Female vocal, conversational and close, memorable
three-word hook phrase repeated. Loud modern mix, vocal front and centre,
no long intro.
```
Exclude: `long intro, slow build`

**The mechanics that actually govern this format:**
- **Optimise the hook, not the song.** A 20-second hook is the unit of success.
- **10–15 second clips outperform full-track uploads.**
- **Keep the chorus to 2–3 lines.** Choruses longer than four lines are reported to produce flatter melodies — the hook needs melodic room, and more words take it away.
- **No long intro.** Reach the hook in the first few seconds.
- **Reuse the same clip** across posts. Recognition compounds.

**Trend-riding:** watch what is **climbing**, not what is saturated — by the time a sound is everywhere, the window has closed. Creators cross-reference short-form platforms against Spotify Viral 50 and Billboard to catch sounds on the way up. Regional and seasonal sounds follow the same logic: publish *into* a rising curve.

> **A caveat about this playbook specifically.** Short-form trends have a shelf life measured in weeks. Everything here about *mechanics* (hook length, clip duration, chorus line count) is durable; any specific trend named in any guide, including this one, is a snapshot. Re-observe before you commit a release to a trend.

---

### 13.3 Output-type approaches

Each of these is a **different application of the same techniques**. The natural/human dimension is §6.7 throughout.

| Output type | The one thing that decides it | Cross-reference |
|---|---|---|
| **Radio-ready full song** | Structure discipline and a real `[Outro]` | §5.7, §5.8, §11 |
| **Instrumental beats / backing tracks** | Instrumental toggle **on**, plus the `[Instrumental]` tag — see below | §13.4 |
| **Cinematic / film-score cues** | Describe *function*, not genre: `underscore, no melody, tension building, sparse` | §6.5 |
| **Cinematic vocal cues** | `wordless vocalise, ethereal solo soprano, no lyrics, sustained` — write vowels (`ahh`, `ooh`) not words | §7.6 |
| **Lo-fi / ambient loops** | Loopability: no dramatic arc, no defined ending, texture over structure | §13.2 lo-fi |
| **Singer-songwriter / acoustic ballad** | The purest §6.7 application — sparse, dry, dynamic, imperfect | §6.3, §6.7 |
| **Rap with tight flow** | Punctuation as cadence control | §5.5, §13.4 |
| **Pop hooks and choruses** | 2–3 lines, repetition, hook-first structure | §13.2 short-form |
| **EDM builds and drops** | Structure cued in **both** boxes | §13.2 EDM |
| **Jingles / short social clips** | Under 30 seconds; one idea; land the hook immediately | §13.2 short-form |
| **Concept album, one voice** | Persona + verbatim style core + one mastering session | §12 |
| **Multilingual songs** | Anchor language + phonetic respelling + short foreign lines | §5.6, §8.5 |

### 13.4 Copy-paste templates

**True instrumental — the reliable no-vocals recipe**

Community-reported as the dependable combination, and it solves the common failure of humming appearing unbidden around the 40-second mark:

```
STYLE BOX:  [genre], [BPM] BPM, [instruments], instrumental
LYRIC BOX:  [Instrumental]
            [No Vocals]
TOGGLE:     Instrumental = ON
EXCLUDE:    vocals, singing, choir, humming
```
The **`[Instrumental]` bracket tag is reported to suppress vocal generation at an architectural level** — more reliably than the toggle alone.

**Solo a cappella**

```
STYLE BOX:
Isolated vocal take, unaccompanied solo [female/male] voice, no instruments,
[warm alto / weathered baritone] with audible breath and slight rasp,
close-mic'd and dry, small natural room, wide dynamic range, minimal
compression, raw first-take feel

EXCLUDE:
instruments, pads, autotune

LYRIC BOX:
[A Cappella]
[Verse 1]
[A Cappella]
...re-assert the tag at every section...
```

**Gospel choir stack**

```
STYLE BOX:
A cappella gospel choir, 76 BPM, full SATB stack with soloist, no
instruments, powerful belted lead over rich harmony, hand claps only, church
room ambience, call and response, wide dynamics from hush to full voice

EXCLUDE:
synth choir, choir pad, organ

LYRIC BOX:
[Call and Response]
[Chorus]
[Choir] [Belted]
Lead line here
(choir response here)
```

**Afrobeats**

```
STYLE BOX:
Contemporary Nigerian Afrobeats, Lagos sound, 107 BPM, log drum bass, talking
drum accents, shekere, clipped kick. Smooth male tenor, laid-back
behind-the-beat phrasing, Nigerian English and Pidgin, light rhythmic
ad-libs. Vocal forward and warm, subtle autotune as texture, spacious modern
mix, deep sub-bass

EXCLUDE:
generic tropical house, marimba synth
```

**Amapiano**

```
STYLE BOX:
South African Amapiano, Johannesburg sound, 112 BPM, deep gliding log drum
groove with swing, jazzy Rhodes piano maj9 voicings, sub-heavy bass, shaker
and rim percussion, airy pads. Soulful female vocal with Zulu and English,
spoken ad-libs and conversational interjections, layered vocal chants. Wide
spacious mix

EXCLUDE:
four-on-the-floor kick, EDM drop
```

**Persona seed — genre-neutral, for album work**

```
STYLE BOX:
[genre], [BPM] BPM, sparse arrangement, single [instrument] only. [Full vocal
description: type, register, texture, accent, delivery]. Lead vocal loud,
dry, close-mic'd, front of mix. Minimal compression, wide dynamic range, raw
first-take feel

EXCLUDE:
autotune, dense arrangement, double-tracked vocals

LYRIC BOX: (exercise the full range)
(whispered)
[Verse 1]
...
(belted)
[Chorus]
...
(falsetto)
[Bridge]
...
[Spoken Word]
[Outro]
...
```

**Extend — paste this every single time**

```
STYLE BOX: <THE FULL ORIGINAL STYLE STRING, VERBATIM, INCLUDING BPM>
PERSONA:   <the same persona>
LYRIC BOX: [Section]
           ...
           [Outro]
           [End]
```

### 13.5 The universal troubleshooting index

| Symptom | Section |
|---|---|
| Robotic / AI-smooth / lifeless | **§6.7** — the master section |
| Vocals buried in the mix | §6.3 |
| Mumbled diction | §7.8 · shorten lines · Remaster (§10.7) |
| Wrong accent | §7.8 · phonetic respelling §5.6 |
| Thin harmonies | §7.6 · exclude `synth choir, choir pad` |
| Autotuned tone | §6.6 · but check §6.7 item 4 first — the genre may want it |
| Unwanted choir / crowd vocals | §6.6 — check for `anthemic`, `festival`, `crowd energy` in your style box |
| Pitch drift | §7.8 · shorter generations + Extend |
| **Genre drift on Extend** | **§10.2 — paste the full style string into every extension** |
| Abrupt ending | §5.8 · `[Outro]` + `[End]`, Extend-then-Crop |
| Muddy mix | §7.8 · §11.3 |
| Voice changes between tracks | §12.4 |
| A cappella keeps adding instruments | §7.1–7.3 · reframe as a format, then stems fallback §7.5 |
| Style box seems partly ignored | §6.1 — you are probably over the character cap; it truncates silently |
| Unrequested pauses / gaps | §5.3 — strip stray blank lines |

---

## Appendix A — Two documented end-to-end workflows

### A.1 One polished vocal-forward single

**Target:** a 3:10 Afro-soul single, one female lead, English verses with a Yoruba hook, vocal forward over sparse acoustic backing.

```
STEP 1 — PREPARE                                        (0 credits)
  Write lyrics in full. Read every line aloud at 88 BPM.
  Cut any line you cannot sing comfortably.
  Build the phonetic glossary for the Yoruba hook (§5.6).
  Keep two lyric versions: phonetic (for Suno), correct (for release).

STEP 2 — SEED THE VOICE                                 (~6 generations)
  Custom Mode, v5.5, Weirdness 20%.
  Sparse persona-seed style box (§9.2), full-range seed lyric.
  Generate 6 takes. Select on VOICE ONLY.
  Capture as a Persona. Name it descriptively. Version it.

STEP 3 — GENERATE THE TRACK                             (~4 generations)
  Persona applied. Style box omits all vocal description (§9.3):
  "Afro-soul with gospel harmony, contemporary Lagos, 88 BPM,
   fingerpicked nylon guitar, upright bass, hand percussion. Lead vocal
   loud, dry, close-mic'd, front of mix. Analog warmth, minimal
   compression, wide dynamic range."
  Exclude: "autotune, synth pad"
  Generate 4 takes. Select the best VOCAL PERFORMANCE.

STEP 4 — FIX WHAT IS WRONG                              (~2 operations)
  Weak chorus?      Replace Section — and CHANGE THE LYRIC SLIGHTLY (§10.3)
  Mumbled line?     Replace Section, or Remaster if otherwise good (§10.7)
  Yoruba mangled?   Replace Section with a revised phonetic spelling
  Too short?        Extend — FULL style string pasted verbatim (§10.2)

STEP 5 — LAND THE ENDING                                (~2 operations)
  Extend with an explicit [Outro] + [End].
  Crop back to where it should land.

STEP 6 — POLISH                                         (1 operation)
  Remaster if the vocal needs rebalancing forward or the diction
  needs sharpening.

STEP 7 — EXPORT                                         (10-50 credits)
  Download WAV — desktop web only.
  Split from Mix (10 cr) for the vocal stem, even if you do not need an
  a cappella: vocal-only processing in your DAW is better than
  processing the full mix (§11.3).

STEP 8 — FINISH                                         (0 credits)
  §11.3 chain. Light compression only.
  -14 LUFS, -1 dBTP. Archive the stems.

REALISTIC COST: 10-14 generations plus stem operations.
```

### A.2 A cohesive multi-track album on one voice

**Target:** 10 tracks, one female lead, Afro-soul / Afro-gospel, English and Yoruba, one sonic identity throughout. Full spec in **§12.5**.

```
PHASE 1 — IDENTITY                              (one session, ~10 generations)
  1. Create the album Workspace (§2.3).
  2. Seed and capture the Persona (§9.2). 6-10 takes.
     DO NOT PROCEED until the voice is right — everything inherits it.
  3. Write the STYLE CORE — the 100-150 chars that appear verbatim in
     every track (§12.3). Save it in a text file. You will paste it ~40
     times across this project; never retype it.
  4. Fix: model = v5.5, Weirdness = 20%, tempo family, key family,
     Exclude string.
  5. Build the album-wide phonetic glossary once (§5.6). One spelling per
     word, used identically in every track — inconsistent respelling
     across tracks is a real and easily-missed source of drift.

PHASE 2 — PER TRACK                             (~6-10 generations each)
  6.  Lyrics per §5. Read aloud at the track's BPM.
  7.  Style box = CORE (pasted) + per-track variable.
  8.  Persona applied. No vocal description in the style box.
  9.  4-6 takes. Select on consistency WITH THE OTHER TRACKS, not on
      isolated quality. Play the previous track's chorus immediately
      before judging — the ear drifts across a long session.
  10. Extend / Replace / Crop (§10). Full style string on every Extend.
  11. Download WAV. DO NOT MASTER YET.

PHASE 3 — THE A CAPPELLA TRACK (track 08)       (budget extra time)
  12. Attempt direct generation first (§7.2), reframed as a format
      ("isolated vocal take") rather than a negation.
  13. If it will not behave — and expect that — switch to the stems
      route (§7.5): generate a deliberately separable vocal-forward
      version, Split from Mix, UVR cleanup if needed.
  14. Optional and strongest: underpaint (§10.6) if you have a clean
      vocal you believe in.

PHASE 4 — ALBUM FINISHING                       (one session)
  15. Once tracks 1-6 are done: optionally train a CUSTOM MODEL on them
      (§1.8) and use it for 7-10. This locks production identity, not
      just vocal identity.
  16. Sequence.
  17. MASTER ALL TEN IN ONE SESSION WITH ONE CHAIN. This is the step
      that turns ten files into a record, and splitting it across days
      is the most common way a coherent album falls apart at the end.
  18. Check transitions, not tracks.
  19. Archive: WAVs, stems, the style core, the persona ID, the phonetic
      glossary, and the per-track variables. You will need all of it for
      the deluxe edition, the remixes, and the sync licensing.

REALISTIC COST: 80-120 generations plus stem operations across the album.
On Pro's 2,500 credits/month this is comfortably one month of work;
it is not a weekend.
```

---

## Appendix B — What this guide could not confirm

Collected in one place, so nothing is quietly glossed over.

| Item | Status |
|---|---|
| **v6 or any model beyond v5.5** | **Does not exist** as a named release as of 2026-08-01 |
| **"Personas v2"** | **Not an official Suno term.** Likely shorthand for the Personas→Voices transition, or a conflation with Custom Models |
| **"Inpainting"** | **Not Suno's terminology.** The feature is called **Replace Section** |
| Credit cost — Extend, Cover, Persona, Remaster, Replace Section, Crop, Song Editor, Upload | **Undocumented.** Only stem-separation modes and Get MIDI have official figures |
| Voices creation credit cost | "4 credits during beta" circulates; not traceable to the official FAQ |
| Concurrent-generation and fast-queue numeric limits per tier | **No official source found.** Priority queueing on paid tiers is confirmed; specific numbers are not |
| Style-box and lyric-box character limits | **OFFICIAL (MCP)**, but **Suno publishes no limits table**. App-side numbers may shift |
| Metatag syntax as a documented specification | **Does not exist.** Six structural tags are documented via MCP; everything else is community convention |
| `suno_generate_with_persona_vox` — what "VOX consistency mode" does | **Undocumented.** Worth testing empirically for album work |
| Vocal gender control as a UI feature | MCP lists it for v4.5+; **no official help article found.** Probably an API-level parameter |
| Audio Upload duration limits | **Two official articles give conflicting figures.** Unreconciled |
| Microsoft Copilot integration currency | Existed Dec 2023; **no 2026 confirmation** it is still live |
| Self-serve public API | **Does not exist.** An "API Partner Program" intake was described publicly in July 2026 |
| Enterprise / Business / Team tier | **Weakly sourced**, not confirmed official |
| Suno reproduction of **agogo, gyil, udu** | **Not confirmed.** Describe the sound rather than naming the instrument |
| Up-tempo Afro-gospel BPM | **No authoritative figure found.** 120–130 is a working guess, flagged as such |
| Chicago drill prompting specifics | **Unmapped** in available sources |
| K-pop *aegyo* as a Suno technique | Real musical convention; **not confirmed** as a working prompt technique |
| WavTool as a separately accessible product | Suno Studio is the confirmed successor; **legacy accessibility of wavtool.com not verified** |
| v5.5 mid-track degradation | **COMMUNITY-reported regression**, not acknowledged by Suno. Workaround in §1.7 |

**A closing note on sourcing.** Official Suno pages could not be fetched directly from the research environment (§0.2), and Reddit — the largest single body of Suno community technique — was unreachable by the research tooling entirely. Community findings labelled here were therefore drawn from creator write-ups, community-compiled repositories, and search-index extraction rather than from primary threads. Where a claim rests on a single source, this guide says so. **Nothing here was verified by generating music**, per the brief's constraint. Treat the techniques as well-sourced starting points to test against your own ears, not as measured results.
