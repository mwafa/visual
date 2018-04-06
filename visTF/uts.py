import numpy as np
import cv2

class dot:
    
    def __init__(ini,lokasi='../image/wajah.jpg'):
        ini.set_loc(lokasi)
        ini.__r      = 10
        ini.__s      = 20

    def __kotak1(ini,x,y,ke = 0):
        s = ini.__s
        r = ini.__r

        x1,x2 = [s*x,s*x+s] if ke == 0 else [int(s*x+.5*s),int(s*x+1.5*s)]
        y1,y2 = [s*y,s*y+s] if ke == 0 else [int(s*y+.5*s),int(s*y+1.5*s)]

        warna   = tuple([int(np.average(ini.__gambar[x1:x2,y1:y2,i])) for i in range(3)])
        rad     = int(np.average(ini.__gray[x1:x2,y1:y2])*r/255)
        center  = (int((y1+y2)/2),int((x1+x2)/2))

        return center,rad,warna

    def __buatLingkaran(ini,ke= 0):
        s   = ini.__s
        for row in range((ini.__len[0]/s)-ke):
            for col in range((ini.__len[1]/s)-ke):
                center,rad,warna = ini.__kotak1(row,col,ke)
                cv2.circle(ini.__hasil,center,rad,warna,-1) if rad > 0 else False
        

    def make(ini):
        ini.__buatLingkaran(0)
        ini.__buatLingkaran(1)
        cv2.imshow('hasil',ini.__hasil)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def setting(ini,s=20,r=10,win = 0):
        ini.__r = r
        ini.__s = s
        ini.__hasil  = np.zeros((ini.__len[0],ini.__len[1],3), np.uint8)        
        ini.make() if win else False
    
    def set_loc(ini,lokasi):
        ini.__lokasi = lokasi
        ini.__gambar = cv2.imread(lokasi)
        ini.__gray   = cv2.imread(lokasi,0)
        ini.__len    = (len(ini.__gray),len(ini.__gray[1]))
        ini.__hasil  = np.zeros((ini.__len[0],ini.__len[1],3), np.uint8)

    def simpan(loc = ''):
        lokasi = ini.__lokasi if loc == '' else loc
        cv2.imwrite(lokasi)

