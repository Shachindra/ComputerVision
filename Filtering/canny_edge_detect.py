import cv2

# Load the image and convert it to grayscale
image = cv2.imread("mr-robot-logo.png", 1)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur it slightly to remove high frequency edges that aren't required
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

# Perform Canny Edge Detection
canny = cv2.Canny(image, 30, 150)

cv2.imshow("Canny", canny)
cv2.waitKey(0)