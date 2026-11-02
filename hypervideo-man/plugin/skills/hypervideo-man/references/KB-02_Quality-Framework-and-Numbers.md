# KB-02 — Quality Framework and Numbers

*Composite. Part I is Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026): the eleven markers, structure and pacing, the visual system, motion language, coherence and the 35-item scorecard. Part II is Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229): the twelve-dimension quality model, craft standards with numbers, the 1–5 rubric with ship bars, the symptom-to-fix table and stage checklists. Audio doctrine lives in KB-07; exemplar analyses in KB-10.*

*Section numbers inside each part keep the numbering of the source they came from (A = §2–§7 and appendices of the Skillgraph document; B = Parts 3–8 of the Claude Code document). Where the two parts disagree, the preface and KB-14 govern; where either disagrees with the installed CLI, the CLI wins.*

## 0. Reconciled values that govern this file

| Topic | Governing value | Note |
|---|---|---|
| Reading hold | ≥ max(1.5 s, 0.5 s + 0.4 s × words); +0.5 s for numbers; +30–50 % when voice or motion competes | A's per-word rate (stricter) with B's 1.5 s floor (stricter) |
| Hook | Visual change ≤ 0.5 s; outcome readable sound-off ≤ 1–2 s social / ≤ 3 s default / ≤ 5 s long-form; never logo-first | union of both tests |
| 9:16 safe box | x 120–780, y 380–1248 (1080×1920) | intersection of the two readings |
| Contrast | body ≥ 7:1 (floor 4.5:1); large ≥ 4.5:1 (floor 3:1); measured on the worst frame | both |
| Transitions | one primary for 60–70 % of cuts + ≤ 2 accents; 1–2 shader heroes per 5–7 beats; presets 0.15–0.7 s; velocity-matched; blur ≤ 3 beats; the transition owns the scene exit | both |
| Ambient motion | decoratives may share one slow ambient motion; content never idle-loops; at most one bounded breath on a held hero | both official generations |
| Evaluation | hard gates → 35-item checklist (Part I §3.9) → twelve dimensions scored 1–5 by a separate judge (Part II §3.4); ship: none < 3, average ≥ 4.0; exceptional: none < 4, average ≥ 4.5; a score without evidence is a 2 | three-layer stack |
| Data motion | ≤ 3 metrics per frame; zero baselines; staged ~1 s changes; object constancy; no overshoot; no pies or legends; tabular figures | both |

## Part I — Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026)

### 3. Quality framework — what makes a HyperFrames video exceptional

This part turns taste into testable statements. Every rule carries an evidence tag (legend in §0.3): **[Documented]** comes from the official HyperFrames documentation or skill files, **[Standard]** from a public standard, **[Demonstrated]** from a film or build that has actually shipped, **[Recommended]** from this author's production judgement. Numbers are expert starting defaults: break them on purpose, never by accident. Where a value changes from the earlier HyperFrames standards in the input set it is marked **(revised)** and explained in Appendix A.

#### 3.1 The eleven markers of a showreel-grade HyperFrames film

The best HyperFrames films do not win on effects. They win because every frame obeys one system, every movement means something, and picture and sound are locked together. The eleven markers below consolidate the earlier "ten best-in-class markers" and "eleven markers" lists into one set; each is testable in the scorecard of §3.9.

| # | Marker | What it looks like on screen | Tag |
|---|---|---|---|
| 1 | **One idea, in the viewer's language, within two seconds** | The value claim lands by beat 2; everything after it is evidence. Delete the value beats and the film must collapse into a feature tour — if it still "works", it was never a story. | [Documented] story-spine.md §1–2 |
| 2 | **A locked visual system** | One `frame.md`: one background world, one accent hue, two type voices, one shape-and-shadow logic. Forty scenes read as one film. | [Documented] design-spec.md; [Recommended] |
| 3 | **Frames built for video, not for the web** | Video-scale type, three depth layers, two focal points, content anchored to the edges, hero text at 60–80 % of frame width. | [Documented] video-composition.md, motion-principles.md |
| 4 | **Motion with intent** | Every element has a verb (slams, draws, locks in, drifts). Eases and durations vary deliberately; every scene builds, breathes and resolves; exits are faster than entrances; stillness is punctuation. | [Documented] beat-direction.md, motion-principles.md |
| 5 | **One continuous world** | Persistent elements never jump across a cut; transitions carry meaning; velocity-matched handoffs read as a single camera move. | [Documented] beat-direction.md § Velocity-matched |
| 6 | **Sound as meaning, not decoration** | A clear voice, a bed carved around it rather than merely turned down, SFX on the frame, rare hero hits, designed silence. | [Documented] production-loop.md (carve before Verify); [Recommended] |
| 7 | **Picture locked to the audio grid** | Cuts on beats, hero reveals on downbeats, narration pauses that leave the visuals room. | [Documented] capability-menu.md (beat analysis); [Demonstrated] website-to-HyperFrames storyboard: "Every second earns a music event" |
| 8 | **Real, specific content** | Real numbers, real UI, real names; each key visual traces to a line of the source; nothing could appear unchanged in another brand's film. | [Documented] story-spine.md §4 |
| 9 | **Legible for everyone** | WCAG contrast, text held long enough to read, safe zones respected, captions that carry the story with the sound off. | [Standard] WCAG 2.x; [Documented] `hyperframes check` contrast audit |
| 10 | **Technically spotless** | Deterministic render, zero `check` findings, no flicker, banding or clipped text, exact runtime and delivery loudness. | [Documented] determinism rules; [Standard] loudness |
| 11 | **An ending that lands** | CTA and logo lock up on the music's final hit and hold long enough to read (≥ 2.5 s). | [Recommended] |

Underneath the markers sits one sentence worth memorising: **professional quality = clear intention + coherent design + controlled timing + intelligible sound + verified delivery.** More effects do not create more value.

#### 3.2 Storytelling and audience relevance

##### 3.2.1 The message line comes first

Nothing is storyboarded until one sentence exists: *"This video tells [audience] that [message]."* [Documented] brief-contract.md § 2 (`message`: "Derive and echo one sentence. Do not storyboard until this is clear."). The message is written in **outcome language** — what the viewer gains, avoids or finally understands — never in subject-internal vocabulary (feature names, file names, section headings). Numbers are allowed in the hook only when they carry stakes ("40 % faster cold starts"), never as inventory ("23 files changed"). [Documented] story-spine.md §1.

##### 3.2.2 The reverse iceberg

