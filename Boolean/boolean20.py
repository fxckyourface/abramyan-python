# Boolean20: Три цифры различны
# Ввод: n; каждое значение с новой строки.

n = int(input())

a = n // 100
b = n // 10 % 10
c = n % 10
print(a != b and a != c and b != c)
