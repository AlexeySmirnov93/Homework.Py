# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

number = int(input('Введите число: '))
h = hex(number)

Hexdecimal_system = 16
binar = ''
while number != 0:
    res = str(number % Hexdecimal_system)
    binar = res + binar
    number //= Hexdecimal_system
print(f'Расчет с помощию кода: {binar}')
print(f'Расчет функцией hex: {(h[2:])}')