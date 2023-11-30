import cv2
import numpy as np


def empty(a):
    pass


cap = cv2.VideoCapture(0)
cap.set(4, 600)
cap.set(3, 600)
cap.set(10, 100)
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("MinHue", "Trackbars", 0, 179, empty)
cv2.createTrackbar("MaxHue", "Trackbars", 70, 179, empty)
cv2.createTrackbar("MinSat", "Trackbars", 110, 255, empty)
cv2.createTrackbar("MaxSat", "Trackbars", 184, 255, empty)
cv2.createTrackbar("MinVal", "Trackbars", 135, 255, empty)
cv2.createTrackbar("MaxVal", "Trackbars", 255, 255, empty)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    showingImage = img.copy()

    cv2.line(showingImage, (200, 150), (200, 350), (0, 255, 0), 3)
    cv2.line(showingImage, (200, 150), (400, 150), (0, 255, 0), 3)
    cv2.line(showingImage, (200, 350), (400, 350), (0, 255, 0), 3)
    cv2.line(showingImage, (400, 350), (400, 150), (0, 255, 0), 3)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    MinHue = cv2.getTrackbarPos("MinHue", "Trackbars")
    MaxHue = cv2.getTrackbarPos("MaxHue", "Trackbars")
    MinSat = cv2.getTrackbarPos("MinSat", "Trackbars")
    MaxSat = cv2.getTrackbarPos("MaxSat", "Trackbars")
    MinVal = cv2.getTrackbarPos("MinVal", "Trackbars")
    MaxVal = cv2.getTrackbarPos("MaxVal", "Trackbars")

    '''
    BLUE_MASK = cv2.inRange(hsv, np.array([108, 0, 115]), np.array([121, 255, 184]))
    GREEN_MASK = cv2.inRange(hsv, np.array([73, 99, 81]), np.array([92, 255, 255]))
    ORANGE_MASK = cv2.inRange(hsv, np.array([MinHue, MinSat, MinVal]), np.array([MaxHue, MaxSat, MaxVal]))

    '''
    YELLOW_MASK = cv2.inRange(hsv, np.array([22, 59, 35]), np.array([28, 252, 255]))
    mask = np.zeros(img.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (200, 150), (400, 350), 255, -1)
    img = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(YELLOW_MASK))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (3, 3), 1)
    img = cv2.bitwise_and(img, img, mask=mask)
    _, thresh = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
        cv2.drawContours(showingImage, [approx], 0, (0, 0, 255), 3)
        x2, y2, w, h = cv2.boundingRect(contour)
        if len(approx) == 4 and 0.95 <= float(w)/h <= 1.05:
            x1 = approx.ravel()[0]
            y1 = approx.ravel()[1]
            cv2.putText(showingImage, "square", (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    cv2.imshow("Camera", showingImage)
    cv2.imshow("Computation", img)
    cv2.imshow("Threshold", thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
