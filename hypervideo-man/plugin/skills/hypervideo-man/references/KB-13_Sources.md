# KB-13 — Sources (merged registries)

*Both registries are reproduced in full so that every evidence tag in KB-02…KB-11 resolves. Part I is Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026) §2.11 (official HyperFrames sources HF-n, practitioner sources P-n, external standards S-n, private materials). Part II is Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229) §8.7 (A1 platform, A2 motion/media/audio skills, B practice, G Gemini video analyses, C craft standards, D prompting and prior work, E hands-on lab, S direct reads). Local paths in Part II refer to the author's Windows machine on 1 Nov 2026.*

## 0. Dedupe statistics (computed over URLs, normalised by scheme, `www.`, trailing slash and fragment)

| Measure | Value |
|---|---|
| Rows in source A's registry | 171 |
| Rows in source B's registry | 276 |
| Distinct URLs in A | 176 |
| Distinct URLs in B | 155 |
| URLs cited by both | 21 |
| Distinct URLs across both | 310 |

Rows without a URL (local skill files, private documents, lab artefacts) are counted in the row totals but not in the URL counts.

### Sources both deliverables relied on

| URL (normalised) | Source A id | Source B id |
|---|---|---|
| https://andrew.ooo/posts/hyperframes-heygen-html-video-agents-review | P-25 | B-44 |
| https://bbc.co.uk/accessibility/forproducts/guides/subtitles | S15 | C-67 |
| https://developer.apple.com/design/human-interface-guidelines/motion | S8 | C-07 |
| https://developer.apple.com/design/human-interface-guidelines/typography | S21 | C-12 |
| https://getmasset.com/resources/blog/hyperframes-vs-remotion-review | P-7 | B-45 |
| https://hyperframes.heygen.com | HF-9 | B-02 |
| https://hyperframes.heygen.com/guides/hyperframes-vs-remotion | HF-33 | B-06 |
| https://nngroup.com/articles/animation-duration | S9 | C-08 |
| https://npmjs.com/package/hyperframes | HF-8 | A1-70 |
| https://onewave-ai.com/blog/hyperframes-video-as-code | P-5 | B-43 |
| https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements | S14 | C-68 |
| https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide | S13 | C-69 |
| https://podcasters.apple.com/support/893-audio-requirements | S57 | C-58 |
| https://support.google.com/google-ads/answer/16041697 | S31 | C-20 |
| https://support.google.com/youtube/answer/15424877 | S44 | C-83 |
| https://support.google.com/youtube/answer/1722171 | S49 | C-81 |
| https://support.spotify.com/us/artists/article/loudness-normalization | S56 | C-57 |
| https://tech.ebu.ch/docs/r/r128.pdf | S51 | C-53 |
| https://voyager.so/blog/hyperframes-vs-remotion | P-24 | B-47 |
| https://w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html | S71 | C-76 |
| https://wireflow.ai/blog/hyperframes-vs-remotion | P-27 | B-46 |

## Part I — Source A — “HyperFrames-Motion-Mastery-Skillgraph” (v1.0, 1 Nov 2026) §2.11

#### 2.11 Sources

##### A. Official HyperFrames sources (fetched 2026-11-01 unless noted)

| ID | Source | URL |
|---|---|---|
| HF-1 | GitHub repository (README, stats, templates) | https://github.com/heygen-com/hyperframes |
| HF-2 | GitHub Releases (v0.8.228, 2026-11-01) | https://github.com/heygen-com/hyperframes/releases |
| HF-3 | ADOPTERS.md | https://github.com/heygen-com/hyperframes/blob/main/ADOPTERS.md |
| HF-4 | Issue tracker | https://github.com/heygen-com/hyperframes/issues |
| HF-5 | Issues #1107, #3391, #3629, #4002, #6882 | https://github.com/heygen-com/hyperframes/issues/1107 · /3391 · /3629 · /4002 · /6882 |
| HF-6 | CLI skill references (preview-render, upgrade-info-misc) | https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes-cli/references/preview-render.md · …/upgrade-info-misc.md |
| HF-7 | Official SKILL.md (raw) | https://raw.githubusercontent.com/heygen-com/hyperframes/main/skills/hyperframes/SKILL.md |
| HF-8 | npm package page (stale cache on the research date) | https://www.npmjs.com/package/hyperframes |
| HF-9 | Documentation home | https://hyperframes.heygen.com/ |
| HF-10 | Introduction | https://hyperframes.heygen.com/introduction |
| HF-11 | CLI package reference | https://hyperframes.heygen.com/packages/cli |
| HF-12 | Developers: CLI | https://hyperframes.heygen.com/developers/cli |
| HF-13 | FAQ | https://hyperframes.heygen.com/faq |
| HF-14 | Help / troubleshooting | https://hyperframes.heygen.com/help |
| HF-15 | Concepts: compositions | https://hyperframes.heygen.com/concepts/compositions |
| HF-16 | Concepts: data attributes | https://hyperframes.heygen.com/concepts/data-attributes |
| HF-17 | Concepts: determinism | https://hyperframes.heygen.com/concepts/determinism |
| HF-18 | Concepts: variables; frame adapters | https://hyperframes.heygen.com/concepts/variables · https://hyperframes.heygen.com/concepts/frame-adapters |
| HF-19 | Reference: HTML schema | https://hyperframes.heygen.com/reference/html-schema |
| HF-20 | Reference: audio effects | https://hyperframes.heygen.com/reference/audio-effects |
| HF-21 | Quickstart | https://hyperframes.heygen.com/quickstart |
| HF-22 | Guides: rendering; media | https://hyperframes.heygen.com/guides/rendering · https://hyperframes.heygen.com/guides/media |
| HF-23 | Guides: performance | https://hyperframes.heygen.com/guides/performance |
| HF-24 | Studio app overview | https://hyperframes.heygen.com/studio-app |
| HF-25 | Studio app: first video | https://hyperframes.heygen.com/studio-app/first-video |
| HF-26 | Studio app: edit with the agent | https://hyperframes.heygen.com/studio-app/edit-with-the-agent |
| HF-27 | Studio app: export | https://hyperframes.heygen.com/studio-app/export |
| HF-28 | Examples / inspiration wall | https://hyperframes.heygen.com/examples |
| HF-29 | Catalog | https://hyperframes.heygen.com/catalog |
| HF-30 | Changelog | https://hyperframes.heygen.com/changelog |
| HF-31 | Prompting guide: product launch | https://hyperframes.heygen.com/prompting/product-launch |
| HF-32 | Guide: product launch video | https://hyperframes.heygen.com/guides/product-launch-video |
| HF-33 | Guide: HyperFrames vs Remotion | https://hyperframes.heygen.com/guides/hyperframes-vs-remotion |
| HF-34 | Guides: skills; MCP; authentication; Figma | https://hyperframes.heygen.com/guides/skills · /guides/mcp · /guides/authentication · /guides/figma |
| HF-35 | Lessons | https://hyperframes.heygen.com/lessons |
| HF-36 | Deploy: overview; cloud | https://hyperframes.heygen.com/deploy/overview · https://hyperframes.heygen.com/deploy/cloud |
| HF-37 | Deploy: AWS Lambda | https://hyperframes.heygen.com/deploy/aws-lambda |
| HF-38 | Docs index (llms.txt) | https://hyperframes.heygen.com/llms.txt |
| HF-39 | Desktop app changelog | https://hyperframes.studio/changelog |
| HF-40 | Community playground / sign-in | https://hyperframes.dev |
| HF-41 | HeyGen research post: HTML to video (James Russo, 2026-06-22) | https://www.heygen.com/research/html-to-video |
| HF-42 | HeyGen help: HyperFrames × HeyGen | https://help.heygen.com/en/articles/15001510-hyperframes-x-heygen |
| HF-43 | HeyGen developers: HyperFrames overview | https://developers.heygen.com/hyperframes-overview |
| HF-44 | Local workspace copy of the official skills (`hyperframes`, `hyperframes-core`, `hyperframes-creative`, `media-use`), read 2026-11-01 | (local files; M365 copy) |
| HF-45 | Look-alike (unofficial): hyperframes.app | https://hyperframes.app/ |
| HF-46 | Look-alike (unofficial): hyperframes.net | https://hyperframes.net/blog/is-hyperframes-free |
| HF-47 | Unrelated product: hyper-frames.com | https://hyper-frames.com/ |
| HF-48 | Unofficial GitHub org | https://github.com/hyperframes/hyperframes |

##### B. Practitioner, community and analysis sources (R2)

