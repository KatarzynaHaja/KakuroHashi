import numpy as np
import cv2
from Hashi.circle import Circle
from Hashi.folders_display import *
import re

def which_file():
    z = open_common_dialog()
    pattern = re.compile('.*txt')
    pattern1 = re.compile('.*png')
    if re.match(pattern,z):
        circle = recognize_txt()
    if re.match(pattern1,z):
        circle = recognize()
    return circle

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

def recognize_txt():
    print("odpalono txt")
    circle_list = list()
    file = 'generated_boards/plansza1.txt'
    with open(file) as file:
        lines = file.readlines()
        print(lines)
        lenght_y = len(lines)
        jump_y = 500/lenght_y
        for i, line in enumerate(lines):
            print(i)
            line = line.strip('\n')
            l = line.split(";")
            lenght_x = len(l)
            jump_x = 600/lenght_x
            for j, chars in enumerate(l):
                if chars!='x':
                    print("to jest j",chars)
                    circle_list.append(Circle(int(chars),j*int(jump_x)+50,i*int(jump_y)+50))
        for i in range(len(circle_list)):
            print(circle_list[i].value)
    return circle_list


