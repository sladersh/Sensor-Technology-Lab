# 2.3. Canny edge detector

import cv2 as cv
import numpy as np

img = cv.imread("piece03.png")
img = cv.resize(img, (1280, 720))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gaussian = cv.GaussianBlur(gray, (3, 3), 0)

img_canny = cv.Canny(img, 100, 200)

cv.imshow("Canny", img_canny)

cv.waitKey(0)
cv.destroyAllWindows()
