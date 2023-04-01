# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод: 3 3 2 12

l1 = int(input('Введите количество эелементов первого массива: '))
list1 = list()
for i in range(l1):
    x = int(input('Введите эелементы первого массива: '))
    list1.append(x)
print(list1)

l2 = int(input('Введите количество эелементов второго массива: '))
list2 = list()
for i in range(l2):
    y = int(input('Введите эелементы второго массива: '))
    list2.append(y)
print(list2)

list_new = list()


def result(list1, list2, list_new):
    for i in list1:
        if i not in list2:
            list_new.append(i)
    return list_new


print(result(list1, list2, list_new))


# a = [int(input()) for i in range(int(input()))]
# b = [int(input()) for j in range(int(input()))]
# c = [i for i in a if i not in b]
# c1 = []
# for i in a:
#     if i not in b:
#         c1.append(i)
# print(c,c1)
