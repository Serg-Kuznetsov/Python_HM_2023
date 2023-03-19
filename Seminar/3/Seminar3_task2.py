# Задача №19. Решение в группах.
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


n = int(input('Введите количество эелементов: '))
list1 = [int(input()) for item in range(n)]
k = int(input('Введите сдвиг элементов: '))
for i in range(k):
    list1.append(list1.pop(0))
print(list1)


a = [1, 2, 3, 4, 5]
k = 3
part1 = a[:k]
part2 = a[k:]
list1 = part2+part1
print(list1)

a = [1, 2, 3, 4, 5]
k = 3
for i in range(k):
    a.insert(0, a.pop(-1))
print(a)
