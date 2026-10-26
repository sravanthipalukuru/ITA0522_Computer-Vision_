import cv2

img = cv2.imread("image.jpg", 0)

x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", cv2.convertScaleAbs(x))
cv2.imshow("Sobel Y", cv2.convertScaleAbs(y))

cv2.waitKey(0)
cv2.destroyAllWindows()
