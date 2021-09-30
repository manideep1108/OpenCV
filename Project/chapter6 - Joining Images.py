import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cat.jpg")
print(img.shape)
img = img[0:427, 320:640]

imgHor = np.hstack((img, img, img))
imgVer = np.vstack((imgHor, imgHor))

cv.imshow("Horizontal", imgHor)
cv.imshow("Vertical", imgVer)
cv.waitKey(0)
