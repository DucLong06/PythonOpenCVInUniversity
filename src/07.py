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
    I  = cv2.imread('../images/hat1.PNG')
    cv2.imshow('Cau 1',I)

    Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
    cv2.imshow("Cau 2:Ihsv Kenh V", Ihsv[:, :, 2])
    print("Câu 2:Mức xám lớn nhất của kênh S của ảnh Ihsv", np.max(Ihsv[:, :, 1]))
    print("Câu 2:Mức xám nhỏ nhất của kênh S của ảnh Ihsv", np.min(Ihsv[:, :, 1]))

    hist = compute_hist(Ihsv[:,:,2])
    plt.title('Câu 3: Histogram của kênh V')
    plt.plot(hist)
    plt.show()

    Is = cv2.medianBlur(Ihsv[:, :, 2],3)
    cv2.imshow("Cau 4:", Is)

    thresh , Ib = cv2.threshold(Is, 0, 255, cv2.THRESH_OTSU)
    _,contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    maxArea = 0.0
    contour_max = []
    for cnt in contours:
        if maxArea < cv2.contourArea(cnt):
            maxArea = cv2.contourArea(cnt)
            contour_max = cnt
    cv2.drawContours(I, [contour_max], -1, (0, 0, 255), 2)
    cv2.imshow('Cau 5:', I)

    cv2.waitKey()

main()