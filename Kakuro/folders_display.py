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


def which_file():
    """
    It allows open common dialog and choose file
    :return: path to the file
    """
    path = ''
    while True:
        path2 = open_common_dialog()
        if path2 == '':
            continue
        else:
            path = path2
            break
    if path.endswith(".txt"):
        return path