| ID | Source (author, date) | URL |
|---|---|---|
| P-1 | Official skill SKILL.md as fetched (may predate the 21→7 consolidation) | https://raw.githubusercontent.com/heygen-com/hyperframes/main/skills/hyperframes/SKILL.md |
| P-2 | HeyGen launch film repo: storyboard, handoff (HANDOFF dated 2026-04-15) | https://github.com/heygen-com/hyperframes-launches/tree/main/hyperframes-launch · …/STORYBOARD.md · …/HANDOFF.md |
| P-3 | Website → HyperFrames demo storyboard | https://github.com/heygen-com/hyperframes-launches/blob/main/website-to-hyperframes/STORYBOARD.md |
| P-4 | hyperframes-launches repo root | https://github.com/heygen-com/hyperframes-launches |
| P-5 | OneWave, "HyperFrames: video as code" (OneWave Team, 2026-09-04) | https://www.onewave-ai.com/blog/hyperframes-video-as-code |
| P-6 | Anfloy, product launch videos with Claude Code (Dima Bilous, 2026-10-27) | https://www.anfloy.com/blog/product-launch-videos-claude-code |
| P-7 | Masset, HyperFrames vs Remotion review (Benjamin Ard, 2026-06-30) | https://www.getmasset.com/resources/blog/hyperframes-vs-remotion-review |
| P-8 | working-ref library: HyperFrames, Oct 2026 (JetBrains, Social SDK, Nedalba, Blockout reports; YouTube comments) | https://www.working-ref.com/en/library/hyperframes-2026-10 |
| P-9 | HeyGen research post (James Russo, 2026-06-22) | https://www.heygen.com/research/html-to-video |
| P-10 | Official prompting guide (Linear.app example) | https://hyperframes.heygen.com/prompting/product-launch |
| P-11 | Alem Tuzlak, hyperframes-video skill (TanStack) | https://github.com/AlemTuzlak/skills/tree/main/skills/hyperframes-video |
| P-12 | dev.to: product launch video with Claude Code and HyperFrames | https://dev.to/dedupedai/how-to-make-a-product-launch-video-with-claude-code-and-hyperframes-html-to-mp4-1ab5 |
| P-13 | launchvideo.com record of the Studio script-editing post (2026-10-23) | https://www.launchvideo.com/directory/hyperframes-studio-script-editing |
| P-14 | Prompt Motion: Remotion vs HyperFrames (2026-10-10) | https://prompt-motion.com/blog/remotion-vs-hyperframes |
| P-15 | Prompt Motion: make AI motion graphics look less AI; AI launch video prompts | https://prompt-motion.com/blog/make-ai-motion-graphics-look-less-ai · https://prompt-motion.com/blog/ai-launch-video-prompts |
| P-16 | ToolRevealed: HyperFrames MCP with Claude (2026-07-27) | https://toolrevealed.com/hyperframes-mcp-claude/ |
| P-17 | PracticalyAI (YouTube) | https://www.youtube.com/watch?v=QJWRMtkZ-4o |
| P-18 | Aqib Mehmood (YouTube) | https://www.youtube.com/watch?v=l7lNODvRTw4 |
| P-19 | JQ Visions summary of Peter Yang's Jake Moran interview (2026-10-27 / 2026-10-25) | https://visions.joaoqueiros.com/blog/claude-hyperframes-video-editing-jake-moran-guide/ |
| P-20 | Tenex, HyperFrames Studio guide (Anthony Dupont-Cinko, 2026-10-09) | https://www.tenex.co/blog/hyperframes-studio-guide |
| P-21 | MartianLee, HyperFrames architecture (SeongHwa Lee, 2026-10-07) | https://martianlee.github.io/posts/2026-10-07-hyperframes-architecture |
| P-22 | User report "Ayo" via working-ref (captions missing in render) | https://www.working-ref.com/en/library/hyperframes-2026-10 |
| P-23 | Nihar Daily: render timings and pricing (Nihar Ranjan Das, 2026-10-17) | https://www.nihardaily.com/posts/remotion-vs-hyperframes-we-timed-renders-and-priced-both |
| P-24 | Voyager: HyperFrames vs Remotion (Anvisha Pai, 2026-09-21) | https://voyager.so/blog/hyperframes-vs-remotion |
| P-25 | andrew.ooo review (2026-05-28) | https://andrew.ooo/posts/hyperframes-heygen-html-video-agents-review/ |
| P-26 | URLtoVideo: HTML to video explained (2026-04-19) | https://urltovideo.com/blog/hyperframes-html-to-video-explained |
| P-27 | Wireflow: HyperFrames vs Remotion | https://www.wireflow.ai/blog/hyperframes-vs-remotion |
| P-28 | Other comparisons and reviews (openskills, arceapps, topaiskills, kompozy, autoae, claudevideo) | https://openskills.app/guides/hyperframes-vs-remotion · https://arceapps.com/blog/hyperframes-vs-remotion-2026/ · https://topaiskills.com/tutorials/comparison/hyperframes-vs-remotion/ · https://kompozy.io/reviews/heygen-hyperframes · https://autoae.online/blog/hyperframes-for-marketers · https://claudevideo.org/guides/hyperframes-remotion-claude-code |
| P-29 | Contradicted by official docs (cite with caution) | https://todayforai.com/en/guides/20260728-guide-code-video-framework-selection · https://softreviewed.com/gsap-vs-hyperframes-vs-remotion/ |
| P-30 | Hacker News posts (negligible engagement) | https://news.ycombinator.com/item?id=47902856 · …/47797513 · …/47822361 |
| P-31 | YouTube: HeyGen official tutorial; demos and tutorials (Kacper Rutkiewicz, Mike Murphy, Prashant, uncredited) | https://www.youtube.com/watch?v=qiek-fBv924 · …/mQmyQZRGQJ4 · …/GBlJEJUlUmg · …/c7y09NIzxbE · …/7DdqzHtnEuY · …/stk9nWQOhpE |
| P-32 | creativeaishow.com (2026-10-10) | https://creativeaishow.com/hyperframes-is-free-and-apache-2-0-turn-html-into-motion-graphics-video-with-your-ai-agent/ |

##### C. External standards, research and practitioner sources (R3)

† = access date (page undated).

