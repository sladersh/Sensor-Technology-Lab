import cv2 as cv
import numpy as np

image = cv.imread("dog.png")
image = cv.resize(image, (900, 600))

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp = sift.detect(gray, None)

img = cv.drawKeypoints(gray, kp, image, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow("SIFT", img)
cv.waitKey(0)
cv.destroyAllWindows()
