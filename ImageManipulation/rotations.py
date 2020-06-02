import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
height, width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)

rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('images/input.jpg')

rotated_image = cv2.transpose(img)

cv2.imshow('Rotated Image - Method 2', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

flipped = cv2.flip(image, 1)
cv2.imshow('Horizontal Flip', flipped) 
cv2.waitKey()
cv2.destroyAllWindows()