| # | Publisher | Date / version | URL | Tag |
|---|---|---|---|---|
| S1 | Google M3 tokens | legacy | https://m3.material.io/styles/motion/easing-and-duration/tokens-specs | DOCUMENTED |
| S2 | Google M3 easing | legacy | https://m3.material.io/styles/motion/easing-and-duration/applying-easing-and-duration | DOCUMENTED |
| S3 | Google M3 physics | May 2025 | https://m3.material.io/styles/motion/overview/how-it-works | DOCUMENTED |
| S4 | Google M3 specs | 2025–26 | https://m3.material.io/styles/motion/overview/specs | DOCUMENTED |
| S5 | Google Material 1 | M1/legacy | https://m1.material.io/motion/duration-easing.html | DOCUMENTED |
| S6 | Google Material 2 | M2/legacy | https://m2.material.io/guidelines/motion/duration-easing.html | DOCUMENTED |
| S7 | IBM Carbon | 2026-08-12 | https://carbondesignsystem.com/elements/motion/overview/ | DOCUMENTED |
| S8 | Apple HIG Motion | 2025-09-09 | https://developer.apple.com/design/human-interface-guidelines/motion | DOCUMENTED |
| S9 | NN/g | 2020-02-09 | https://www.nngroup.com/articles/animation-duration/ | PRACTITIONER |
| S10 | Lasseter, SIGGRAPH | 1987 | https://www.cs.northwestern.edu/~animation/Lasseter_1987.pdf | RESEARCH |
| S11 | ACM SIGGRAPH Education | n.d. | https://education.siggraph.org/static/Drupal_2025/education.siggraph.org/static/HyperGraph/animation/character_animation/principles/prin_trad_anim.html | PRACTITIONER |
| S12 | Makiola (blog) | 2026-09-20 | https://jeanlucmakiola.de/blog/material-3-expressive-compose/ | PRACTITIONER |
| S13 | Netflix EN-US TTSG | 2025-12-19 | https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide | DOCUMENTED |
| S14 | Netflix TTSG General | 2022-10-07 | https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements | DOCUMENTED |
| S15 | BBC Subtitle Guidelines | v1.2.3+ | https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/ | DOCUMENTED |
| S16 | Broadcast Writer (BBC copy) | 2024-12-12 | https://broadcastwriter.com/2024/12/12/bbc-subtitle-style-guide-2024/ | DOCUMENTED (copy) |
| S17 | DCMP Captioning Key | current | https://dcmp.org/learn/601 | DOCUMENTED |
| S18 | SubtitleGenerator | 2026 | https://subtitlegenerator.app/guides/subtitle-guidelines | PRACTITIONER |
| S19 | W3C WCAG 1.4.3 | WCAG 2.2 | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html | DOCUMENTED |
| S20 | EBU R 95 | v1.1/2017-06 | https://tech.ebu.ch/docs/r/r095.pdf | DOCUMENTED |
| S21 | Apple HIG Typography | 2025-12-16 | https://developer.apple.com/design/human-interface-guidelines/typography | DOCUMENTED |
| S22 | legibility.info | n.d. | https://legibility.info/rules-for-text-in-videos | PRACTITIONER |
| S23 | CapsAI | 2026-10-26 | https://capsai.co/blogs/subtitle-font-size-for-reels-shorts-and-tiktok | PRACTITIONER |
| S24 | Blitzcut | 2026-05-22 | https://blitzcutai.com/blog/best-caption-size-tiktok-2026 | PRACTITIONER |
| S25 | TikTok Ads specs | 2026-06 | https://ads.tiktok.com/resources/help/article/tiktok-auction-in-feed-ads?lang=en | DOCUMENTED |
| S26 | AdCheckLab (TikTok) | 2026-09 | https://adchecklab.com/articles/tiktok-ad-specs | PRACTITIONER |
| S27 | EzUGC | 2026-08-01 | https://www.ezugc.ai/blog/tiktok-safe-zones-guide | PRACTITIONER |
| S28 | Apogee | 2026-10-14 | https://www.apogee.ad/en/blog/meta-ads-safe-zones/ | PRACTITIONER |
| S29 | Jem Social | 2026-10-25 | https://www.jem.social/blog/instagram-reels-safe-zone | PRACTITIONER |
| S30 | Google Ads specs | 2026-11† | https://support.google.com/google-ads/answer/13547298 | DOCUMENTED |
| S31 | Google Shorts ads | 2026-11† | https://support.google.com/google-ads/answer/16041697 | DOCUMENTED |
| S32 | AdCheckLab (Shorts) | 2026-09 | https://adchecklab.com/articles/youtube-shorts-safe-area-dimensions | PRACTITIONER |
| S33 | Anglr | 2026-10-12 | https://anglr.co/tools/youtube-shorts-safe-zone | PRACTITIONER |
| S34 | Cutting, Psych. Sci. | 2010 | https://www.psychologicalscience.org/journals/psychological-science/0956797610361679/ | RESEARCH |
| S35 | Cutting, i-Perception | 2011 | https://journals.sagepub.com/doi/pdf/10.1068/i0441aap | RESEARCH |
| S36 | MacLachlan & Logan, JAR | 1993 | https://www.thefreelibrary.com/Camera+shot+length+in+TV+commercials+and+their+memorability+and...-a013980912 | RESEARCH |
| S37 | Lang, JOBEM | 2000 | https://scholars.cityu.edu.hk/en/publications/the-effects-of-edits-on-arousal-attention-and-memory-for-televisi/ | RESEARCH |
| S38 | Lang, JOBEM | 1999 | https://scite.ai/reports/the-effects-of-production-pacing-GvOplJ | RESEARCH |
| S39 | Facebook/Nielsen | 2016-02 | https://www.tayloegray.com/2016/02/capture-attention-with-updated-features-for-video-ads/ | RESEARCH (vendor) |
| S40 | TikTok Creative Codes | 2026-11† | https://ads.tiktok.com/business/en-US/blog/creative-best-practices-top-performing-ads | RESEARCH (vendor) |
| S41 | TikTok guide | 2024-11-24 | https://ads.tiktok.com/business/en-US/blog/tiktok-short-video-best-practice | DOCUMENTED |
| S42 | Guo et al., L@S | 2014 | https://dl.acm.org/doi/epdf/10.1145/2556325.2566239 | RESEARCH |
| S43 | Wistia | 2025-07-01 | https://wistia.com/blog/optimal-video-length | RESEARCH (vendor) |
| S44 | YouTube Help | 2024-10-15 | https://support.google.com/youtube/answer/15424877 | DOCUMENTED |
| S45 | The Verge | 2025-01-18 | https://www.theverge.com/2025/1/18/24346567/instagram-announces-reels-3-minute-video-posts | DOCUMENTED (news) |
| S46 | Variety | 2024-10-03 | https://variety.com/2024/digital/news/youtube-shorts-maximum-video-length-three-minutes-1236166349/ | DOCUMENTED (news) |
| S47 | LinkedIn specs | 2026-11† | https://business.linkedin.com/advertise/ads/sponsored-content/video-ads/specs | DOCUMENTED |
| S48 | Sume (X specs) | 2026-09-28 | https://www.sume.com/guides/x-twitter-video-ad-specs | PRACTITIONER |
| S49 | YouTube encoding | 2026-11† | https://support.google.com/youtube/answer/1722171 | DOCUMENTED |
| S50 | MarketerTools | 2026-06-28 | https://www.marketertools.fyi/blog/meta-ad-sizes-safe-zones-2026 | PRACTITIONER |
| S51 | EBU R 128 | v5.0/2023-11 | https://tech.ebu.ch/docs/r/r128.pdf | DOCUMENTED |
| S52 | EBU R 128 s1 | v3/2020-08 | https://tech.ebu.ch/docs/r/r128s1.pdf | DOCUMENTED |
| S53 | ATSC A/85 | 2026-07-08 | https://www.atsc.org/wp-content/uploads/2026/07/A85-2026-07-Annex-M.pdf | DOCUMENTED |
| S54 | AES TD1008 | 2021-09-24 | https://www.aes.org/wp-content/uploads/2026/10/20210924_TD1008_v3.13.pdf | DOCUMENTED |
| S55 | AES loudness refs | AES77-2023 | https://www.aes.org/resources/audio-topics/loudness-project/resources-and-references/ | DOCUMENTED |
| S56 | Spotify | 2026-11† | https://support.spotify.com/us/artists/article/loudness-normalization/ | DOCUMENTED |
| S57 | Apple Podcasts | 2026-11† | https://podcasters.apple.com/support/893-audio-requirements | DOCUMENTED |
| S58 | Netflix sound spec | current | https://studiopartner.netflix.net/studio/branded-sound-mix-spec-and-best-practices | DOCUMENTED |
| S59 | LOUDMETER | 2026-09 | https://www.loudmeter.net/youtube-loudness | PRACTITIONER |
| S60 | Valmera | 2026-10-06 | https://valmera.io/tools/audio-loudness-targets | PRACTITIONER |
| S61 | W3C WCAG 1.4.7 | WCAG 2.2 | https://www.w3.org/WAI/WCAG22/Understanding/low-or-no-background-audio.html | DOCUMENTED |
| S62 | Torcoli et al., JAES | 2019 | https://www.aes.org/publications/elibrary-page/?id=20711 | RESEARCH |
| S63 | Moreno & Mayer | 2000 | https://psycnet.apa.org/psycinfo/2000-03003-010 | RESEARCH |
| S64 | Mayer et al. | 2001 | https://psycnet.apa.org/getdoi.cfm?doi=10.1037/0022-0663.93.1.187 | RESEARCH |
| S65 | Mora Velasco & Hirumi | 2020 | https://link.springer.com/article/10.1007/s11423-020-09783-4 | RESEARCH |
| S66 | Oakes, JAR | 2007 | https://www.warc.com/en/article/evaluating-empirical-research-into-music-in-advertising%3A-a-congruity-perspective-22e9109b57034a3a9429793af504ff1c | RESEARCH |
| S67 | Otterbeck, Cont. Islam | 2008 | https://link.springer.com/article/10.1007/s11562-008-0062-y | RESEARCH |
| S68 | Otterbeck & Ackfeldt | 2012 | https://link.springer.com/article/10.1007/s11562-012-0220-0 | RESEARCH |
| S69 | Chabad.org | n.d. | https://www.chabad.org/library/article_cdo/aid/277597/jewish/Omer-Mourning-Observances.htm | PRACTITIONER |
| S70 | Meshiv Kahalachah | 2024 | https://meshiv.co.il/en/shelot_vetshuvot/listening-to-vocal-music-during-the-days-of-sefirat-haomer/ | PRACTITIONER |
| S71 | W3C WCAG 2.3.1 | WCAG 2.2 | https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html | DOCUMENTED |
| S72 | W3C WCAG 2.3.2 | draft | https://w3c.github.io/wcag/understanding/three-flashes | DOCUMENTED |
| S73 | ITC/Ofcom | 2001/2002 | https://www.ofcom.org.uk/siteassets/resources/documents/tv-radio-and-on-demand/broadcast-guidance/gn_flash.pdf | DOCUMENTED |
| S74 | ITU-R BT.1702-3 | 2023-11 | https://www.itu.int/rec/R-REC-BT.1702-3-202311-I | DOCUMENTED |
| S75 | HardingFPA (CRS) | v6 | https://www.hardingfpa.com/ | PRACTITIONER |
| S76 | Epilepsy Foundation | 2026-11† | https://www.epilepsy.com/what-is-epilepsy/seizure-triggers/photosensitivity | PRACTITIONER |
| S77 | Epilepsia consensus | 2025 | https://www.visualstress.info/2025-288.pdf | RESEARCH |
| S78 | NEI (NIH) | 2026-11† | https://www.nei.nih.gov/eye-health-information/eye-conditions-and-diseases/color-blindness | DOCUMENTED |
| S79 | FigEditor | 2026-08-18 | https://figeditor.com/blog/okabe-ito-palette | PRACTITIONER |
| S80 | Google Ads ABCDs | 2021 | https://support.google.com/google-ads/answer/14783551 | DOCUMENTED |
| S81 | Think with Google | 2022-04 | https://business.google.com/en-all/think/future-of-marketing/youtube-video-ad-creative/ | RESEARCH (vendor) |
| S82 | Iwamoto, PCHARM | n.d. | https://ojs.library.carleton.ca/index.php/pcharm/article/view/4340/3310 | RESEARCH |
| S83 | StudioBinder | 2025-05-16 | https://www.studiobinder.com/blog/dan-harmon-story-circle/ | PRACTITIONER |
| S84 | Throughline | 2026-10-19 | https://getthroughline.com/learn/dan-harmon-story-circle/ | PRACTITIONER |
| S85 | Copywriting School | 2026-06 | https://copywriting.school/formulas/bab | PRACTITIONER |
| S86 | dataviz-codex (Tufte) | n.d. | https://github.com/williamrthomas/dataviz-codex/blob/master/principles/data-ink-ratio.md | PRACTITIONER |
| S87 | storytelling with data | n.d. | https://www.storytellingwithdata.com/blog/two-tips-for-better-graphs | PRACTITIONER |
| S88 | Business Floss | n.d. | https://www.businessfloss.com/books/storytelling-with-data | PRACTITIONER |
| S89 | Heer & Robertson | 2007 | http://vis.stanford.edu/files/2007-AnimatedTransitions-InfoVis.pdf | RESEARCH |
| S90 | Robertson et al. | 2008 | https://www.microsoft.com/en-us/research/publication/effectiveness-of-animation-in-trend-visualization/ | RESEARCH |
| S91 | Pandey et al., CHI | 2015 | https://dl.acm.org/doi/epdf/10.1145/2702123.2702608 | RESEARCH |

##### D. Private materials supplied by the author (read 2026-11-01)

