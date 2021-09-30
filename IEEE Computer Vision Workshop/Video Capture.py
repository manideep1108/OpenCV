import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)
if not cap.isOpened():
    print("Error opening the camera")
    exit()

while True:
    ret,frame = cap.read()
    if not ret:
        print("Can't receive video ")
        break
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    cv.imshow("frame",hsv)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllwindows()