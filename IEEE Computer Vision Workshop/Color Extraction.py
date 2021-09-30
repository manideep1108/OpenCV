import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/unnamed.png", cv.IMREAD_COLOR)

rmin = 143
gmax = 38
bmax = 46

cv.namedWindow("mywindow")

def rmin_update(value):
    global rmin
    rmin = value


def gmax_update(value):
    global gmax
    gmax = value


def bmax_update(value):
    global bmax
    bmax = value


cv.createTrackbar("rmin", "mywindow", 143, 255, rmin_update)
cv.createTrackbar("gmax", "mywindow", 38, 255, gmax_update)
cv.createTrackbar("bmax", "mywindow", 46, 255, bmax_update)

while(1):
    myimg = img.copy()
    for i in range(myimg.shape[0]):
        for j in range(myimg.shape[1]):
            if(not(myimg[i][j][2]>=rmin) or not(myimg[i][j][0]<=bmax) or not(myimg[i][j][1]<=gmax)):
                myimg[i][j][0] = 0
                myimg[i][j][1] = 0
                myimg[i][j][2] = 0
    cv.imshow("mywindow",myimg)
    cv.waitKey(1)







