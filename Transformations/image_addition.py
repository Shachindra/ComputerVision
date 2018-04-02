import numpy as np
import cv2

# Read the images
img1 = cv2.imread('tron_legacy.jpg', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('galactic.jpg', cv2.IMREAD_UNCHANGED)

# Additon of images 
# result = cv2.add(img1, img2)

# Addition with different weights given to images to have a blending or transparency effect
result = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
