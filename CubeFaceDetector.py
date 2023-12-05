import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(4, 600)
cap.set(3, 600)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    showingImage = img.copy()

    cv2.line(showingImage, (200, 150), (200, 350), (0, 255, 0), 3)
    cv2.line(showingImage, (200, 150), (400, 150), (0, 255, 0), 3)
    cv2.line(showingImage, (200, 350), (400, 350), (0, 255, 0), 3)
    cv2.line(showingImage, (400, 350), (400, 150), (0, 255, 0), 3)

    mask = np.zeros(img.shape[:2], dtype="uint8")
    kernel3 = np.ones((3, 3), np.uint8)
    kernel5 = np.ones((5, 5), np.uint8)
    kernel9 = np.ones((9, 9), np.uint8)
    cv2.rectangle(mask, (200, 150), (400, 350), 255, -1)
    img = cv2.bitwise_and(img, img, mask=mask)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.equalizeHist(img)
    _, img = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel5)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel5)
    img = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel5)

    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
        x2, y2, w, h = cv2.boundingRect(contour)
        x1 = approx.ravel()[0]
        y1 = approx.ravel()[1]
        if len(approx) == 4 and 0.92 <= float(w)/h <= 1.08:
            if 25000 > cv2.contourArea(contour) > 20000:
                cv2.imwrite('Capture.jpg', showingImage[150:350, 200:400])
                break
            cv2.putText(showingImage, "square", (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
            cv2.rectangle(showingImage, (x2, y2), (x2+w, y2+h), (0, 0, 255), 3)

    cv2.imshow("Camera", showingImage)
    cv2.imshow("Computation", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
