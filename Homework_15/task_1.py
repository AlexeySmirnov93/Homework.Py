# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.

import logging

FORMAT = '{levelname} - {asctime} {msg}'

logging.basicConfig(filename='student.log', encoding='utf-8', level=logging.INFO, filemode='a', format=FORMAT, style='{')

class Name_check:

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if not value.isalpha():
            error_message = 'ФИО должно содержать только буквы'
            logging.error(f'{error_message}. Введенное значение: {value}')
            raise ValueError(error_message)
        if not value.istitle():
            error_message = 'ФИО должно быть с заглавной буквы'
            logging.error(f'{error_message}. Введенное значение: {value}')
            raise ValueError(error_message)
        setattr(instance, self._name, value)

class Student:

    first_name = Name_check()
    middle_name = Name_check()
    last_name = Name_check()

    def __init__(self, last_name, first_name, middle_name):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        logging.info('Объект Student успешно создан')
        logging.info(f'Введенные данные: Фамилия: {last_name}, Имя: {first_name}, Отчество: {middle_name}')

    def __repr__(self) -> str:
        return f'ФИО: {self.last_name} {self.first_name} {self.middle_name}'

if __name__ == '__main__':
    try:
        name = Student('Смирнов', 'Алексей', 'Михайлович')
        print(name)
    except ValueError as e:
        logging.error(f'Произошла ошибка: {str(e)}')
