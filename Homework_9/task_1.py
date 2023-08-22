# Создать декоратор для использования кэша. 
# Т.е. сохранять аргументы и результаты в словарь, если вызывается функция с агрументами, 
# которые уже записаны в кэше - вернуть результат из кэша, если нет - выполнить функцию. 
# Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.

import json
from typing import Callable


def json_cache(func: Callable):
    try:
        with open(f'{func.__name__}.json', 'r') as data:
            result_dict = json.load(data)

    except FileNotFoundError:
        result_dict = {}


    def wrapper(*args):
        if result_dict.get('+'.join(map(str,args))):
            print(f"is cache: {(result_dict.get('+'.join(map(str,args))))}")
            return result_dict.get('+'.join(map(str,args)))
        else:                                 
            result_dict['+'.join(map(str,args))] = func(*args)
            with open(f'{func.__name__}.json', 'w') as data:
                json.dump(result_dict, data, indent= 4)
            return func(*args)
    return wrapper

@json_cache
def sum_args(*args):
    return sum(args)


if __name__ == "__main__":
    sum_args(1, 2, 3, 4)

