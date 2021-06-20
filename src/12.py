import cv2 
import numpy as np
import matplotlib.pyplot as plt

def equal_hist(hist):
    cumulator = np.zeros_like(hist, np.float64)
    for i in range(len(cumulator)):
        cumulator[i] = hist[:i].sum()
    new_hist = (cumulator - cumulator.min())/(cumulator.max() - cumulator.min()) * 255
    new_hist = np.uint8(new_hist)
    return new_hist


def main():
    I  = cv2.imread('../images/I04.jpg')
    # cv2.imshow('I04.jpg',I)

    height = I.shape[0]
    width = I.shape[1]
    print('Câu 1:Tỷ lệ giữa giá trị độ cao và độ rộng của ảnh I:',float(height/width))


    I2 = cv2.resize(I, (256, int(256/(height/width))))
    cv2.imshow('Cau 2',I2)

    Ihsv = cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
    cv2.imshow('Cau 3',Ihsv[:,:,1])

    Ihsv[:, :, 1] = cv2.medianBlur(Ihsv[:, :, 1],3)
    I3 = cv2.cvtColor(Ihsv,cv2.COLOR_HSV2BGR)
    cv2.imshow("Cau 4", I3)

    Ihsv[:, :, 1] = equal_hist(Ihsv[:, :, 1])
    # Ihsv[:, :, 1] = cv2.equalizeHist(img)
    I4 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2RGB)
    cv2.imshow('Cau 5:', I4)
    
    cv2.waitKey()

main()