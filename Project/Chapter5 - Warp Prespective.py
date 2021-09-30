import numpy as np
import cv2 as cv

img = cv.imread("Resources/Photos/cards.jpg")
print(img.shape)
# img = cv.resize(img,(650,460))
cv.imshow("cards", img)
cv.waitKey(1000)

# Changing the perspective
# Get 4 corner points. One can do this by opening the image in paint and hovering the cursor

width, height = 250, 350  # defining the output image width and height
pts1 = np.float32([[149, 183], [182, 79], [452, 214], [460, 102]])  # This array stores the 4 corner points of the part we like to change perspective in the input image
pts2 = np.float32([[0, 0], [width, 0], [0, height],
                   [width, height]])  # This array stores the corresponding points in the output image
matrix = cv.getPerspectiveTransform(pts1, pts2)  # This transform matrix is created using above two point matrices
imgOutput = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("Output", imgOutput)
cv.waitKey(0)
