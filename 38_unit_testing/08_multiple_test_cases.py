import unittest

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2+3, 5)

    def test_sub(self):
        self.assertEqual(5-2, 3)

unittest.main()