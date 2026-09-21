# Begin37: Расстояние при встречном движении автомобилей
# Ввод: v1, v2, s, t; каждое значение с новой строки.

v1 = float(input())
v2 = float(input())
s = float(input())
t = float(input())

print(abs(s - (v1 + v2) * t))
