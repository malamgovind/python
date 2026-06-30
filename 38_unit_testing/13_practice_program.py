import unittest

def square(x):
    return x*x

class TestSquare(unittest.TestCase):

    def test_square(self):
        self.assertEqual(
            square(5),
            25
        )

unittest.main()