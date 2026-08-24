from fastapi import HTTPException, UploadFile


MAX_IMAGE_SIZE = 10 * 1024 * 1024       # 10 MB
MAX_AUDIO_SIZE = 100 * 1024 * 1024      # 100 MB


IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp",
}


AUDIO_TYPES = {
    "audio/mpeg",
    "audio/wav",
    "audio/x-wav",
    "audio/mp4",
    "audio/x-m4a",
    "audio/webm",
    "video/mp4",
    "video/webm",
}


async def validate_image(file: UploadFile) -> bytes:

    if file.content_type not in IMAGE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, PNG, and WebP images are supported."
        )

    data = await file.read()

    if len(data) > MAX_IMAGE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Image must be smaller than 10 MB."
        )

    if not data:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    return data


async def validate_audio(file: UploadFile) -> bytes:

    if file.content_type not in AUDIO_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported audio/video format."
        )

    data = await file.read()

    if len(data) > MAX_AUDIO_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Audio/video file must be smaller than 100 MB."
        )

    if not data:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    return data