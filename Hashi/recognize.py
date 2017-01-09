import numpy as np
import cv2

img  = cv2.imread('generated_boards/57391.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=100,param2=15,minRadius=10,maxRadius=30)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    print(i[0])
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected',cimg)
cv2.waitKey(0)