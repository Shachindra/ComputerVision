# Steps to get HSV Boundary Values
#green = np.uint8([[[0, 255, 0]]])
#hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
#print (hsv_green)

import cv2
import numpy as np
print("OpenCV Version: " + cv2.__version__)

frame = cv2.imread('social.png', cv2.IMREAD_UNCHANGED)

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of colors in HSV
lower_red = np.array([-1, 128, 128])
upper_red = np.array([11, 255, 255])
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([40, 255, 255])
lower_green = np.array([50, 50, 50])
upper_green = np.array([70, 255, 255])

# Threshold the HSV image to get only the specified colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame, frame, mask=mask)

cv2.imshow('frame', frame)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
