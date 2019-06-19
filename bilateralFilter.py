import cv2
import numpy

image = cv2.imread("img.png")

pixelDim = 7
color = 100
space =100

filter = cv2.bilateralFilter(image, pixelDim, color, space)
                             
cv2.imshow("filtered", filter)
cv2.waitKey(0)
cv2.destroyAllWindows()