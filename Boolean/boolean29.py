# Boolean29: Точка строго внутри прямоугольника
# Ввод: x, y, x1, y1, x2, y2; каждое значение с новой строки.

x = float(input())
y = float(input())
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(x1 < x < x2 and y2 < y < y1)
