import cv2
import numpy as np

img = cv2.imread('galactic.jpg', cv2.IMREAD_UNCHANGED)
# (rows, cols, channels) = img.shape
(rows, cols) = img.shape[:2]

M = np.float32([[1, 0, 100], [0, 1, 50]])

result = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Result',result)

cv2.waitKey(0)
cv2.destroyAllWindows()
