import io

import easyocr
import numpy as np
from PIL import Image


reader = None


def get_reader():
    global reader

    if reader is None:
        reader = easyocr.Reader(
            ["en"],
            gpu=False
        )

    return reader


def extract_text(image_data: bytes) -> dict:
    """
    Extract text from an image using EasyOCR.
    """

    try:
        image = Image.open(
            io.BytesIO(image_data)
        ).convert("RGB")

        image_array = np.array(image)

        results = get_reader().readtext(
            image_array
        )

        detections = []

        for result in results:
            bounding_box = [
                [int(x), int(y)]
                for x, y in result[0]
            ]

            text = result[1]
            confidence = float(result[2])

            detections.append({
                "text": text,
                "confidence": round(confidence, 4),
                "bounding_box": bounding_box
            })

        full_text = "\n".join(
            detection["text"]
            for detection in detections
        )

        return {
            "text": full_text,
            "detections": detections,
            "count": len(detections)
        }

    except Exception as e:
        raise RuntimeError(
            f"OCR processing failed: {str(e)}"
        )