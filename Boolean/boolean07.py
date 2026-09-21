# Boolean7: B строго между A и C
# Ввод: a, b, c; каждое значение с новой строки.

a = int(input())
b = int(input())
c = int(input())

print(a < b < c or c < b < a)
