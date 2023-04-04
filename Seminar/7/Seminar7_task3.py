# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:
# values = [0, 2, 10, 6]
# Вывод: same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


# values = [0, 2, 10, 6]


# def same_by(characteristic, objects):
#     count = 0
#     for i in objects:
#         if i % 2 != 0:
#             count += 1
#     return count == 0


# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')


def same_by(characteristic, objects):
    return len(list(filter(characteristic, objects)))==0
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
