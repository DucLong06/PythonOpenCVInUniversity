import cv2
import numpy as np

I  = cv2.imread('../images/anh5.jpg')
cv2.imshow('Cau 1', I)

height = I.shape[0]
width = I.shape[1]
Ig = np.zeros((height, width), dtype='uint8')
for i in range(height):
    for j in range(width):
        Ig[i][j] = int(0.39*I[i][j][2]) + int(0.5*I[i][j][1]) + int(0.11*I[i][j][0])
cv2.imshow('Cau 2', Ig)
print('Câu 2: Mức xám lớn nhất của ảnh Ig:', np.max(Ig))

print('Câu 3:Mức xám lớn nhất của ảnh Ig:', np.max(Ig))
print('Câu 3:Mức xám nhỏ nhất của ảnh Ig:', np.min(Ig))
print('Câu 3:Mức xám trung bình của ảnh Ig', np.mean(Ig))

thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('Cau 4:', Ib)

_,contours, _ = cv2.findContours(Ib, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
maxPre = 0.0
contour_max = []
for cnt in contours:
    if maxPre < cv2.arcLength(cnt, True):
        maxPre = cv2.arcLength(cnt, True)
for cnt in contours:
    if cv2.arcLength(cnt, True) > maxPre / 3.0:
        contour_max.append(cnt)
cv2.drawContours(I, contour_max, -1, (0, 0, 255), 2)
cv2.imshow('Cau 5', I)

cv2.waitKey(0)