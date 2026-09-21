# If9: Меньшее значение в A, большее в B
# Ввод: a, b; каждое значение с новой строки.

a = float(input())
b = float(input())

if a > b:
    a, b = b, a
print(a, b)
