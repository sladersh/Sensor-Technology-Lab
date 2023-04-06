import cv2 as cv

yourImg = cv.imread("img.tif")
print(f"Shape of the image is {yourImg.shape}")
print(f"Image type is {yourImg.dtype}")

print(f"Pixel at (0, 0) is {yourImg[0, 0]}")
(blue, green, red) = yourImg[0, 0]
print(f"RGB values at (0, 0) - Red: {red}, Green: {green}, Blue: {blue}")

yourImg[0, 0] = (255, 0, 255)
print(f"Pixel at (0, 0) after modification is {yourImg[0, 0]}")

roi = yourImg[50:100, 50:100]
print(f"Shape of ROI is {roi.shape}")

yourImg[50:100, 50:100] = (0, 255, 255)
cv.imshow("Updated", yourImg)
cv.waitKey(0)
