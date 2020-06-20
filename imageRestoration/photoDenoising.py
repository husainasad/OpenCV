import numpy as np
import cv2

image = cv2.imread('images/elephant.jpg')

dst = cv2.fastNlMeansDenoisingColored(image, None, 11, 6, 7, 21)

cv2.imshow('Original Image', image)
cv2.imshow('Fast Means Denoising', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()