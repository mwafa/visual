import numpy as np
import cv2
import matplotlib.pyplot as plt
k = lambda x : np.array([[[x[2],x[1],x[0]] for i in k] for k in x])


img = cv2.imread("../image/mesi.jpg")
img = cv2.cvtColor(img,cv2.COLOR_RGB2YUV)

cv2.imshow("hore",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
