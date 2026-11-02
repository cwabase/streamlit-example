#!/usr/bin/env python3
"""Post-render QA gate for a finished video file.

Checks the delivered file, not the composition (run `npx hyperframes check` for that):
spec (size, fps, duration, codec, pixel format), loudness (integrated LUFS, true peak),
black / frozen / silent spans, a full-frame flash-risk heuristic, and a contact sheet
for visual review.

Usage:
  python scripts/qa_render.py renders/final.mp4 --width 1920 --height 1080 --fps 30 --duration 45
      [--lufs -14 --lufs-tol 1 --true-peak -1] [--sheet sheet.png] [--json report.json]
  python scripts/qa_render.py --selftest

Needs ffmpeg and ffprobe on PATH. Exit codes: 0 all hard checks pass, 1 a hard check failed,
2 usage or tool error. Black, frozen and silent spans are warnings: holds and pauses can be
intentional, so review them against the storyboard.
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path


def run(args, cwd=None):
    p = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=cwd)
    return p.returncode, p.stdout, p.stderr


def rate(value):
    try:
        f = Fraction(value)
        return float(f) if f else 0.0
    except (ValueError, ZeroDivisionError, TypeError):
        return 0.0


def probe(path):
    code, out, err = run(['ffprobe', '-v', 'error', '-show_streams', '-show_format', '-of', 'json', str(path)])
    if code:
        raise RuntimeError(err.strip() or 'ffprobe failed')
    data = json.loads(out)
    info = {'duration': float(data['format'].get('duration', 0)), 'container': data['format'].get('format_name')}
    v = next((s for s in data['streams'] if s['codec_type'] == 'video'), None)
    a = next((s for s in data['streams'] if s['codec_type'] == 'audio'), None)
    if v:
        info.update(width=v['width'], height=v['height'], vcodec=v['codec_name'], profile=v.get('profile'),
                    pix_fmt=v.get('pix_fmt'), fps=rate(v.get('avg_frame_rate')) or rate(v.get('r_frame_rate')),
                    color_space=v.get('color_space'), color_primaries=v.get('color_primaries'),
                    color_transfer=v.get('color_transfer'))
    if a:
        info.update(acodec=a['codec_name'], sample_rate=int(a.get('sample_rate', 0)), channels=a.get('channels'))
    return info


def spans(text, start_re, end_re):
    starts = [float(x) for x in re.findall(start_re, text)]
    ends = [float(x) for x in re.findall(end_re, text)]
    return [[round(s, 2), round(e, 2)] for s, e in zip(starts, ends)]


def analyse(path, has_audio):
    """One decode pass: black/freeze detection, per-frame luma, and (if audio) loudness + silence."""
    with tempfile.TemporaryDirectory() as tmp:
        vf = ('blackdetect=d=0.5:pix_th=0.10,freezedetect=n=-60dB:d=2,scale=160:-2,signalstats,'
              'metadata=mode=print:key=lavfi.signalstats.YAVG:file=luma.txt')
        args = ['ffmpeg', '-hide_banner', '-nostats', '-i', str(Path(path).resolve()), '-vf', vf]
        args += ['-af', 'silencedetect=noise=-50dB:d=1.5,ebur128=peak=true'] if has_audio else ['-an']
        code, _, err = run(args + ['-f', 'null', '-'], cwd=tmp)
        if code:
            raise RuntimeError(err.strip().splitlines()[-1] if err.strip() else 'ffmpeg failed')
        luma_txt = (Path(tmp) / 'luma.txt').read_text(encoding='utf-8', errors='replace')
    res = {
        'black': spans(err, r'black_start:\s*([\d.]+)', r'black_end:\s*([\d.]+)'),
        'freeze': spans(err, r'freeze_start:\s*([\d.]+)', r'freeze_end:\s*([\d.]+)'),
        'silence': spans(err, r'silence_start:\s*([\d.]+)', r'silence_end:\s*([\d.]+)'),
    }
    if has_audio:
        summary = err[err.rfind('Summary:'):]
        num = lambda pat: (float(m.group(1)) if (m := re.search(pat, summary)) and m.group(1) != '-inf' else None)
        res['loudness'] = {'I': num(r'I:\s+(-?[\d.]+|-inf) LUFS'), 'LRA': num(r'LRA:\s+(-?[\d.]+) LU'),
                           'TP': num(r'Peak:\s+(-?[\d.]+|-inf) dBFS')}
    times = [float(t) for t in re.findall(r'pts_time:\s*([\d.]+)', luma_txt)]
    yavg = [float(y) for y in re.findall(r'YAVG=([\d.]+)', luma_txt)]
    # Limited-range luma (16-235) to approximate linear relative luminance.
    lum = [min(max((y - 16) / 219, 0.0), 1.0) ** 2.2 for y in yavg]
    res['flash'] = {'max_per_second': max_flashes_per_second(transitions(list(zip(times, lum))))}
    return res


def transitions(samples, min_delta=0.10, dark_max=0.80):
    """Times of opposing full-frame luminance swings of >= min_delta whose darker side is < dark_max.

    ponytail: full-frame average only. It catches whole-screen strobes but misses small flashing
    regions; use a PEAT/Harding-style analyser when content flashes locally or is broadcast-bound.
    """
    if not samples:
        return []
    out, last_dir = [], 0
    lo_t, lo = hi_t, hi = samples[0]
    for t, v in samples[1:]:
        if v > hi:
            hi_t, hi = t, v
        if v < lo:
            lo_t, lo = t, v
        if hi - lo >= min_delta and lo < dark_max:
            direction = 1 if hi_t > lo_t else -1
            if direction != last_dir:
                out.append(t)
                last_dir = direction
            lo_t, lo = hi_t, hi = t, v
    return out


def max_flashes_per_second(times):
    """A flash is a pair of opposing transitions; return the most flashes in any 1-second window."""
    best, j = 0, 0
    for i, t in enumerate(times):
        while t - times[j] > 1.0:
            j += 1
        best = max(best, (i - j + 1) // 2)
    return best


def contact_sheet(path, duration, out_png, cols=4, rows=3):
    n = cols * rows
    fps = n / max(duration, 0.1)
    code, _, err = run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-i', str(path), '-vf',
                        f'fps={fps:.6f},scale=480:-2,tile={cols}x{rows}', '-frames:v', '1', str(out_png)])
    if code:
        raise RuntimeError(err.strip() or 'contact sheet failed')


def evaluate(info, res, a):
    checks = []
    add = lambda name, ok, detail, hard=True: checks.append({'name': name, 'ok': bool(ok), 'hard': hard, 'detail': detail})
    if a.width and a.height:
        add('resolution', (info.get('width'), info.get('height')) == (a.width, a.height),
            f"{info.get('width')}x{info.get('height')} (want {a.width}x{a.height})")
    if a.fps:
        add('fps', abs(info.get('fps', 0) - a.fps) < 0.01, f"{info.get('fps', 0):.3f} (want {a.fps})")
    if a.duration:
        add('duration', abs(info['duration'] - a.duration) <= a.duration_tol,
            f"{info['duration']:.2f}s (want {a.duration}±{a.duration_tol}s)")
    if info.get('vcodec') == 'h264':
        add('pix_fmt', info.get('pix_fmt') == 'yuv420p', f"{info.get('pix_fmt')} (yuv420p plays everywhere)")
    if a.lufs is not None:
        loud = res.get('loudness') or {}
        I, tp = loud.get('I'), loud.get('TP')
        add('audio present', 'loudness' in res, 'audio stream found' if 'loudness' in res else 'no audio stream')
        if I is not None:
            add('integrated loudness', abs(I - a.lufs) <= a.lufs_tol, f'{I:.1f} LUFS (want {a.lufs}±{a.lufs_tol})')
        if tp is not None:
            add('true peak', tp <= a.true_peak, f'{tp:.1f} dBTP (max {a.true_peak})')
    flashes = res['flash']['max_per_second']
    add('flash risk (full-frame heuristic)', flashes <= 3, f'{flashes} flashes in worst 1-s window (max 3)')
    for key, label in (('black', 'black spans'), ('freeze', 'frozen spans'), ('silence', 'silent spans')):
        add(label, not res[key], res[key] or 'none', hard=False)
    return checks


def qa(path, a):
    info = probe(path)
    res = analyse(path, has_audio='acodec' in info)
    if a.sheet:
        contact_sheet(path, info['duration'], a.sheet)
    checks = evaluate(info, res, a)
    return {'file': str(path), 'probe': info, **res, 'checks': checks}


def selftest():
    with tempfile.TemporaryDirectory() as tmp:
        calm, strobe = Path(tmp, 'calm.mp4'), Path(tmp, 'strobe.mp4')
        run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'testsrc2=s=320x240:r=30:d=3', '-f', 'lavfi', '-i',
             'sine=f=440:d=3', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-shortest', str(calm)])
        # Toggles black/white every 3 frames at 30 fps: 5 flashes per second.
        run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'nullsrc=s=320x240:r=30:d=2,format=yuv420p,'
             "geq=lum='if(lt(mod(N\\,6)\\,3)\\,16\\,235)':cb=128:cr=128", '-c:v', 'libx264',
             '-pix_fmt', 'yuv420p', str(strobe)])
        a = argparse.Namespace(width=320, height=240, fps=30, duration=3, duration_tol=0.1, lufs=-14,
                               lufs_tol=30, true_peak=0, sheet=str(Path(tmp, 'sheet.png')))
        r = qa(calm, a)
        assert all(c['ok'] for c in r['checks'] if c['hard']), r['checks']
        assert r['loudness']['I'] is not None and Path(a.sheet).exists()
        s = qa(strobe, argparse.Namespace(width=None, height=None, fps=None, duration=None, duration_tol=0,
                                          lufs=None, lufs_tol=0, true_peak=0, sheet=None))
        assert s['flash']['max_per_second'] > 3, s['flash']
        assert max_flashes_per_second([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]) == 4
    print('selftest: ok')


def main():
    ap = argparse.ArgumentParser(description='Post-render QA gate for a finished video file.')
    ap.add_argument('video', nargs='?')
    ap.add_argument('--width', type=int)
    ap.add_argument('--height', type=int)
    ap.add_argument('--fps', type=float)
    ap.add_argument('--duration', type=float, help='expected seconds')
    ap.add_argument('--duration-tol', type=float, default=0.1)
    ap.add_argument('--lufs', type=float, help='integrated loudness target, e.g. -14 for most streaming')
    ap.add_argument('--lufs-tol', type=float, default=1.0)
    ap.add_argument('--true-peak', type=float, default=-1.0, help='max true peak in dBTP')
    ap.add_argument('--sheet', help='write a 4x3 contact sheet PNG for visual review')
    ap.add_argument('--json', help='write the full report as JSON')
    ap.add_argument('--selftest', action='store_true')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.video:
        ap.error('video path required (or --selftest)')
    try:
        report = qa(a.video, a)
    except (RuntimeError, OSError, json.JSONDecodeError) as e:
        print(f'ERROR: {e}', file=sys.stderr)
        sys.exit(2)
    if a.json:
        Path(a.json).write_text(json.dumps(report, indent=2), encoding='utf-8')
    p = report['probe']
    print(f"{report['file']}: {p.get('width')}x{p.get('height')} {p.get('fps', 0):.3f}fps "
          f"{p['duration']:.2f}s {p.get('vcodec')}/{p.get('pix_fmt')} audio={p.get('acodec', 'none')}")
    for c in report['checks']:
        mark = 'PASS' if c['ok'] else ('FAIL' if c['hard'] else 'WARN')
        print(f"  {mark:4}  {c['name']}: {c['detail']}")
    sys.exit(0 if all(c['ok'] for c in report['checks'] if c['hard']) else 1)


if __name__ == '__main__':
    main()
