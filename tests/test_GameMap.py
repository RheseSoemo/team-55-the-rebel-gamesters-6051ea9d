from unittest import TestCase
from levelup.GameMap import GameMap

class TestGameMap(TestCase):
    def test_init(self):
        testObj = GameMap(10)
        assert testObj.get_total_positions() == 10
        
