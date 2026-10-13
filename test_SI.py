
import unittest
from SI import simInt

class TestSI(unittest.TestCase):

    def test_simple_interest(self):
        self.assertEqual(simInt(1000, 5, 2), 100.0)

    def test_zero_principal(self):
        self.assertEqual(simInt(0, 5, 2), 0.0)

    def test_zero_interest(self):
        self.assertEqual(simInt(1000, 0, 2), 0.0)

    def test_zero_time(self):
        self.assertEqual(simInt(1000, 5, 0), 0.0)

if __name__ == "__main__":
    unittest.main()

