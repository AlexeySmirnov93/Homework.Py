import unittest

from func_fib import fib


RESULT = [0, 1, 1, 2, 3]

class TestFuncFib(unittest.TestCase):
    def test_expected_result(self):
        self.assertEqual(list(fib(5)), RESULT)

    def test_type_float(self):
        self.assertRaises(TypeError, "'float' object cannot be interpreted as an integer", fib, 5.1 )

    def test_type_str(self):
        self.assertRaises(TypeError, "'<' not supported between instances of 'str' and 'int'", fib, 's') 

    def test_valie_negative_number(self):
        self.assertRaises(ValueError, "The number n must be greater than 2", fib, -5)
        
    def test_valie_border_number(self):
        self.assertRaises(ValueError, "The number n must be greater than 2", fib, 1)
        

if __name__ == "__main__":
    unittest.main(verbosity=10)