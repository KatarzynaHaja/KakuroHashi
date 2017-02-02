import unittest
from Kakuro.sumofcolumn import *


class TestSumOfColumn(unittest.TestCase):

    def setUp(self):
        self.s = SumOfColumn(0, 0, 0, 0, 'column')

    def test_update(self):
        self.s.update(8)
        self.assertEquals(self.s.number, 8)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSumOfColumn)
print(unittest.TextTestRunner(verbosity=3).run(suite))
