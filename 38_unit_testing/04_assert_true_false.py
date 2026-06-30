import unittest

class TestDemo(unittest.TestCase):

    def test_true(self):
        self.assertTrue(10 > 5)

    def test_false(self):
        self.assertFalse(5 > 10)

unittest.main()