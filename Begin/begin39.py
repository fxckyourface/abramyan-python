# Begin39: Корни квадратного уравнения по возрастанию
# Ввод: a, b, c; каждое значение с новой строки.

a = float(input())
b = float(input())
c = float(input())

d = b * b - 4 * a * c
x1 = (-b - d ** 0.5) / (2 * a)
x2 = (-b + d ** 0.5) / (2 * a)
print(min(x1, x2), max(x1, x2))
