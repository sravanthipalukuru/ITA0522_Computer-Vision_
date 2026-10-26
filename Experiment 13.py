import cv2
import numpy as np

img = cv2.imread("image.jpg")
rows, cols = img.shape[:2]

p1 = np.float32([[50, 50], [200, 50], [50, 200]])
p2 = np.float32([[10, 100], [200, 50], [100, 250]])

matrix = cv2.getAffineTransform(p1, p2)
result = cv2.warpAffine(img, matrix, (cols, rows))

cv2.imshow("Affine Transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
