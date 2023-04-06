# 2.5. Otsu Threshold

import cv2 as cv

image = cv.imread("dog.png")
image = cv.resize(image, (900, 600))

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 120, 255, cv.THRESH_OTSU)

cv.imshow("Otsu Threshold", thresh)
cv.waitKey(0)
cv.destroyAllWindows()
