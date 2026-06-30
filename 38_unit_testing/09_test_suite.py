import unittest

class TestDemo(unittest.TestCase):

    def test_one(self):
        self.assertEqual(1,1)

suite = unittest.TestSuite()

suite.addTest(
    TestDemo("test_one")
)

runner = unittest.TextTestRunner()

runner.run(suite)