import cv2
from Hashi.circle import Circle
from Hashi.settings import *
from Hashi.folders_display import *
import numpy as np
from PIL import Image


def number_recognition(file):
    """
    This function recognizes numbers which are on the circle
    :param file: path of file
    :return:
    """
    img = Image.open(file).convert('RGB')
    arr = np.array(img)

    y = arr.shape[0]
    x = arr.shape[1]
    print(x, y)
    values = list()
    row = 40
    while row < y:
        column = 40
        while column < x:
            if all(i in [45, 22, 80] for i in arr[row][column]):
                values.append(1)
                print(row, column)
                column += 90
            if column < 600 and all(i in [45, 22, 81] for i in arr[row][column]):
                values.append(2)
                column += 90
            if column < 600 and all(i in [45, 21, 80] for i in arr[row][column]):
                values.append(3)
                column += 90
            if column < 600 and all(i in [45, 21, 81] for i in arr[row][column]):
                values.append(4)
                column += 90
            if column < 600 and all(i in [44, 22, 80] for i in arr[row][column]):
                values.append(5)
                column += 90
            if column < 600 and all(i in [44, 21, 80] for i in arr[row][column]):
                values.append(6)
                column += 90
            if column < 600 and all(i in [45, 21, 81] for i in arr[row][column]):
                values.append(7)
                column += 90
            if column < 600 and all(i in [45, 22, 82] for i in arr[row][column]):
                values.append(8)
                column += 90
            else:
                column += 1

        row += 10
    for i in values:
        print(i)
    return values


def which_file():
    """
    It allows open common dialog and choose file. It also call recognize which depends on txt or png
    :return: list of recognized circle
    """
    circle = list()
    path = ''
    while True:
        path2 = open_common_dialog()
        if path2 == '':
            continue
        else:
            path = path2
            break
    pattern = re.compile('.*txt')
    pattern1 = re.compile('.*png')
    if re.match(pattern, path):
        circle = recognize_txt(path)
    if re.match(pattern1, path):
        circle = recognize(path)
    return circle


def recognize(file):
    """
    Recognition from png
    :return: list of circle
    """
    z = file
    img = cv2.imread(z, 0)
    img = cv2.medianBlur(img, 5)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, param1=100, param2=15, minRadius=10, maxRadius=30)
    circles = np.uint16(np.around(circles))
    circle_list = list()
    list_value = number_recognition(file)
    for i in circles[0, :]:
        print(i[0])
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
        circle_list.append(Circle(0, i[0], i[1], circle_violet))
    print(len(circle_list))
    for i in range(len(list_value)):
        circle_list[i].value = list_value[i]

    return circle_list


def recognize_txt(file):
    """
    Recognition from txt. It scales distance between each pair of circles
    :return: list of circles
    """
    circle_list = list()
    with open(file) as file:
        lines = file.readlines()
        lenght_y = len(lines)
        jump_y = 500 / lenght_y
        for i, line in enumerate(lines):
            line = line.strip('\n')
            l = line.split(";")
            lenght_x = len(l)
            jump_x = 600 / lenght_x
            for j, chars in enumerate(l):
                if chars != 'x':
                    circle_list.append(Circle(int(chars), j * int(jump_x) + 50, i * int(jump_y) + 50, circle_violet))
        for i in range(4):
            print(circle_list[i].x, '  ', circle_list[i].y)
    return circle_list
