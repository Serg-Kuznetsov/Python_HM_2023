# Создайте список из случайных чисел. Найдите сторой максимум.

import random

n = int(input('Введите количество эелементов: '))
list1 = [random.randint(-50, 50) for item in range(n)]
print(list1)
list1.sort()
print(list1[-1])
print(list1[-2])

# max1 = list1[0]
# max2 = list1[0]
# for i in list1:
#     if i>max1:
#         max1 = i


#print(max1)
