import cv2 as cv

# In openCV Y-axis is inverted compared to usual convention

img = cv.imread("Resources/Photos/cats.jpg")
print(img.shape)  # Prints (a,b,c) a - Height | b - Width | c - no. of channels
cv.imshow("cats", img)
cv.waitKey(1000)

# Resizing an image

imgResize = cv.resize(img, (30, 200))  # dsize is an ordered pair (width, height)
print(imgResize.shape)
cv.imshow("Resized Cats", imgResize)
cv.waitKey(1000)

# Cropping an image

# As it's just a matrix, we can just read some part of it
# img[a,b] a - Range of height & b - Range of Width

imgCropped = img[0:200, 200:500]
cv.imshow("Cropped Cats", imgCropped)
cv.waitKey(0)

#
