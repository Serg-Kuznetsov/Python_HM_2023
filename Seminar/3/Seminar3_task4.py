# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


n = int(input('Введите количество эелементов: '))
list1 = [int(input()) for i in range(n)]
count = 0
for i in range(len(list1)-1):
    if list1[i] < list1[i+1]:
        count += 1
print(count)


a = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        count += 1
print(count)
