# Напишите функцию для транспонирования матрицы 
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def func_matrix(matrix):
    temp = zip(*matrix)
    matrix_transpose = [list(i) for i in temp]
    return matrix_transpose

matrix = [[1, 2, 3], [4, 5, 6]]
print(func_matrix(matrix))