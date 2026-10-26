import cv2

img = cv2.imread("image.jpg")

roi = img[50:200, 50:200]
copy = roi.copy()

img[200:350, 200:350] = copy

cv2.imshow("ROI Copy and Paste", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
