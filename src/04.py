import cv2 
import numpy as np
import matplotlib.pyplot as plt

I  = cv2.imread('../images/anh5.jpg')
cv2.imshow('Cau 1',I)

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2]) + int(0.5 * I[i][j][1]) + int(0.11 * I[i][j][0])

cv2.imshow('Cau 2', Ig)
print('Câu 2: Mức xám lớn nhất của ảnh Ig:', np.max(Ig))

Ie = cv2.Canny(Ig, 255, 0)
cv2.imshow('Cau 3', Ie)

y = 160
x = 326
if Ie[y][x] == 255:
    print('Câu 3: Yes!')
else:
    print('Câu 3: No!')

thresh, Ib = cv2.threshold(255-Ig, 0, 255, cv2.THRESH_OTSU)
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