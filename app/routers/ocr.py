from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.ocr_service import extract_text
from app.utils.file_validation import validate_image

router = APIRouter(
    prefix="/api/ocr",
    tags=["OCR"]
)

@router.post("/scan")
async def scan_image(
    file: UploadFile = File(...)
):

    image_data = await validate_image(file)

    return extract_text(image_data)