import unittest
from Hashi.solver import *
from Hashi.recognize import *


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.solver = Solver()

    def test_solver_txt(self):
        list_circle = recognize_txt("../generated_boards/plansza.txt")

        self.assertEqual(ready(self.solver.solve(list_circle)),[])

    def test_solver_png(self):
        list_circle = recognize("../generated_boards/83886.png")

        self.assertEqual(ready(self.solver.solve(list_circle)), [])



suite = unittest.TestLoader().loadTestsFromTestCase(TestSolver)
print(unittest.TextTestRunner(verbosity=3).run(suite))
