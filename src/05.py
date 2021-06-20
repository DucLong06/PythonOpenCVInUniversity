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
print('Câu 2: Mức xám lớn nhất của ảnh Ig:', np.max(Ig))

GradientX = cv2.Sobel(Ig, cv2.CV_64F, 1, 0, 3)
GradientY = cv2.Sobel(Ig, cv2.CV_64F, 0, 1, 3)
# plt.subplot(2,2,1), plt.imshow(GradientX, cmap='gray')
# plt.title('Cau 3: Gradient X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2), plt.imshow(GradientY, cmap='gray')
# plt.title('Cau 3: Gradient Y'), plt.xticks([]), plt.yticks([])
# plt.show()
print('Cau 2: Gradient X:',GradientX)
print('Cau 2: Gradient Y:',GradientY)

Ie = cv2.Canny(Ig, 0, 255)
cv2.imshow('Cau 4', Ie)

y = 179
x = 123
print("Cau 4: Các độ xám của cửa sổ lân cận 3x3 của pixel có toạ độ y = 179, x = 123 của ảnh Ig là: ")
for i in range(-1, 2):
    for j in range(-1, 2):
        if (y + i >= 0 & y + i <= Ig.shape[0] - 1 & x + j >= 0 & x + j <= Ig.shape[1] -1):
            print(Ig[y+i][x+j])


thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
_,contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I, contours, -1, (0,0,255), 2)
cv2.imshow("Cau 5:", I)

cv2.waitKey()
