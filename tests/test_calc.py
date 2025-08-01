import unittest

from src import calc

class CalcTests(unittest.TestCase):
    def test_sum1(self):
        res = calc.sum(5, 10)
        self.assertEqual(res, 15)

    def test_mul1(self):
        res = calc.mul(5, 10)
        self.assertEqual(res, 50)

if __name__ == "__main__":
    unittest.main()