# Begin6: Объем и площадь поверхности параллелепипеда
# Ввод: a, b, c; каждое значение с новой строки.

a = float(input())
b = float(input())
c = float(input())

print(a * b * c, 2 * (a * b + b * c + a * c))
