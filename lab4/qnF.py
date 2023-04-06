# 2.6. Adaptive Threshold

import cv2 as cv

image = cv.imread("Coins.png")
image = cv.resize(image, (900, 600))

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

thresh1 = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 21, 10
)

thresh2 = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 21, 10
)

cv.imshow("Adaptive Mean Threshold", thresh1)
cv.imshow("Adaptive Gauss Threshold", thresh2)
cv.waitKey(0)
cv.destroyAllWindows()
