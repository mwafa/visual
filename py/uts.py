import cv2
import numpy as np

frame = cv2.imread('../image/lala.JPG')


gambar = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
# gambar = frame

salala = np.zeros((len(gambar),len(gambar[1]),3), np.uint8)

a = 20
b = 6
warna = (255,255,222)
# salala += 255
for i in range(0,len(salala),a)[:-1]:
    x1 = i
    x2 = i+a
    for j in range(0,len(salala[1]),a)[:-1]:
        y1 = j
        y2 = j+a
        hasil =  int(np.average(gambar[x1:x2,y1:y2])*b/255.)-1
        if(hasil > 0):
            warna =  (int(np.average(frame[x1:x2,y1:y2,0])),int(np.average(frame[x1:x2,y1:y2,1])),int(np.average(frame[x1:x2,y1:y2,2])))
            cv2.circle(salala,((y1+y2)/2,(x1+x2)/2),hasil,warna,-1)
# salala += 255
for i in range(0,len(salala)-1*a,a):
    x1 = i+a/2
    x2 = i+a+a/2
    for j in range(0,len(salala[1])-1*a,a):
        y1 = j+a/2
        y2 = j+a+a/2
        hasil =  int(np.average(gambar[x1:x2,y1:y2])*b/255.)-1
        if(hasil > 0):
            warna =  (int(np.average(frame[x1:x2,y1:y2,0])),int(np.average(frame[x1:x2,y1:y2,1])),int(np.average(frame[x1:x2,y1:y2,2])))
            cv2.circle(salala,((y1+y2)/2,(x1+x2)/2),hasil,warna,-1)



# cv2.imshow("gray1",gambar)
cv2.imshow("gray",salala)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('../image/wajah_bulet2.jpg',salala)