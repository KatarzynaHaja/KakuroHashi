import random
import unittest
from Hashi.randomize import *


class TestRandomize(unittest.TestCase):
    def test_random_circle_easy(self):
        self.randomize = Randomize(0)
        self.assertTrue(4 <= self.randomize.random_circle() <= 7)

    def test_random_circle_midi(self):
        self.randomize = Randomize(1)
        self.assertTrue(8 <= self.randomize.random_circle() <= 12)

    def test_random_circle_hard(self):
        self.randomize = Randomize(2)
        self.assertTrue(13 <= self.randomize.random_circle() <= 17)


suite = unittest.TestLoader().loadTestsFromTestCase(TestRandomize)
print(unittest.TextTestRunner(verbosity=3).run(suite))
