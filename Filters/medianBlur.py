import cv2
import numpy

image = cv2.imread("img.png")
kernel = 3

median = cv2.medianBlur(image, kernel)

cv2.imshow("blurred", median)
cv2.waitKey(0)
cv2.destroyAllWindows()