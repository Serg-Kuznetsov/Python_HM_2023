# Создайте список случайных чисел. Найдите номер его последнего локалного максимума
# (элмент, который больше любого из своих соседей).

import random

n = int(input('Введите количество эелементов: '))
list1 = [random.randint(-50, 50) for item in range(n)]
print(list1)
max = list1[0]
for i in range(1, len(list1)-1):
    if list1[i-1] < list1[i] > list1[i+1]:
        max = i
print(max)
