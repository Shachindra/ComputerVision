import cv2
import numpy as np

# Import the Image and Convert it to GrayScale
frame = cv2.imread("mr-robot-logo.png", 1)
image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Averaging
avg_blur = cv2.blur(image, (5, 5))

# Gaussian Blurring
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Median Blurring
median_blur = cv2.medianBlur(image, 5)

#Bilateral Filtering
bilateral_filter = cv2.bilateralFilter(image, 9, 41, 41)

# Display the results
cv2.imshow("Averaged", avg_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Filter", bilateral_filter)
cv2.waitKey(0)