import io

import cv2
from PIL import ImageFilter
import numpy as np

from .run import process


def preprocess(image_bytes: bytes) -> bytes:
    # Converting input image
    input_image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)

    # Process to mask
    mask = process(input_image).filter(ImageFilter.BLUR)

    image = io.BytesIO()
    mask.save(image, format='PNG')

    return image.getvalue()

