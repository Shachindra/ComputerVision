import numpy as np
import cv2

img = cv2.imread('galactic.jpg', cv2.IMREAD_UNCHANGED)
print(img.shape)

result = cv2.resize(img, None, fx=2, fy=1, interpolation = cv2.INTER_LINEAR)
print(result.shape)

# Lets view the result
cv2.imshow("Scale", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
