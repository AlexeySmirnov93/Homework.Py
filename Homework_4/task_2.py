# Напишите функцию принимающую на вход только ключевые параметры(kwargs) 
# и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}


def reverse_kwargs(**kwargs):
    return {v if v.__hash__ is not None else str(v):k for k,v in kwargs.items()}
 
print(reverse_kwargs(rev=True, acc="YES", stroka=4))