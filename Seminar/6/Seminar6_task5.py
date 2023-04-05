# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105 . Программа должна вывести все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую пару не дает).

# Ввод: 300
# Вывод:220 284


# k = int(input('Введите число к: '))

# list1 = list()
# for i in range(k):
#     sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             sum += j
#     list1.append([i, sum])
# print(list1)


k = int(input('Введите число к: '))
lsum = []
for i in range(k):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    lsum.append([i, sum])
print (lsum)
res = []
for l1 in range(len(lsum)):
    for l2 in range(l1+1, len(lsum)):
        if lsum[l1][0] == lsum[l2][1] and lsum[l1][1] == lsum[l2][0]:
            res.append([lsum[l1][0], lsum[l2][0]])
print(*res)


# a= [[1,2],[3,4,6],[8,[9,0]]]
# print (a[0][1])
# print (a[1][2])
# print (a[2][1][0])