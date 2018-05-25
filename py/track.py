import cv2
import numpy as np
import serial
import time

arduino = serial.Serial('com3',9600)

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')
cv2.namedWindow('track')

cv2.resizeWindow('track', 400,250)


vid = cv2.VideoCapture(0)

# create trackbars for color change
cv2.createTrackbar('S','track',155,255,nothing)
cv2.createTrackbar('S_m','track',183,255,nothing)
cv2.createTrackbar('H','track',59,255,nothing)
cv2.createTrackbar('H_m','track',147,255,nothing)
cv2.createTrackbar('V','track',7,255,nothing)
cv2.createTrackbar('V_m','track',220,255,nothing)

step = 0

while(1):

    ret, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    
    step = 0 if step>20 else step+1

    # get current positions of four trackbars
    s = cv2.getTrackbarPos('S','track')
    s_m = cv2.getTrackbarPos('S_m','track')
    h = cv2.getTrackbarPos('H','track')
    h_m = cv2.getTrackbarPos('H_m','track')
    v = cv2.getTrackbarPos('V','track')
    v_m = cv2.getTrackbarPos('V_m','track')
    
    
    # define range of blue color in HSV
    lower_blue = np.array([s,h,v])
    upper_blue = np.array([s_m,h_m,v_m])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)


    ret,thresh = cv2.threshold(mask,127,255,0)
    im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
#    for cnt in contours:
#        x,y,w,h = cv2.boundingRect(cnt)
#        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
    # Bitwise-AND mask and original image
    
    l = [cv2.boundingRect(cnt) for cnt in contours]
    if(len(l)):
        l = max(l,key=lambda item:item[2]+item[3])
    #    print l
        (x,y,w,h) = list(l)
#        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        loc = (x+w//2,y+h//2)
        cv2.circle(frame,loc,1,(255,0,0),5)
        cv2.line(frame,loc,(x+w//2+20,y+h//2-40),(0,0,255))

        tinggi = len(frame)
        lebar = len(frame[1])

        cx = lambda x: x*150//lebar
        cy = lambda x: x*150//tinggi
        
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Ini Bendanya", loc, font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(frame,"(%i,%i)"%(cx(loc[0]),cy(loc[1])),(100,100),font, .8, (0,255,255),1)
        # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        values = bytearray([cx(loc[0]),cy(loc[1])])
        if(step == 0):
            arduino.write(values)

        # arduino.write(conf(loc[1]))
        # arduino.write(conf(loc[0]))
    
#    res = frame
    
    cv2.imshow('image',res)
    cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    
    #keren sekali
    
    img[:] = [s,h,v]

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    

#print mask
cv2.destroyAllWindows()