import random
import unittest
import Hashi


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Hashi.board.Board(4)

    def test_generate_default_board(self):
        self.assertTrue(len(self.board.generate_default_board()) == 30)


suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
print(unittest.TextTestRunner(verbosity=3).run(suite))
