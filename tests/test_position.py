from unittest import TestCase
from levelup.position import Position 

class TestXPosition(TestCase):
    def test_init(self):
        testdescription = "asdf"
        testobj = Position(testdescription)
        self.assertEqual(testdescription, testobj.Description)

