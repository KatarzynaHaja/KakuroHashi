import numpy as np
import cv2
from Hashi.circle import Circle
from Hashi.folders_display import *

def recognize():
    z = open_common_dialog()
    img  = cv2.imread(z,0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,param1=100,param2=15,minRadius=10,maxRadius=30)
    circles = np.uint16(np.around(circles))
    circle_list = list()
    for i in circles[0,:]:
        print(i[0])
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        circle_list.append(Circle(0,i[0],i[1]))
    return circle_list

