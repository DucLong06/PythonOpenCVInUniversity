import cv2 
import numpy as np

I  = cv2.imread('../images/clother1.jpg')
cv2.imshow('Cau 1:', I)

Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
cv2.imshow('Cau 2:Kenh S cua Ihsv', Ihsv[:, :, 1])

print("Cau 2: Các độ xám của cửa sổ lân cận 5x5 của pixel có toạ độ y = 10, x = 20 của ảnh Ig là: ")
y = 10
x = 20
for i in range(-2, 3):
    for j in range(-2, 3):
        if (y + i >= 0 & y + i <= Ihsv.shape[0] - 1 & x + j >= 0 & x + j <= Ihsv.shape[1] -1):
            print(Ihsv[y+i][x+j])


thresh, Ib = cv2.threshold(Ihsv[:, :, 1], 0, 255, cv2.THRESH_OTSU)
cv2.imshow('Cau 3:', Ib)

Im = cv2.blur(Ihsv[:, :, 1], (5,5))
cv2.imshow("Cau 4", Im)

_,contours, _ = cv2.findContours(Im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255), 2)
cv2.imshow("Cau 5:", I)

cv2.waitKey()