# Read an Image and Display it in different formats
# python read_display_save.py

# Import the required Libraries
import cv2

# Load the image and show some basic information on it
image = cv2.imread("seagull.jpg", cv2.IMREAD_UNCHANGED)

# Show the image and wait for a keypress
cv2.namedWindow("Image Display", cv2.WINDOW_NORMAL)
cv2.imshow("Image Display", image)

# Wait for keypress
key = cv2.waitKey(0)
if key == 27:
    # wait for ESC key to exit
    cv2.destroyAllWindows()
elif key == ord('s'):
    # wait for 's' key to save and exit
    cv2.imwrite('newimage.png', image)
    cv2.destroyAllWindows()
