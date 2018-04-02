import numpy as np
import cv2

img = cv2.imread('galactic.jpg', cv2.IMREAD_UNCHANGED)
(rows, cols, channels) = img.shape
print(img.shape)

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
result = cv2.warpAffine(img, M, (cols, rows))
print(result.shape)

# Lets view the result
cv2.imshow("Rotation", result)
cv2.imwrite("rotated.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
