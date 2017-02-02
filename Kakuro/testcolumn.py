import unittest
from Kakuro.column import *


class TestColumn(unittest.TestCase):
    def setUp(self):
        self.c = Column([0, 0], [0, 0], [0, 0], 'h')

    def test_add_instance(self):
        result = self.c.add(2)
        node = Node(2, self.c.x[0], self.c.y[1] + self.c.count * 40)
        self.assertEquals(result.hidden_number, node.hidden_number)

    def test_add_not_instance(self):
        node = Node(3, self.c.x[0], self.c.y[1] + self.c.count * 40)
        result = self.c.add(node)
        self.assertEquals(result, node)

suite = unittest.TestLoader().loadTestsFromTestCase(TestColumn)
print(unittest.TextTestRunner(verbosity=3).run(suite))