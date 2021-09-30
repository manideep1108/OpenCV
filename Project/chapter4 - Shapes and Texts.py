import cv2 as cv
import numpy as np

img = np.zeros((512, 512))  # Creating a 512x512 matrix with zeros filled in it using numpy
cv.imshow("image", img)  # Using cv.imshow() function to display the matrix as an image
cv.waitKey(1000)

img = np.zeros((512, 512, 3), np.uint8)  # Also giving no. of channels ( Color image), Basically a 3d array
img[:] = 255, 0, 56  # Giving B,G,R values for the whole array
cv.imshow("image", img)  # Using cv.imshow() function to display the matrix as an image
cv.waitKey(1000)

img[200:300, 100:300] = 0, 69, 255
img[0:200, 300:512] = 34, 67, 45
cv.imshow("image", img)
cv.waitKey(1000)

img[:] = 0, 0, 0  # Changing the whole image back to black

# Drawing Lines

cv.line(img, (0, 0), (300, 300), (0, 255, 255), 3)
cv.line(img, (0, 512), (img.shape[1], 0), (0, 255, 0), 4)  # width is taken from the img.shape array
cv.imshow("image", img)
cv.waitKey(1000)

img[:] = 0, 0, 0  # Reset to Black

# Drawing Rectangles

cv.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 5)
cv.imshow("image", img)
cv.waitKey(1000)

cv.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv.FILLED)  # Fills the rectangle
cv.imshow("image", img)
cv.waitKey(1000)

img[:] = 0, 0, 0

# Drawing Circles

cv.circle(img, (256, 256), 100, (255, 255, 0), 5)
cv.imshow("image", img)
cv.waitKey(1000)

img[:] = 0, 0, 0

# Adding Text

cv.putText(img, "OpenCV Rocks!", (50, 250), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 69, 255), 2)
cv.imshow("image", img)
cv.waitKey(0)
