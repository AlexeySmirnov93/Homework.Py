import unittest

from func_fib import fib

class TestFuncFib(unittest.TestCase):
    def test_expected_result(self):
        self.assertEqual(list(fib(5)), [0, 1, 1, 2, 3])

    def test_type_float(self):
        with self.assertRaises(TypeError):
            list(fib(5.1))

    def test_type_str(self):
        with self.assertRaises(TypeError):
            list(fib('s'))

    def test_valie_negative_number(self):
        with self.assertRaises(ValueError):
            list(fib(-5))

    def test_valie_border_number(self):
        with self.assertRaises(ValueError):
            list(fib(1))


if __name__ == "__main__":
    unittest.main(verbosity=10)