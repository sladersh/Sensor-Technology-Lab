# 2.2.1. Averaging

import cv2 as cv

# reading the images
gaussianImg = cv.imread("gaussianNoiseImg.tif")
pepperSaltImg = cv.imread("peppersaltImg.tif")

# applying averaging
gaussianBlur = cv.blur(gaussianImg, (5, 5))
pepperSaltBlur = cv.blur(pepperSaltImg, (3, 3))

# displaying the image
cv.imshow("Original gaussianNoiseImg.tif", gaussianImg)
cv.imshow("5 x 5 kernel on gaussianNoiseImg", gaussianBlur)
cv.waitKey(0)

cv.imshow("Original peppersaltImg.tif", pepperSaltImg)
cv.imshow("5 x 5 kernel on peppersaltImg", pepperSaltBlur)
cv.waitKey(0)
