# Boolean14: Ровно одно число положительное
# Ввод: a, b, c; каждое значение с новой строки.

a = int(input())
b = int(input())
c = int(input())

print((a > 0) + (b > 0) + (c > 0) == 1)