Lead with why it is valuable, not with what it is or how it was made. The value claim lands by the second beat; the mechanism, the demo, the diff and the screenshots are evidence in service of that claim. Two self-checks on a finished beat list [Documented] story-spine.md §2:

1. Delete every evidence beat — the remaining beats must still state the value on their own.
2. Delete the value beats — if the film still seems to work, it was a feature tour, not a story.

Structure is value-first; the **voice** stays whatever the genre prescribes. A developer changelog keeps its plain, no-hype register — leading with value is an ordering decision, not a marketing register.

##### 3.2.3 Audience relevance is a design input, not a tone note

The brief must state who watches, where, on what device, and whether sound is likely on or off. These four facts set type size, pacing, hook length and audio density [Recommended]:

| Audience / context fact | What it changes |
|---|---|
| Phone, in-feed, sound-off likely (LinkedIn, X, Instagram, TikTok) | Burned-in captions mandatory; on-screen keywords; headline ≥ 90 px, body ≥ 32 px; hook in 1–2 s; frame 0 doubles as the thumbnail |
| Desktop or TV, sound on (YouTube, website embed, event screen) | Headline 64–120 px, body 28–42 px; hook within 5 s; room for a 2–3 s opening breath |
| Second-language listeners, AI voices in French | Duck music about 3 dB deeper; slower narration (2.0–2.3 w/s); captions on |
| Children, learners, older adults | Narration 1.8–2.2 w/s; larger type; music ≥ 20 dB under speech or off; no sudden peaks |
| Executives, auditors, finance peers | Voice first; a minimal bed at about −20 dB or none; half the effects; no drama on numbers |
| Faith communities (FSY, YSA, devotionals) | Reverent, warm acoustic or orchestral music for celebration; quiet or silence under scripture; everything within the Church's standards |

##### 3.2.4 Narrative structures that work in 15 s to 10 min

| Structure | Shape | Best for | Tag |
|---|---|---|---|
| Hook → Problem → Mechanism → Proof → CTA | The default value-first arc | Product launches, explainers, promos | [Documented] narration.md § Structure; storyboard-format `arc` example; official prompt guide "hook → 3 feature beats → end card" |
| PAS (Problem – Agitate – Solve) | Pain, consequence, relief | Short social promos, fundraising | [Recommended] |
| Before – After – Bridge | Old state, new state, how to cross | Transformation stories, training | [Recommended] |
| List / countdown | N items with a running motif | Tips, features, "5 ways" | [Recommended] |
| Journey / timeline | Chronology with a destination | Case studies, history, event recaps | [Recommended] |
| Orientation → Demonstration → Recap | Where we are, how it works, what to remember | Tutorials and training — do not impose an advertising arc on instruction | [Recommended], carried from the Expert Motion Prompt |
| Beat grid | The track's sections are the acts | Music-led promos, hype reels | [Documented] music-to-video route |

##### 3.2.5 The storyboard is a proposal, not a listing

