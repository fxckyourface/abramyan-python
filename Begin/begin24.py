# Begin24: Перестановка A → C → B → A
# Ввод: a, b, c; каждое значение с новой строки.

a = float(input())
b = float(input())
c = float(input())

a, b, c = b, c, a
print(a, b, c)
