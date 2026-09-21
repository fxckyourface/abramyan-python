# If10: Замена переменных суммой или нулями
# Ввод: a, b; каждое значение с новой строки.

a = int(input())
b = int(input())

if a != b:
    total = a + b
    a = total
    b = total
else:
    a = 0
    b = 0
print(a, b)
