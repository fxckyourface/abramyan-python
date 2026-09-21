# Integer29: Количество квадратов и свободная площадь
# Ввод: a, b, c; каждое значение с новой строки.

a = int(input())
b = int(input())
c = int(input())

count = (a // c) * (b // c)
free_area = a * b - count * c * c
print(count, free_area)
