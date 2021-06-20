import cv2 
import numpy as np


I  = cv2.imread('../images/anh5.jpg')
cv2.imshow('Cau 1',I)

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2]) + int(0.5 * I[i][j][1]) + int(0.11 * I[i][j][0])

cv2.imshow('Cau 2', Ig)
print('Câu 2: Mức xám Trung bình của ảnh Ig:', np.mean(Ig))

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
print('Câu 3: Mức xám lớn nhất của kênh S:', np.max(Ihsv[:,:,1]))

thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('Cau 4',Ib)

_,contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
maxPre = 0.0
contours_max = []
for cnt in contours:
    if maxPre < cv2.arcLength(cnt,True):
        maxPre = cv2.arcLength(cnt,True)
        contours_max = cnt

cv2.drawContours(I, [contours_max], -1, (0, 255, 255), 2)
cv2.imshow('Cau 5', I)

cv2.waitKey()