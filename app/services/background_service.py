from rembg import remove


def remove_background(image_data: bytes) -> bytes:
    """
    Remove the background from an image.

    Returns:
        PNG image bytes with transparent background.
    """

    result = remove(image_data)

    return result