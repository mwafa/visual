import cv2 as cv


mesi = cv.imread("../image/mesi.jpg")

mesi = cv.GaussianBlur(mesi, (35, 1), 0)
mesi = cv.cvtColor(mesi,cv.COLOR_RGB2GRAY)

cv.imshow("coba", mesi)
cv.waitKey(0)
cv.destroyAllWindows()
