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

    Ihsv = cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
    cv2.imshow('Cau 2',Ihsv[:, :, 0])
    print('Câu 2: Giá trị mức sáng trung bình của kênh S của ảnh Ihsv:',np.mean(Ihsv[:, :, 1]))

    hist = compute_hist(Ihsv[:,:,2])
    plt.title('Câu 3: Histogram của kênh V')
    plt.plot(hist)
    plt.show()

    Is = cv2.blur(Ihsv[:, :, 1], (5,5))
    cv2.imshow('Cau 4',Is)

    Ig = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
    thresh, Ib = cv2.threshold(Ig, 0, 255, cv2.THRESH_OTSU)
    _,contours, _ = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    maxRate = 0.0
    contours_max = []
    for cnt in contours:  
        if cv2.contourArea(cnt) != 0:
            if maxRate < float(cv2.arcLength(cnt, True))/float(cv2.contourArea(cnt)):
                maxRate = float(cv2.arcLength(cnt, True))/float(cv2.contourArea(cnt))
                contours_max = cnt
    cv2.drawContours(I, [contours_max], -1, (0, 0, 255), 2)
    cv2.imshow('Cau 5:', I)
    cv2.waitKey(0)

main()