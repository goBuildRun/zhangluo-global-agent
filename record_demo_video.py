#!/usr/bin/env python3
"""
Automated 1080p Demo Video Recorder & English Voiceover Synthesizer for Zhangluo (小張羅).
Generates a judge-ready < 2.5 minute MP4 video with synchronized English TTS narration,
on-screen subtitle banners, and live interactive walkthrough across all 4 tabs and 3 sponsor tracks.
"""

import json
import os
import subprocess
import tempfile
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

FFMPEG_BIN = "/opt/homebrew/bin/ffmpeg"
FFPROBE_BIN = "/opt/homebrew/bin/ffprobe"
SAY_BIN = "/usr/bin/say"
BASE_URL = "http://127.0.0.1:8765"

SCENES = [
    {
        "id": "scene1_intro_orchestrate",
        "caption": "Scene 1 · Zhangluo (小張羅): iOS Native Plugins + 6-Stage Fiduciary Orchestration (Qloo × Nebius NVIDIA × Tavily)",
        "narration": (
            "Meet Zhangluo, a fiduciary household and cultural taste orchestration agent built with five native iOS Swift plugins "
            "and a multi-agent backend. Unlike ad-driven shopping bots, Zhangluo orchestrates seasonal living across twenty-four solar terms. "
            "In our Frost's Descent scenario, we trigger six-stage orchestration powered by Nebius NVIDIA Nemotron Seventy-B, "
            "Qloo Taste A.I. with zero-point-nine-six cultural affinity, and Tavily real-time verification."
        ),
    },
    {
        "id": "scene2_household_video_sweep",
        "caption": "Scene 2 · 起居簿 Household 4 Pillars: 12-Second Camera Video Sweep (750ms Keyframe Diff ≥ 0.035), Granary & Gout Redline",
        "narration": (
            "Switching to the Household Ledger tab, Zhangluo manages four pillars: the Seasonal Granary, Spatial Home Inventory, "
            "Guest Dietary Redlines such as Mr. Wang's strict low-purine gout restriction, and the Seasonal Gift Reciprocity Ledger. "
            "When we click Run Twelve-Second Video Sweep Intake, Zhangluo samples camera frames every seven hundred fifty milliseconds, "
            "filters keyframes by pixel difference, and batch-adds household items like our Dyson vacuum and Suzhou winter wine directly into the spatial ledger."
        ),
    },
    {
        "id": "scene3_paypal_fiduciary_checkout",
        "caption": "Scene 3 · 买得对 Fiduciary Checkout: Duplicate-Purchase Guard Saves $19.50 + PayPal Agentic Order & Ledger Auto-Sync",
        "narration": (
            "Back on the Orchestrate tab, every recommendation carries a cryptographically signed comparison digest with zero ad bias. "
            "Before checkout, Zhangluo's duplicate-purchase guard detects five hundred grams of organic ginger already in the fridge drawer, "
            "automatically saving nineteen dollars and fifty cents. Clicking Authorize PayPal Fiduciary Order captures the PayPal Sandbox transaction, "
            "syncs the new item into the household ledger, and marks Old Chen's return gift as fulfilled."
        ),
    },
    {
        "id": "scene4_terroir_and_sovereign_memory",
        "caption": "Scene 4 · 风物志 2,843-County AAA Terroir & 自留地 OpenViking Force-Directed Taste Star Graph + Proof-of-Taste",
        "narration": (
            "In the Solar Terroir tab, our hybrid vector and PostGIS spatial index spans two thousand eight hundred forty-three counties "
            "with triple-A anti-noise purity. Finally, in the Sovereign Memory tab, users inspect their force-directed taste star graph, "
            "confirm or revoke OpenViking memory consent with a single click, and mint anonymized Proof-of-Taste discoveries. "
            "Thank you for watching Zhangluo."
        ),
    },
]


def get_audio_duration(path: Path) -> float:
    cmd = [
        FFPROBE_BIN,
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        str(path),
    ]
    out = subprocess.check_output(cmd, text=True).strip()
    return float(out)


