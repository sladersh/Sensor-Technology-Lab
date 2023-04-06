# 2.2. Object Localization and Size Estimation

import cv2 as cv
import numpy as np

# reading the image
img = cv.imread("img2.tif")

# creating kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (9, 9))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gauss_filter_img = cv.GaussianBlur(gray, (5, 5), 0)

ret, thresh = cv.threshold(gauss_filter_img, 127, 255, cv.THRESH_BINARY)

closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)

ind = np.where(closing > 0)
rows = ind[0]
cols = ind[1]

y = rows
x = cols

w = max(x) - min(x)
h = max(y) - min(y)

cx = int(min(x) + (w / 2))
cy = int(min(y) + (h / 2))

c = (cx, cy)
print(f"Center, c = {c}")

cv.circle(img, (cx, cy), 7, (0, 0, 255), -1)

cv.imshow("Original Image", img)
cv.waitKey(0)
