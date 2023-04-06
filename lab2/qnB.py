# 2.1.2. Log Transformations

import cv2 as cv
import numpy as np

# reading img.tif
img = cv.imread("img.tif")

# applying log transformation
c = 255 / np.log(1 + np.max(img))
log_image = c * (np.log(img + 1, where=img + 1 > 0))

# convert float to int
log_image = np.array(log_image, dtype=np.uint8)

# displaying the image
cv.imshow("Original Image", img)
cv.imshow("Logarithmic Image", log_image)
cv.waitKey(0)
