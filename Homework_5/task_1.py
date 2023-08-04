# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ('c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')


import os


def get_path_parse(text_path):
    path, file_extension = os.path.splitext(text_path)
    dirname, filename = os.path.split(path)
    return (dirname, filename, file_extension)


text = 'c:/Users/Vladislav/Desktop/deep_to_python/test.txt'
print(text)
print(get_path_parse(text))