The plan is presented as a proposal: open by echoing the strategy line, then a frame table — frame · beat (type, duration) · on screen · **why** (the frame's `narrativeRole`, traced to the message). A frame whose *why* cannot be traced to the message is cut, not decorated. A change costs 30 seconds here and minutes after the build. [Documented] story-spine.md §3; review-loop.md §1. Practitioners confirm it: "We approve the script word by word before generating a single shot. Every time we skipped this, we threw the footage away" (Anfloy, 2026-10-27) and Jake Moran's habit of asking for still frames before any full render [Demonstrated, §2.8].

#### 3.3 Structure and pacing

##### 3.3.1 Beat counts, density and narration budget by runtime

[Recommended], carried forward from the earlier Master Prompt Checklist and reconciled with the official narration pace (2.5 w/s natural; the reference launch narration runs 2.3 w/s [Documented] narration.md; the official prompting guide budgets ~130 spoken words per minute and reports a 78-word script running 35.5 s [Documented]).

| Runtime | Scenes / beats | New visual every | VO words (≈ 2.1–2.5 w/s) | Hero moments |
|---|---|---|---|---|
| 15 s | 3–5 | 1.5–3 s | 30–37 | 1 |
| 30 s | 5–8 | 2–4 s | 65–75 | 1–2 |
| 60 s | 8–14 | 3–5 s | 130–150 | 2–3 |
| 90 s | 12–18 | 3–5 s | 190–225 | 2–3 |
| 3 min | 18–30, in 3–5 sections | 3–6 s | 380–430 | 3–5 |
| 10 min | 60–110, in 4–7 chapters | 4–8 s | 1,250–1,450 | 1 per chapter + finale |

Capability note [Documented]: the specialised narrative workflows (faceless-explainer, product-launch-video, pr-to-video) support up to about 3 minutes and are strongest at 30–90 s; a clearly longer piece routes to `/general-video` (hyperframes SKILL.md § 2). Long-form is therefore a `/general-video` build with chapters, which the production loop supports but the shipped genre pipelines do not script for you. Past about a minute, practitioners keep one scene per file: "A monolithic file is fine for 40 seconds; past a minute, one scene per file is the only way an agent can edit a beat without breaking its neighbours" (OneWave, 2026-09-04) [Demonstrated]; HeyGen's own launch film is 49.77 s with one root and 17 sub-compositions [Demonstrated].

##### 3.3.2 Rhythm is declared before HTML is written

Name the pattern — *fast-fast-SLOW-fast-HERO-hold* — before implementing. Derive it from the storyboard and the brand, not from a lookup: a 15 s architectural-firm spot and a 15 s gaming spot have different rhythms at the same length. [Documented] beat-direction.md § Rhythm planning. Defaults [Recommended]: the slowest scene runs at least 3× slower than the fastest; long-form gets a chapter card every 1.5–3 min and a pattern interrupt (new visual mode, music shift, palette beat) every 30–60 s.

##### 3.3.3 Scene shape: build / breathe / resolve

Every scene has three phases [Documented] motion-principles.md: **Build (0–30 %)** — elements enter, staggered, in order of importance; **Breathe (30–70 %)** — content visible, alive with ONE ambient motion; **Resolve (70–100 %)** — exit or decisive end, exits faster than entrances. The first motion after a cut is offset 0.1–0.3 s; a zero-delay start reads as a jump cut. One nuance from the current official SKILL.md [Documented, R2]: at **scene** level "the transition IS the exit" — never author a separate scene-exit animation except on the final scene; the resolve phase choreographs element-level settles and hand-offs, and the transition carries the scene out.

##### 3.3.4 Hooks and endings

- **Frame 0 shows something meaningful** — it doubles as the thumbnail. The outcome is stated within 1–2 s for social, 5 s for long-form. Never "Welcome to…", never logo-first, no slow fade from black. [Recommended]; hook language [Documented] narration.md § The opening line ("If the opening is generic … start over"); the launch film's storyboard opens with "camera is already moving … No fade in. No preamble" [Demonstrated].
- **Vary the hook type**: a bold claim, a provoking question, a contrast, a striking number — not a statistic every time. [Documented] narration.md.
- **Ending**: CTA and logo lock up on the music's final hit; hold ≥ 2.5 s; no fade to black before the CTA has been read; the music ends on a button or natural ending, 2–4 s fade only if the track has none, never mid-phrase. [Recommended]

##### 3.3.5 Attention and retention realities

[Recommended, informed by platform practice]: viewers decide whether to keep watching in roughly the first second of a feed video; in-feed autoplay is muted by default on most platforms; a 60 s explainer loses most of its drop-off in the first 5–8 s. Design consequences: a meaningful first frame, a hook that is readable with the sound off, and no visual dead zone longer than 2 s (the animation map from `hyperframes-animation/scripts/animation-map.mjs` [Documented] exposes dead zones). Prompt Motion's analysis of 230 prompts found "long holds / dead time" among the strongest "AI-made" giveaways [Demonstrated, §2.8].

#### 3.4 Visual system

##### 3.4.1 The design spec is brand, not layout

`frame.md` (preferred) → `design.md` → `DESIGN.md`: read the first that exists; frontmatter tokens are normative (quote hex and font names verbatim), prose is context. [Documented] design-spec.md. **Strict from the spec**: hex values including background, font families, weight relationships, Do's and Don'ts. **Adapt for video**: type sizes, spacing, decorative opacity, border weight. A web card at `1px solid #e2e3e6` with a 4 px shadow is invisible on video. [Documented] video-composition.md. The official skill's hard gate puts it bluntly: "If you're reaching for `#333`, `#3b82f6`, or `Roboto`, you skipped it." [Documented, R2]

Thirteen-plus shipped frame presets exist (biennale-yellow, blockframe, blue-professional, bold-poster, broadside, capsule, cartesian, code-editorial, cobalt-grid, coral, creative-mode, daisy-days, editorial-forest, …), each with a `frame-showcase.html`; users pick **by eye**, never from a list of names. Init templates include warm-grain, play-mode, swiss-grid, kinetic-type, decision-tree, product-promo, nyt-graph, vignelli and blank. [Documented] design-spec.md; capability-menu.md § The design ask; README.

##### 3.4.2 Visual hierarchy and composition

| Rule | Default | Why | Tag |
|---|---|---|---|
| Focal points | ≥ 2 per scene | The eye needs somewhere to travel; a single floating text block reads as a web page | [Documented] motion-principles.md |
| Fill the frame | Hero text 60–80 % of frame width | Web-sized elements vanish on video | [Documented] |
| Depth | 3 layers: background treatment · content · foreground accents; 2–5 decoratives with slow ambient motion | Scenes feel empty during entrance staggering without a dressed background | [Documented] house-style.md § Background layer |
| Anchor to edges | Pin content left/top or right/bottom; zoned or split layouts | Centred-and-floating is a web pattern | [Documented] |
| Structural elements | Rules, dividers, border panels (animate `scaleX` 0→1) | They create eye paths and animate well | [Documented] |
| Connector lines | Must name a start anchor, an end anchor and a job | A line the frame can lose without losing meaning is decoration | [Documented] motion-principles.md |
| Negative space | 45–60 % of the frame unoccupied on hero frames | Breathing room is what reads as premium | [Recommended], reconciled from the 55 % rule in the earlier specification |
| Grid | 12 columns landscape, 4–6 portrait; 8 px spacing scale; 60–140 px padding | Alignment is felt even when it is not seen | [Documented] padding (video-composition.md); grid [Recommended] |
| Safe zones | Action-safe 90 % (5 % inset) for everything visible; title-safe 80 % (10 % inset) for text and key content | Overscan legacy and platform cropping | [Standard] SMPTE/EBU practice; [Recommended] |
| 9:16 platform UI | Keep text and logos clear of roughly the top 10–15 %, the bottom 20–30 % and a strip down the right edge; verify against the platform's own template | Captions, buttons and usernames overlay those zones; "text in the corners" is a documented AI giveaway | [Recommended]; platform figures in §2.9 |
| Density | 6–10 visual roles is a useful starting point for produced marketing frames, not a contract; lower-thirds, stings and static titles need few | Decoration must not become new content or claims | [Documented] video-composition.md § Density |

##### 3.4.3 Colour

- Declare bg, fg and ONE accent (hex) plus two neutrals **before** writing HTML; same background world across all scenes; tint neutrals toward the accent hue; no pure `#000` / `#fff`. [Documented] house-style.md § Color.
- Light canvas for food, wellness, kids; dark for tech, cinema, finance — but *make light cinematic* rather than switching to dark: bolder borders (2 px+), stronger rules, full-saturation accent hits, subtle texture. "No dark-mode-default." [Documented] video-composition.md § Color presence; SKILL.md (R2).
- Accent presence: 15–25 % opacity for atmosphere, full saturation on focal elements; decorative opacity under 10 % is invisible after compression. "Push color presence. Muted is fine, flat is not." [Documented]
- **No full-screen linear gradients on dark backgrounds** — they band under H.264. Use a radial gradient, a solid, or solid + localised glow. [Documented]
- 60/30/10 split (canvas / structural surfaces / accent). [Recommended]
- Contrast is enforced by `hyperframes check` at WCAG AA; text must stay readable with the decoratives removed. [Documented] house-style.md.

##### 3.4.4 Light and depth

One virtual key light for the whole film (default top-left, 45°); every shadow, highlight, gradient and glow follows it. One shadow recipe (offset along the light, 30–80 px blur, 15–35 % opacity, tinted toward the background hue). Accent radial glows at 12–25 % breathing over 4–8 s; 10–20 % vignette; 2–4 % grain. Light sweeps (0.6–1.2 s) on hero text or the logo once per hero moment; flash-through-white reserved for the single biggest reveal (shader duration range 0.01–0.3 s [Documented] beat-direction.md). Rack focus (background blur 0→8–12 px) and 3D tilt (`rotationY` ±6–12°, `transformPerspective: 1200`) during hero moments [Documented] image treatment in motion-principles.md. Safety: no more than three flashes per second and no large saturated-red flashes [Standard] WCAG 2.3.1. All level values in this paragraph: [Recommended]. Note that Prompt Motion's banned list includes "glows/neon" and "3D effects" as AI tells [Demonstrated] — the difference between a tell and a craft choice is restraint and motivation: one accent glow that breathes with the music is design; neon on everything is a template.

##### 3.4.5 Typography

**Rendering facts [Documented] typography.md; FAQ.** The compiler pre-bundles 18 families (Inter, Roboto, Open Sans, Lato, Nunito, Montserrat, Poppins, Outfit, Oswald, League Gothic, Archivo Black, Playfair Display, EB Garamond, Space Mono, IBM Plex Mono, JetBrains Mono, Source Code Pro, Noto Sans JP) with only the listed weights; League Gothic and Archivo Black ship weight 400 only. Any other real Google font is fetched at build time and embedded — with a `font_family_without_font_face` lint warning and a **fail-closed** behaviour in distributed/cloud renders. Common aliases resolve (Helvetica/Arial → Inter, Futura/Arial Black → Montserrat, Bebas Neue → League Gothic, Segoe UI → Roboto, Courier → JetBrains Mono, Garamond → EB Garamond). The FAQ's rule for everything else: put the font file in the project and declare it with `@font-face`; an undeclared font can fall back to a default face in the render and lint reports it. HeyGen's website-to-HyperFrames demo uses only local woff2 files — "no CDN at render" [Demonstrated].

**Taste rules [Documented] typography.md.** A banned "monoculture" list (Inter, Roboto, Open Sans, Noto Sans, Arimo, Lato, Source Sans, PT Sans, Nunito, Poppins, Outfit, Sora, Playfair Display, Cormorant Garamond, Bodoni Moda, EB Garamond, Cinzel, Prata, Syne — Syne being the most overused "distinctive" display font). The safe-and-distinctive bundled picks are therefore Montserrat, Oswald, League Gothic, Archivo Black, Space Mono, IBM Plex Mono, JetBrains Mono, Source Code Pro, Noto Sans JP. Never pair two sans-serifs; one expressive font per scene; weight contrast 300 vs 900, not 400 vs 700; display tracking −0.03 to −0.05 em; on dark backgrounds drop body weight one notch (350 instead of 400) and add 0.05–0.1 to line-height; `tabular-nums` on anything numeric that stacks. The launch film's storyboard goes further for a multi-world piece: "No single font family across the whole video. Each aesthetic world gets its own typographic voice" [Demonstrated] — a deliberate exception for a film whose concept is variety.

**Sizes (1080-px short side).** [Documented] video-composition.md table and typography.md floors; in-feed values are "first-pass values; calibrate against real renders".

| Element | Full-screen (YouTube, TV, web embed) | In-feed / mobile (X, LinkedIn, Instagram, TikTok) |
|---|---|---|
| Headline | 64–120 px (floor 60) | ≥ 90 px |
| Body / supporting | 28–42 px (official floor 20; recommended floor 24) | ≥ 32 px |
| Labels / data labels | 18–24 px (floor 16) | ≥ 24 px |
| Captions | 48–72 px | 56–80 px |
| Decorative opacity | 12–25 % | 12–25 % |
| Borders | 2–4 px | 2–4 px |

**Words and time [Recommended].** Headline ≤ 7 words, supporting line ≤ 15. On-screen text is keywords, never the narration transcript (the redundancy effect: viewers retain less when they read the words they are hearing). Reading budget: **hold ≥ words ÷ 2.5 + 0.5 s after the text has settled, minimum 1.2 s (revised** from words ÷ 3 + 0.5 s — the more conservative figure from the Expert Motion Prompt is adopted because reading time starts when text is comfortably readable, not when its animation starts). "Fixed reading time: 3 seconds on screen = must be readable in 2" [Documented] typography.md.

**Captions [Recommended, aligned with Netflix/BBC practice — §2.9].** 2–3 words per group for high-energy pieces, 3–5 conversational, 4–6 calm; ≤ 20 characters per second (17 for children); ≤ 42 characters per line; two lines maximum; one group on screen at a time, inside title-safe, on a contrast plate over busy backgrounds; every spoken word captioned. HyperFrames produces word-level timings (`transcribe` → `transcript.json`, SRT/VTT export; Parakeet TDT 0.6B v3 in 25 languages or whisper.cpp, locally) and ships 74 text-and-caption catalog items [Documented, R1].

**Contrast.**

| Item | Floor | Showreel target | Tag |
|---|---|---|---|
| Body, captions, labels | 4.5:1 | ≥ 7:1 | [Standard] WCAG 1.4.3 / 1.4.6 |
| Large text (≥ 24 px, or ≥ 19 px bold) | 3:1 | ≥ 4.5:1 | [Standard] |
| Icons, chart marks, UI strokes | 3:1 | ≥ 4.5:1 | [Standard] WCAG 1.4.11 |
| Text over photo or video | 4.5:1 on the busiest region | 40–70 % scrim or blur plate | [Recommended] |
| Hero : body size ratio | — | ≥ 3:1 | [Recommended] |

Never: hairlines under 2 px (they shimmer), saturated red on blue (it vibrates), thin light text over busy footage, text within 5 % of the frame edge, meaning carried by red and green alone. The earlier specification's "≥ 10:1 for display type" is **not adopted**: it constrains palettes without a legibility payoff beyond AAA (Appendix A). ToolRevealed's critique of a hosted-agent film — "contrast below what a phone screen in daylight needs" — is the practical reason the showreel target sits at 7:1 rather than the 4.5:1 floor [Demonstrated].

##### 3.4.6 Asset quality

- **No raw, flat images.** Every image gets a treatment: perspective tilt (`gsap.set(el, { transformPerspective: 1200, rotationY: -8 })` + shadow), slow zoom (scale 1 → 1.04 over the beat), a device frame, floating UI parallax, or a scroll reveal. All images share one grade. [Documented] motion-principles.md § Image motion treatment.
- Logos are resolved, never redrawn (`resolve --type logo`: theSVG → GitHub avatar → favicon). Icons come from one family and one stroke weight (about 3–4 px at 1080p), filled or outline but never both, animated by path draw. [Documented] media-use SKILL.md; weight [Recommended].
- **Rebuild product UI as HTML where you can**: "not a screen recording — it is markup and CSS with an animated pointer" (OneWave); dashboards built "as real HTML at twice the size it appears, then scaled into its window" so nothing is blurry at 4K (Anfloy) [Demonstrated]. Exception: training content that must show the real interface needs accurate screenshots (Masset) [Demonstrated].
- Photographic media gets **one** grounded media-polish scan in the final quality pass; leaving suitable media unchanged is a valid result. A gray-world "correction" ruins an intentional sunset. Use the canonical treatment path (`hyperframes media-treatment`, `data-color-grading`), never a CSS filter or overlay that bypasses Studio controls. [Documented] media-use SKILL.md; html-schema.
- **Iframes are banned for captured content** — they do not seek with the timeline and render frozen or blank. Use `capture/` screenshots as stacked panels. [Documented] motion-principles.md § Load-bearing GSAP rules.
- Data: at most three metrics per frame, each number paired with visual weight (bar, ring, fill), tabular figures, same visual space for successive values of one concept. No pie charts, multi-axis charts, gridlines, legends, six-panel dashboards or chart-library output — build with GSAP + SVG/CSS. [Documented] data-in-motion.md. Charts need honest scales, units, labels and sources; animation must not imply false relationships [Recommended].

#### 3.5 Motion language and transitions

##### 3.5.1 Timing and easing defaults

| Motion | Duration | Ease | Tag |
|---|---|---|---|
| Micro / snappy | 0.15–0.3 s | `expo.out`, `power3.out` | [Documented] speed bands, motion-principles.md |
| Standard entrance | 0.3–0.5 s | `power2.out` … `power4.out` (vary) | [Documented] |
| Premium / luxury | 0.5–0.8 s | `expo.out`, `sine.inOut` | [Documented] |
| Cinematic / atmospheric | 0.8–2.0 s | `sine.inOut`, `power1.inOut` | [Documented] |
| Exit (element-level) | 60–70 % of its entrance | `power2.in`, `power3.in` | [Documented] asymmetry (0.4 s in / 0.25 s out) |
| Move between positions | 0.4–0.8 s | `.inOut` | [Documented] direction rules |
| Stagger | 40–80 ms per item; < 500 ms total | — | [Documented] "< 500 ms regardless of item count"; per-item band [Recommended] |
| Scene transition presets | instant 0.15 · snappy 0.2 · smooth 0.4 · dramatic 0.5 · gentle 0.6 · luxe 0.7 s | velocity-matched | [Documented] beat-direction.md |
| Ambient loop | 4–8 s cycle, 2–6 % scale or 10–30 px drift | `sine.inOut` | [Recommended] |
| Ken Burns | 1.00 → 1.04 (up to 1.08) over the beat | `none` (linear) | [Documented] 1 → 1.04 |
| First motion after a cut | 0.1–0.3 s delay | — | [Documented] |

**Easing is emotion** [Documented]: the transition is the verb, the easing the adverb — `expo.out` reads confident, `sine.inOut` dreamy, `elastic.out` / `back.out(1.4–1.7)` playful. `.out` to enter, `.in` to exit, `.inOut` to move; LLMs get this backwards constantly. No more than two independent tweens in a scene share an ease; the slowest scene is 3× slower than the fastest; entry directions vary (left, right, scale, opacity-only, letter-spacing, blur); each scene has its own stagger rhythm and its own ambient motion (or none — stillness after motion is powerful). Anfloy's practice matches: "sharp expo-out for slamming type, in-out for camera, tiny overshoot for pops, slow sine idle … Something is always moving, even in a hold" [Demonstrated]. Prompt Motion's data puts "bouncy easing" on the AI-tell list — keep overshoot for a brand that can carry it [Demonstrated].

##### 3.5.2 Choreography is hierarchy

The element that moves first is perceived as most important: stagger by importance, not DOM order; overlap entries rather than waiting for completion. [Documented] motion-principles.md. Every element has a **verb** from a physical vocabulary — impact (SLAMS, STAMPS, DROPS), directional (SLIDES, WIPES, CUTS), reveal (DRAWS, FILLS, COUNTS UP), organic (FLOATS, BREATHES, ORBITS), mechanical (TYPES ON, LOCKS IN, SNAPS). "If you can't name the verb, the element is not yet designed." Text can name one of 24 deterministic effects by id (`typewriter`, `kinetic-center-build`, `soft-blur-in`, …) from `hyperframes-animation/adapters/animate-text.md`. [Documented] beat-direction.md. Motion that is not connected to an element already on screen is filler [Demonstrated, Prompt Motion].

A **signature move** — one recurring brand motion, such as an accent line that draws itself and then becomes the transition mask, or "the orange dot connects every scene" — is what makes a film feel authored rather than assembled. [Recommended; example Demonstrated]

**Camera** [Recommended]: push-ins of 3–8 % per scene; punch-ins of 10–20 % over 0.2–0.4 s on emphasis; parallax planes at 0.3×, 0.6× and 1×; whip pans of ±400 px with 20–30 px blur over 0.3 s (matches the documented whip-pan quick-pick: exit `x:-400, blur:24px, 0.3s power3.in` → entry `x:400→0, 0.3s power3.out` [Documented]). Animate the inner visual/crop wrapper, never the timed clip. [Documented] hyperframes SKILL.md § 5. Avoid "perpetual zooms and a compulsory entrance for every minor object" [Recommended, Expert Motion Prompt].

##### 3.5.3 Transitions are meaning

Crossfade = "this continues"; hard cut = "wake up"; slow dissolve = "drift with me". LLMs crossfade everything — use hard cuts for disruption and register shifts. [Documented] motion-principles.md. Choice table [Documented] beat-direction.md:

| Shader transition | CSS transition | Hard cut |
|---|---|---|
| Reveals, big reactions, product/logo unveils, energy shifts, "wow" moments; any downbeat or SFX hit; brand moments where the transition *is* the visual | Continuous camera-motion beats; beats that ease into the next with shared motion vocabulary; minimal/editorial pacing | Rapid-fire lists, percussive edits on the beat, comedic timing; 3+ tempo-matched switches; anywhere 0.3–0.8 s would feel slow |

Rule of thumb: shader-transition **into** the centrepiece; crossfade connective tissue; a 5–7 beat brand reel wants 1–2 shader transitions (hero reveal + CTA) — too many flatten their impact. Fourteen built-in WebGL shaders (domain-warp, ridged-burn, whip-pan, sdf-iris, ripple-waves, gravitational-lens, cinematic-zoom, chromatic-split, swirl-vortex, thermal-distortion, flash-through-white, cross-warp-morph, light-leak, glitch; each with a documented duration range), 30+ CSS patterns in 13 categories (the catalog lists 31 transition items), and the freedom to write custom GLSL. **Velocity matching**: exit with `power2.in`/`power3.in` plus a blur ramp, enter with `power2.out`/`power3.out` as the blur clears; the fastest points meet at the cut, within ~5 %. [Documented]

Two official statements must be read together [Documented, R2]: the current SKILL.md says "ALWAYS use transitions between scenes. No jump cuts", while HeyGen's own launch storyboard uses "HARD smash cuts… no dissolves… The abrupt switches ARE the proof" in its flex montage. The reconciliation: the rule is a default against *accidental* jump cuts; a hard cut chosen for meaning, on the beat, is a transition.

##### 3.5.4 Continuity and stillness [Recommended]

Persistent elements never jump across a cut — scrub every cut. Cursors and scrolled content leave through the frame edge. At least one deliberate hold of one second or more around the hero moment; no undesigned dead zone longer than 2 s. "Freeze what already works and re-render only the affected section" (Jake Moran) is the editing discipline that protects continuity late in a build [Demonstrated].

##### 3.5.5 HyperFrames motion rules that lint cannot catch

From motion-principles.md § Load-bearing GSAP rules [Documented] and practitioner post-mortems [Demonstrated, §2.8]:

1. Never overlap conflicting transform tweens on one element (a `y` entrance plus a simultaneous `scale` Ken Burns on the same `<img>` can leave it invisible with no warning). Combine into one `fromTo` or split parent/child.
2. Prefer `tl.fromTo()` over `tl.from()` inside `.clip` scenes — `from()`'s `immediateRender` writes state before the scene's `data-start` is active and breaks non-linear seeking. Where a later entrance must not pre-render, use `immediateRender: false` (Anfloy). Write explicit start **and** end values for every animation — the fix for captions that showed in preview but vanished in the render (user report via working-ref).
3. Ambient pulses attach to the seekable `tl`, never a bare `gsap.to()` — standalone tweens run on wall-clock time and are absent from the render while looking fine in the preview.
4. Hard-kill exiting inner elements (not the `.clip`) with a zero-duration `tl.set()` after their fade when a later tween could resurrect them.
5. No iframes for captured content.
6. Use absolute positions, not relative tweens (`"+=8"`), which can differ between seeking and playing (Anfloy); drive a gauge and its numeral from one proxy value so they never drift (OneWave); set counter text only from the tween, never on page load (otherwise the final number shows at frame 0).
7. Tween SVG `stroke-dashoffset` as an attribute, not as CSS, or the line pops in fully drawn (Anfloy).
8. Pad each sub-timeline to its host slot with a no-op tween (`tl.to({}, { duration: slot }, 0)`) when visibility must follow the host's `data-duration` — HeyGen's HANDOFF fix for black flashes between beats.

## Part I (continued) — coherence and the scorecard

#### 3.7 Coherence — the whole film as one object

Three freeze-frames — the opening, an information-heavy frame and the ending — must share a visual language with an obvious reading order. Watched once muted, the essential message and next step must survive; listened to without picture, the narration must still make sense; scrubbed cut by cut, nothing jumps. The animation map shows no dead zone longer than 2 s and no scene where everything moves at once. [Recommended; muted/blind review carried from the Expert Motion Prompt.]

#### 3.9 The consolidated pass/fail scorecard

The LLM reports every line as pass or fail **before rendering**, with evidence (a command output, a snapshot time, a measured value). Any fail blocks the delivery render. (This supersedes the earlier 22-line scorecard and the 40-item gate: same content, deduplicated.)

**Story (5)**
1. The message line is stated; every beat's *why* traces to it.
2. Frame 0 shows a meaningful visual; the outcome is stated within 2 s (social) or 5 s (long-form).
3. The value claim lands by beat 2.
4. CTA and logo land on the final music hit and hold ≥ 2.5 s.
5. Runtime within ±0.5 s of target (`ffprobe`).

**Visual system (5)**
6. One background world, one accent, ≤ 2 type families across all scenes (or a written concept for more); `frame.md` tokens quoted verbatim.
7. Every scene has three depth layers and ≥ 2 focal points.
8. Zero banned AI tells, or a written reason for each one used.
9. Key content inside title-safe (80 %), everything visible inside action-safe (90 %); 9:16 clear of platform UI.
10. No banding, flicker, shimmering hairlines or clipped text in any snapshot.

**Text and contrast (4)**
11. `hyperframes check` contrast audit passes; body text and captions reach 7:1.
12. Type floors met (body ≥ 28 px full-screen, ≥ 32 px in-feed; labels ≥ 18 / 24 px).
13. Every text block readable within two-thirds of its hold; captions ≤ 20 cps, ≤ 42 chars/line, one group at a time.
14. Captions cover every spoken word.

**Motion (5)**
15. Every element has a named verb; no scene uses one ease on more than two tweens.
16. The slowest scene is ≥ 3× slower than the fastest, with ≥ 1 deliberate hold.
17. Element exits faster than entrances; every stagger completes in < 500 ms; scene exits are owned by the transition.
18. Persistent elements never jump across a cut (every cut scrubbed).
19. No undesigned dead zone > 2 s (animation map).

**Light (3)**
20. One light direction with consistent shadows.
21. Light hits within ±1 frame of their sound hits.
22. ≤ 3 flashes per second anywhere.

**Audio (7)**
23. VO intelligible on a phone speaker and summed to mono.
24. Bed carved against the voice group and returning between phrases without pumping.
25. SFX count within the density band; hero hits ≥ 15 s apart.
26. Every SFX transient within ±1 frame of its visual event, none early.
27. No sample three times in a row; nothing louder than the voice while it speaks.
28. Music ends on a button or natural ending — no abrupt cut, no fade mid-phrase.
29. Measured loudness on target ±1 LU; true peak ≤ −1 dBTP (`ffmpeg ebur128`).

**Technical and delivery (6)**
30. `npx hyperframes check` reports 0 findings — and lint reported no error (a lint error silently disables the layout and contrast audits [Documented] hyperframes-core SKILL.md).
31. Every scene midpoint snapshotted and inspected at full resolution; reference-timed clips verified to start where intended (silent-zero failures [Documented] tracks-and-clips.md); file size sane (a tiny MP4 means GSAP never loaded [Demonstrated]).
32. `ffprobe` confirms duration = `data-duration` ±1 frame, briefed fps, and an audio stream.
33. Fonts bundled or embedded; no fallback faces; no `font_family_without_font_face` warnings for cloud renders.
34. The Studio preview was approved before the delivery render; render was user-gated [Documented] brief-contract.md.
35. All deliverables present: MP4 (and cut-downs), captions file, stems, assumptions list, and — if requested — the published link with explicit visibility.

## Part II — Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229)

### 3.1 The quality model

Twelve dimensions, each with what "exceptional" means and the most common way it fails. The rubric in §3.4 scores the same twelve.

| # | Dimension | Exceptional looks like | Typical failure |
|---|---|---|---|
| 1 | Purpose and audience fit | One message for a named viewer in a named context; every scene serves it | "A video about our product" for everyone |
| 2 | Story and structure | A hook in the first seconds, a clear turn, a payoff the hook promised | Logo-first opening; feature tour; no payoff |
| 3 | Pacing and rhythm | Pace set by information and voice; contrast between fast and slow; holds after payoffs | Uniform speed; rushed reads; dead air |
| 4 | Composition and hierarchy | One focal point per moment; safe areas respected; each aspect composed for itself | Centered cards everywhere; crowding; cropped masters |
| 5 | Typography and legibility | Distinct, on-brand faces; sizes and hold times that read on a phone | Default faces; small, thin, fleeting text |
| 6 | Color, light and depth | Role-based palette; one accent that means something; consistent light | Accent everywhere; banding; muddy contrast |
| 7 | Asset quality and art direction | Licensed, sharp, on-brand assets under one design spec | Stock clichés; soft zooms; scene-by-scene restyling |
| 8 | Motion language | Smooth, purposeful easing; every element has a verb; restraint | Bounce everywhere; floating everything; slideshow reveals |
| 9 | Transitions and continuity | Two or three transition types used by meaning; matched seams; object constancy | A new effect per cut; double exits; teleporting objects |
| 10 | Sound and sync | Intelligible voice, fitting music or deliberate silence, effects with visible causes, tight sync | Music over the voice; effects on every cut; drift |
| 11 | Accessibility and safety | Captions, contrast, no harmful flashes, comfortable motion | Strobes, unreadable captions, motion sickness |
| 12 | Coherence and technical integrity | Feels like one film; deterministic render; on spec for every platform | Patchwork look; preview/render mismatch; off-spec files |

The model draws on the official motion and creative doctrine [DOC] [A2-24] [A2-27], practitioner evidence [DEMO] [B-29] [B-30] and external standards and research [STD] [C-37] [C-53] [RES] [C-23] [C-45]; the numbers behind each dimension are in §3.3.

### 3.3 Craft standards with numbers

Defaults to apply when the brief is silent. Each is a starting point the brief can override; none overrides a platform's own specification.

#### Story, structure and pacing

- **Hook.** Up to 47 % of a video campaign's value arrives in the first 3 s and 74 % in the first 10 s; of viewers who watch 3 s, 65 % reach 10 s [STD] [C-14]. Over 63 % of the highest-performing TikTok ads show the key message or product within 3 s [STD] [C-15]. Show a visual change within 0.5 s and the core promise as readable text by 3 s; never open on a slow logo build [REC] [C-14].
- **Value early.** The official story spine puts the value claim by beat 2 and tests it by deleting evidence beats [DOC] [A2-33].
- **Structures.** Explainer: hook 0–3 s, problem ≈10 %, pre-training ≈5–10 %, mechanism in 2–4 signalled segments ≈50 %, proof ≈10–15 %, CTA last 3–5 s [REC] [C-23] [C-17]. Brand film: set-up 10–15 %, rising tension 35–40 %, turn at 60–70 %, resolution plus brand in the last 20 %; ads with all five dramatic acts rated higher [RES] [C-28].
- **Pacing by genre, not fashion.** UI-demo launch films average 2.2–5.2 s per shot; sizzle work 1.0–1.5 s; talking-head reels 1.1–1.4 s with the first cut at 0.6–1.0 s [DEMO] [G-01] [B-29] [B-30]. Instructional units under 6 minutes keep near-full engagement, falling to about 50 % at 9–12 minutes [RES] [C-21] [C-22]. No authoritative cut-rate standard exists for social video [REC] [C-29].
- **Cognitive load.** One new idea per beat; no more than 3–5 new labels at once; never make viewers read and listen to different content; pre-train vocabulary before mechanism; signal structure ("first… second…") [REC] [C-23].
- **Multimedia principles** (median effect sizes, directional): temporal contiguity d = 1.30, redundancy 0.87, spatial contiguity 0.79, modality 0.72, coherence 0.70, signalling 0.46 [RES] [C-23] [CONFLICT]. In practice: sync visuals to the spoken word, show keywords rather than the transcript, put labels on objects, and cut decoration and music under dense explanation.
- **End on a summary frame.** Animation is transient; finish an animated explanation on a static, comparable frame held long enough to read [RES] [C-45].
- **Holds.** Hold at least 1 s after any payoff [DOC] [A2-22]; brand or CTA holds of 2–8 s appear across the exemplars [DEMO] [G-02] [G-04].

#### Composition and safe areas

- 16:9 broadcast-safe: title 90 % × 90 %, action 93 % × 93 % (SMPTE ST 2046-1); EBU R 95 uses 5 % graphics-safe per edge. At 1920×1080 keep text 96 px from the sides and 54 px from top and bottom [STD] [C-31] [C-33].
- 9:16: Instagram Reels ads keep the top 14 %, bottom 35 % and sides 6 % clear; TikTok and YouTube publish templates rather than numbers [STD] [C-41] [C-44] [C-43]. A union "safe everywhere" box on 1080×1920 is x 120–780, y 288–1248, with burned-in captions ending around y 1248 [REC] [C-41].
- One focal point per moment; use a 12-column grid for 16:9 and 4–6 columns inside the 9:16 safe box [REC] [C-41]. Official video-medium scale: headlines 64–120 px, body 28–42 px, labels 18–24 px, padding 60–140 px on 1080p [DOC] [A2-29].
- Square and vertical: cut UI density roughly in half relative to 16:9 [DEMO] [G-05]; recompose, never crop the 16:9 master [REC].

#### Typography

- **Size.** Body text cap height ≥ 2.5 % of frame height (≥ 40–45 px at 1080p); ≥ 48–56 px on 1080×1920 [REC] [C-12] [C-67]. Official guardrails: full-screen viewing body ≥ 20 px, headline ≥ 60 px, labels ≥ 16 px; in-feed viewing body ≥ 32 px, headline ≥ 90 px, labels ≥ 24 px [DOC] [A2-31]. Use the larger figure for phones.
- **Hold time** for supers and titles: `max(1.5 s, 0.5 + 0.33 s × words)`, plus 0.5 s for numbers and 30–50 % more when voice or motion competes [REC] [C-67] [C-69]. The official test: "three seconds on screen must be readable in two" [DOC] [A2-31].
- **Lines.** ≤ 32–42 characters per line for 16:9 and ≤ 20–25 for 9:16; ≤ 2 lines landscape, ≤ 3 vertical [REC] [C-67] [C-69].
- **Faces.** At most two families; never two sans-serifs together; one expressive face per scene; weight contrast such as 300 against 900; tighten display tracking −0.03 to −0.05 em; avoid hairline weights below ~60 px; medium and semibold survive compression best [DOC] [A2-31] [REC] [C-13]. Question the official "monoculture" list of overused faces (Inter, Roboto, Poppins, Playfair Display and others) before using them [DOC] [A2-31].
- **Motion.** Never tween `fontSize` or `letterSpacing` [DOC] [A2-13]; give masks glyph room; use tabular numerals for counters [DOC] [A2-22].

#### Color, light and depth

- Contrast: text ≥ 4.5:1, large text ≥ 3:1, meaningful graphics ≥ 3:1 (WCAG 2.2) [STD] [C-37]; measure against the worst background frame or add a scrim [REC] [C-67]. `check` audits contrast automatically [DOC] [A1-14].
- One accent hue carrying meaning; tint neutrals toward it; avoid pure `#000` and `#fff`; same background across scenes [DOC] [A2-27]. Never rely on hue alone for meaning [STD] [C-37].
- Banding: 8-bit limited range gives about 220 luma steps; avoid long dark linear gradients, add 1–2 % noise, master at CRF ≤ 18 [REC] [C-34] [C-40] [DOC] [A2-29].
- 4:2:0 delivery halves chroma resolution: separate text from background by luminance, not hue [REC] [C-81].
- Depth: one global light direction; elevation through consistent shadow blur and offset; background blur 4–12 px at 1080p; focus pulls ≥ 500 ms; parallax with 2–4 planes and small amplitude [REC] [C-07] [C-77].
- Color tags: BT.709 for platform uploads; consider the sRGB transfer tag for self-hosted web embeds and test in Safari and Chrome [STD] [C-81] [DEMO] [C-39] [CONFLICT].

#### Motion and transitions

- Entrances `power3.out` (calm `power1/2`, punch `power4`/`expo`); exits `.in`; moves `.inOut`; overshoot only as a declared playful register [DOC] [A2-11].
- Durations by weight: 0.15–0.3 s urgency, 0.3–0.5 s professional, 0.5–0.8 s gravity, 0.8–2.0 s cinematic; entrances longer than exits; slowest scene about 3× the fastest [DOC] [A2-28]. Interface research suggests 100–500 ms for UI-scale moves, 200–300 ms typical [STD] [C-08]. At 30 fps a frame is 33 ms; avoid moves shorter than 6 frames unless they are cuts [REC] [C-45].
- Stagger totals ≤ 0.5 s, in order of importance [DOC] [A2-28]. Staggers bring little benefit for tracking data marks [RES] [C-47].
- Reveal on the voice across the later half of the scene; no idle breathing loops; one bounded breath at most on a held hero [DOC] [A2-24].
- Transitions: one primary for 60–70 % of cuts plus 1–2 accents; durations calm 0.5–0.8 s, medium 0.3–0.5 s, high energy 0.15–0.3 s; exits only on the final scene [DOC] [A2-06]. Velocity-match seams within about 5 % [DOC] [A2-30]. Blur only 1–3 snapping beats [DOC] [A2-09].
- Camera: zooms of 1.0–2.0 s starting after content lands, dwell ≥ 1 s [DOC] [A2-22]; cap camera moves at about 10–15 % of frame width per second for comfort [REC] [C-07].

#### Data in motion

- Keep each datum the same visual object through a change (object constancy); never morph one object into an unrelated one [RES] [C-45] [DEMO] [C-49].
- Stage complex changes; give each stage about 1 s; keep common scales; if rescaling is unavoidable, stage it and call it out [RES] [C-45].
- Slow-in/slow-out improves tracking [RES] [C-48]. Bars start at zero; truncated axes inflate perceived effects even when flagged [RES] [C-50]. No overshoot on data marks [REC].
- Count-ups 0.8–1.5 s with ease-out, then hold ≥ 1.5 s plus reading time; ≤ 5–7 animated series, one highlighted [REC] [C-45]. Official rule: pair every number with a visual; avoid pie charts, legends, gridlines and chart libraries in motion [DOC] [A2-36].

#### Accessibility and safety

- No more than 3 flashes in any 1-second period; no saturated-red flashes; flashing areas count when they exceed 25 % of a 10° field (≈ 21,824 px at 1024×768) [STD] [C-76] [C-78]. Automated tools do not guarantee broadcast compliance [DEMO] [C-94].
- Captions for prerecorded audio (WCAG 1.2.2, level A), including speaker identity and meaningful non-speech sound [STD] [C-37] [C-73].
- Vestibular comfort: 35.4 % of US adults over 40 showed vestibular dysfunction in one national study [RES] [C-80]; avoid full-frame spins, zoom tunnels and large parallax; keep a stable reference element [REC] [C-77] [C-07]. For looping web embeds, honour `prefers-reduced-motion` and provide pause controls when motion exceeds 5 s [STD] [C-37] [C-79].

#### Delivery

- Universal deliverable: MP4 with `+faststart`, H.264 High, 8-bit 4:2:0 `yuv420p`, closed GOP, constant frame rate, AAC-LC 48 kHz stereo, BT.709 tags, limited range [REC] [C-81] [C-87] [C-41]. HyperFrames' default MP4 already meets this except `faststart`, which matters only for progressive web playback [TESTED] [E-01].
- Upload above the target quality: YouTube recommends 8 Mbps at 1080p30 and 12 Mbps at 1080p60 for SDR [STD] [C-81].
- Platform limits change often; see Part 6 for the per-platform table.
