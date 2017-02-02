import random
import unittest
from Hashi.board import *
from operator import attrgetter


class TestBoard(unittest.TestCase):

    def test_sort_circle(self):
        self.circles = list()
        for i in range(5):
            self.circles.append(Circle(2,500 -i * 20, 100, violet))
        self.assertEqual(sort_circle(self.circles,'x'),sorted(self.circles, key=attrgetter('x')))

suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
print(unittest.TextTestRunner(verbosity=3).run(suite))
