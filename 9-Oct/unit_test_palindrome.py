import unittest
from palindrome import is_palindrome

class Test_is_palindrome(unittest.TestCase):

    def test_madam(self):
        self.assertTrue(is_palindrome("madam"))

    def test_empty(self):
        self.assertTrue(is_palindrome(""))

    def test_python(self):
        self.assertFalse(is_palindrome("python"))

    def test_Racecar(self):
        self.assertTrue(is_palindrome("Racecar"))

    def test_single_char(self):
        self.assertTrue(is_palindrome("T"))

    def test_string_with_space(self):
        self.assertTrue(is_palindrome("Taco cat"))

if __name__ == '__main__':
    unittest.main()
