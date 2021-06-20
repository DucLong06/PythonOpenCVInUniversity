import cv2 
import numpy as np

I  = cv2.imread('../images/anh5.jpg')
cv2.imshow('Cau 1',I)

Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2]) + int(0.5 * I[i][j][1]) + int(0.11 * I[i][j][0])

cv2.imshow('Cau 2', Ig)
print('Câu 2: Mức xám lớn nhất của ảnh Ig:', np.mean(Ig))

Ie = cv2.Canny(Ig, 255, 0)
cv2.imshow('Cau 3', Ie)

y = 100
x = 300
if Ie[y][x] == 255:
    print('Câu 4: Yes!')
else:
    print('Câu 4: No!')

thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('Cau 5',Ib)

_,contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
maxArea = 0.0
contour_max = []
for cnt in contours:
    if maxArea < cv2.contourArea(cnt):
        maxArea = cv2.contourArea(cnt)
for cnt in contours:
    if cv2.contourArea(cnt) > maxArea / 5.0:
        contour_max.append(cnt)
cv2.drawContours(I, contour_max, -1, (0, 255, 255), 2)
cv2.imshow('Cau 5', I)

cv2.waitKey()