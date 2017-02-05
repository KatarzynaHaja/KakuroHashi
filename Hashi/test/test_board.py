import unittest
from Hashi.board import *
from operator import attrgetter


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(4)

    def test_sort_circle(self):
        self.circles = list()
        for i in range(4):
            self.circles.append(Circle(2, 500 - i * 20, 100, violet))
        self.assertEqual(sort_circle(self.circles, 'x'), sorted(self.circles, key=attrgetter('x')))

    def test_generate_default_board(self):
        self.assertEquals(len(self.board.generate_default_board()), 30)

    def test_generate_by_recognition(self):
        list_x = [350, 250, 250, 350]
        list_y = [50, 150, 250, 350]
        self.board.list_circle = recognize_txt(
            "C:/Users/Kasior/PycharmProjects/KakuroHashi/Hashi/generated_boards/plansza.txt")
        for i in range(4):
            self.assertEqual(self.board.list_circle[i].x, list_x[i])
            self.assertEqual(self.board.list_circle[i].y, list_y[i])

    def test_random_board(self):
        self.board.generate_default_board()
        self.assertEquals(len(self.board.random_board()), 4)

    def test_set_neighbors(self):
        list_y = [50, 150, 250, 350]
        for i in range(4):
            self.board.list_circle.append(Circle(2, 100, i * 100 + 50, violet))
        self.board.set_neighbors()
        for i in range(4):
            self.assertEqual(self.board.list_circle[1].neighbors_x[i].y, list_y[i])

    def test_set_close_neighbors(self):
        list_y = [50, 250]
        for i in range(4):
            self.board.list_circle.append(Circle(2, 100, i * 100 + 50, violet))
        self.board.set_neighbors()
        self.board.set_close_neighbors()
        for i in range(len(self.board.list_circle[1].close_neighbors)):
            self.assertEqual(self.board.list_circle[1].close_neighbors[i].y, list_y[i])

    def test_set_bridges(self):
        self.board.generate_default_board()
        self.board.random_board()
        self.board.set_neighbors()
        self.board.set_close_neighbors()
        self.board.set_bridges()
        for i in range(len(self.board.list_bridge)):
            print(self.board.list_bridge[i].number)
            self.assertTrue(1 <= self.board.list_bridge[i].number <= 2)


suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
print(unittest.TextTestRunner(verbosity=3).run(suite))
