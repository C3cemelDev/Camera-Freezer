import cv2
import numpy as np
import pyvirtualcam

# Initialize real webcam capture
real_cam = cv2.VideoCapture(0)  # Change the index if you have multiple cameras
cameraToggle = False

# Initialize virtual webcam
with pyvirtualcam.Camera(width=640, height=480, fps=30) as virtual_cam:
    while True:
        # Capture frame from real webcam
        ret, frame = real_cam.read()
        
        if not ret:
            print("Failed to capture frame from real webcam")
            break

        # Show the captured frame from the real webcam
        cv2.imshow('Real Webcam Input', frame)
        
        # Check for key press (for freezing the frame)
        key = cv2.waitKey(1)
        if key == ord('f'):  # Press 'f' to freeze the frame
            virtual_cam.send(frame)
            cameraToggle = not cameraToggle
            print(cameraToggle)
            # Show the frozen frame on the virtual webcam
        if cameraToggle:
            virtual_cam.send(frame)
        
        # Check for 'q' key press to quit
        if key == ord('q'):
            break

        # Process any other frame here if needed

    # Release resources
    real_cam.release()
    cv2.destroyAllWindows()
