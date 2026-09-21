# Boolean33: Существование треугольника
# Ввод: a, b, c; каждое значение с новой строки.

a = int(input())
b = int(input())
c = int(input())

print(a + b > c and a + c > b and b + c > a)
