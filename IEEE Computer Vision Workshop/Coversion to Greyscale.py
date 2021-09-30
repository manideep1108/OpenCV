import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/unnamed.png",cv.IMREAD_COLOR)
img = cv.resize(img, (312, 258))
cv.imshow("ColorFruit",img)


# Conversion of RGB to GreyScale

# Method 1 ( Taking mean of R,G,B values )
GreyFruit1 = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        #GreyFruit1[i][j] = (int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2]))/3
        GreyFruit1[i][j] = np.sum(img[i][j])/3

cv.imshow("GreyFruit1", GreyFruit1)

# Method 2 ( Grey = 0.21R + 0.72G + 0.07B )
GreyFruit2 = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        GreyFruit2[i][j] = 0.21*int(img[i][j][0]) + 0.72*int(img[i][j][1]) + 0.07*int(img[i][j][2])

cv.imshow("GreyFruit2", GreyFruit2)

# Method 3 ( Taking mean of greatest and lowest values )
GreyFruit3 = np.full((img.shape[0], img.shape[1]), 0, dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        GreyFruit3[i][j] = (max(int(img[i][j][0]), int(img[i][j][1]), int(img[i][j][2])) + min(int(img[i][j][0]), int(img[i][j][1]), int(img[i][j][2])))/2

cv.imshow("GreyFruit3", GreyFruit3)

cv.waitKey(0)
