# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.


class Name_check:

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError('ФИО должно содержать только буквы')
        if not value.istitle():
            raise ValueError('ФИО должно быть с заглавной буквы')
        setattr(instance, self._name, value)

class Student:

    first_name = Name_check()
    middle_name = Name_check()
    last_name = Name_check()

    def __init__(self, last_name, first_name, middle_name):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name

    def __repr__(self) -> str:
        return f'ФИО: {self.last_name} {self.first_name} {self.middle_name}'


if __name__ == '__main__':  
     name = Student('Cмирнов','Алексей','Mихайлович')
     print(name)