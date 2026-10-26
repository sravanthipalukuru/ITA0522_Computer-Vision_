import cv2
import numpy as np

img = cv2.imread("image.jpg")

p1 = np.float32([[50, 50], [300, 50], [50, 300], [300, 300]])
p2 = np.float32([[0, 0], [250, 0], [0, 250], [250, 250]])

matrix = cv2.getPerspectiveTransform(p1, p2)
result = cv2.warpPerspective(img, matrix, (300, 300))

cv2.imshow("Perspective Transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
