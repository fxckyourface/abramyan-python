# Begin40: Решение системы двух линейных уравнений
# Ввод: a1, b1, c1, a2, b2, c2; каждое значение с новой строки.

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())

d = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / d
y = (a1 * c2 - a2 * c1) / d
print(x, y)
