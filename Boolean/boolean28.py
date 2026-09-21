# Boolean28: Точка в первой или третьей четверти
# Ввод: x, y; каждое значение с новой строки.

x = float(input())
y = float(input())

print((x > 0 and y > 0) or (x < 0 and y < 0))
