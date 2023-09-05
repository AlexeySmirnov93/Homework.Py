def fib(n):
    
    if n < 2:
        raise ValueError('The number n must be greater than 2')

    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b
