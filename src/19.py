import cv2 
import numpy as np

I  = cv2.imread('../images/apple.jpg')
cv2.imshow('Cau 1',I)
Ig = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
for i in range(I.shape[0]):
    for j in range(I.shape[1]):
        Ig[i][j] = int(0.39 * I[i][j][2]) + int(0.5 * I[i][j][1]) + int(0.11 * I[i][j][0])

cv2.imshow('Cau 2', Ig)
print('Câu 2: Mức xám trung binh của ảnh Ig:', np.mean(Ig))

GradientX = cv2.Sobel(Ig, cv2.CV_64F, 1, 0, 3)
print('Cau 3: Gradient X:',GradientX)

Ie = cv2.Canny(Ig, 0, 255)
cv2.imshow('Cau 4', Ie)

y = 100
x = 120
if Ie[y][x] == 255:
    print('Câu 4: Yes!')
else:
    print('Câu 4: No!')

thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
_,contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
maxArea = 0.0
contours_max = []
for cnt in contours:
    if maxArea < cv2.contourArea(cnt):
        maxArea = cv2.contourArea(cnt)
        contours_max = cnt
        
cv2.drawContours(I, [contours_max], -1, (0, 255, 255), 2)
cv2.imshow('Cau 5', I)
cv2.waitKey(0)