from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.transcription_service import (
    transcribe_audio
)
from app.utils.file_validation import validate_audio

router = APIRouter(
    prefix="/api/transcription",
    tags=["Audio Transcription"]
)


ALLOWED_AUDIO_TYPES = {
    "audio/mpeg",
    "audio/mp3",
    "audio/wav",
    "audio/x-wav",
    "audio/mp4",
    "audio/x-m4a",
    "audio/webm",
    "video/mp4",
    "video/webm"
}

@router.post("/transcribe")
async def transcribe(
    file: UploadFile = File(...)
):

    audio_data = await validate_audio(file)

    return transcribe_audio(
        audio_data,
        file.filename or "audio.mp3"
    )