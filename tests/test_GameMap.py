from unittest import TestCase
from levelup.GameMap import GameMap

class TestGameMap(TestCase):
    def test_init(self):
        testObj = GameMap(100)
        assert testObj.get_total_positions() == 100
        
