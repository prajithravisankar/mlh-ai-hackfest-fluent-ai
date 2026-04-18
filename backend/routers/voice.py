import logging
import os
from typing import Optional

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/voice", tags=["voice"])


@router.post("/clone")
async def clone_voice(
    audio: UploadFile = File(...),
    user_id: str = Form(...),
    name: Optional[str] = Form(None),
):
    """
    Accept user audio, call ElevenLabs Instant Voice Clone API,
    store the cloned voice ID in the user's profile.
    """
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="ELEVENLABS_API_KEY not configured")

    audio_bytes = await audio.read()
    if len(audio_bytes) < 1000:
        raise HTTPException(status_code=400, detail="Audio clip too short for voice cloning")

    # Call ElevenLabs voice clone API
    import httpx

    clone_name = name or f"fluent-ai-{user_id}"
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            resp = await client.post(
                "https://api.elevenlabs.io/v1/voices/add",
                headers={"xi-api-key": api_key},
                data={
                    "name": clone_name,
                    "description": f"FluentAI voice clone for user {user_id}",
                },
                files={"files": (audio.filename or "recording.webm", audio_bytes, audio.content_type or "audio/webm")},
            )
            if resp.status_code != 200:
                logger.error(f"Voice clone API error: {resp.status_code} {resp.text}")
                raise HTTPException(status_code=502, detail=f"ElevenLabs API error: {resp.status_code}")

            result = resp.json()
            voice_id = result.get("voice_id", "")
    except httpx.HTTPError as e:
        logger.error(f"Voice clone request failed: {e}")
        raise HTTPException(status_code=502, detail="Failed to contact ElevenLabs API")

    # Store voice ID in database
    from database import get_db

    db = await get_db()
    try:
        # Add cloned_voice_id column if it doesn't exist (safe migration)
        try:
            await db.execute(
                "ALTER TABLE users ADD COLUMN cloned_voice_id TEXT DEFAULT ''",
            )
            await db.commit()
        except Exception:
            pass  # Column already exists

        await db.execute(
            "UPDATE users SET cloned_voice_id = ? WHERE id = ?",
            (voice_id, user_id),
        )
        await db.commit()
    finally:
        await db.close()

    logger.info(f"Voice cloned for user={user_id}, voice_id={voice_id}")
    return {"voice_id": voice_id, "user_id": user_id, "status": "cloned"}
