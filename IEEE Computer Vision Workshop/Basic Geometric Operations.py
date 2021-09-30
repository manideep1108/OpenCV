import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/Doraemon.png", cv.IMREAD_GRAYSCALE)
print(img.shape)
img = cv.resize(img,(254, 365))
cv.imshow("Original", img)


def horizontalflip(image):
    flipped_image = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            flipped_image[image.shape[0] - i - 1][j] = image[i][j]
    return flipped_image


def verticalflip(image):
    flipped_image = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            flipped_image[i][image.shape[1] - j - 1] = image[i][j]
    return flipped_image


Horizontal_flip = horizontalflip(img)
Vertical_flip = verticalflip(img)
Double_flip = horizontalflip(verticalflip(img))

# cv.imshow("Horizontal Flip", Horizontal_flip)
# cv.imshow("Vertical Flip", Vertical_flip)
# cv.imshow("Horizontal & Vertical Flip", Double_flip)


# Image Padding ( Adding borders )

def pad(img,padding):
    (padx,pady) = padding
    h,w = img.shape

    padded_img = np.full((h+2*pady,w+2*padx),255,dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            padded_img[i+pady][j+padx] = img[i][j]
    return padded_img

padded = pad(img,(15,15))
cv.imshow("Padded image",padded)


# Predefined function in openCV for padding
# cv.copyMakeBorder(src,top,bottom,left,right,borderType,value)  = returns padded image

padded = cv.copyMakeBorder(img,15,15,15,15,borderType=cv.BORDER_CONSTANT,value=255)
cv.imshow("Padded image",padded)
cv.waitKey(0)