# If5: Количество положительных и отрицательных чисел
# Ввод: a, b, c; каждое значение с новой строки.

a = int(input())
b = int(input())
c = int(input())

positive = 0
negative = 0
if a > 0:
    positive += 1
elif a < 0:
    negative += 1
if b > 0:
    positive += 1
elif b < 0:
    negative += 1
if c > 0:
    positive += 1
elif c < 0:
    negative += 1
print(positive, negative)
