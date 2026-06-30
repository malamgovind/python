import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 10), 15)

unittest.main()

# test_add()
#         │
#         ▼
# add(5,10)
#         │
#         ▼
# 15
#         │
#         ▼
# assertEqual(15,15)
#         │
#    True ?
#    │      │
#  Yes      No
#  │         │
# PASS     FAIL