# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

list1 = [1, 1, 2, 0, -1, 3, 4, 4]
a = set(list1)
print(len(a))

# вариант на семинаре:

n = int(input('Введите количество эелементов: '))
list1 = [int(input()) for item in range(n)]
list = set(list1)
print(len(list))


lnew = []
for i in list1:
    if i not in lnew:
        lnew.append(i)
print(len(lnew))
