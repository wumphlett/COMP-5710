import unittest
import calculator

class TestCalc(unittest.TestCase):
    def testSanitize(self):
        self.assertEqual((4, 2), calculator._sanitize(4, 2))
        self.assertEqual((4, 2), calculator._sanitize(4., 2.))
        self.assertEqual((4, 2), calculator._sanitize("4", "2"))
        self.assertRaises(ValueError, calculator._sanitize, "a", "b")

    def testAdd(self):
        self.assertEqual(6, calculator.add(4, 2), "Addition operation for 4+2 is = 6")

    def testSubtract(self):
        self.assertEqual(2, calculator.subtract(4, 2), "Subtraction operation for 4-2 is = 2")

    def testMultiply(self):
        self.assertEqual(8, calculator.multiply(4, 2), "Multiply operation for 4*2 is = 8")

    def testDivide(self):
        self.assertEqual(2, calculator.divide(4, 2), "Divide operation for 4/2 is = 2")
        self.assertRaises(ZeroDivisionError, calculator.divide, 4, 0)


if __name__ == '__main__': 
    unittest.main() 