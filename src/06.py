import cv2 
import numpy as np

def gianmucxam(Ig):
    max = np.max(Ig)
    min = np.min(Ig)
    Alut = np.zeros(256, dtype='uint8')
    for i in range(0, 255 + 1):
        # Công thức giãn mức xám
        Alut[i] = (255*(i-min))//(max-min)
    for u in range(Ig.shape[0]):
        for v in range(Ig.shape[1]):
            Ig[u, v] = Alut[Ig[u, v]] 
    return Ig
    
def main():
    I  = cv2.imread('../images/anh5.jpg')
    cv2.imshow('Cau 1',I)

    Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
    cv2.imshow('Cau 2: Kenh H cua Ihsv', Ihsv[:, :, 0])
    print('Câu 2: Mức sáng lớn nhất của kênh S ảnh Ihsv: ', np.max(Ihsv[:, :, 1]))

    Is = cv2.blur(Ihsv[:, :, 1], (7, 7))
    cv2.imshow('Cau 3', Is)

    thresh, Ib = cv2.threshold(255-Is, 0, 255, cv2.THRESH_OTSU)
    _,contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    maxArea = 0.0
    contours_max = []
    for cnt in contours:
        if maxArea < cv2.contourArea(cnt):
            maxArea = cv2.contourArea(cnt)
            contours_max = cnt
    cv2.drawContours(I, [contours_max], -1, (0, 0, 255), 2)
    cv2.imshow('Cau 4:', I)

    Ihsv[:, :, 2] = gianmucxam(Ihsv[:, :, 2])
    I2 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2RGB)
    cv2.imshow('Cau 5', I2)

    cv2.waitKey(0)

main()