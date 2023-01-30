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
pages = convert_from_path(r'docs/prescription/pre_1.pdf', poppler_path=r"C:\poppler-22.12.0\Library\bin")
# pages is an array of PIL images, i.e a bunch of images....stores the image file
# you'll get image per pdf page....
pages[0].show()      # this helps you view the file

# 2. fetch the preprocessing function
img = preprocess_image(pages[0])
Image.fromarray(img).show()

# 3. then we extract the text
import pytesseract  # this module converts image to text
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(img, lang='eng')


import re

pattern1 = "Name:(.*)Date"

match1 = re.findall(pattern1, text)
print(match1[0].strip())

pattern2 = "Address:(.*)\n"

match2 = re.findall(pattern2, text)
print(match2[0].strip())

pattern3 = "K[^\n]*(.*)Directions"

match3 = re.findall(pattern3, text, flags=re.DOTALL)
print(match3[0].strip())

pattern4 = "Directions:[^\n]*(.*)Refill"

match4 = re.findall(pattern4, text, flags=re.DOTALL)
print(match4[0].strip())

pattern5 = "Refill:(.*)times"   # to extract only the number of refill

match5 = re.findall(pattern5, text, flags=re.DOTALL)
print(match5[0].strip())


print(zdlvlznv;NXv;ZDv)
