# Boolean39: Ход ферзя
# Ввод: x1, y1, x2, y2; каждое значение с новой строки.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print(x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1))
