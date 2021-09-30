import cv2 as cv

print("Package Imported")

img1 = cv.imread("Resources/Photos/cat.jpg")  # Importing Image
cap1 = cv.VideoCapture("Resources/Videos/vid1.mp4")  # Importing Video

cv.imshow("cat",img1)  # Displaying Image
cv.waitKey(1000)  # 0 means infinite delay but if we add a value instead it adds the value no. of milliseconds delay

# As video is a sequence of images we need a loop to display it
while True:
    success, img = cap1.read()
    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xFF == ord('q'):       #This statement will break the loop if 'q' key is pressed
        break

# Using a webcam

cap2= cv.VideoCapture(0)    # Argument 0 uses the default webcam of the computer
cap2.set(3,640)             # Setting the width
cap2.set(4,480)             # Setting the height
cap2.set(10,100)            # Setting the brightness

while True:
    success, img = cap2.read()
    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break