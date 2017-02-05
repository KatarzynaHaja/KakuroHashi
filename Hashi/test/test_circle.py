import unittest
from Hashi.game import *
from Hashi.circle import Circle


class TestCircle(unittest.TestCase):
    def test_change_color(self):
        circle = Circle(2, 50, 100, red)
        circle.change_color(violet)
        self.assertTrue(circle.color, violet)

    def test_add_bridge(self):
        circle1 = Circle(2, 50, 100, violet)
        circle2 = Circle(3, 50, 150, violet)
        circle1.add_bridge(circle2, 2)
        self.assertTrue(circle1.conections, 2)
        self.assertTrue(circle2.conections, 2)

    def test_both_no_update_color(self):
        circle1 = Circle(3, 50, 100, violet)
        circle2 = Circle(3, 50, 150, violet)
        circle2.add_bridge(circle1, 2)
        circle1.update_color()
        circle2.update_color()
        print(circle2.conections)
        print(circle2.value)
        self.assertEqual(circle1.color, violet)
        self.assertEqual(circle2.color, violet)

    def test_one_no_update_color(self):
        circle1 = Circle(3, 50, 100, violet)
        circle2 = Circle(2, 50, 150, violet)
        circle2.add_bridge(circle1, 2)
        circle1.update_color()
        circle2.update_color()
        print(circle2.conections)
        print(circle2.value)
        self.assertEqual(circle1.color, violet)
        self.assertEqual(circle2.color, max_circle)

    def test_update_color(self):
        circle1 = Circle(2, 50, 100, violet)
        circle2 = Circle(2, 50, 150, violet)
        circle2.add_bridge(circle1, 2)
        circle1.update_color()
        circle2.update_color()
        print(circle2.conections)
        print(circle2.value)
        self.assertEqual(circle1.color, max_circle)
        self.assertEqual(circle2.color, max_circle)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCircle)
print(unittest.TextTestRunner(verbosity=3).run(suite))
