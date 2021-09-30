import cv2 as cv
import numpy as np

path = "Resources/Photos/Shapes.png"
img = cv.imread(path)
# img = cv.resize(img, (288, 288))
imgContour = img.copy()


def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area > 500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            print(peri)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, width, height = cv.boundingRect(approx)

            if objCor == 3:
                objectType = "Triangle"
            elif objCor ==4:
                aspRatio = width/float(height)
                if aspRatio >0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            else:
                objectType = "Circle"

            cv.rectangle(imgContour, (x, y), (x + width, y + height), (0, 255, 0), 2)
            cv.putText(imgContour, objectType, (x + int(width / 2) - 20, y + int(height / 2) ), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 0), 1)


imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv.Canny(img, 50, 50)

getContours(imgCanny)

cv.imshow("Shapes", img)
# cv.imshow("GrayShapes",imgGray)
# cv.imshow("GrayBlurShapes",imgBlur)
# cv.imshow("GrayBlurCannyShapes",imgCanny)
cv.imshow("ImgaeContours", imgContour)
cv.waitKey(0)
