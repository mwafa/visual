import numpy as np
import cv2

class bulat:
    """
    Bulat merupakan funsi yang digunakan untuk membuat efek bulat-bulat.
    """
    def __init__(self,lokasi='../image/wajah.jpg'):
        self.set_loc(lokasi)
        self.__r      = 10
        self.__s      = 20

    def __kotak1(self,x,y,ke = 0):
        s = self.__s
        r = self.__r

        x1,x2 = [s*x,s*x+s] if ke == 0 else [int(s*x+.5*s),int(s*x+1.5*s)]
        y1,y2 = [s*y,s*y+s] if ke == 0 else [int(s*y+.5*s),int(s*y+1.5*s)]

        warna   = tuple([int(np.average(self.__gambar[x1:x2,y1:y2,i])) for i in range(3)])
        rad     = int(np.average(self.__gray[x1:x2,y1:y2])*r/255)
        center  = (int((y1+y2)/2),int((x1+x2)/2))

        return center,rad,warna

    def __buatLingkaran(self,ke= 0):
        s   = self.__s
        for row in range(int(self.__len[0]/s)-ke):
            for col in range(int(self.__len[1]/s)-ke):
                center,rad,warna = self.__kotak1(row,col,ke)
                cv2.circle(self.__hasil,center,rad,warna,-1) if rad > 0 else False
        

    def __build(self):
        self.__buatLingkaran(0)
        self.__buatLingkaran(1)

    def make(self):
        self.__build()
        cv2.imshow('hasil',self.__hasil)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def setting(self,s=20,r=10,win = 0):
        self.__r = r
        self.__s = s
        self.__hasil  = np.zeros((self.__len[0],self.__len[1],3), np.uint8)        
        self.make() if win else False
    
    def set_loc(self,lokasi):
        self.__lokasi = lokasi
        self.__gambar = cv2.imread(lokasi)
        self.__gray   = cv2.imread(lokasi,0)
        self.__len    = (len(self.__gray),len(self.__gray[1]))
        self.__hasil  = np.zeros((self.__len[0],self.__len[1],3), np.uint8)

    def simpan(self,loc = ''):
        lokasi = self.__lokasi if loc == '' else loc
        self.__build()
        cv2.imwrite(lokasi,self.__hasil)

