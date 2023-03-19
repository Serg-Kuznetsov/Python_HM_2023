# list_1 = [] - создание пустого списка
# list_2 = list() - создание пустого списка

# list_1 = [7, 9, 11, 13, 17] - заполненный список

# prin(list_1) - вывод списка из list_1
# prin(*list_1) - вывод списка из list_1 без квадратных скобочек


# list_1 = [7, 9, 11, 13, 17]
# for i in list_1:
#     print(i) - вывод каждого элемента списка

# print (len(list_1)) - вывод количества элементов списка
# prin(list_1[0]) - печать первого элемента списка
# prin(list_1[-1]) - печать последнего элемента списка


# list_1 = [1,5]
# print (list_1)
# list_1.append(8) - добавление элемента в список в конец
# print (list_1)


# list_1 = [] - готовим список через цикл for
# print (list_1)
# for i in range(5):
#     list_1.append(i)
#     print (list_1)


# Удаление последнего элемента списка:
# list_1 = [7, 9, 11, 13, 17]
# print(list_1)
# list_1.pop() - удалить 17
# print (a) - вывести 17
# а = list_1.pop()
# print (list_1.pop()) - удаление и возвращение последнего элемента
# print(list_1)

# list_1 = [7, 9, 11, 13, 17]
# list_1.pop() - удалить последний элемент списка
# list_1.pop(1) - удалить элемент списка с индексом 1


# Добавление эелементов списка

# list_1 = [1,5]
# print (list_1)
# list_1.append(8) - добавление элемента в список в конец
# print (list_1)

# list_1 = [1,5]
# print (list_1.insert(2,11)) - в скобках указывается 1 - позиция элемента (индекс) 2 - значение элемента

# СРЕЗЫ

# list_1 = [1, 5, 2, 4, 6]
# print (list_1[0]) - вывод 1
# print (list_1[1]) - вывод 5
# print (list_1[len(list_1)-1])- печать последнего элемента списка
# prin(list_1[-1]) - печать последнего элемента списка
# prin(list_1[-2]) - печать второго с конца элемента списка
# print (list_1[:]) - печать всего списка с первого элемента
# print (list_1[:2]) - печать всего списка до второго индекса
# print (list_1[len(list_1)-2]:)- печать двух последних елементов списка
# print (list_1[1:2]) - печать с 1 по 3 элемент списка
# print (list_1[0:len(list_1)]:3) - печасть всего списка с первого элемента с шагом 3
# print (list_1[::3]) - печать всего списка с первого элемента с шагом 3


# КОРТЕЖИ - неизменяемые списки (более быстро работают, занимают меньшее места)

# t = () - создание пустого кортежа
# print(type(t)) - класс - tuple

# t = (1)
# print(type(t)) - класс - int

# t = (1, ) - для того, чтоб класс распозновался как кортеж, в конце обязателльно нужно оставлять запятую.
# print(type(t)) - класс - tuple


# v = [1, 2, 3]
# print(type(v)) - класс list - список

# v = tuple(v) - класс кортеж tuple - преобразовали в кортеж
# print(type(v))

# (((a = 1
# b = 2
# a, b = 1, 2))))

# a, b, c = v
# print (a,b,c)


# t = (1, 2, 3, 5,)
# print(t[1])
# for i in t:
#     print (i)

# for i in range(len(t)):
#     print (t[i])


# ### СЛОВАРИ

# # d = {} #- создание пустого словаря
# # d = dict () #- создание пустого словаря

# # d['q'] = 'qwert'  #- в нашем словаре есть ключ q, если по нему мы обратимся, мы получим qwert
# # print (d)

# # d['w'] = 'www'  #- в нашем словаре есть ключ q, если по нему мы обратимся, мы получим qwert
# # print (d['q']) # - вывод значения по ключу

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# # del dictionary['left'] # удаление элемента
# dictionary [895] = 98887789
# print (dictionary)

# for item in dictionary:
#     print ('{}: {}'.format(item, dictionary[item]))

#     print(item)

# for (k,v) in dictionary.items():
#     print (k,v) - к - ключ, v - значение

# print (dictionary.items()) - список, где каждый элемент - картеж из 2 элементов, ключ и значение ему принадлежащее в словаре


# МНОЖЕСТВА содержат только уникальные значения


# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # дабавление значения
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # Удаление из множества
# print(colors)

# # colors.remove('red') # KeyError: 'red' не может удалить значение, которого нет в множестве
# colors.discard('red') # Проверяет есть ли значение в множестве, если оно есть, то может удалить
# print(colors)
# colors.clear() # выводит пустое множество set ()
# print(colors)
# q = set() - создает пустое множество


# Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} - копируем в переменную С множество
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} - объеденяем множества A и B - получаем одно уникальное множество
# i = a.intersection(b) # i = {8, 2, 5} - найти пересечения в обоих множествах
# dl = a.difference(b) # dl = {1, 3} - найти уникальные значения в множестве A
# dr = b.difference(a) # dr = {13, 21} - найти уникальные значения в множестве B
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13} - объеденить два множества

# ## ЗАМОРОЖЕННОЕ МНОЖЕСТВО, множество, которе нельзя изменять

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


# ГЕНЕРАТОР СПИСКОВ

# #Простая ситуация — список:
# list_1 = [exp for item in iterable]

# #Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)

# print(list_1)  # [1, 2, 3,..., 100]

# #Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)]  # [1, 2, 3,..., 100]
# print(list_1)


# #2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0]# [2, 4, 6,..., 100]

# #Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]

# #Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]



### ОШИБКИ Профилирование и отладка
#Самые распространенные ошибки:

# #SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second 
#  print(number_first)
# # Отсутствие :


# #IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first)
# # Отсутствие отступов


# #TypeError(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа


# #ZeroDivisionError(Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя


# #KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует


# #NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существует


# #ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые значения
