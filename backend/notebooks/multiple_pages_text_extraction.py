# Challenge: Convert a multi-page PDF into a directory of images

# let's convert pdf to image
import numpy as np
import cv2
from PIL import Image


# colorful image -- gray -- resized -- adaptive threshold

# create a function for processing the image after pdf conversion before we read the text
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


# 1. fetch the pdf file and convert to image
from pdf2image import convert_from_path

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError)

pages = convert_from_path(r"docs/prescription/tka.pdf", poppler_path=r"C:\poppler-22.12.0\Library\bin")
# pages is an array of PIL images, i.e a bunch of images....stores the image file
# you'll get image per pdf page....
for i, page in enumerate(pages):
    fname = "page" + str(i) + ".jpg"
    page.save(fname, 'JPEG')


#
# for page in pages:
#     n = 1
#     page.save(f'page{n}.png', 'PNG')
#     n += 1
# print(page())

    # this helps you view the file
