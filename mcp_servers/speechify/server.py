"""Speechify Text-to-Speech MCP server.

Wraps the official Speechify TTS REST API (https://api.speechify.ai) and exposes
it over the Model Context Protocol so MCP clients can synthesize speech and list
available voices.

Requires the SPEECHIFY_API_KEY environment variable. Get a key from
https://console.sws.speechify.com/.
"""

import base64
import os
import time
from pathlib import Path
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

API_BASE = os.environ.get("SPEECHIFY_API_BASE", "https://api.speechify.ai")
REQUEST_TIMEOUT = 120.0

mcp = FastMCP("speechify")


def _auth_headers() -> dict[str, str]:
    api_key = os.environ.get("SPEECHIFY_API_KEY")
    if not api_key:
        raise RuntimeError(
            "SPEECHIFY_API_KEY is not set. Export it before launching the server "
            "(get a key at https://console.sws.speechify.com/)."
        )
    return {"Authorization": f"Bearer {api_key}"}


@mcp.tool()
async def list_voices() -> list[dict[str, Any]]:
    """List the text-to-speech voices available to the account.

    Returns a compact list of voices with their id, display name, gender and
    locale so a caller can pick a voice_id for text_to_speech.
    """
    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
        resp = await client.get(f"{API_BASE}/v1/voices", headers=_auth_headers())
        resp.raise_for_status()
        voices = resp.json()

    return [
        {
            "id": v.get("id"),
            "display_name": v.get("display_name"),
            "gender": v.get("gender"),
            "locale": v.get("locale"),
            "type": v.get("type"),
            "tags": v.get("tags"),
        }
        for v in voices
    ]


@mcp.tool()
async def text_to_speech(
    text: str,
    voice_id: str = "george",
    audio_format: str = "mp3",
    output_path: str | None = None,
) -> dict[str, Any]:
    """Synthesize speech from text using the Speechify API.

    Args:
        text: The text to convert to speech.
        voice_id: Voice to use (see list_voices). Defaults to "george".
        audio_format: Output format, e.g. "mp3", "wav", "ogg", "aac".
        output_path: Where to write the audio file. If omitted, a timestamped
            file is written to the current working directory.

    Returns the absolute path of the written audio file and the billable
    character count reported by the API.
    """
    payload = {"input": text, "voice_id": voice_id, "audio_format": audio_format}

    async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
        resp = await client.post(
            f"{API_BASE}/v1/audio/speech",
            headers={**_auth_headers(), "Content-Type": "application/json"},
            json=payload,
        )
        resp.raise_for_status()
        data = resp.json()

    audio_bytes = base64.b64decode(data["audio_data"])

    if output_path:
        dest = Path(output_path).expanduser().resolve()
    else:
        dest = Path.cwd() / f"speechify_{int(time.time())}.{audio_format}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(audio_bytes)

    return {
        "output_path": str(dest),
        "bytes_written": len(audio_bytes),
        "audio_format": data.get("audio_format", audio_format),
        "billable_characters_count": data.get("billable_characters_count"),
    }


if __name__ == "__main__":
    mcp.run()
