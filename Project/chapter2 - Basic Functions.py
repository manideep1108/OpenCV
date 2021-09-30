import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cat.jpg")

# Let's change the color space to Greyscale
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GreyCat",imgGray)
cv.waitKey(2000)

# Adding Gaussian Blur
# Ksize is kernal size and it should be (a,a) where a is an odd number
imgBlur = cv.GaussianBlur(img,(17,17),0)
cv.imshow("BlurCat",imgBlur)
cv.waitKey(2000)

# Edge detector
imgCanny = cv.Canny(img,150,200)
cv.imshow("CannyCat",imgCanny)
cv.waitKey(2000)

# Dilation
kernel = np.ones((5,5),np.uint8)
imgDilation = cv.dilate(imgCanny,kernel,iterations=1)
cv.imshow("DilationCat",imgDilation)
cv.waitKey(2000)

# Erossion
imgEroded = cv.erode(imgDilation,kernel,iterations=1)
cv.imshow("ErodedCat",imgEroded)
cv.waitKey(0)