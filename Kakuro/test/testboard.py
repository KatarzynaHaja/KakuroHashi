import unittest
import os
from Kakuro.board import *


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        column = Column(0, 0, 0, 'column', 4)
        self.board.columns[(0, 1)] = column
        column1 = Column(0, 0, 0, 'column', 6)
        self.board.columns[(0, 2)] = column1
        row = Column(0, 0, 0, 'row', 3)
        self.board.rows[(1, 0)] = row
        row2 = Column(0, 0, 0, 'row', 7)
        self.board.rows[(2, 0)] = row2
        for key in self.board.columns.keys():
            for i in range(0, 2):
                w, k = key
                node = Node("", 0, 0)
                self.board.columns[key].column.append(node)
                self.board.rows[(k, w)].column.append(node)

    def test_hint(self):
        self.assertEquals("", self.board.hint())

    def test_hint_used(self):
        self.board.number_of_hints = 3
        self.assertEquals(self.board.hint(), "Wykorzystano wszystkie podpowiedzi")

    def test_find_nearest_column(self):
        result = self.board.find_nearest_column(2, 2)
        self.assertEquals((0, 2), result)

    def test_find_nearest_column_false(self):
        result = self.board.find_nearest_column(0, 0)
        self.assertFalse(result)

    def test_find_nearest_row(self):
        result = self.board.find_nearest_row(2, 2)
        self.assertEquals((2, 0), result)

    def test_find_nearest_row_false(self):
        result = self.board.find_nearest_row(0, 0)
        self.assertFalse(result)

    def test_check_partial_empty(self):
        self.assertTrue(self.board.check_partial())

    def test_check_partial_true(self):
        self.board.rows[(1, 0)].column[0].number = 1
        self.board.rows[(2, 0)].column[0].number = 3
        self.board.rows[(1, 0)].column[1].number = ""
        self.board.rows[(2, 0)].column[1].number = ""
        self.assertTrue(self.board.check_partial())

    def test_check_partial_false(self):
        self.board.rows[(1, 0)].column[0].number = 4
        self.board.rows[(2, 0)].column[0].number = ""
        self.board.rows[(1, 0)].column[1].number = 3
        self.board.rows[(2, 0)].column[1].number = ""
        self.assertFalse(self.board.check_partial())

    def test_check_true(self):
        self.board.rows[(1, 0)].column[0].number = 1
        self.board.rows[(1, 0)].column[1].number = 2
        self.board.rows[(2, 0)].column[0].number = 3
        self.board.rows[(2, 0)].column[1].number = 4
        self.assertTrue(self.board.check_partial())

    def test_check_false(self):
        self.board.rows[(1, 0)].column[0].number = 1
        self.board.rows[(1, 0)].column[1].number = 7
        self.board.rows[(2, 0)].column[0].number = 3
        self.board.rows[(2, 0)].column[1].number = 4
        self.assertFalse(self.board.check_partial())

    def test_create_board_from_file(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        b = Board()
        b.create_board_from_file(os.path.join(os.path.dirname(dir_path), 'text_files', 'test.txt'))
        self.assertEquals(b.columns.keys(), self.board.columns.keys())
        self.assertEquals(b.rows.keys(), self.board.rows.keys())


suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
print(unittest.TextTestRunner(verbosity=3).run(suite))