#unit testing
import math
import unittest
from calculator import square_root, factorial, natural_logarithm, power

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-1)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_natural_logarithm(self):
        self.assertAlmostEqual(natural_logarithm(1), 0)
        self.assertAlmostEqual(natural_logarithm(math.e), 1)
        with self.assertRaises(ValueError):
            natural_logarithm(-1)

    def test_power(self):
        self.assertAlmostEqual(power(2, 3), 8)
        self.assertAlmostEqual(power(2, 0.5), math.sqrt(2))
        self.assertAlmostEqual(power(10, -1), 0.1)

if __name__ == '__main__':
    unittest.main()
