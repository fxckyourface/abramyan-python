# Begin22: Обмен значениями A и B
# Ввод: a, b; каждое значение с новой строки.

a = float(input())
b = float(input())

a, b = b, a
print(a, b)
