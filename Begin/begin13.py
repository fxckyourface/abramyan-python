# Begin13: Площади двух кругов и кольца
# Ввод: r1, r2; каждое значение с новой строки.

r1 = float(input())
r2 = float(input())

pi = 3.14
s1 = pi * r1 ** 2
s2 = pi * r2 ** 2
print(s1, s2, s1 - s2)
