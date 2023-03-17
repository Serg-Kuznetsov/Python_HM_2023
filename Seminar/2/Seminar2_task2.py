# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6

# 0 1 1 2 3 5 8 13

n = int(input('Введите натуральное число: '))
n0 = 0
n1 = 1
cur_num = n0+n1
count = 2
while cur_num < n:
    cur_num = n0+n1
    n0 = n1
    n1 = cur_num

    count += 1
if cur_num ==n:
    print (count)
else:
    print(-1)

# f1 = f2 = 1
# f = f2
# i = 3
# while a > f:
#     f = f1+f2
#     f1 = f2
#     f2 = f
#     i += 1
# if a == f:
#     print(f' Номер позии: {i}')
# else:
#     print(-1)