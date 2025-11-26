#import unittest and SimpleCalculator class from simple_calculator.py
from simple_calculator import SimpleCalculator
import unittest

class Test(unittest.TestCase):
    def test_addition(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.add)

    def test_subtraction(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.subtract)

    def test_multiplication(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.multiply)

    def test_division(self):
        calc = SimpleCalculator()
        self.assertEqual(self.calc.divide)
    