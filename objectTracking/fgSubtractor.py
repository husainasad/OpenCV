import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

average = np.float32(frame)

while True:
    ret, frame = cap.read()
    
    frame = cv2.flip(frame, 1)

    cv2.accumulateWeighted(frame, average, 0.01)

    background = cv2.convertScaleAbs(average)

    cv2.imshow('Input', frame)
    cv2.imshow('Disapearing Background', background)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()