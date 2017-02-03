import unittest
from Hashi.game import *
from Hashi.circle import Circle
from Hashi.bridge import *


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_set_level_easy(self):
     self.assertEqual(set_level('easy'),0)

    def test_set_level_midi(self):
        self.assertEqual(set_level('midi'), 1)

    def test_set_level_hard(self):
        self.assertEqual(set_level('hard'), 2)

    def test_is_finish_true(self):
        list_circle = list()
        for i in range(3):
            list_circle.append(Circle(2,i*100+50,i*100+50,violet))
        for i in range(3):
            list_circle[i].conections = list_circle[i].value
        self.assertTrue(is_finished(list_circle))

    def test_is_finish_false(self):
        list_circle = list()
        for i in range(3):
            list_circle.append(Circle(2, i * 100 + 50, i * 100 + 50, violet))
        self.assertFalse(is_finished(list_circle))

    def test_is_in_true(self):
        list_bridge = list()
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2,i*100+50,50,violet))
        list_bridge.append(Bridge(list_circle[0],list_circle[1],violet,1))
        self.assertEqual(is_in(list_bridge,list_circle[0],list_circle[1]),(True,0))

    def test_is_in_false(self):
        list_bridge = list()
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2, i * 100 + 50, 50, violet))
        self.assertEqual(is_in(list_bridge, list_circle[0], list_circle[1]), (False, 0))

    def test_if_remove_true(self):
        list_bridge = list()
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2,i*100+50,50,violet))
        list_bridge.append(Bridge(list_circle[0],list_circle[1],violet,2))
        self.assertEqual(if_remove(list_bridge,list_circle[0],list_circle[1]),(True,0))

    def test_if_remove_is_not_enough(self):
        list_bridge = list()
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2,i*100+50,50,violet))
        list_bridge.append(Bridge(list_circle[0],list_circle[1],violet,1))
        self.assertEqual(if_remove(list_bridge,list_circle[0],list_circle[1]),(False,0))

    def test_if_remove_lack_of_bridge(self):
        list_bridge = list()
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2,i*100+50,50,violet))
        self.assertEqual(if_remove(list_bridge,list_circle[0],list_circle[1]),(False,0))

    def test_check_one_bridge(self):
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2, i * 100 + 50, 50, violet))
        list_circle[0].close_neighbors.append(list_circle[1])
        list_circle[1].close_neighbors.append(list_circle[0])
        check(list_circle,self.game)
        self.assertEqual(self.game.board.user_list_bridge[0].number,1)

    def test_check_two_bridge(self):
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2, i * 100 + 50, 50, violet))
        list_circle[0].close_neighbors.append(list_circle[1])
        list_circle[1].close_neighbors.append(list_circle[0])
        self.game.board.user_list_bridge.append(Bridge(list_circle[0],list_circle[1],violet,1))
        check(list_circle,self.game)
        self.assertEqual(self.game.board.user_list_bridge[0].number,2)

    def test_check_remove(self):
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2, i * 100 + 50, 50, violet))
        list_circle[0].close_neighbors.append(list_circle[1])
        list_circle[1].close_neighbors.append(list_circle[0])
        self.game.board.user_list_bridge.append(Bridge(list_circle[0], list_circle[1], violet, 2))
        check(list_circle, self.game)
        self.assertEqual(len(self.game.board.user_list_bridge), 0)

    def test_clear_bridges_one(self):
        list_bridge = list()
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2, i * 100 + 50, 50, violet))
        list_bridge.append(Bridge(list_circle[0],list_circle[1],violet,1))
        list_circle[0].add_bridge(list_circle[1],1)
        clear_bridges(list_bridge)
        self.assertEqual(list_bridge[0].circle1.conections,0)
        self.assertEqual(list_bridge[0].circle2.conections, 0)

    def test_clear_bridges_two(self):
        list_bridge = list()
        list_circle = list()
        for i in range(2):
            list_circle.append(Circle(2, i * 100 + 50, 50, violet))
        list_bridge.append(Bridge(list_circle[0], list_circle[1], violet, 2))
        list_circle[0].add_bridge(list_circle[1], 2)
        clear_bridges(list_bridge)
        self.assertEqual(list_bridge[0].circle1.conections, 0)
        self.assertEqual(list_bridge[0].circle2.conections, 0)





suite = unittest.TestLoader().loadTestsFromTestCase(TestGame)
print(unittest.TextTestRunner(verbosity=3).run(suite))
