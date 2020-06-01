import cv2
import numpy

image = cv2.imread("img.png")
thresholdval1 = 50
thresholdval2 = 100
canny = cv2.Canny(image, thresholdval1, thresholdval2) 
                            
cv2.imshow("canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()