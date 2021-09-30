import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/unnamed.png', cv.IMREAD_COLOR)
#cv.namedWindow("Fruits",cv.WINDOW_AUTOSIZE)
print(img.shape)
cv.imshow("Fruits", img)
#cv.imwrite('Resources/Photos/unnamed_copy.jpg', img) # Saving a image we already have in numpy array format into any file type

# Creating our own image by creating an array

myimg = np.full((400,400,3),255,dtype = np.uint8)   # White image
#cv.imshow("My image",myimg)
transparent = np.full((400,400,4),0,dtype=np.uint8)
#cv.imwrite("Resources/Photos/Transparent.png",transparent)


cv.waitKey(0)




