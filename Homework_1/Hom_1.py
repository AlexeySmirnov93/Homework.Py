# 1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = 2
b = 3
c = 4

if (a + b > c and a + c > b and b + c > a):
    if (a != b and b != c and c != a):
        print('треугольник разносторонний')
    elif(a == b and b == c and c == a):
        print('треугольник равносторонний')
    elif(a == c or c == b or a == b):
        print('треугольник равнобедренный')
else:
    print('Треугольник не существует')    
