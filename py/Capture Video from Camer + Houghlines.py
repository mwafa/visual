# Capture Video from Camera + hough_lines

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,50,120)
    minLineLength = 50
    maxLineGap = 40
    lines = cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength,maxLineGap)

    #for x1,y1,x2,y2 in lines[0]:
        #cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

    cv2.imshow("edges",edges)
    #cv2.imshow("lines",lines)
    
    cv2.imshow('frame',gray)
    cv2.imwrite('opencv.jpg',gray)
    cv2.imwrite('canny_camera.jpg',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # tekan q untuk tutup dan meng-capture
        break


cap.release()
cv2.destroyAllWindows()
