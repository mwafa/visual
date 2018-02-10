from PIL import ImageGrab
import numpy as np
import cv2




while(True):
    img = ImageGrab.grab(bbox=(107,188,465,294))
    
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
#    frame = cv2.resize(frame,(1366/2,780),(100,100))
    
    lower_blue = np.array([0,0,64])
    upper_blue = np.array([15,17,85])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(frame, lower_blue, upper_blue)
    
    
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    
    cv2.imshow("test", mask)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
