# Напишите функцию, которая сереализует содержимое текущей директории в json-файл. 
# В файле должен храниться список словарей, словарь описывает элемент внутри директории: имя, расширение, тип. 
# Если элемент - директория, то только тип и имя. Пример результата для папки, где лежит файл test.txt и директория directory_test:


import os
import json


def direct(path):
    results = []
    for _, dirs, files in os.walk(path):
        for name in files:
            results.append({'name': name.rpartition('.')[0],
                            'extension': '.' + name.rpartition('.')[-1],
                            'type': 'file'})
        for name in dirs:
            results.append({'name': name,
                            'type': 'directory'})        
    
    with open('out.json', 'w') as js_file:
         json.dump(results, js_file, indent= 4)


direct('Homework_8')