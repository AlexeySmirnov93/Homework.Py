    Импорт функции
    >>> from func_fib import fib
    
    Проверка ОР
    >>> list(fib(5))
    [0, 1, 1, 2, 3]

    Проверка ошибки на вещественные числа
    >>> list(fib(5.1))
    Traceback (most recent call last):
    ...
    TypeError: 'float' object cannot be interpreted as an integer

    Проверка ошибки на ввод строки вместо числа
    >>> list(fib('s'))
    Traceback (most recent call last):
    ...
    TypeError: '<' not supported between instances of 'str' and 'int'

    Проверка ошибки на отритцательные числа
    >>> list(fib(-5))
    Traceback (most recent call last):
    ...
    ValueError: The number n must be greater than 2
    
    Проверка приграничного значения
    >>> list(fib(1))
    Traceback (most recent call last):
    ...
    ValueError: The number n must be greater than 2