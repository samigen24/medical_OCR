import numpy as np
import cv2
from PIL import Image

# colorful image -- gray -- resized -- adaptive threshold

def preprocess_image(img):
    # this helps to convert colorful image into gray (black & white)
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    # also do a resize of the image...
    # making the image bigger for pixels are more visible/readable for better output
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

    processed_image = cv2.adaptiveThreshold(
    resized, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    61,
    11
    )
    return processed_image
