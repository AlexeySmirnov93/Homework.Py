# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
# и возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# И весь период действует григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


import sys
import time


def validate_date(date):
    try:
        time.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False


def _check_leap_year(date):
    d,m,y = (int(i) for i in date.split('.')) 
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    return False
   

if __name__ == '__main__':
    task, date = sys.argv
    print(validate_date(str(date)))
    print(_check_leap_year(str(date)))