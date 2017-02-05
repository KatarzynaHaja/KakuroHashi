import unittest
from Kakuro.solver import *
from Kakuro.board import *


class TestSolver(unittest.TestCase):

    def setUp(self):
        b = Board()
        self.solver = Solver(b)

    def test_factorise(self):
        list_of_factors = [[1, 4], [4, 1], [3, 2], [2, 3]]
        self.solver.factorise(5, 2)
        self.assertEquals(sorted(self.solver.list_of_all), sorted(list_of_factors))

    def test_factor_last_factor_ok(self):
        result = self.solver.factor(7, 1, 9, [1, 2, 7])
        self.assertEquals(result, [7])

    def test_factor_last_factor_not_ok(self):
        result = self.solver.factor(7, 1, 9, [1, 2])
        self.assertEquals([], result)

    def test_factor(self):
        result = self.solver.factor(5, 2, 9, [x for x in range(1, 10)])
        list_of_factors = [[1, 4], [2, 3]]
        self.assertEquals(list_of_factors, result)

    def test_solver(self):
        board = Board()
        board.generate(4)
        solver = Solver(board)
        solver.solve()
        self.assertEquals(board.check(), "Wygrana")


suite = unittest.TestLoader().loadTestsFromTestCase(TestSolver)
print(unittest.TextTestRunner(verbosity=3).run(suite))
