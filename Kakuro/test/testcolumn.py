import unittest
from Kakuro.column import *


class TestColumn(unittest.TestCase):
    def setUp(self):
        self.c = Column([0, 0], [0, 0], [0, 0], 'h')
        self.c.sum.number = 8

    def test_add_instance(self):
        result = self.c.add(2)
        node = Node(2, self.c.x[0], self.c.y[1] + self.c.count * 40)
        self.assertEquals(result.hidden_number, node.hidden_number)

    def test_add_not_instance(self):
        node = Node(3, self.c.x[0], self.c.y[1] + self.c.count * 40)
        result = self.c.add(node)
        self.assertEquals(result, node)

    def test_check_partial_true(self):
        node = Node(1, 0, 0)
        self.c.column.append(node)
        node = Node(2, 0, 0)
        self.c.column.append(node)
        self.assertTrue(self.c.check_partial())

    def test_check_partial_false_sum_greater_than_number(self):
        node = Node(9, 0, 0)
        node.number = 9
        self.c.column.append(node)
        node = Node(2, 0, 0)
        node.number = 2
        self.c.column.append(node)
        self.assertFalse(self.c.check_partial())

    def test_check_partial_false_repeated(self):
        node = Node(2, 0, 0)
        node.number = 2
        self.c.column.append(node)
        node = Node(2, 0, 0)
        node.number = 2
        self.c.column.append(node)
        self.assertFalse(self.c.check_partial())

    def test_is_filled_true(self):
        node = Node(1, 0, 0)
        node.number = 1
        self.c.column.append(node)
        node = Node(2, 0, 0)
        node.number = 2
        self.c.column.append(node)
        self.assertTrue(self.c.is_filled())

    def test_is_filled_false(self):
        node = Node("", 0, 0)
        self.c.column.append(node)
        node = Node(2, 0, 0)
        self.c.column.append(node)
        self.assertFalse(self.c.is_filled())

    def test_check_true(self):
        node = Node(6, 0, 0)
        self.c.column.append(node)
        node = Node(2, 0, 0)
        self.c.column.append(node)
        self.assertTrue(self.c.check_partial())

    def test_check_false_sum_greater_than_number(self):
        node = Node(7, 0, 0)
        node.number = 7
        self.c.column.append(node)
        node = Node(2, 0, 0)
        node.number = 2
        self.c.column.append(node)
        self.assertFalse(self.c.check_partial())

    def test_check_false_repeated(self):
        node = Node(4, 0, 0)
        node.number = 4
        self.c.column.append(node)
        node = Node(4, 0, 0)
        node.number = 4
        self.c.column.append(node)
        self.assertFalse(self.c.check_partial())



suite = unittest.TestLoader().loadTestsFromTestCase(TestColumn)
print(unittest.TextTestRunner(verbosity=3).run(suite))