def build_voiceover_tracks(work_dir: Path):
    wav_files = []
    durations = []
    for idx, scene in enumerate(SCENES):
        aiff_path = work_dir / f"{idx:02d}_{scene['id']}.aiff"
        wav_path = work_dir / f"{idx:02d}_{scene['id']}.wav"
        subprocess.run(
            [SAY_BIN, "-v", "Samantha", "-r", "182", "-o", str(aiff_path), scene["narration"]],
            check=True,
        )
        # Convert to 44.1kHz stereo wav with a 0.6s silence pad at the end
        subprocess.run(
            [
                FFMPEG_BIN,
                "-y",
                "-i",
                str(aiff_path),
                "-af",
                "apad=pad_dur=0.6",
                "-ar",
                "44100",
                "-ac",
                "2",
                str(wav_path),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        dur = get_audio_duration(wav_path)
        wav_files.append(wav_path)
        durations.append(dur)
        print(f"  [TTS] {scene['id']}: {dur:.2f}s")

    concat_list = work_dir / "concat_audio.txt"
    concat_list.write_text("\n".join(f"file '{w.as_posix()}'" for w in wav_files), encoding="utf-8")
    full_audio = work_dir / "full_voiceover.wav"
    subprocess.run(
        [
            FFMPEG_BIN,
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(full_audio),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return full_audio, durations


def set_caption(page, text: str):
    page.evaluate(
        """(captionText) => {
            let banner = document.getElementById('judge-caption-banner');
            if (!banner) {
                banner = document.createElement('div');
                banner.id = 'judge-caption-banner';
                banner.style.cssText = [
                    'position: fixed',
                    'bottom: 16px',
                    'left: 50%',
                    'transform: translateX(-50%)',
                    'z-index: 9999',
                    'background: rgba(18, 18, 22, 0.94)',
                    'border: 1.5px solid #D4A056',
                    'box-shadow: 0 8px 30px rgba(0,0,0,0.65)',
                    'color: #F2F0EB',
                    'padding: 10px 22px',
                    'border-radius: 999px',
                    'font-size: 14.5px',
                    'font-weight: 600',
                    'letter-spacing: 0.2px',
                    'white-space: nowrap'
                ].join(';');
                document.body.appendChild(banner);
            }
            banner.textContent = captionText;
        }""",
        text,
    )


def highlight_and_click(page, selector: str, wait_after: float = 1.2):
    loc = page.locator(selector).first
    loc.scroll_into_view_if_needed()
    loc.evaluate(
        """(el) => {
            const prevOutline = el.style.outline;
            const prevShadow = el.style.boxShadow;
            el.style.outline = '2.5px solid #D4A056';
            el.style.boxShadow = '0 0 22px rgba(212, 160, 86, 0.75)';
            setTimeout(() => {
                el.style.outline = prevOutline;
                el.style.boxShadow = prevShadow;
            }, 1400);
        }"""
    )
    time.sleep(0.45)
    loc.click()
    time.sleep(wait_after)


def record_browser_walkthrough(work_dir: Path, durations: list[float]) -> Path:
    video_dir = work_dir / "pw_video"
    video_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            device_scale_factor=1,
            record_video_dir=str(video_dir),
            record_video_size={"width": 1920, "height": 1080},
        )
        page = context.new_page()
        page.goto(BASE_URL, wait_until="networkidle")
        time.sleep(0.6)

        # --- SCENE 1: Intro & 6-Stage Orchestration ---
        t0 = time.monotonic()
        set_caption(page, SCENES[0]["caption"])
        time.sleep(2.5)
        highlight_and_click(page, "button:has-text('Qloo Taste AI')", wait_after=1.8)
        highlight_and_click(page, "button:has-text('Nebius × NVIDIA + Tavily')", wait_after=1.8)
        highlight_and_click(page, "button:has-text('Full Matrix')", wait_after=1.2)
        highlight_and_click(page, "button:has-text('张罗 Orchestrate')", wait_after=2.5)
        elapsed = time.monotonic() - t0
        rem = max(0.2, durations[0] - elapsed)
        time.sleep(rem)

        # --- SCENE 2: 起居簿 Household 4 Pillars & 12s Video Sweep ---
        t0 = time.monotonic()
        set_caption(page, SCENES[1]["caption"])
        highlight_and_click(page, "button.tab-btn:has-text('起居簿 Household')", wait_after=2.2)
        highlight_and_click(page, "button:has-text('Run 12s Video Sweep Intake')", wait_after=3.0)
        page.mouse.wheel(0, 360)
        time.sleep(2.8)
        page.mouse.wheel(0, -360)
        elapsed = time.monotonic() - t0
        rem = max(0.2, durations[1] - elapsed)
        time.sleep(rem)

        # --- SCENE 3: PayPal Fiduciary Checkout & Ledger Sync ---
        t0 = time.monotonic()
        set_caption(page, SCENES[2]["caption"])
        highlight_and_click(page, "button.tab-btn:has-text('找张罗 Orchestrate')", wait_after=1.8)
        highlight_and_click(page, "button:has-text('PayPal Agentic Commerce')", wait_after=1.5)
        page.mouse.wheel(0, 280)
        time.sleep(1.5)
        highlight_and_click(page, "#orch-cards button:has-text('Authorize PayPal Fiduciary Order')", wait_after=2.8)
        # Also authorize the second card (Old Chen's return gift tea)
        second_btn = page.locator("#orch-cards button:has-text('Authorize PayPal Fiduciary Order')").nth(1)
        second_btn.scroll_into_view_if_needed()
        second_btn.click()
        time.sleep(2.2)
        page.mouse.wheel(0, -280)
        elapsed = time.monotonic() - t0
        rem = max(0.2, durations[2] - elapsed)
        time.sleep(rem)

        # --- SCENE 4: 风物志 Solar Terroir & 自留地 Sovereign Memory ---
        t0 = time.monotonic()
        set_caption(page, SCENES[3]["caption"])
        highlight_and_click(page, "button.tab-btn:has-text('风物志 Solar Terroir')", wait_after=3.2)
        highlight_and_click(page, "button.tab-btn:has-text('自留地 Sovereign')", wait_after=2.2)
        highlight_and_click(page, "button:has-text('Confirm into OpenViking Profile')", wait_after=2.2)
        highlight_and_click(page, "button:has-text('Anonymize & Share Discovery')", wait_after=2.2)
        # Brief bilingual toggle showcase
        highlight_and_click(page, "#lang-btn", wait_after=1.8)
        highlight_and_click(page, "#lang-btn", wait_after=1.2)
        elapsed = time.monotonic() - t0
        rem = max(0.5, durations[3] - elapsed)
        time.sleep(rem)

        video_path = Path(page.video.path())
        context.close()
        browser.close()
        return video_path


def merge_video_and_audio(raw_video: Path, full_audio: Path, output_mp4: Path):
    output_mp4.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            FFMPEG_BIN,
            "-y",
            "-i",
            str(raw_video),
            "-i",
            str(full_audio),
            "-c:v",
            "libx264",
            "-preset",
            "fast",
            "-crf",
            "20",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-shortest",
            "-movflags",
            "+faststart",
            str(output_mp4),
        ],
        check=True,
    )


def main():
    output_mp4 = Path(
        "/Users/aronezhang-mini/buildrun-agent-engineering-platform/products/hackathon/submissions/zhangluo-demo-1080p.mp4"
    )
    with tempfile.TemporaryDirectory(prefix="zhangluo_video_") as tmp:
        work_dir = Path(tmp)
        print("1. Synthesizing English TTS voiceover scenes...")
        full_audio, durations = build_voiceover_tracks(work_dir)
        total_audio_sec = sum(durations)
        print(f"   Total voiceover duration: {total_audio_sec:.2f}s ({total_audio_sec/60:.2f} min)")

        print("2. Recording 1920x1080 Playwright live browser walkthrough...")
        raw_video = record_browser_walkthrough(work_dir, durations)
        print(f"   Raw browser video recorded: {raw_video}")

        print("3. Muxing H.264 1080p MP4 with AAC English voiceover...")
        merge_video_and_audio(raw_video, full_audio, output_mp4)

    final_dur = get_audio_duration(output_mp4)
    size_mb = output_mp4.stat().st_size / (1024 * 1024)
    print(f"\n✅ Demo Video Ready: {output_mp4}")
    print(f"   Duration: {final_dur:.2f}s (< 180s Devpost limit) | Size: {size_mb:.2f} MB")


if __name__ == "__main__":
    main()
