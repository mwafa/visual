import cv2
import numpy as np


#b = input("lorem")

face_cascade = cv2.CascadeClassifier(r"haarcascades\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"haarcascades\haarcascade_eye.xml")

v = cv2.VideoCapture(0)

n = []
while True:
    ret, frame = v.read();
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        cv2.circle(img,(x+w/2,y+h/2),1,(255,0,0),5)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        n.append(w)
        if(len(n)>30):
            n = n[-30:]
        cv2.putText(img, str(np.average(n)), (40, 100), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(img, str(w), (40, 80), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

#        crop_img = img[y:y+h, x:x+w]
#        crop_img = cv2.resize(crop_img,(100,100))
        #crop_img = cv2.blur(crop_img,(30,30))
#        img[0:100, 0:100] = crop_img
#        cv2.resize(crop_img,(x+w,y+h),(200,200))

        

    #jok = cv2.subtract(crop_img,img)
    vis = np.concatenate((frame, img), axis=1)
    cv2.imshow("gray",img);
    k = frame;
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break;
#print img
v.release()
cv2.destroyWindow("gray")
cv2.destroyWindow("gray2")

