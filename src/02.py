import cv2 
import numpy as np
import matplotlib.pyplot as plt

def compute_hist(img):
    hist=np.zeros(( 256,),dtype='uint32')  
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i][j]] += 1
    return hist

def main():
    I  = cv2.imread('../images/I04.jpg')
    height = I.shape[0]
    width = I.shape[1]
    print('Câu 1:Tỷ lệ giữa giá trị độ cao và độ rộng của ảnh I:',float(height/width))

    I2 = cv2.resize(I, (256, 256))
    cv2.imshow('Cau 2',I2)

    Ihsv = cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
    cv2.imshow('Cau 3',Ihsv[:,:,1])

    Ivb = cv2.Canny(Ihsv[:,:,2],0,255)
    cv2.imshow('Cau 4',Ivb)

    hist = compute_hist(Ihsv[:,:,1])
    plt.title('Cau 5:Histogram của kênh S')
    plt.plot(hist)
    plt.show()

    cv2.waitKey()

main()