import cv2
import numpy as np
import imutils

img = imutils.url_to_image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/OpenCV_Logo_with_text_svg_version.svg/1200px-OpenCV_Logo_with_text_svg_version.svg.png")

resized_image = imutils.resize(img, width=512, height=512)

shifted_image = imutils.translate(resized_image, 100, 50)

rotated_image = imutils.rotate(resized_image, angle = 90)

cv2.imshow("Image", rotated_image)
cv2.waitKey(0)