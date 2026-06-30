import unittest

class TestDemo(unittest.TestCase):

    def test_in(self):
        self.assertIn(
            "Govind",
            ["Govind", "Hari"]
        )

unittest.main()

# assertIn()
# ↓
# Value Collection માં
# છે કે નહીં
# તે Check કરે.