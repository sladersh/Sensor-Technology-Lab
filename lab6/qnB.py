# Task 2: Detect multiple objects inside Image with different rotations

import cv2 as cv
import numpy as np

image = cv.imread("./Task2_pics/cards.png")

template = cv.imread("./Task2_pics/Templateshape.png")

image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

w, h = template_gray.shape[::-1]

result = cv.matchTemplate(image_gray, template_gray, cv.TM_CCOEFF_NORMED)

threshold = 0.6
loc = np.where(result >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(image, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 2)

cv.imshow("Matched Image", image)
cv.waitKey(0)
cv.destroyAllWindows()
