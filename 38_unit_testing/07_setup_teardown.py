import unittest

class TestDemo(unittest.TestCase):

    def setUp(self):
        print("Before Test")

    def tearDown(self):
        print("After Test")

    def test_demo(self):
        self.assertEqual(5, 5)

unittest.main()