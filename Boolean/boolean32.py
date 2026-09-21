# Boolean32: Треугольник прямоугольный
# Ввод: a, b, c; каждое значение с новой строки.

a = int(input())
b = int(input())
c = int(input())

print(a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a)
