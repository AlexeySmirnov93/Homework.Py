# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


one_fractional = input('Введите перовое дробное число в виде "a/b": ')
two_fractional = input('Введите второе дробное число в виде "c/d": ')

a = list(map(int, one_fractional.split('/')))
b = list(map(int, two_fractional.split('/')))

if a[1] == b[1]:

    addition_m = a[0] + b[0]
    addition_n = a[1]
    print(f'Натуральная сумма: {addition_m}/{addition_n}')
    print(f'Сокращенная сумма: {Fraction (addition_m,addition_n)}')

else:
    addition_m = a[0] * b[1] + b[0] * a[1]
    addition_n = a[1] * b[1]
    print(f'Натуральная сумма: {addition_m}/{addition_n}')
    print(f'Сокращенная сумма: {Fraction (addition_m,addition_n)}')

multiplication_m = a[0]*b[0] 
multiplication_n = a[1]*b[1]
print(f'Натуральное произведение: {a[0]*b[0]}/{a[1]*b[1]}')
print(f'Сокращенное произведение: {Fraction (multiplication_m,multiplication_n)}')

f1 = Fraction(a[0],a[1])
f2 = Fraction(b[0],b[1])
print(f'Проверка модулем fractions суммы: {f1 + f2}')
print(f'Проверка модулем fractions произведения: {f1 * f2}')