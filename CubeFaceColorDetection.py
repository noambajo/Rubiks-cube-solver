import cv2
cap = cv2.VideoCapture(0)   # opens the main camera (built-in camera for laptops)
while True:
    success, img = cap.read()   # Captures a frame
    # Displays the frame, until 'q' is pressed
    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# releases the capture from the camera and frees up memory
cap.release()
cv2.destroyAllWindows()
