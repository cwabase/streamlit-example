---
description: "AUDIT mode: score a film or a prompt against gates, the 35-item checklist and the twelve-dimension rubric"
argument-hint: "<file, composition or prompt>"
---

Use the `hypervideo-man` skill in AUDIT mode.

Target: $ARGUMENTS

Run the binary gates, then the 35-item checklist (`scripts/scorecard.py --format md` prints it), then score the twelve dimensions 1 to 5 as a separate judge pass. Ship rule: every dimension at least 3 and average at least 4.0. Report evidence for every item.
