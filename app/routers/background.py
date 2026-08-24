from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import Response

from app.services.background_service import remove_background
from app.utils.file_validation import validate_image

router = APIRouter(
    prefix="/api/background",
    tags=["Background Removal"]
)

@router.post("/remove")
async def remove_image_background(
    file: UploadFile = File(...)
):

    image_data = await validate_image(file)

    result = remove_background(image_data)

    return Response(
        content=result,
        media_type="image/png"
    )