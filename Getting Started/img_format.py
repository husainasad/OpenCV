import numpy
import cv2

img = cv2.imread("img.png")
img2 = cv2.imwrite("img2.jpg", img)
cv2.imshow("original",img)
cv2.imshow("changed",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
