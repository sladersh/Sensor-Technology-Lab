# Task 1: Image recognition using template matching

import cv2 as cv

image = cv.imread("./Task1_pics/test1.png")

template = cv.imread("./Task1_pics/template.png")

image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
template_gray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

w, h = template_gray.shape[::-1]

result = cv.matchTemplate(image_gray, template_gray, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
bottom_right = (max_loc[0] + w, max_loc[1] + h)
cv.rectangle(image, max_loc, bottom_right, (255, 0, 0), 2)

cv.imshow("Matched Image", image)
cv.waitKey(0)
cv.destroyAllWindows()
