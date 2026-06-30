import unittest

def divide(a, b):
    return a / b

class TestDemo(unittest.TestCase):

    def test_error(self):

        with self.assertRaises(
            ZeroDivisionError
        ):
            divide(10, 0)

unittest.main()