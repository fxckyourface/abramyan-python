# Boolean35: Шахматные поля одного цвета
# Ввод: x1, y1, x2, y2; каждое значение с новой строки.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print((x1 + y1) % 2 == (x2 + y2) % 2)
