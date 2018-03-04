import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../image/mesi.jpg")
cv2.imshow("hore",image)

cv2.waitKey(0)
cv2.destroyAllWindows()