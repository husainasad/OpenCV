import cv2
import numpy as np

image = cv2.imread('images/input.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

keypoints = fast.detect(gray, None)

keypoints, descriptors = brief.compute(gray, keypoints)
print ("Number of keypoints Detected: ", len(keypoints))

image = cv2.drawKeypoints(image, keypoints, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                                    
cv2.imshow('Feature Method - BRIEF', image)
cv2.waitKey()
cv2.destroyAllWindows()