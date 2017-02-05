from Kakuro.folders_display import *


def which_file():
    """
    It allows open common dialog and choose file. It also call recognize which depends on txt or png
    :return: list of recognized circle
    """
    path = ''
    while True:
        path2 = open_common_dialog()
        if path2 == '':
            continue
        else:
            path = path2
            break
    pattern = re.compile('.*txt')
    if re.match(pattern, path):
        return path
    return False
