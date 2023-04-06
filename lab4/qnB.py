# 2.2. Sobel edge detector

import cv2 as cv
import numpy as np

img = cv.imread("dog.png")
img = cv.resize(img, (1280, 720))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gaussian = cv.GaussianBlur(gray, (3, 3), 0)

img_sobelx = cv.Sobel(img_gaussian, cv.CV_8U, 1, 0, ksize=5)
img_sobely = cv.Sobel(img_gaussian, cv.CV_8U, 0, 1, ksize=5)
img_sobel = img_sobelx + img_sobely

cv.imshow("Sobel X", img_sobelx)
cv.imshow("Sobel Y", img_sobely)
cv.imshow("Sobel", img_sobel)

cv.waitKey(0)
cv.destroyAllWindows()
