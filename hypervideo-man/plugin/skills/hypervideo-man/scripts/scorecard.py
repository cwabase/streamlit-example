#!/usr/bin/env python3
"""Print the HyperFrames Motion Mastery 35-item pass/fail scorecard.

Deterministic, dependency-free. Usage:
    python scorecard.py --format md      # fillable Markdown checklist (default)
    python scorecard.py --format json    # machine-readable list
    python scorecard.py --format csv     # spreadsheet-friendly
Each item must be reported PASS / FAIL / NOT VERIFIABLE with evidence before the
delivery render. Any FAIL blocks the render.
"""
import argparse
import csv
import json
import sys

ITEMS = [
    ("Story", 1, "The message line is stated; every beat's why traces to it.", "STORYBOARD.md frame table"),
    ("Story", 2, "Frame 0 shows a meaningful visual; outcome stated within 2 s (social) or 5 s (long-form).", "snapshot --at 0 and the hook timestamp"),
    ("Story", 3, "The value claim lands by beat 2.", "STORYBOARD.md"),
    ("Story", 4, "CTA and logo land on the final music hit and hold >= 2.5 s.", "snapshot at end; audio_meta.json / audiomap.json"),
    ("Story", 5, "Runtime within +/-0.5 s of target.", "ffprobe duration"),
    ("Visual system", 6, "One background world, one accent, <= 2 type families (or a written concept for more); frame.md tokens quoted verbatim.", "frame.md vs compositions"),
    ("Visual system", 7, "Every scene has three depth layers and >= 2 focal points.", "contact sheet"),
    ("Visual system", 8, "Zero banned AI tells, or a written reason for each one used.", "expanded-prompt.md negative section"),
    ("Visual system", 9, "Key content inside title-safe (80 %), everything visible inside action-safe (90 %); 9:16 clear of platform UI.", "check layout audit; snapshots"),
    ("Visual system", 10, "No banding, flicker, shimmering hairlines or clipped text in any snapshot.", "snapshots at full resolution"),
    ("Text and contrast", 11, "hyperframes check contrast audit passes; body text and captions reach 7:1.", "check --json"),
    ("Text and contrast", 12, "Type floors met (body >= 28 px full-screen, >= 32 px in-feed; labels >= 18 / 24 px).", "CSS inspection"),
    ("Text and contrast", 13, "Every text block readable within two-thirds of its hold; captions <= 20 cps, <= 42 chars/line, one group at a time.", "timeline + transcript.json"),
    ("Text and contrast", 14, "Captions cover every spoken word.", "transcript.json vs caption track"),
    ("Motion", 15, "Every element has a named verb; no scene uses one ease on more than two tweens.", "expanded-prompt.md; timeline source"),
    ("Motion", 16, "The slowest scene is >= 3x slower than the fastest, with >= 1 deliberate hold.", "STORYBOARD.md rhythm line"),
    ("Motion", 17, "Element exits faster than entrances; every stagger completes in < 500 ms; scene exits owned by the transition.", "timeline source"),
    ("Motion", 18, "Persistent elements never jump across a cut (every cut scrubbed).", "scrub pass notes"),
    ("Motion", 19, "No undesigned dead zone > 2 s.", "animation-map.mjs output"),
    ("Light", 20, "One light direction with consistent shadows.", "contact sheet"),
    ("Light", 21, "Light hits within +/-1 frame of their sound hits.", "timeline vs cue sheet"),
    ("Light", 22, "<= 3 flashes per second anywhere.", "frame scan"),
    ("Audio", 23, "VO intelligible on a phone speaker and summed to mono.", "listening pass"),
    ("Audio", 24, "Bed carved against the voice group and returning between phrases without pumping.", "data-fx-carve present; listening pass"),
    ("Audio", 25, "SFX count within the density band; hero hits >= 15 s apart.", "cue sheet"),
    ("Audio", 26, "Every SFX transient within +/-1 frame of its visual event, none early.", "timeline vs cue sheet"),
    ("Audio", 27, "No sample three times in a row; nothing louder than the voice while it speaks.", "cue sheet; meter"),
    ("Audio", 28, "Music ends on a button or natural ending - no abrupt cut, no fade mid-phrase.", "listening pass at the end"),
    ("Audio", 29, "Measured loudness on target +/-1 LU; true peak <= -1 dBTP.", "ffmpeg -af ebur128=peak=true"),
    ("Technical and delivery", 30, "npx hyperframes check reports 0 findings and lint reported no error.", "lint; check --json"),
    ("Technical and delivery", 31, "Every scene midpoint snapshotted and inspected; reference-timed clips verified; file size sane.", "snapshot list; ls -l"),
    ("Technical and delivery", 32, "ffprobe confirms duration = data-duration +/-1 frame, briefed fps, and an audio stream.", "ffprobe"),
    ("Technical and delivery", 33, "Fonts bundled or embedded; no fallback faces; no font_family_without_font_face warnings for cloud renders.", "lint"),
    ("Technical and delivery", 34, "The Studio preview was approved before the delivery render.", "conversation record"),
    ("Technical and delivery", 35, "All deliverables present: MP4 (and cut-downs), captions file, stems, assumptions list, published link with explicit visibility if requested.", "delivery folder listing"),
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--format", choices=["md", "json", "csv"], default="md")
    args = parser.parse_args()

    if args.format == "json":
        json.dump([
            {"group": g, "id": i, "item": text, "evidence": ev, "status": "", "notes": ""}
            for g, i, text, ev in ITEMS
        ], sys.stdout, indent=2, ensure_ascii=False)
        print()
        return 0

    if args.format == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(["group", "id", "item", "evidence", "status", "notes"])
        for g, i, text, ev in ITEMS:
            writer.writerow([g, i, text, ev, "", ""])
        return 0

    current = None
    print("# HyperFrames Motion Mastery - 35-item scorecard\n")
    print("Report every item PASS / FAIL / NOT VERIFIABLE with evidence before the delivery render.\n")
    for g, i, text, ev in ITEMS:
        if g != current:
            current = g
            print(f"\n## {g}\n")
        print(f"- [ ] {i}. {text}  \n      Evidence: {ev}  |  Status: ____  |  Notes: ____")
    print(f"\nTotal items: {len(ITEMS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
