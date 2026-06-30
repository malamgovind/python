import unittest

class TestDemo(unittest.TestCase):

    def test_one(self):
        self.assertEqual(10,10)

runner = unittest.TextTestRunner()

runner.run(
    unittest.makeSuite(TestDemo)
)