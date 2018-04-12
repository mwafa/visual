# from visTF.uts import bulat
import cv2
# import matplotlib.pyplot as plt
# import numpy as np

a = cv2.imread('example/image/kei.jpg')
cv2.circle(a,(20,20),5,(255,255,255),2)
print(a.shape)
# cv2.imshow('nama',a)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
