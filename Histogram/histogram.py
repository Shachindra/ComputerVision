# import the required packages
from matplotlib import pyplot as plt
import cv2

# loading the image & converting it to grayscale
image = cv2.imread("applemusic.png", 1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", image)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# construct a grayscale histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Numbers of Pixels")
plt.plot(hist)

# Set the x limits of the current axis.
# plt.xlim([0, 256])

plt.axis([0, 256, 0, 15000])

# Display the histogram
plt.show()

cv2.waitKey(0)
