import cv2
import numpy as np;

image = cv2.imread("images/Sunflowers.jpg", 0)

detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(image)

blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
cv2.imshow("Blobs", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()