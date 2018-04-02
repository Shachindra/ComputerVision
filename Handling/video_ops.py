# Video Operations
# python video_ops.py

# Import the required Libraries
import cv2

camera_port = 0
cap = cv2.VideoCapture(camera_port)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'FMP4')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

#  Default size: 640x480
#ret = cap.set(3,320)
#ret = cap.set(4,240)

while cap.isOpened():
    # Capture each frame
    ret, frame = cap.read()

    if ret==True:
        
        # Operations
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # write the frame
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
