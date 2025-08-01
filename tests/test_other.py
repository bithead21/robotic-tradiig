import unittest

from src import calc

class CalcTests2(unittest.TestCase):
    def test_sum1(self):
        res = calc.sum(5, 32)
        self.assertEqual(res, 15)

    def test_mul1(self):
        res = calc.mul(5, 32)
        self.assertEqual(res, 50)

