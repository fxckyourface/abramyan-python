# Boolean24: Квадратное уравнение имеет вещественные корни
# Ввод: a, b, c; каждое значение с новой строки.

a = float(input())
b = float(input())
c = float(input())

d = b * b - 4 * a * c
print(d >= 0)
