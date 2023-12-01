import cv2
import numpy as np

img = cv2.imread("Capture.jpg")
'''
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    MinHue = cv2.getTrackbarPos("MinHue", "Trackbars")
    MaxHue = cv2.getTrackbarPos("MaxHue", "Trackbars")
    MinSat = cv2.getTrackbarPos("MinSat", "Trackbars")
    MaxSat = cv2.getTrackbarPos("MaxSat", "Trackbars")
    MinVal = cv2.getTrackbarPos("MinVal", "Trackbars")
    MaxVal = cv2.getTrackbarPos("MaxVal", "Trackbars")

    BLUE_MASK = cv2.inRange(hsv, np.array([108, 0, 115]), np.array([121, 255, 184]))
    GREEN_MASK = cv2.inRange(hsv, np.array([73, 99, 81]), np.array([92, 255, 255]))
    ORANGE_MASK = cv2.inRange(hsv, np.array([MinHue, MinSat, MinVal]), np.array([MaxHue, MaxSat, MaxVal]))
    YELLOW_MASK = cv2.inRange(hsv, np.array([22, 59, 35]), np.array([28, 252, 255]))
    
    cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("MinHue", "Trackbars", 0, 179, empty)
cv2.createTrackbar("MaxHue", "Trackbars", 70, 179, empty)
cv2.createTrackbar("MinSat", "Trackbars", 110, 255, empty)
cv2.createTrackbar("MaxSat", "Trackbars", 184, 255, empty)
cv2.createTrackbar("MinVal", "Trackbars", 135, 255, empty)
cv2.createTrackbar("MaxVal", "Trackbars", 255, 255, empty)


def empty(a):
    pass

'''
