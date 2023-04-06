# 2.1. Basic morphological operations

import cv2 as cv
import numpy as np

# reading the image
img = cv.imread("img1.tif", 0)

# creating kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
hit_or_miss = cv.morphologyEx(img, cv.MORPH_HITMISS, kernel)

cv.imshow("Original Image", img)
cv.imshow("Erosion", erosion)
cv.imshow("Dilation", dilation)
cv.imshow("Opening", opening)
cv.imshow("Closing", closing)
cv.imshow("Hit or Miss", hit_or_miss)
cv.waitKey(0)
