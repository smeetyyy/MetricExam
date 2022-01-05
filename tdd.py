import math
import unittest
from mathfunction import *

class TestMathFunction(unittest.TestCase):
    "This tests whether the parameter is missing"
    def test_missing_param(self):
        with self.assertRaises(TypeError):
            self.assertEqual(math.modf(), True)
        with self.assertRaises(TypeError):
            self.assertEqual(math.modf(''), True)

    "This tests whether the parameter for x is wrong"
    def test_wrong_param(self):
        with self.assertRaises(TypeError):
            math.modf('Wrong String')

    def test_expected_value(self):
        self.assertEqual(math.modf(12), (0.0, 12.0), True)


if __name__ == '__main__':
    unittest.main()
