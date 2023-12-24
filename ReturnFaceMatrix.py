import cv2
import numpy as np

img = cv2.imread("Capture.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

BLUE_MASK = cv2.inRange(hsv, np.array([110, 224, 0]), np.array([134, 255, 255]))
GREEN_MASK = cv2.inRange(hsv, np.array([62, 135, 31]), np.array([103, 255, 69]))
WHITE_MASK = cv2.inRange(hsv, np.array([102, 22, 143]), np.array([118, 100, 218]))
YELLOW_MASK = cv2.inRange(hsv, np.array([22, 132, 164]), np.array([30, 246, 207]))
ORANGE_MASK = cv2.inRange(hsv, np.array([6, 200, 186]), np.array([11, 255, 253]))
RED_MASK = cv2.inRange(hsv, np.array([0, 176, 143]), np.array([5, 255, 226]))

cv2.imshow("Image", img)
cv2.imshow("Mask", cv2.bitwise_and(img, img, mask=RED_MASK))

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
