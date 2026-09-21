# Boolean37: Ход короля
# Ввод: x1, y1, x2, y2; каждое значение с новой строки.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print(abs(x2 - x1) <= 1 and abs(y2 - y1) <= 1)
