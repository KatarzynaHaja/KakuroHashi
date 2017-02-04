from tkinter import *
from tkinter import filedialog


def open_common_dialog():
    """
    It opens common dialog and user can choose file
    :return: file's path
    """
    root = Tk()
    root.fileName = filedialog.askopenfilename(filetype=(("png", ".png"), ("txt", ".txt"), ("all files", "*.*")))
    path = root.fileName
    root.destroy()
    return path




