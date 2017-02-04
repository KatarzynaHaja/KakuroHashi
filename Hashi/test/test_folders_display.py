import unittest

from Kakuro.folders_display import *


class TestFolders(unittest.TestCase):

    def test_open_common_dialog(self):
        path = open_common_dialog()
        self.assertTrue(len(path)!=0)

    def test_cancel_common_dialog(self):
        path = open_common_dialog()
        self.assertTrue(len(path) == 0)
