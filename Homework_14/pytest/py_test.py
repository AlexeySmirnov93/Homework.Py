import pytest

from func_fib import fib

RESULT = [0, 1, 1, 2, 3]

def test_expected_result():
    assert list(fib(5)) == RESULT

def test_type_float():
        with pytest.raises(TypeError):
            list(fib(5.1))

def test_type_with_text():
        with pytest.raises(TypeError, match=r"'float' object cannot be interpreted as an integer"):
            list(fib(5.1))

def test_type_str():
        with pytest.raises(TypeError):
            list(fib('s'))

def test_type_str_with_text():
        with pytest.raises(TypeError, match=r"'<' not supported between instances of 'str' and 'int'" ):
            list(fib('s'))

def test_valie_negative_number():
        with pytest.raises(ValueError):
            list(fib(-5))

def test_valie_negative_number_with_text():
        with pytest.raises(ValueError, match=r"The number n must be greater than 2" ):
            list(fib(-5))

def test_valie_border_number():
        with pytest.raises(ValueError):
            list(fib(1))


if __name__ == "__main__":
    pytest.main(['-v'])

