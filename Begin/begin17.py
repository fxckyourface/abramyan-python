# Begin17: Длины AC, BC и их сумма
# Ввод: a, b, c; каждое значение с новой строки.

a = float(input())
b = float(input())
c = float(input())

ac = abs(c - a)
bc = abs(c - b)
print(ac, bc, ac + bc)
