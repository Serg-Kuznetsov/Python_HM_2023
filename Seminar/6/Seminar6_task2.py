# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5
# 1 2 3 4 5

# 5 Вывод: 0

# 1 5 1 5 1
# 0 Вывод: 0

# l1 = int(input('Введите количество эелементов массива: '))
# list1 = list()
# for i in range(l1):
#     x = int(input('Введите эелементы массива: '))
#     list1.append(x)
# print(list1)

# count = 0


# def sum(list1, count):
#     for i in range(1,len(list1)-1):
#         if list1[i-1] < list1[i] > list1[i+1]:
#             count += 1
#     return count


# print(sum(list1, count))



a = [int(input()) for i in range(int(input()))]
d=len([a[i] for i in range(1,len(a)-1) if a[i-1]<a[i]>a[i+1]])
count=0
for i in range (1,len(a)-1):
    if a[i-1]<a[i]>a[i+1]:
        count+=1
print(count,d)

