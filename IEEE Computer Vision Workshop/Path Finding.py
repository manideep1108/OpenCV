import cv2 as cv
import numpy as np
import threading
import colorsys


# Point class with + and = operators overloaded
class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p = 0
start = Point()
end = Point()

# Array containing the points for 4 directions to perform BSF
dir4 = [Point(0, -1), Point(0, 1), Point(1, 0), Point(-1, 0)]


def BFS(s, e):
    global img, h, w
    const = 2000

    found = False
    q = []
    v = [[0 for j in range(w)] for i in range(h)]
    parent = [[Point() for j in range(w)] for i in range(h)]

    q.append(s)
    v[s.y][s.x] = 1
    while len(q) > 0:
        p = q.pop(0)
        for d in dir4:
            cell = p +  d
            if(cell.x >=0 and cell.x<w and cell.y>=0 and cell.y<h and v[cell.y][cell.x]==0 and ((img[cell.y][cell.x][0]!=0) or (img[cell.y][cell.x][1]!=0) or (img[cell.y][cell.x][2]!=0)) ):
                q.append(cell)
                v[cell.y][cell.x] = v[p.y][p.x] + 1
                img[cell.y][cell.x] = [1,2,3]
                parent[cell.y][cell.x] = p
                if cell == e:
                    found = True
                    del q[:]
                    break



def mouse_event(event, pX, pY, flags, parameter):
    global img, start, end, p

    if event == cv.EVENT_LBUTTONUP:
        if p == 0:
            cv.rectangle(img, (pX - 2, pY - 2), (pX + 2, pY + 2), (0, 0, 255), -1)
            start = Point(pX, pY)
            print("Start = ", start.x, start.y)
            p += 1
        elif p == 1:
            cv.rectangle(img, (pX - 2, pY - 2), (pX + 2, pY + 2), (255, 0, 0), -1)
            end = Point(pX, pY)
            print("end = ", end.x, end.y)
            p += 1

def disp():
    global img
    cv.imshow("Image",img)
    cv.setMouseCallback("Image", mouse_event)
    while(1):
        cv.imshow("Image",img)
        cv.waitKey(1)


img = cv.imread("Resources/Photos/Simple Maze.png", cv.IMREAD_GRAYSCALE)

# Convert into Binary
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (img[i][j] > 120):
            img[i][j] = 255
        else:
            img[i][j] = 0

h, w = img.shape

img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
print("Select start and end points: ")

t = threading.Thread(target=disp, args=())
t.daemon = True
t.start()


while p < 2:
    pass

BFS(start, end)

cv.waitKey(0)


