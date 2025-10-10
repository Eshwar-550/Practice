import unittest
from reverse_str import reverse_string

class Test_reverse_str(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(reverse_string("hello"),"olleh")

    def test_empty(self):
        self.assertEqual(reverse_string(""),"")

    def test_string_with_space(self):
        self.assertEqual(reverse_string("Hello World"),"dlroW olleH")

if __name__ == '__main__':
    unittest.main()
