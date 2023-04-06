import cv2 as cv
import numpy as np

image = cv.imread("testImg.jpg")
image = cv.resize(image, (900, 600))

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
ret, thresh = cv.threshold(blur, 40, 255, cv.THRESH_BINARY)

# finding contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

i = 1
for cnt in contours:
    M = cv.moments(cnt)
    print(f"Moments of contour {i} = {M}")
    area = cv.contourArea(cnt)
    print(f"Area of contour {i} = {area}")
    perimeter = cv.arcLength(cnt, True)
    print(f"Perimeter of contour {i} = {perimeter}")
    hull = cv.convexHull(cnt)
    print(f"Convex hull of contour {i} = {hull}")
    k = cv.isContourConvex(cnt)
    print(f"Convexity of contour {i} = {hull}")

    x, y, w, h = cv.boundingRect(cnt)
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    rect = cv.minAreaRect(cnt)
    box = cv.boxPoints(rect)
    box = np.int0(box)
    cv.drawContours(image, [box], 0, (0, 0, 255), 2)

    ellipse = cv.fitEllipse(cnt)
    cv.ellipse(image, ellipse, (255, 0, 0), 2)

    (x, y), (MA, ma), angle = cv.fitEllipse(cnt)

    x, y, w, h = cv.boundingRect(cnt)
    aspectRatio = float(w) / h

    area = cv.contourArea(cnt)
    diameter = np.sqrt(4 * area / np.pi)

    leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
    rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
    topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
    bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])

    i += 1

cv.imshow("Contour", image)
cv.waitKey(0)
cv.destroyAllWindows()
