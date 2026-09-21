# Begin23: Перестановка A → B → C → A
# Ввод: a, b, c; каждое значение с новой строки.

a = float(input())
b = float(input())
c = float(input())

a, b, c = c, a, b
print(a, b, c)
