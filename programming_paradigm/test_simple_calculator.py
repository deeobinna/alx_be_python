import unittest
from simple_calculator import SimpleCalculator

class test_simple_calc_test(unittest.TestCase):
    def test_addition(self):
        self.calc = SimpleCalculator()
        self.assertEqual(self.calc.add(5, 3), 8)
      
    
    def test_subtraction(self):
        self.calc = SimpleCalculator()
        self.result = self.calc.subtract(5, 3)
        self.assertEqual(self.result, 2)

    def test_multiply(self):
        self.calc = SimpleCalculator()
        self.result = self.calc.multiply(5, 3)
        self.assertEqual(self.result, 15)

    def test_divide(self):
        self.calc = SimpleCalculator()
        self.result = self.calc.divide(6, 3)
        self.assertEqual(self.result, 2.0)

    def test_divide_by_zero(self):
        self.calc = SimpleCalculator()
        self.result = self.calc.divide(6, 0)
        self.assertEqual(self.result, "Error: Cannot divide by zero.")