# # def f(x):
# #     return x*x
# # print (f(5))
# # a=f
# # print (type(f))
# # print (a(5))


# def calk1(a,b):
#     return a+b

# def calk2(a, b):
#     return a*b

# def math (op, x,y):
#     print (op(x,y))

#--------------------------- # ЛЯМДА ФИНКЦИИ
# #calc(lambda x, y: x + y, 4, 5) # 9

# # def calk1(a,b):
# #     return a+b

# calk1 = lambda a,b: a + b 

# math (lambda a,b: a + b , 5,45)
# math (calk2, 5,45)


# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = list()
# for i in data :
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)




# data1 = [1, 2, 3, 5, 8, 15, 23, 38]
# # def select(f,col):
# #         return[f(x) for x in col]

# def where (f, col):
#      return [x for x in col if f(x)]
# res = map(int,data1)
# print(res)
# res = where(lambda x: x%2 ==0, res)
# print(res)
# res = list(map(lambda x: (x,x**2),res))
# print(res)
#--------------------------- #

# list1= [x for x in range(1,20)]
# print (list1)
# list1 = list(map(lambda x: x+10, list1))
# print (list1)

# .split() - преобразование строки в список .split(", ") замена разделителя
# data = '15 156 96 3 5 8 52 5'
# print (data)
# # data = data.split()
# # print (data)

# data = list(map(int, data.split()))
# print (data)


# data = [15, 65, 9 ,36 ,175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)


# data1 = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map (int,data1)
# res = filter(lambda x: x%2 ==0, res)
# res = list(map(lambda x: (x,x**2),res))
# print(res)



# Пример:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]




# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users)
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]



# 1. Режим a
# colors = ['red', 'green', 'blue']
# data = open('Lecture4_file.txt', 'a', encoding='utf-8') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

#1.Ещё один способ записи данных в файл:
# with open('Lecture4_file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')



#2. Режим r Чтение данных из файла:
# path = 'Lecture4_file.txt'
# data = open('Lecture4_file.txt', 'r')
# for line in data:
#     print(line)
# data.close()






# Познакомимся с базовыми функциями данного модуля:
# ● os.chdir(path) - смена текущей директории.
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')

# ● os.getcwd() - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'


# os.path - является вложенным модулем в модуль os и реализует некоторые полезные функции для работы с
# путями, такие как:
# ○ os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #'main.py'
# ● os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'



