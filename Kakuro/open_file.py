from Kakuro.folders_display import *


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
