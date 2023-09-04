# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
# Напишите к ним классы исключения с выводом подробной информации. 
# Поднимайте исключения внутри основного кода. 
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.


class TriangleExistenceError(Exception):
    pass

class NegativeLengthError(TriangleExistenceError):
    pass

class CreationError(TriangleExistenceError):
    pass

class Triangle:

    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def triangle_definition(self):
            
            try:
                if (self.a <= 0 or self.b <= 0 or self.c <= 0):
                    raise NegativeLengthError
                elif(self.a > self.b + self.c or self.b > self.c + self.a or self.c > self.a + self.b):
                    raise CreationError

            except  NegativeLengthError:
                print(f'Нельзя создавать прямоугольник со сторонами: {self.a}, {self.b}, {self.c} отрицательной длины.')
            except CreationError:
                print(f'Треугольник со сторонами: {self.a}, {self.b}, {self.c} не существует.')

            else:
                if (self.a != self.b and self.b != self.c and self.c != self.a):
                    return f'Треугольник разносторонний'
                elif(self.a == self.b and self.b == self.c and self.c == self.a):
                    return f'Треугольник равносторонний'
                elif(self.a == self.c or self.c == self.b or self.a == self.b):
                    return f'Треугольник равнобедренный'


if __name__ == '__main__':        
    t1 = Triangle(4, 4, 4)
    print(t1.triangle_definition())