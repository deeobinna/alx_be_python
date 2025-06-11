import unittest
from simple_calculator import SimpleCalculator

class test_simple_calc_test(unittest.TestCase):
    def test_add(self):
        calc = SimpleCalculator()
        result = calc.add(5, 3)
        self.assertEqual(result, 8)
    
    def test_subtract(self):
        calc = SimpleCalculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        calc = SimpleCalculator()
        result = calc.multiply(5, 3)
        self.assertEqual(result, 15)

    def test_divide(self):
        calc = SimpleCalculator()
        result = calc.divide(6, 3)
        self.assertEqual(result, 2.0)

    def test_divide_by_zero(self):
        calc = SimpleCalculator()
        result = calc.divide(6, 0)
        self.assertEqual(result, "Error: Cannot divide by zero.")