from PIL import ImageGrab
import numpy as np
import cv2


def nothing(x):
    pass

cv2.namedWindow('track')
# create trackbars for color change
cv2.createTrackbar('S','track',155,255,nothing)
cv2.createTrackbar('S_m','track',183,255,nothing)
cv2.createTrackbar('H','track',59,255,nothing)
cv2.createTrackbar('H_m','track',147,255,nothing)
cv2.createTrackbar('V','track',7,255,nothing)
cv2.createTrackbar('V_m','track',220,255,nothing)


cv2.resizeWindow('track', 400,250)


while(True):
    img = ImageGrab.grab(bbox=(0,0,1366/2,780)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
    frame = cv2.resize(frame,(1366/2,780),(100,100))
    
    
    
    # get current positions of four trackbars
    s = cv2.getTrackbarPos('S','track')
    s_m = cv2.getTrackbarPos('S_m','track')
    h = cv2.getTrackbarPos('H','track')
    h_m = cv2.getTrackbarPos('H_m','track')
    v = cv2.getTrackbarPos('V','track')
    v_m = cv2.getTrackbarPos('V_m','track')
    
    lower_blue = np.array([s,h,v])
    upper_blue = np.array([s_m,h_m,v_m])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(frame, lower_blue, upper_blue)
    
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    
    cv2.imshow("test", mask)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
