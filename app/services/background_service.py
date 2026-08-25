def remove_background(image_data: bytes) -> bytes:
    """
    Remove the background from an image.

    Returns:
        PNG image bytes with transparent background.
    """

    from rembg import remove

    return remove(image_data)