HyperFrames-Master-Prompt-Checklist (.md/.html/.pdf, 18 pp.) · HyperFrames_Master_Prompt_Checklist (.html/.pdf, 17 pp.) · HyperFrames-Showreel-Standard (.html/.pdf, 19 pp.) · Hyperframes_Expert_Motion_Prompt field guide (.html/.pdf, 16 pp., dated 1 Nov 2026) · Hyperframe Motion Design Master Checklist & Prompt Specification (.pdf, 6 pp.) · hyperframe_interactive_prompt_studio_specification (.html). Internal productions referenced as exemplars: "The Price of AI" (2:27, Oct 2026), "Marche avec moi" (59 s, Oct 2026), "Journal IA, semaine 42" (11:50, Oct 2026).

## Part II — Source B — “HyperFrames-Motion-Mastery” (Claude Code, 1 Nov 2026; CLI lab on hyperframes 0.8.229) §8.7

### 8.7 Source registry

**Evidence legend.** [DOC] official HeyGen or vendor documentation, repository or official skills · [STD] official standard or platform specification · [RES] peer-reviewed research · [DEMO] demonstrated practitioner practice · [TESTED] reproduced on this machine · [PRIOR] the user's earlier documents · [REC] this document's recommendation · [CONFLICT] sources disagree · [UNVERIFIED] could not be confirmed.

**ID prefixes.** A1 platform research · A2 official motion, media and audio skills, Herk Edit Kit · B practitioner practice and exemplars · G Gemini video analyses · C craft standards · D prompting research and prior-work audit · E hands-on lab · S sources read directly for this document. All were accessed on 2026-11-01. Research notes are in `research-notes/` next to this document.

