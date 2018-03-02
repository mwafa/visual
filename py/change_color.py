import cv2
import numpy as np


v = cv2.VideoCapture(0)
while True:
    ret, frame = v.read();
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

#    gray = np.concatenate(frame,gray,axis=1)
#    a = cv2.bitwise_xor(gray,frame)
    cv2.imshow("gray",gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break;
#print img
v.release()
cv2.destroyWindow("gray")
cv2.destroyWindow("gray2")