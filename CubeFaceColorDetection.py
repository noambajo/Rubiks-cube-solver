import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(4, 600)
cap.set(3, 600)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    showingImage = img

    cv2.line(showingImage, (200, 150), (200, 350), (0, 255, 0), 3)
    cv2.line(showingImage, (200, 150), (400, 150), (0, 255, 0), 3)
    cv2.line(showingImage, (200, 350), (400, 350), (0, 255, 0), 3)
    cv2.line(showingImage, (400, 350), (400, 150), (0, 255, 0), 3)

    mask = np.zeros(img.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (200, 150), (400, 350), 255, -1)
    mask = cv2.bitwise_and(img, img, mask=mask)

    DisplayStack = np.hstack((showingImage, mask))
    cv2.imshow("Camera", DisplayStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
