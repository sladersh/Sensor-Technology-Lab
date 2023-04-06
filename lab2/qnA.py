# 2.1.1. Image Negatives

import cv2 as cv

# reading img.tif
img = cv.imread("img.tif")

# inverting the image using bitwise_not
inverted_img = cv.bitwise_not(img, mask=None)

# displaying the image
cv.imshow("Original Image", img)
cv.imshow("Inverted Image", inverted_img)
cv.waitKey(0)
