import cv2
import numpy as np


img = cv2.imread("Capture.jpg")
# img = (np.power(img/255, 1.1) * 255).astype(np.uint8)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img = cv2.GaussianBlur(img, (3, 3), 3)
gray = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
dst = cv2.dilate(cv2.cornerHarris(gray, 2, 3, 0.04), None)
red, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)
dst = np.uint8(dst)
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
res = np.hstack((centroids, corners))
res = np.int0(res)
img[res[:, 1], res[:, 0]] = [0, 0, 255]
img[res[:, 3], res[:, 2]] = [0, 255, 0]

BLUE_MASK = cv2.inRange(hsv, np.array([108, 239, 141]), np.array([119, 255, 255]))
GREEN_MASK = cv2.inRange(hsv, np.array([70, 227, 60]), np.array([83, 255, 139]))
ORANGE_MASK = cv2.inRange(hsv, np.array([4, 140, 178]), np.array([14, 221, 255]))
YELLOW_MASK = cv2.inRange(hsv, np.array([27, 87, 84]), np.array([41, 177, 255]))
WHITE_MASK = cv2.inRange(hsv, np.array([0, 0, 247]), np.array([168, 45, 255]))
RED_MASK = cv2.inRange(hsv, np.array([170, 190, 200]), np.array([180, 250, 255]))

TOP_LEFT_MASK = np.zeros(img.shape[:2], dtype="uint8")
TOP_RIGHT_MASK = np.zeros(img.shape[:2], dtype="uint8")
TOP_MID_MASK = np.zeros(img.shape[:2], dtype="uint8")
MID_LEFT_MASK = np.zeros(img.shape[:2], dtype="uint8")
MID_RIGHT_MASK = np.zeros(img.shape[:2], dtype="uint8")
MID_MID_MASK = np.zeros(img.shape[:2], dtype="uint8")
BOTTOM_LEFT_MASK = np.zeros(img.shape[:2], dtype="uint8")
BOTTOM_RIGHT_MASK = np.zeros(img.shape[:2], dtype="uint8")
BOTTOM_MID_MASK = np.zeros(img.shape[:2], dtype="uint8")

cv2.rectangle(TOP_LEFT_MASK, (0, 0), (67, 67), 255, -1)
cv2.rectangle(TOP_MID_MASK, (67, 0), (134, 67), 255, -1)
cv2.rectangle(TOP_RIGHT_MASK, (134, 0), (200, 67), 255, -1)
cv2.rectangle(MID_LEFT_MASK, (0, 67), (67, 134), 255, -1)
cv2.rectangle(MID_MID_MASK, (67, 67), (134, 134), 255, -1)
cv2.rectangle(MID_RIGHT_MASK, (134, 67), (200, 134), 255, -1)
cv2.rectangle(BOTTOM_LEFT_MASK, (0, 134), (67, 200), 255, -1)
cv2.rectangle(BOTTOM_MID_MASK, (67, 134), (134, 200), 255, -1)
cv2.rectangle(BOTTOM_RIGHT_MASK, (134, 134), (200, 200), 255, -1)

color_masks = [BLUE_MASK, GREEN_MASK, WHITE_MASK, YELLOW_MASK, ORANGE_MASK, RED_MASK]
pos_masks = [TOP_LEFT_MASK, TOP_MID_MASK, TOP_RIGHT_MASK, MID_LEFT_MASK, MID_MID_MASK, MID_RIGHT_MASK, BOTTOM_LEFT_MASK, BOTTOM_MID_MASK, BOTTOM_RIGHT_MASK]

FINAL_ARRAY = [[9, 9, 9],
               [9, 9, 9],
               [9, 9, 9]]

for i in range(len(pos_masks)):
    for j in range(len(color_masks)):
        color_mask = cv2.bitwise_and(img, img, mask=color_masks[j])
        color_pos_mask = cv2.bitwise_and(color_mask, color_mask, mask=pos_masks[i])
        gray = cv2.cvtColor(color_pos_mask, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Test'+str(i), gray)
        if cv2.countNonZero(gray) > 100:
            FINAL_ARRAY[i//3][i % 3] = j
            break

cv2.imshow("Image", img)

if cv2.waitKey(0) & 0xFF == ord('q'):
    print(FINAL_ARRAY)
    cv2.destroyAllWindows()
