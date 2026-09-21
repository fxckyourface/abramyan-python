# Boolean40: Ход коня
# Ввод: x1, y1, x2, y2; каждое значение с новой строки.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = abs(x2 - x1)
dy = abs(y2 - y1)
print((dx == 1 and dy == 2) or (dx == 2 and dy == 1))
