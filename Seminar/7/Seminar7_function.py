# Функции

# #-------------------- list comprehension
# #Старый способ
# a =[]
# b = list()
# for i in range 10:
#     b.append(i)

# # Новый способ
# a =[if i%2==0 else 0 i for i in range(1,10)]


# -------------------- Enumerade - выводит индексы и значения
# a = [1,2,4,6,8,3,5]
# for i, val in enumerate(a):
#     print(i,val)


# -------------------- ZIP объеденияет в один кортеж и проходится по нему
# a = (1,2,4,6,8,3,5) # Кортеж
# b ="asdasda" # Строка
# f ={45:'d',54:'s',33:'a'} # Словарь
# print (f.values())
# print (f.keys())
# print (f.items())
# #for keys, val in f.items():
# for i in zip(a,b,f):

#     print(i)


# --------------------LAMBDA

# def  summa(x,y):
#     return x+y

# summa = lambda x,y: x+y if x%2==0 else 0
# print (summa(8,6))


# --------------------MAP

# def pow(x):
#     return x**2


# # a = [i for i in range(1,6)]
# a = [1, 2, 3, 4, 5, 6]
# a = list(map(pow, a))
# print(a)


# --------------------Filter (оставляет или убирает из списка, тру или фолс)

# a = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda x: True if x%2==0 else False, a)) # x%2 - false__not x%2 - true
# print (a)


# -------------------- Сортировка по ключу
a = [(8, 2), (3, 9), (4, -1)]
a.sort(key=lambda x: x[1], reverse=True)
maxx = max(a, key=lambda x: x[1])
maxx1 = max(a)
print(maxx)
print(maxx1)
#sorted - сортировка кортежей ыщкеув (a, key=lambda.....)
