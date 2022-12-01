
from QD44 import *
import unittest

class tests(unittest.TestCase):
    def test(self):
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(6),720)
        self.assertEqual(factorial(12),479001600)

        self.assertEqual(fibonacci(10),55)
        self.assertEqual(fibonacci(19),4181)
        self.assertEqual(fibonacci(1),1)

        self.assertTrue(palindrome_checker('malayalam'))
        self.assertFalse(palindrome_checker('geeks'))
        self.assertTrue(palindrome_checker('racecar'))


if __name__ == "__main__":
    unittest.main()