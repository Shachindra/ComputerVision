import cv2
import numpy as np

# Load the image and Convert to GrayScale
frame = cv2.imread("mr-robot-logo.png", 1)
image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Calculation of SobelX
sobelX = cv2.Sobel(image, ddepth = cv2.CV_64F, dx = 1, dy = 0, ksize = 3)
sobelX = np.uint8(np.absolute(sobelX))

# Calculation of SobelY
sobelY = cv2.Sobel(image, ddepth = cv2.CV_64F, dx = 0, dy = 1, ksize = 3)
sobelY = np.uint8(np.absolute(sobelY))

sobelXY = cv2.bitwise_or(sobelX, sobelY)

# Calculation of Laplacian
laplacian = cv2.Laplacian(image, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

cv2.imshow('sobelXY',sobelXY)
cv2.imshow('laplacian',laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
