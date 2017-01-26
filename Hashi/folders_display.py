from tkinter import *
from tkinter import filedialog
import re

def open_common_dialog():
    root = Tk()
    root.fileName = filedialog.askopenfilename(filetype =(("png", ".png"), ("txt", ".txt"), ("all files","*.*")))
    path = root.fileName
    print(path)
    return path


