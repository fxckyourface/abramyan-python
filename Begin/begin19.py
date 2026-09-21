# Begin19: Периметр и площадь прямоугольника по вершинам
# Ввод: x1, y1, x2, y2; каждое значение с новой строки.

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

a = abs(x2 - x1)
b = abs(y2 - y1)
print(2 * (a + b), a * b)
