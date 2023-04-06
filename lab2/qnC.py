# 2.1.3. Power-Law (Gamma) Transformations

import cv2 as cv
import numpy as np

# reading img.tif
img = cv.imread("./img.tif")

# case: 0 < gamma < 1
for gamma in [0.4, 0.8]:
    gamma_transform = np.array(255 * (img / 255) ** gamma, dtype="uint8")
    cv.imshow(f"gamma_transformed {str(gamma)}.jpg", gamma_transform)

# case: gamma > 1
for gamma in [1.6, 2.7]:
    gamma_transform = np.array(255 * (img / 255) ** gamma, dtype="uint8")
    cv.imshow(f"gamma_transformed {str(gamma)}.jpg", gamma_transform)

cv.waitKey(0)
