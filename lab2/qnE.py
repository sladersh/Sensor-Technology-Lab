# 2.2.2. Gaussian Filter

import cv2 as cv

# reading the images
gaussianImg = cv.imread("gaussianNoiseImg.tif")
pepperSaltImg = cv.imread("peppersaltImg.tif")

# applying gaussian blur
gaussianBlur = cv.GaussianBlur(gaussianImg, (5, 5), 0)
pepperSaltBlur = cv.GaussianBlur(pepperSaltImg, (3, 3), 0)

# displaying the image
cv.imshow("Original gaussianNoiseImg.tif", gaussianImg)
cv.imshow("5 x 5 kernel on gaussianNoiseImg", gaussianBlur)
cv.waitKey(0)

cv.imshow("Original peppersaltImg.tif", pepperSaltImg)
cv.imshow("5 x 5 kernel on peppersaltImg", pepperSaltBlur)
cv.waitKey(0)
