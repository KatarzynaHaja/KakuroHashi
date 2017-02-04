import numpy as np
from PIL import Image
import pprint

def number_recognition():
    img = Image.open('generated_boards/83886.png').convert('RGB')
    arr = np.array(img)
    print(arr.shape)
    pprint.pprint(arr)

    y = arr.shape[0]
    x = arr.shape[1]
    print(x,y)
    values = list()
    row =40
    while row < y:
        column = 40
        while column < x:
            if all(i in [45, 22, 80] for i in arr[row][column]):
                values.append(1)
                print(row,column)
                column += 90
            if column <600 and all(i in [45, 22, 81] for i in arr[row][column]):
                values.append(2)
                column += 90
            if column <600 and all(i in [45, 21, 80] for i in arr[row][column]):
                values.append(3)
                column += 90
            if column <600 and all(i in [45, 21, 81] for i in arr[row][column]):
                values.append(4)
                column += 90
            if column <600 and all(i in [44, 22, 80] for i in arr[row][column]):
                values.append(5)
                column += 90
            if column <600 and all(i in [44, 21, 80] for i in arr[row][column]):
                values.append(6)
                column += 90
            if column <600 and all(i in [45, 21, 81] for i in arr[row][column]):
                values.append(7)
                column += 90
            if column <600 and all(i in [45, 22, 82] for i in arr[row][column]):
                values.append(8)
                column += 90
            else:
                column += 1

        row +=10
    for i in values:
        print(i)
    return values

number_recognition()
