#/usr/bin/python3

# Video Operations
# python play_video_cam.py

# Import the required Libraries
import cv2

# Select the source as video or Webcam Play
cap = cv2.VideoCapture('fileName.avi')
#camera_port = 0
#cap = cv2.VideoCapture(camera_port)

while cap.isOpened():
    ret, frame = cap.read()

    # Convert the frame to greyscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    #Wait for Key 'Q' to be pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
