# Создайте класс Матрица. 
# Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц

import numpy as np

class Matrix:

    """~ Работа с матрицами ~"""

    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def __eq__(self, other)-> bool:
        return f'Результат сравнения: \n{self.matrix == other.matrix}\n'
    
    def __add__(self, other):
        result = np.array(self.matrix) + np.array(other.matrix)
        return f'Результат сложения: \n{result}\n'
    
    def __mul__(self, other):
        result = np.multiply(self.matrix, other.matrix)
        return f'Результат умножения: \n{result}\n'
    

m1 = Matrix([[2, 2],[5, 5]])
m2 = Matrix([[2, 2],[5, 5]])
print(Matrix.__doc__)
print()
print(m1 == m2)
print(m1 + m2)
print(m1 * m2)