| ID | Source | Location | Publisher / author | Version or date |
|---|---|---|---|---|
| A1-02 | hyperframes-core SKILL.md | C:\Users\cwako\.claude\skills\hyperframes-core\SKILL.md | HeyGen | 2026-10-21 |
| A1-04 | data-attributes.md | C:\Users\cwako\.claude\skills\hyperframes-core\references\data-attributes.md | HeyGen | 2026-10-21 |
| A1-05 | determinism-rules.md | C:\Users\cwako\.claude\skills\hyperframes-core\references\determinism-rules.md | HeyGen | 2026-10-21 |
| A1-06 | tracks-and-clips.md | C:\Users\cwako\.claude\skills\hyperframes-core\references\tracks-and-clips.md | HeyGen | 2026-10-21 |
| A1-07 | sub-compositions.md | C:\Users\cwako\.claude\skills\hyperframes-core\references\sub-compositions.md | HeyGen | 2026-10-21 |
| A1-08 | variables-and-media.md | C:\Users\cwako\.claude\skills\hyperframes-core\references\variables-and-media.md | HeyGen | 2026-10-21 |
| A1-10 | creator-editing-recipes.md | C:\Users\cwako\.claude\skills\hyperframes-core\references\creator-editing-recipes.md | HeyGen | 2026-10-21 |
| A1-12 | hyperframes-cli SKILL.md | C:\Users\cwako\.claude\skills\hyperframes-cli\SKILL.md | HeyGen | 2026-10-21 |
| A1-13 | preview-render.md | C:\Users\cwako\.claude\skills\hyperframes-cli\references\preview-render.md | HeyGen | 2026-10-21 |
| A1-14 | lint-validate-inspect.md | C:\Users\cwako\.claude\skills\hyperframes-cli\references\lint-validate-inspect.md | HeyGen | 2026-10-21 |
| A1-15 | init-and-scaffold.md | C:\Users\cwako\.claude\skills\hyperframes-cli\references\init-and-scaffold.md | HeyGen | 2026-10-21 |
| A1-16 | doctor-browser.md | C:\Users\cwako\.claude\skills\hyperframes-cli\references\doctor-browser.md | HeyGen | 2026-10-21 |
| A1-19 | lambda.md | C:\Users\cwako\.claude\skills\hyperframes-cli\references\lambda.md | HeyGen | 2026-10-21 |
| A1-20 | cloudrun.md | C:\Users\cwako\.claude\skills\hyperframes-cli\references\cloudrun.md | HeyGen | 2026-10-21 |
| A1-21 | compare-and-batch.md + beats.md | C:\Users\cwako\.claude\skills\hyperframes-cli\references\ | HeyGen | 2026-10-21 |
| A1-22 | hyperframes-studio SKILL.md | C:\Users\cwako\.claude\skills\hyperframes-studio\SKILL.md | HeyGen | 2026-10-21 |
| A1-25 | Skill install lock (source, hashes, installedAt/updatedAt) | C:\Users\cwako\.agents\.skill-lock.json | skills CLI | v3; entries 2026-07-03 / 2026-10-21 |
| A1-30 | README.md | https://github.com/heygen-com/hyperframes/blob/main/README.md | HeyGen | main, 2026-11-01 |
| A1-32 | Upstream /hyperframes SKILL.md | https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/SKILL.md | HeyGen | main (post-#5651) |
| A1-33 | Upstream format.md | https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/references/format.md | HeyGen | main |
| A1-34 | Upstream runtimes.md | https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/references/runtimes.md | HeyGen | main |
| A1-35 | Upstream /hyperframes-cli SKILL.md + refs (conventions, cloud, preview-render, lint-validate-inspect, init-and-scaffold) | https://github.com/heygen-com/hyperframes/tree/main/skills/hyperframes-cli | HeyGen | main |
| A1-36 | Git tree of main (skills/ listing) | https://api.github.com/repos/heygen-com/hyperframes/git/trees/main?recursive=1 | GitHub API | 2026-11-01 |
| A1-37 | Commit 688229314 "publish seven knowledge skills… retire the workflow skills (#5651)"; compare v0.8.184…v0.8.185 | https://github.com/heygen-com/hyperframes/commit/688229314 | HeyGen | 2026-10-21T19:19Z |
| A1-38 | Changelog (release archive v0.6.52–v0.8.229) | https://github.com/heygen-com/hyperframes/blob/main/docs/changelog.mdx | HeyGen | 2026-11-01 |
| A1-39 | Weekly updates (Week of Oct 19, 2026) | https://github.com/heygen-com/hyperframes/blob/main/docs/weekly-updates.mdx | HeyGen | 2026-10-26 digest |
| A1-40 | How a HyperFrames project works | https://github.com/heygen-com/hyperframes/blob/main/docs/concepts/index.mdx | HeyGen | main |
| A1-41 | Deterministic Rendering | https://github.com/heygen-com/hyperframes/blob/main/docs/concepts/determinism.mdx | HeyGen | main |
| A1-44 | HTML schema reference | https://github.com/heygen-com/hyperframes/blob/main/docs/reference/html-schema.mdx | HeyGen | main |
| A1-45 | Lint rules (141 codes) | https://github.com/heygen-com/hyperframes/blob/main/docs/reference/lint-rules.mdx | HeyGen | main |
| A1-46 | Render from the command line | https://github.com/heygen-com/hyperframes/blob/main/docs/guides/rendering.mdx | HeyGen | main |
| A1-48 | 4K rendering | https://github.com/heygen-com/hyperframes/blob/main/docs/guides/4k-rendering.mdx | HeyGen | main |
| A1-49 | Render HDR video | https://github.com/heygen-com/hyperframes/blob/main/docs/guides/hdr.mdx | HeyGen | main |
| A1-52 | Cloud rendering | https://github.com/heygen-com/hyperframes/blob/main/docs/deploy/cloud.mdx | HeyGen | main |
| A1-53 | Create through an AI chat (MCP) | https://github.com/heygen-com/hyperframes/blob/main/docs/guides/mcp.mdx | HeyGen | main |
| A1-54 | Install and update agent skills | https://github.com/heygen-com/hyperframes/blob/main/docs/guides/skills.mdx | HeyGen | main |
| A1-55 | Install the HyperFrames plugin | https://github.com/heygen-com/hyperframes/blob/main/docs/guides/plugins.mdx | HeyGen | main |
| A1-56 | Troubleshooting | https://github.com/heygen-com/hyperframes/blob/main/docs/help.mdx | HeyGen | main |
| A1-57 | FAQ | https://github.com/heygen-com/hyperframes/blob/main/docs/faq.mdx | HeyGen | main |
| A1-60 | @hyperframes/producer | https://github.com/heygen-com/hyperframes/blob/main/docs/packages/producer.mdx | HeyGen | main |
| A1-63 | Edit in the browser editor | https://github.com/heygen-com/hyperframes/blob/main/docs/studio/index.mdx | HeyGen | main |
| A1-64 | Install the Studio app | https://github.com/heygen-com/hyperframes/blob/main/docs/studio-app/index.mdx | HeyGen | main |
| A1-70 | npm metadata `hyperframes` (`npm view`) | https://www.npmjs.com/package/hyperframes | HeyGen (npm) | 0.8.229 |
| A1-71 | npm publish timeline (`npm view hyperframes time`) | https://registry.npmjs.org/hyperframes | npm registry | 581 versions |
| A1-72 | Scoped @hyperframes/* versions (`npm view`) | https://www.npmjs.com/org/hyperframes | npm registry | 0.8.229 |
| A1-73 | GitHub repo metadata | https://api.github.com/repos/heygen-com/hyperframes | GitHub API | 2026-11-01 |
| A1-75 | hyperframes@0.8.229 package dist (pinned Chrome constants, env var names) | C:\Users\cwako\AppData\Local\npm-cache\_npx\14c72154496ec8ad\node_modules\hyperframes\dist\ | HeyGen | 0.8.229 |
| A1-80 | CLI `--help` captures, v0.8.229 [TESTED] | C:\Users\cwako\AppData\Local\Temp\claude\C--Users-cwako--claude-spares-spare-189Aid\42df6680-5621-46a1-9dfd-2fada7d345dd\scratchpad\research\help\ | own run | 2026-11-01 |
| A1-81 | CLI `--help` captures, v0.7.109 (Herk pin) [TESTED] | C:\Users\cwako\AppData\Local\Temp\claude\C--Users-cwako--claude-spares-spare-189Aid\42df6680-5621-46a1-9dfd-2fada7d345dd\scratchpad\research\help\v07109\ | own run | 2026-11-01 |
| A1-85 | HeyGen HyperFrames hosted MCP: server instructions + tool schemas (compose, render_video, get_project_status, get_render_status, list_projects, get-send-to-hyperframes-guide) | https://mcp.heygen.com/mcp/hyperframes/ (as connected in this session) | HeyGen | observed 2026-11-01 |
| A1-92 | Herk vendored hyperframes SKILL.md + NOTICE.txt | C:\Users\cwako\herk-edit-kit\.claude\skills\hyperframes\ | HeyGen, adapted by Herk Edit Kit | kit HEAD 2026-10-14 |
| A2-01 | hyperframes-animation SKILL | `...\.claude\skills\hyperframes-animation\SKILL.md` | HeyGen | no version; file 2026-10-21 |
| A2-02 | Visual Techniques Reference | `...\hyperframes-animation\techniques.md` | HeyGen | no version |
| A2-03 | Rules Index | `...\hyperframes-animation\rules-index.md` | HeyGen | no version |
| A2-04 | Blueprints index | `...\hyperframes-animation\blueprints-index.md` | HeyGen | no version |
| A2-05 | Transition Registry | `...\hyperframes-animation\transitions\TRANSITION-REGISTRY.md` | HeyGen | prototype verified 2026-05-31 |
| A2-06 | Scene Transitions overview | `...\hyperframes-animation\transitions\overview.md` | HeyGen | no version |
| A2-07 | Transition Catalog | `...\hyperframes-animation\transitions\catalog.md` | HeyGen | no version |
| A2-09 | Motion blur reference | `...\hyperframes-animation\references\motion-blur.md` | HeyGen | no version |
| A2-10 | HyperFrames GSAP adapter | `...\hyperframes-animation\adapters\gsap.md` | HeyGen | GSAP 3.14.2 CDN |
| A2-11 | Easing, Stagger, Function-Based Values | `...\adapters\gsap-easing-and-stagger.md` | HeyGen | no version |
| A2-13 | Transforms and Performance | `...\adapters\gsap-transforms-and-perf.md` | HeyGen | no version |
| A2-14 | Lottie adapter | `...\adapters\lottie.md` | HeyGen | lottie-web 5.12.2 |
| A2-15 | Three.js adapter | `...\adapters\three.md` | HeyGen | three 0.181.2 |
| A2-16 | CSS Animations adapter | `...\adapters\css-animations.md` | HeyGen | no version |
| A2-17 | WAAPI adapter | `...\adapters\waapi.md` | HeyGen | no version |
| A2-18 | Anime.js adapter | `...\adapters\animejs.md` | HeyGen | animejs 4.5.0 |
| A2-19 | TypeGPU / WebGPU adapter | `...\adapters\typegpu.md` | HeyGen | no version |
| A2-21 | HTML-in-Canvas Patterns | `...\adapters\html-in-canvas-patterns.md` | HeyGen | three 0.181.2 |
| A2-22 | Rules folder (48 rules; 21 read) | `...\hyperframes-animation\rules\*.md` | HeyGen | no version |
| A2-23 | Blueprints folder (22; 9 read) | `...\hyperframes-animation\blueprints\*.md` | HeyGen | no version |
| A2-24 | Motion language doctrine | `...\product-launch-video\references\motion-language.md` | HeyGen | no version |
| A2-25 | Sub-compositions; determinism rules | `...\hyperframes-core\references\sub-compositions.md`, `determinism-rules.md` | HeyGen | no version |
| A2-26 | hyperframes-creative SKILL | `...\hyperframes-creative\SKILL.md` | HeyGen | file 2026-10-21 |
| A2-27 | House Style | `...\hyperframes-creative\references\house-style.md` | HeyGen | no version |
| A2-28 | Motion Principles | `...\references\motion-principles.md` | HeyGen | rules dated 2026-04-20 |
| A2-29 | Video Composition | `...\references\video-composition.md` | HeyGen | no version |
| A2-30 | Beat Direction | `...\references\beat-direction.md` | HeyGen | no version |
| A2-31 | Typography | `...\references\typography.md` | HeyGen | no version |
| A2-32 | Narration & Script | `...\references\narration.md` | HeyGen | no version |
| A2-33 | Story spine | `...\references\story-spine.md` | HeyGen | no version |
| A2-35 | Prompt Expansion | `...\references\prompt-expansion.md` | HeyGen | no version |
| A2-36 | Data in Motion | `...\references\data-in-motion.md` | HeyGen | no version |
| A2-38 | Design Spec | `...\references\design-spec.md` | HeyGen | no version |
| A2-42 | Visual Style Library | `...\references\visual-styles.md` | HeyGen | no version |
| A2-43 | Palettes (9) | `...\hyperframes-creative\palettes\*.md` | HeyGen | no version |
| A2-44 | Frame presets (13) + caption skins | `...\hyperframes-creative\frame-presets\*\FRAME.md`, `caption-skin.html` | HeyGen | `version: alpha` frontmatter |
| A2-45 | hyperframes-media SKILL | `...\hyperframes-media\SKILL.md` | HeyGen | file 2026-07-03 |
| A2-46 | Text To Speech | `...\hyperframes-media\references\tts.md` | HeyGen | no version |
| A2-48 | Transcription | `...\references\transcribe.md` | HeyGen | no version |
| A2-49 | Captions authoring | `...\references\captions\authoring.md` | HeyGen | no version |
| A2-50 | Dynamic Caption Techniques | `...\references\captions\motion.md` | HeyGen | no version |
| A2-51 | Transcript Guide | `...\references\captions\transcript-handling.md` | HeyGen | no version |
| A2-52 | Sound effects | `...\references\sfx.md` | HeyGen | no version |
| A2-53 | Background music | `...\references\bgm.md` | HeyGen | no version |
| A2-54 | Background Removal | `...\references\remove-background.md` | HeyGen | no version |
| A2-56 | SFX credits + manifest | `...\hyperframes-media\assets\sfx\CREDITS.md`, `manifest.json` | HeyGen (Pixabay audio) | no version |
| A2-57 | hyperframes-audio SKILL | `...\hyperframes-audio\SKILL.md` | HeyGen | file 2026-10-21 |
| A2-60 | Effect registry | `...\references\fx-registry.md` | HeyGen | generated from `HF_AUDIO_FX` |
| A2-61 | Diagnosing audio | `...\references\diagnosis.md` | HeyGen | ffmpeg 8.1.1 verified |
| A2-62 | Remotion to HyperFrames | `...\remotion-to-hyperframes\SKILL.md`, `references\api-map.md`, `timing.md`, `transitions.md` | HeyGen | baseline 2026-04-27 |
| A2-70 | MOTION_PHILOSOPHY | `...\herk-edit-kit\MOTION_PHILOSOPHY.md` | Nate Herk | kit v2.0.0 (2026) |
| A2-77 | make-a-video + references | `...\.claude\skills\make-a-video\` | Nate Herk | v2.0.0 |
| A2-78 | motion-showreel + references + script headers | `...\.claude\skills\motion-showreel\` | Nate Herk | reference reel Sept 2026 |
| A2-79 | short-form-video (legacy) | `...\.claude\skills\short-form-video\SKILL.md` | Nate Herk | legacy May Shorts |
| A2-80 | short-form-edit + references | `...\.claude\skills\short-form-edit\` | Nate Herk | v2.0.0 |
| A2-83 | video-storytelling + design-system | `...\.claude\skills\video-storytelling\` | Nate Herk | v2.0.0 |
| A2-85 | Editing playbook | `...\herk-edit-kit\docs\EDITING-PLAYBOOK.md` | Nate Herk | measured Mar–Sep 2026 |
| A2-89 | GSAP core source | `...\herk-edit-kit\node_modules\gsap\gsap-core.js` | GreenSock | 3.14.2 |
| B-02 | HyperFrames homepage showcase (45 films; MP4 metadata read in browser) | https://hyperframes.heygen.com/ | HeyGen | undated (live) |
| B-05 | Verified example prompts | https://hyperframes.heygen.com/prompting/examples.md | HeyGen | undated |
| B-06 | HyperFrames vs Remotion (official guide) | https://hyperframes.heygen.com/guides/hyperframes-vs-remotion | HeyGen | undated (cites Opus 5.5, GSAP 3.14.2) |
| B-07 | hyperframes-launch-video README | https://github.com/heygen-com/hyperframes-launch-video | HeyGen | Apr 2026 |
| B-08 | Launch film STORYBOARD.md (v3) | https://raw.githubusercontent.com/heygen-com/hyperframes-launch-video/main/STORYBOARD.md | HeyGen | Apr 2026 |
| B-09 | Launch film SCRIPT.md (v3, change table) | https://raw.githubusercontent.com/heygen-com/hyperframes-launch-video/main/SCRIPT.md | HeyGen | Apr 2026 |
| B-10 | Launch film HANDOFF.md | https://raw.githubusercontent.com/heygen-com/hyperframes-launch-video/main/HANDOFF.md | HeyGen | 2026-04-15 (session 4) |
| B-12 | Timeline Editor launch v2 HANDOFF.md | https://raw.githubusercontent.com/heygen-com/hyperframes-launches/main/timeline-launch/HANDOFF.md | HeyGen | 2026 (undated) |
| B-13 | Issue #318 "Hyperframes vs Remotion" | https://github.com/heygen-com/hyperframes/issues/318 | tonxxd; maintainer jrusso1020 | 2026-04-18 to 04-20 |
| B-15 | Issue #911 Sub-composition slot goes black | https://github.com/heygen-com/hyperframes/issues/911 | community; maintainers | closed 2026-05-17 |
| B-16 | Issue #1231 v0.6.74 render hang at calibration | https://github.com/heygen-com/hyperframes/issues/1231 | community; maintainers | closed 2026-06-07 |
| B-18 | Issue #1009 White bar at bottom of render | https://github.com/heygen-com/hyperframes/issues/1009 | community; maintainers | closed 2026-05-27 |
| B-20 | Issue #5025 Skills contradictions audit | https://github.com/heygen-com/hyperframes/issues/5025 | community; maintainers | opened 2026-10-04 |
| B-21 | Issue #5548 WSL2/Windows GPU rendering | https://github.com/heygen-com/hyperframes/issues/5548 | ajp-productions; maintainers | closed 2026-10-24 |
| B-23 | Issues index, sorted by comments | https://github.com/heygen-com/hyperframes/issues?q=is%3Aissue%20sort%3Acomments-desc | GitHub / HeyGen | live |
| B-28 | Herk Edit Kit README | https://github.com/nateherkai/herk-edit-kit | Nate Herk | last commit 2026-10-14 |
| B-29 | MOTION_PHILOSOPHY.md | https://github.com/nateherkai/herk-edit-kit/blob/main/MOTION_PHILOSOPHY.md | Nate Herk | ≤2026-10-17 |
| B-30 | Editing playbook | https://github.com/nateherkai/herk-edit-kit/blob/main/docs/EDITING-PLAYBOOK.md | Nate Herk | 2026-10-13 |
| B-31 | motion-showreel skill + reference breakdown | https://github.com/nateherkai/herk-edit-kit/tree/main/.claude/skills/motion-showreel | Nate Herk | Sep 2026 |
| B-34 | Full Tutorial: Make Professional Launch Videos for Free with HyperFrames | https://creatoreconomy.so/p/full-tutorial-make-professional-launch-videos-for-free-hyperframes-ai | Peter Yang (guests Bin Liu, Jake Moran) | 2026-06-21 |
| B-37 | First Contact With Hyperframes | https://trilogyai.substack.com/p/first-contact-with-hyperframes | David Proctor (Trilogy) | 2026-05-27 |
| B-38 | How I make motion graphics with HyperFrames and Claude Code | https://claudecodeformarketers.com/blog/motion-graphics-with-hyperframes/ | Keanan Koppenhaver | 2026-07-23 |
| B-41 | HyperFrames + Codex: How to Make a Free AI Launch Video | https://www.nocode.mba/articles/hyperframes-codex-launch-videos | No Code MBA | updated 2026-09-10 |
| B-42 | AI video creation with Hyperframes and Claude Code | https://www.mejba.me/blog/ai-video-creation-hyperframes-claude-code | Engr Mejba Ahmed | 2026-05-11 |
| B-43 | HyperFrames: video as code | https://www.onewave-ai.com/blog/hyperframes-video-as-code | OneWave Team | 2026-09-04 |
| B-44 | HyperFrames review (HeyGen HTML video for agents) | https://andrew.ooo/posts/hyperframes-heygen-html-video-agents-review/ | andrew.ooo (AI-operated, human-supervised) | 2026-05-28 |
| B-45 | HyperFrames vs Remotion review | https://www.getmasset.com/resources/blog/hyperframes-vs-remotion-review | Benjamin Ard (Masset) | 2026-06-30 |
| B-46 | HyperFrames vs Remotion | https://www.wireflow.ai/blog/hyperframes-vs-remotion | Andrew Adams (Wireflow) | 2026-10-13 |
| B-47 | HyperFrames vs Remotion: Which Should You Use in 2026? | https://voyager.so/blog/hyperframes-vs-remotion | Anvisha Pai (Voyager) | updated 2026-09-21 |
| C-07 | Human Interface Guidelines: Motion | https://developer.apple.com/design/human-interface-guidelines/motion | Apple | change log latest 2025-09-09 |
| C-08 | Executing UX Animations: Duration and Motion Characteristics (Laubheimer) | https://www.nngroup.com/articles/animation-duration/ | Nielsen Norman Group | 2020-02-09 |
| C-12 | Human Interface Guidelines: Typography (tvOS styles; minimum sizes) | https://developer.apple.com/design/human-interface-guidelines/typography | Apple | change entry 2025-12-16 |
| C-13 | `typography.dart` (M3 2021 type scale) | https://raw.githubusercontent.com/flutter/flutter/master/packages/flutter/lib/src/material/typography.dart | Google / Flutter | master branch |
| C-14 | "Capta la atención con nuevas funcionalidades para anuncios de video" (Facebook/Nielsen findings) | https://about.fb.com/es/news/2016/02/capta-la-atencion-con-nuevas-funcionalidades-para-anuncios-de-video/ | Meta Newsroom | 2016-02-10; updated 2019-11-04 |
| C-15 | 9 creative tips to drive auction ad performance | https://ads.tiktok.com/business/en-US/blog/9-creative-tips-to-drive-auction-ad-performance | TikTok For Business | 2020-10-21 |
| C-16 | 7 Top Tips for Making TikTok Videos (SMB one-pager) | https://ads.tiktok.com/business/library/Top_Tips_One_Pager_SMB.pdf | TikTok For Business | data May–Jul 2021 |
| C-17 | ABCDs of effective video ads | https://business.google.com/us/resources/articles/abcds-of-effective-video-ads/ | Google (study: Google/Kantar) | study Apr 2021 |
| C-20 | YouTube Shorts ads: asset specs and best practices | https://support.google.com/google-ads/answer/16041697 | Google Ads Help | undated (live page) |
| C-21 | Brame, "Effective Educational Videos," CBE—Life Sciences Education 15(4):es6 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5132380/ | ASCB / PMC | 2016 |
| C-22 | Guo, Kim & Rubin, "How Video Production Affects Student Engagement," L@S 2014 | https://www.cs.rochester.edu/hci/pubs/pdfs/edX-MOOC-video-production-and-engagement_LAS-2014.pdf | ACM (authors' copy) | 2014 |
| C-23 | Mayer, "Using multimedia for e-learning," JCAL 33(5):403–423 | https://doi.org/10.1111/jcal.12197 | Wiley | 2017 |
| C-26 | Höffler & Leutner, "Instructional animation versus static pictures: A meta-analysis," Learning and Instruction 17(6):722–738 | https://www.leibniz-ipn.de/en/research/publications/instructional-animation-versus-static-pictures-a-meta-analysis | Elsevier (IPN listing) | 2007 |
| C-27 | Berney & Bétrancourt, "Does animation enhance learning? A meta-analysis," Computers & Education 101:150–167 | https://archive-ouverte.unige.ch/unige:92234 | Elsevier (UNIGE archive) | 2016 |
| C-28 | Quesenberry & Coolsen, "What Makes a Super Bowl Ad Super? Five-Act Dramatic Form…," JMTP 22(4):437–454 | https://doi.org/10.2753/mtp1069-6679220406 | Taylor & Francis | 2014 |
| C-29 | Cutting et al., "Quicker, faster, darker: Changes in Hollywood film over 75 years," i-Perception 2(6):569–576 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3485803/ | SAGE / PMC | 2011 |
| C-31 | SMPTE ST 2046-1:2009, Safe Areas for 16:9 Television Systems | https://pub.smpte.org/doc/st2046-1/ | SMPTE | 2009 |
| C-33 | EBU R 95, Safe areas for 16:9 television production | https://tech.ebu.ch/publications/r095 | EBU | v1.1, June 2017 |
| C-34 | ITU-R BT.709-6, Parameter values for the HDTV standards | https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.709-6-201506-I!!PDF-E.pdf | ITU-R | 06/2015 |
| C-37 | Web Content Accessibility Guidelines (WCAG) 2.2 | https://www.w3.org/TR/WCAG22/ | W3C | Recommendation 2024-12-12 |
| C-39 | ORI/ASWF Encoding Guidelines: Color Metadata and Web Color Preservation | https://academysoftwarefoundation.github.io/EncodingGuidelines/WebColorPreservation.html | Academy Software Foundation | © 2022, live page |
| C-40 | CAMBI: Contrast-aware Multiscale Banding Index (and Netflix TechBlog post, 2021) | https://arxiv.org/pdf/2102.00079 | Netflix (arXiv) | 2021 |
| C-41 | Instagram Reels video ad specs (Meta Ads Guide) | https://www.facebook.com/business/ads-guide/update/video/instagram-reels | Meta | live page |
| C-43 | Use square and vertical video to engage mobile customers | https://support.google.com/google-ads/answer/9128498 | Google Ads Help | undated (live page) |
| C-44 | TikTok Auction In-Feed Ads (specs) | https://ads.tiktok.com/help/article/tiktok-auction-in-feed-ads | TikTok Ads Help | last updated June 2026 |
| C-45 | Heer & Robertson, "Animated Transitions in Statistical Data Graphics," IEEE TVCG 13(6) | https://idl.cs.washington.edu/files/2007-AnimatedTransitions-InfoVis.pdf | IEEE (authors' copy) | 2007 |
| C-47 | Chevalier, Dragicevic & Franconeri, "The Not-so-Staggering Effect of Staggered Animated Transitions on Visual Tracking," IEEE TVCG 20(12) | https://hal.archives-ouvertes.fr/hal-01054408v1 | IEEE (HAL copy) | 2014 |
| C-48 | Dragicevic et al., "Temporal Distortion for Animated Transitions," CHI 2011 | https://hal.archives-ouvertes.fr/inria-00556177v2 | ACM (HAL copy) | 2011 |
| C-49 | Bostock, "Object Constancy" | https://bost.ocks.org/mike/constancy | Mike Bostock | c. 2012 |
| C-50 | Correll, Bertini & Franconeri, "Truncating the Y-Axis: Threat or Menace?" CHI 2020 | https://www.tableau.com/research/publications/truncating-y-axis-threat-or-menace | Tableau Research / ACM | 2020 |
| C-53 | EBU R 128, Loudness normalisation and permitted maximum level of audio signals | https://tech.ebu.ch/docs/r/r128.pdf | EBU | v5.0, Nov 2023 |
| C-55 | Report ITU-R BS.2434-0, Loudness for Internet delivery of broadcast-originated soundtracks | https://www.itu.int/dms_pub/itu-r/opb/rep/R-REP-BS.2434-2018-PDF-E.pdf | ITU-R | 2018 |
| C-57 | Loudness normalization | https://support.spotify.com/us/artists/article/loudness-normalization/ | Spotify for Artists | undated (live page) |
| C-58 | Audio requirements | https://podcasters.apple.com/support/893-audio-requirements | Apple Podcasts for Creators | undated (© 2026) |
| C-59 | Netflix Sound Mix Specifications & Best Practices v1.5 | https://backlothelp.netflix.com/hc/en-us/articles/360001794307-Netflix-Sound-Mix-Specifications-Best-Practices-v1-5 | Netflix | v1.5 (indexed; live URL now redirects to the Studio Partner portal) |
| C-61 | Torcoli et al., "Preferred Levels for Background Ducking…," JAES 67(12):1003–1011 | https://doi.org/10.17743/jaes.2019.0052 | AES | 2019 |
| C-62 | ITU-R BT.1359-1, Relative timing of sound and vision for broadcasting | https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1359-1-199811-I!!PDF-E.pdf | ITU-R | 11/1998 |
| C-64 | Olsen, "Creating the contrast: The influence of silence and background music on recall and attribute importance," J. Advertising 24(4):29–44 | https://asu.elsevierpure.com/en/publications/creating-the-contrast-the-influence-of-silence-and-background-mus/ | Taylor & Francis (ASU listing) | 1995 |
| C-65 | Bruner, "Music, Mood, and Marketing," J. Marketing 54(4):94–104 | https://doi.org/10.1177/002224299005400408 | AMA / SAGE | 1990 |
| C-66 | Speaking rate | https://tfcs.baruch.cuny.edu/speaking-rate/ | Tools for Clear Speech, Baruch College CUNY | undated (© 2026) |
| C-67 | BBC Subtitle Guidelines | https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/ | BBC | v1.2.5, March 2026 |
| C-68 | Timed Text Style Guide: General Requirements | https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements | Netflix | change log 2022-10-07 |
| C-69 | English (USA) Timed Text Style Guide | https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide | Netflix | 2025-12-19 |
| C-70 | Timed Text Style Guide: Subtitle Timing Guidelines | https://partnerhelp.netflixstudios.com/hc/en-us/articles/360051554394-Timed-Text-Style-Guide-Subtitle-Timing-Guidelines | Netflix | 2025-07-04 |
| C-71 | 47 CFR §79.1 Closed captioning of televised video programming, (j)(2) caption quality standards | https://www.law.cornell.edu/cfr/text/47/79.1 | US FCC (via Cornell LII) | current CFR text |
| C-72 | DCMP Captioning Key: Presentation Rate (601) and Captioning Text (597) | https://dcmp.org/learn/captioningkey/601 | Described and Captioned Media Program | undated (© 2026) |
| C-73 | Understanding SC 1.2.2 Captions (Prerecorded) | https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html | W3C WAI | updated 2026-08-10 |
| C-76 | Understanding SC 2.3.1 Three Flashes or Below Threshold | https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html | W3C WAI | updated 2025-09-17 |
| C-77 | Understanding SC 2.3.3 Animation from Interactions | https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html | W3C WAI | updated 2025-09-16 |
| C-78 | ITU-R BT.1702-3, Guidance for the reduction of photosensitive epileptic seizures caused by television | https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1702-3-202311-I!!PDF-E.pdf | ITU-R | 11/2023 |
| C-79 | prefers-reduced-motion | https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion | MDN (Mozilla) | last modified 2026-06-10 |
| C-80 | Agrawal et al., vestibular disorders in US adults (Arch Intern Med 2009), summary | https://mdedge.com/content/vestibular-dysfunction-common-after-age-40 | MDedge (summary of AMA journal article) | 2009 |
| C-81 | YouTube recommended upload encoding settings | https://support.google.com/youtube/answer/1722171 | YouTube Help | undated (© 2026) |
| C-82 | Upload videos longer than 15 minutes | https://support.google.com/youtube/answer/71673 | YouTube Help | undated |
| C-83 | Understand three-minute YouTube Shorts | https://support.google.com/youtube/answer/15424877 | YouTube Help | rule from 2024-10-15 (amended 2025-12-08) |
| C-85 | Content Posting API: Media Transfer Guide | https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide | TikTok for Developers | live page |
| C-86 | Video specifications for posting (a548372) | https://www.linkedin.com/help/linkedin/answer/a548372 | LinkedIn Help | "last updated 2 years ago" |
| C-87 | Media best practices | https://docs.x.com/x-api/media/quickstart/best-practices | X Developer Platform | live page |
| C-88 | About longer videos for X Premium subscribers | https://help.x.com/en/using-x/premium-longer-videos | X Help Center | live page (403 on fetch; indexed snippet) |
| C-94 | ASA Ruling on Citroen UK Ltd (flashing images; Ofcom guidance applied) | https://www.asa.org.uk/rulings/citroen-uk-ltd-a11-164759.html | Advertising Standards Authority (UK) | 2012-01-18 |
| C-95 | Olsen, "Salient stimuli in advertising: the effect of contrast interval length and type on recall," J. Exp. Psychology: Applied | https://asu.elsevierpure.com/en/publications/salient-stimuli-in-advertising-the-effect-of-contrast-interval-le | APA (ASU listing) | 2002 |
| D-01 | HyperFrames Master Prompt Checklist (+ .html, .pdf) | C:\Users\cwako\OneDrive\AgentOS\GENERAL\VIDEO\HYPERFRAME RESOURCES\HyperFrames-Master-Prompt-Checklist.md | user (PRIOR) | file 2026-11-01 |
| D-02 | The HyperFrames Master Prompt (+ .pdf) | …\HYPERFRAME RESOURCES\HyperFrames_Master_Prompt_Checklist.html | user (PRIOR) | v1.0, Nov 2026 |
| D-03 | HyperFrames Showreel Standard (+ .pdf) | …\HYPERFRAME RESOURCES\HyperFrames-Showreel-Standard.html | user (PRIOR) | v1.0, 2026-11-01 |
| D-04 | HyperFrames Expert Motion Prompt (+ .pdf) | …\HYPERFRAME RESOURCES\Hyperframes_Expert_Motion_Prompt.html | user (PRIOR) | docs checked 2026-11-01 |
| D-05 | Hyperframe Motion Video Master Specification & Prompt Studio | …\HYPERFRAME RESOURCES\hyperframe_interactive_prompt_studio_specification.html | user (PRIOR) | file 2026-11-01 |
| D-06 | Hyperframe Motion Video Master Specification & LLM Prompt Checklist | …\HYPERFRAME RESOURCES\Hyperframe Motion Design Master Checklist & Prompt Specification.pdf | user (PRIOR) | 6 pp, truncated |
| D-07 | Ask for a great video | https://hyperframes.heygen.com/guides/prompting | HeyGen | undated |
| D-08 | Ask for smooth motion and transitions | https://hyperframes.heygen.com/prompting/motion.md | HeyGen | undated |
| D-09 | Brand, templates and storyboards | https://hyperframes.heygen.com/prompting/design-systems.md | HeyGen | undated |
| D-12 | Lesson: The brief | https://hyperframes.heygen.com/lessons/the-brief | HeyGen | undated |
| D-13 | Lesson: Review and correct | https://hyperframes.heygen.com/lessons/review-and-correct | HeyGen | undated |
| D-15 | Brief contract | …\skills\hyperframes\references\brief-contract.md | HeyGen | 2026-10-21 |
| D-16 | Brief format — BRIEF.md | …\skills\hyperframes\references\brief-format.md | HeyGen | 2026-10-21 |
| D-17 | The intent layer | …\skills\hyperframes\references\intent-interview.md | HeyGen | 2026-10-21 |
| D-18 | Pitch round | …\skills\hyperframes\references\pitch-round.md | HeyGen | 2026-10-21 |
| D-19 | The review loop | …\skills\hyperframes\references\review-loop.md | HeyGen | 2026-10-21 |
| D-20 | Production loop | …\skills\hyperframes\references\production-loop.md | HeyGen | 2026-10-21 |
| D-21 | Storyboard format | …\skills\hyperframes\references\storyboard-format.md | HeyGen | 2026-10-21 |
| D-23 | Prompt expansion | …\skills\hyperframes-creative\references\prompt-expansion.md | HeyGen | 2026-10-21 |
| D-24 | House style | …\skills\hyperframes-creative\references\house-style.md | HeyGen | 2026-10-21 |
| D-26 | Story spine | …\skills\hyperframes-creative\references\story-spine.md | HeyGen | 2026-10-21 |
| D-27 | Beat direction | …\skills\hyperframes-creative\references\beat-direction.md | HeyGen | 2026-10-21 |
| D-28 | Typography | …\skills\hyperframes-creative\references\typography.md | HeyGen | 2026-10-21 |
| D-32 | hyperframes-core + determinism rules | …\skills\hyperframes-core\SKILL.md; …\references\determinism-rules.md | HeyGen | 2026-10-21 |
| D-33 | hyperframes-cli + lint/check + preview/render | …\skills\hyperframes-cli\SKILL.md; …\references\lint-validate-inspect.md; …\references\preview-render.md | HeyGen | 2026-10-21 |
| D-34 | hyperframes-audio + fx registry | …\skills\hyperframes-audio\SKILL.md; …\references\fx-registry.md | HeyGen | 2026-10-21 |
| D-36 | motion-graphics shot-plan IR, Director, Finalize | …\skills\motion-graphics\references\shot-plan-ir.md; …\agents\director.md; …\agents\finalize.md | HeyGen | 2026-10-21 |
| D-37 | Prompting best practices | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | Anthropic | undated; covers Opus 5.5 etc. |
| D-38 | Prompting Claude Opus 5.5 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5 | Anthropic | undated |
| D-39 | Prompting Claude Opus 4.8 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8 | Anthropic | undated |
| D-40 | Prompting Claude Opus 5 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5 | Anthropic | undated |
| D-41 | Prompt engineering overview; metaprompt notebook | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview ; https://github.com/anthropics/claude-cookbooks/blob/main/misc/metaprompt.ipynb | Anthropic | undated (helper) |
| D-43 | Skill authoring best practices; Agent Skills overview; Equipping agents… | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices ; https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills | Anthropic | blog 2025-10-16 (helper) |
| D-44 | Best practices for Claude Code | https://code.claude.com/docs/en/best-practices | Anthropic | undated (helper) |
| D-46 | Effective context engineering for AI agents | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Anthropic | 2025-09-29 (helper) |
| D-47 | Effective harnesses for long-running agents | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | Anthropic | 2025-11-26 (helper) |
| D-48 | Harness design for long-running application development | https://www.anthropic.com/engineering/harness-design-long-running-apps | P. Rajasekaran, Anthropic | 2026-03-24 |
| D-49 | Demystifying evals for AI agents | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | Anthropic | 2026-01-09 (helper) |
| D-51 | Frontend Design (community copy) | …\skills\frontend-design\SKILL.md | community (DEMO) | date_added 2026-02-27 |
| D-52 | No AI slop + eval | …\skills\no-ai-slop\SKILL.md; …\eval.md | unknown author (DEMO) | file 2026-10-17 |
| D-54 | Prompt guidance (GPT-5.5 / GPT-6) | https://developers.openai.com/api/docs/guides/prompt-guidance | OpenAI | undated (helper) |
| D-55 | Frontend prompt instructions; Designing delightful frontends with GPT-5.4 | https://developers.openai.com/api/docs/guides/frontend-prompt ; https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4 | OpenAI | undated (helper) |
| D-58 | Gemini 3 developer guide | https://ai.google.dev/gemini-api/docs/gemini-3 | Google | updated 2026-10-09 (helper) |
| D-60 | Generate Remotion code using LLMs; system prompt; Claude Code page | https://www.remotion.dev/docs/ai/generate ; https://www.remotion.dev/docs/ai/system-prompt ; https://www.remotion.dev/docs/ai/claude-code | Remotion | undated (helper) |
| D-61 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | https://arxiv.org/abs/2306.05685 | Zheng et al. | 2023, NeurIPS D&B (helper) |
| D-64 | MLLM-as-a-Judge | https://arxiv.org/abs/2402.04788 | D. Chen et al. | ICML 2024, v3 |
| D-66 | LLM Evaluators Recognize and Favor Their Own Generations | https://arxiv.org/abs/2404.13076 | Panickssery et al. | 2024 (helper) |
| D-70 | TICKing All the Boxes | https://arxiv.org/abs/2410.03608 | Cook et al. | 2024 (helper) |
| D-71 | Rubrics as Rewards | https://arxiv.org/abs/2507.17746 | Gunjal et al. | 2025 (helper) |
| D-78 | Vision language models are blind | https://arxiv.org/abs/2407.06581 | Rahmanzadehgervi et al. | 2024 (helper) |
| D-81 | Self-Refine | https://arxiv.org/abs/2303.17651 | Madaan et al. | NeurIPS 2023 (helper) |
| D-93 | Scaling Laws for Reward Model Overoptimization | https://arxiv.org/abs/2210.10760 | Gao et al. | 2022 (helper) |
| D-102 | Verbalized Sampling | https://arxiv.org/abs/2510.01171 | J. Zhang et al. | 2025, v3 |
| D-104 | The Client Brief | https://www.slideshare.net/slideshow/the-client-brief-o-briefing-do-cliente/7720934 | IPA, ISBA, MCCA, PRCA | 2003 (helper; third-party upload) |
| D-111 | SMPTE ST 2046-1:2009 Safe Areas (listing + extracts) | https://pub.smpte.org/doc/st2046-1/ | SMPTE (via search extracts) | 2009 |
| E-01 | Hands-on CLI verification lab (51-command help capture, renders, lint negatives, determinism, alpha) | research-notes/E-cli-verification.md | this project | hyperframes 0.8.229, 2026-11-01 |
| G-01 | Gemini video analysis of E2 Studio launch (static, 4 fps; OK) | static.heygen.ai MP4 | gemini-3.8-flash via gemini-api CLI | 2026-11-01 |
| G-02 | Gemini video analysis of E3 A launch video in 6 hours (default; OK) | static.heygen.ai MP4 | gemini-3.8-flash via gemini-api CLI | 2026-11-01 |
| G-03 | Gemini video analysis of E4 Storyboard first (default; OK) | static.heygen.ai MP4 | gemini-3.8-flash via gemini-api CLI | 2026-11-01 |
| G-04 | Gemini video analysis of E5 It's just HTML (default; OK) | static.heygen.ai MP4 | gemini-3.8-flash via gemini-api CLI | 2026-11-01 |
| G-05 | Gemini video analysis of E6 Claude Motion (default; OK) | static.heygen.ai MP4 | gemini-3.8-flash via gemini-api CLI | 2026-11-01 |
| G-07 | Gemini video analysis of E10 Jake Moran episode (default; OK) | YouTube MC1g2fHYC88 | gemini-3.8-flash via gemini-api CLI | 2026-11-01 |
| G-08 | Gemini video analysis of E9 Nate Herk video (default; OK) | YouTube Aw3BkmhYu4I | gemini-3.8-flash via gemini-api CLI | 2026-11-01 |
| S-01 | Qualia v2.0 — The Quantum Prompt Engineer & Compression Architect (canonical persona text) | C:\Users\cwako\OneDrive\AgentOS\GENERAL\PROMPTS & PERSONAS\Qualia v2.0\Qualia-v2.0-The-Quantum-Prompt-Engineer-&-Compression-Architect.txt | bonskills | v2.0 |
| S-02 | qualia-nexus-forge SKILL.md (pipelines, output modes, requirements) | C:\Users\cwako\.claude\skills\qualia-nexus-forge\SKILL.md | bonskills | installed copy |
| S-03 | qualia-nexus-forge Sentinel agent (22-point audit, skill validation) | C:\Users\cwako\.claude\skills\qualia-nexus-forge\references\sentinel-agent.md | bonskills | installed copy |
| S-04 | qualia-nexus-forge Architect agent (SkillGraph notation, skill architecture) | C:\Users\cwako\.claude\skills\qualia-nexus-forge\references\architect-agent.md | bonskills | installed copy |
| S-05 | qualia-nexus-forge templates (persona, skill, SkillGraph, audit) | C:\Users\cwako\.claude\skills\qualia-nexus-forge\references\templates.md | bonskills | installed copy |
| S-06 | qualia-nexus-forge compliance_auditor.py | C:\Users\cwako\.claude\skills\qualia-nexus-forge\scripts\compliance_auditor.py | bonskills | installed copy |
| S-07 | Qualia v2.0 specification and 22-point audit (openbot-forge KB) | C:\Users\cwako\.claude\skills\openbot-forge\references\kb\qualia-v2-spec.md | bonskills | reviewed 2026-10-30 |
| S-08 | skill-creator quick_validate.py (allowed frontmatter keys) | C:\Users\cwako\.claude\skills\skill-creator\scripts\quick_validate.py | Anthropic skill-creator | installed copy |
| S-09 | Official hyperframes entry-point SKILL.md (generation B) | C:\Users\cwako\.claude\skills\hyperframes\SKILL.md | HeyGen | updated 2026-10-21 |
| S-10 | Official hyperframes-cli SKILL.md (generation B) | C:\Users\cwako\.claude\skills\hyperframes-cli\SKILL.md | HeyGen | updated 2026-10-21 |
| S-11 | Official hyperframes-cli lint-validate-inspect.md | C:\Users\cwako\.claude\skills\hyperframes-cli\references\lint-validate-inspect.md | HeyGen | updated 2026-10-21 |
| S-13 | npm registry: hyperframes (npm view) | https://www.npmjs.com/package/hyperframes | npm / HeyGen | 0.8.229, 2026-11-01 |
| S-14 | Herk Edit Kit package.json (pins hyperframes 0.7.109, gsap 3.14.2) | C:\Users\cwako\herk-edit-kit\package.json | Nate Herk | kit v2.0.0 |
| S-15 | Qualia_v2.0_Persona.pdf (a derived crypto-coach persona, not the spec) | C:\Users\cwako\OneDrive\AgentOS\GENERAL\PROMPTS & PERSONAS\Qualia_v2.0_Persona.pdf | bonskills | 2 pages |
