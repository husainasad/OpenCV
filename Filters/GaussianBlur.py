import cv2
import numpy

image = cv2.imread("img.png")
matrix = (7,7)

blur = cv2.GaussianBlur(image, matrix, 0)

cv2.imshow("blurred", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()