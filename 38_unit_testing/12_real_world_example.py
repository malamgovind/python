import unittest

def login(password):
    return password == "admin"

class TestLogin(unittest.TestCase):

    def test_login(self):
        self.assertTrue(
            login("admin")
        )

unittest.main()