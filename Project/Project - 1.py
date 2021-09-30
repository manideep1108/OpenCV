
# Virtual paint


import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)    # Argument 0 uses the default webcam of the computer
cap.set(3, 640)             # Setting the width
cap.set(4, 480)             # Setting the height
cap.set(10, 150)            # Setting the brightness


myColors = [[61, 55, 109, 121, 250, 255]]
myColorValues = [[101,213,4]]
myPoints = []           #[x, y, colorID]
def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x,y,width,height =0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            #cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            x, y, width, height = cv.boundingRect(approx)
    return int(x+width/2),y


def drawOnCanvas(mypoints,myColorValues):
    for point in mypoints:
        cv.circle(imgResult, (point[0], point[1]), 20, myColorValues[point[2]], cv.FILLED)



def findColor(img, myColors, myColorValues):
    newPoints = []
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv.inRange(imgHSV, lower, upper)
    x,y=getContours(mask)
    cv.circle(imgResult, (x, y), 20, myColorValues[0], cv.FILLED)
    if x!=0 and y!=0:
        newPoints.append([x,y,0])
    #cv.imshow("img", mask)
    return newPoints



while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints)!=0:
        for newp in newPoints:
            myPoints.append(newp)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
    cv.imshow("Video", imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
