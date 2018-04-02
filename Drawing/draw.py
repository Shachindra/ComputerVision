import numpy as np
import cv2

# Create a black image
canvas = np.zeros((512, 512, 3), np.uint8)
#canvas[:] = (255, 255, 255)

# Draw a diagonal green line with thickness of 5 px
cv2.line(canvas, (0, 0), (511, 511), (0, 255, 0), 5)
cv2.line(canvas, (0, 511), (511, 0), (0, 255, 0), 5)

# Draw a red rectangle at the top-right corner of image
cv2.rectangle(canvas, (384, 0), (510, 128), (0, 0, 255), 3)

# Draws an ellipse at the center of the image
cv2.ellipse(canvas, (256, 256), (100, 50), 0, 0, 360, (255, 0, 0), -1)

# Use font ITALIC, HERSHEY_COMPLEX or HERSHEY_SIMPLEX ...
cv2.putText(canvas, 'Gear 1', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 2, cv2.LINE_AA)

#Lets see our drawing
cv2.imshow("Drawing", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
