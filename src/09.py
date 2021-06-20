import cv2 
import numpy as np
import matplotlib.pyplot as plt

I  = cv2.imread('../images/Coins.jpg')
cv2.imshow('Cau 1',I)

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2]) + int(0.5 * I[i][j][1]) + int(0.11 * I[i][j][0])

cv2.imshow('Cau 2', Ig)
print('Câu 2: Mức xám Trung bình của ảnh Ig:', np.mean(Ig))

y = 100
x = 120
print("Cau 3: Các độ xám của cửa sổ lân cận 3x3 của pixel có toạ độ y = 100, x = 120 của ảnh Ig là: ")
for i in range(-2, 3):
    for j in range(-2, 3):
        if (y + i >= 0 & y + i <= Ig.shape[0] - 1 & x + j >= 0 & x + j <= Ig.shape[1] -1):
            print(Ig[y+i][x+j])


Ie = cv2.Canny(Ig, 0, 255)
cv2.imshow('Cau 4', Ie)

if Ie[100][120] == 255:
    print("Cau 4: YES")
else:
    print("Cau 4: NO")

thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
_,contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255), 2)
cv2.imshow("Cau 5:", I)

cv2.waitKey(0)
