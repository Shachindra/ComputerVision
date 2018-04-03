import cv2
import numpy as np

# Load the image and convert it to grayscale
frame = cv2.imread("cup-saucers.jpg", 1)
image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Blur it to remove high frequency edges that aren't required
image = cv2.GaussianBlur(image, (5, 5), 0)

# Perform Canny Edge Detection of image
edged = cv2.Canny(image, 30, 150)

# find the contours of the outlines
image_ret, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

# Draw the outline
cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

cv2.imshow("Edge Detection", edged)
cv2.imshow("Image", frame)
cv2.waitKey(0)