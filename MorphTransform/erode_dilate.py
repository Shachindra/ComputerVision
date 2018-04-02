import cv2
import numpy as np

image = cv2.imread("mr-robot.jpg", 1)

# Convert to GrayScale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kernel - matrix size of 5
kernel = np.ones((5,5), np.uint8)

# Erosion - 1 iteration
erosion = cv2.erode(gray, kernel, iterations = 1)

# Dilation - 1 iteration
dilation = cv2.dilate(gray, kernel, iterations = 1)

# Opening - Erosion followed by Dilation
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

# Closing - Dilation followed by Erosion
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Display the results

cv2.imshow("original", gray)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
