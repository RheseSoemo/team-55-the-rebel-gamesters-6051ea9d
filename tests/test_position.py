from unittest import TestCase
from levelup.position import Position 

class TestXPosition(TestCase):
    def test_init(self):
        ARBITRARY_XPosition = 1
        testobj = Position(ARBITRARY_XPosition)
        self.assertEqual(ARBITRARY_XPosition, testobj.coordinates)

class TestYPosition(TestCase):
    def test_init(self):
        ARBITRARY_YPosition = 2
        testobj = Position(ARBITRARY_YPosition)
        self.assertEqual(ARBITRARY_YPosition, testobj.coordinates)

