import cv2
import numpy as np

def equal_hist(hist):
    cumulator = np.zeros_like(hist, np.float64)
    for i in range(len(cumulator)):
        cumulator[i] = hist[:i].sum()
    new_hist = (cumulator - cumulator.min())/(cumulator.max() - cumulator.min()) * 255
    new_hist = np.uint8(new_hist)
    return new_hist
    
def main():
    I  = cv2.imread('../images/anh5.jpg')
    cv2.imshow('Cau 1:', I)

    Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
    cv2.imshow('Cau 2:Kenh S cua Ihsv', Ihsv[:, :, 1])
    print('Câu 2:Mức sáng lớn nhất của kênh V ảnh Ihsv: ', np.max(Ihsv[:, :, 2]))

    Iv = cv2.blur(Ihsv[:, :, 2], (3, 3))
    cv2.imshow('Cau 3:', Iv)

    Ig = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
    thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
    _,contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    maxPre = 0.0
    contour_max = []
    for cnt in contours:
        if maxPre < cv2.arcLength(cnt, True):
            maxPre = cv2.arcLength(cnt, True)
            contour_max = cnt
    cv2.drawContours(I, [contour_max], -1, (0, 0, 255), 2)
    cv2.imshow('Cau 5', I)

    Ihsv[:, :, 2] = equal_hist(Ihsv[:, :, 2])
    I2 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2RGB)
    cv2.imshow('Cau 6:', I2)
    cv2.waitKey(0)

main()