import cv2

img = cv2.imread("img.png")
print('Original Dimensions : ',img.shape)
cv2.imshow("original", img)

#Resizing
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)


#greyscaled
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyscaleR", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()