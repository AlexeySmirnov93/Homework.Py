# Возьмите 1-3 любые задания из прошлых семинаров, которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра. (Например: Треугольник дз1, дроби дз2)


import os
import json


class Direct:
    def __init__(self, names: str, result= []):
        self.names = names
        self.result = result
        
    def this_repository(self):
        for _, dirs, files in os.walk(self.names):
            for name in files:
                self.result.append({'name': name.rpartition('.')[0],
                                'extension': '.' + name.rpartition('.')[-1],
                                'type': 'file'})
            for name in dirs:
                self.result.append({'name': name,
                                'type': 'directory'})        
        
        with open('out.json', 'w') as js_file:    
            json.dump(self.result, js_file, indent= 4)

direct = Direct('d:/deepening in python/Homework/Homework_8')
direct.this_repository()