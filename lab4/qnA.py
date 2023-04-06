# 2.1. Prewitt edge detector

import cv2 as cv
import numpy as np

img = cv.imread("car.png")
img = cv.resize(img, (1280, 720))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gaussian = cv.GaussianBlur(gray, (3, 3), 0)

kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

img_prewitt_x = cv.filter2D(img_gaussian, -1, kernel_x)
img_prewitt_y = cv.filter2D(img_gaussian, -1, kernel_y)

cv.imshow("Prewitt X", img_prewitt_x)
cv.imshow("Prewitt Y", img_prewitt_y)
cv.imshow("Prewitt", img_prewitt_x + img_prewitt_y)

cv.waitKey(0)
cv.destroyAllWindows()
