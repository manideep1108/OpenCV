import cv2 as cv
import numpy as np

def empty(a):
    pass

path = 'Resources/Photos/group 2.jpg'

#Creating Track Bars

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("Hue Min", "TrackBars", 146, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv.createTrackbar("Sat Min", "TrackBars", 55, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 250, 255, empty)
cv.createTrackbar("Val Min", "TrackBars", 145, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


cap= cv.VideoCapture(0)    # Argument 0 uses the default webcam of the computer
cap.set(3,640)             # Setting the width
cap.set(4,480)             # Setting the height
cap.set(10,140)            # Setting the brightness

while True:
    _, img = cap.read()
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)      # Converting into HSV Color Space

    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)

    imgResult = cv.bitwise_and(img,img,mask=mask)

    cv.imshow("Original", img)
    #cv.imshow("HSV", imgHSV)
    cv.imshow("Mask", mask)
    cv.imshow("Result",imgResult)
    cv.waitKey(1)

