import cv2 
import numpy as np

I  = cv2.imread('../images/the_cancuoc_congdan.jpg')

cv2.imshow('Cau 1',I[:,:,0])

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2]) + int(0.5 * I[i][j][1]) + int(0.11 * I[i][j][0])

cv2.imshow('Cau 2',Ig)

threshold, Ib = cv2.threshold(Ig,0,255,cv2.THRESH_OTSU)
cv2.imshow("Cau 3", Ib)


Im = cv2.blur(Ig, (4,4))
cv2.imshow("Cau 4", Im)

_,contours,_ = cv2.findContours(Im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(I, contours, -1, (0,0,255),2)
cv2.imshow('Cau 5',I)

cv2.waitKey()