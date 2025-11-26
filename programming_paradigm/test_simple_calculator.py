#import unittest and SimpleCalculator class from simple_calculator.py
from simple_calculator import SimpleCalculator
import unittest

class Test(unittest.TestCase):
    def test_addition(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtraction(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.subtract(5, 3), 2)
        self.assertEqual(calc.subtract(0, 0), 0)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        calc = SimpleCalculator()
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertIsNone(calc.divide(5, 0))
    