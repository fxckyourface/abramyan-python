# Begin35: Путь лодки по озеру и против течения
# Ввод: v, u, t1, t2; каждое значение с новой строки.

v = float(input())
u = float(input())
t1 = float(input())
t2 = float(input())

s = v * t1 + (v - u) * t2
print(s)
