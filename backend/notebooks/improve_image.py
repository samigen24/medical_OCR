# What we want to do here is to improve the image quality
# import libraries: opencv and pillow
import cv2
from PIL import Image

# then read the image
img = cv2.imread("dark_image.jpg", flags=cv2.IMREAD_GRAYSCALE)

print(img)

Image.fromarray(img).show()  # to show original image

# improve the read image using simple thresholding
_, img2 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
print(img2)

Image.fromarray(img2).show()  # shows the new image

# because of the dark areas, we need to use adaptive threshold

img3 = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    61,
    11
)
Image.fromarray(img3).show()  # shows the new image with adaptive threshold
