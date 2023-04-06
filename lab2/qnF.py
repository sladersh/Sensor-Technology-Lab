# 2.2.3. Median Filtering

import cv2 as cv

# reading the images
gaussianImg = cv.imread("gaussianNoiseImg.tif")
pepperSaltImg = cv.imread("peppersaltImg.tif")

# applying median blur
gaussianBlur = cv.medianBlur(gaussianImg, 5)
pepperSaltBlur = cv.medianBlur(pepperSaltImg, 3)

# Displaying the image
cv.imshow("Original gaussianNoiseImg.tif", gaussianImg)
cv.imshow("5 x 5 kernel on gaussianNoiseImg", gaussianBlur)
cv.waitKey(0)

cv.imshow("Original peppersaltImg.tif", pepperSaltImg)
cv.imshow("5 x 5 kernel on peppersaltImg", pepperSaltBlur)
cv.waitKey(0)
