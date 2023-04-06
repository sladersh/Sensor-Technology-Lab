# 2.4. Hough Transform

import cv2 as cv
import numpy as np

image = cv.imread("piece03.png")
image = cv.resize(image, (900, 600))

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray, 50, 150, apertureSize=3)

lines1 = cv.HoughLines(edges, 1, np.pi / 180, 130)
img_lines1 = image.copy()

for r_theta in lines1:
    arr = np.array(r_theta[0], dtype=np.float64)
    r, theta = arr

    a = np.cos(theta)

    b = np.sin(theta)

    x0 = a * r

    y0 = b * r

    x1 = int(x0 + 1000 * (-b))

    y1 = int(y0 + 1000 * (a))

    x2 = int(x0 - 1000 * (-b))

    y2 = int(y0 - 1000 * (a))

    cv.line(img_lines1, (x1, y1), (x2, y2), (0, 0, 255), 2)

lines2 = cv.HoughLinesP(
    edges, 1, np.pi / 180, threshold=40, minLineLength=5, maxLineGap=50
)

for points in lines2:
    x1, y1, x2, y2 = points[0]
    cv.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv.imshow("Hough", img_lines1)
cv.imshow("Hough Transform", image)

cv.waitKey(0)
cv.destroyAllWindows()
