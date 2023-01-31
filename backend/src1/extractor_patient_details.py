# responsible for extracting data from pdf
# let's convert pdf to image

# 1. fetch the pdf file and convert to image
from pdf2image import convert_from_path
import pytesseract  # this module converts image to text
# from PIL import Image
# import numpy as np
# import cv2
import util

POPPLER_PATH = r"C:\poppler-22.12.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# colorful image -- gray -- resized -- adaptive threshold
# create a function for processing the image after pdf conversion before we read the text


def extract(file_path, file_format):
    # extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    # pages is an array of PIL images, i.e a bunch of images....stores the image file
    # you'll get image per pdf page...
    document_text = ''
    for page in pages:
        processed_image = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = '\n' + text
        return document_text

    # if file_format == 'prescription':
    #     pass    # extract data from prescription
    # elif file_format == 'patient_details':
    #     pass    # extract data from patient details


if __name__ == '__main__':
    data = extract('../resources1/patient_details/pd_1.pdf', 'patient_details')
    print(data)
