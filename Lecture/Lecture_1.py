# print (5)
# print(5,8,6)

# n=5
# print(n)
# n1=None # пустое значение
# print(n1)

# n=1
# print(type(n))
# n="qwerty"
# print(type(n))
# n='qwerty'
# print(type(n))


# n='фраза в "кавычках" вот'
# n='вывод кавычки \' нужен слеш'
# print(type(n))
# print(n)


# a = 5
# b = 5.89
# c = 'hello'
# print(a, b, c)
# print(f'{a} - {b} - {c}')
# print("{} - {} - {}".format(a, b, c))


# print('Введите первое число')
# a = input()
# print(a)


# print('Введите первое число')  # Ввод данных идет с новой строки
# a = int(input())
# b = int(input('Введиет второе число: '))  # Ввод данных идет в ТЕКУЩЕЙ СТРОКЕ
# print(a, ' + ', b, ' = ', a + b)


# c = 5.89
# print(c)
# print(type(c))
# c = int (c)
# print(c)
# print(type(c))
# c = str (c)
# print(c + '89!')
# print(type(c))

# c = 1
# print(c)
# print(type(c))
# c = bool (c)
# print(c)
# print(type(c))


# a=5.6565656
# b=5.23423424
# print(round(a*b,2))


# i = 2
# i += 3  # inter = i + 3
# i -= 4  # inter = i - 4
# i *= 5  # inter = i * 5
# i /= 6  # inter = i / 6


# a = 1 < 4 and 4 < 5
# print(a)

# a = 1==2 # == оператор равенства
# print(a)

# a= 1!=2 # == оператор НЕравенства
# print(a)

# a = "qwe"
# b = "qwe"
# print(a == b)

# a=1<3<5<10
# print(a)



# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, Маша!')
# elif username == 'Марина':
#     print('Ура, Марина!')
# else:
#     print('Привет,', username, '!')


# i = 0
# while i<5:
#     # if i ==3:
#     #     break # остановка цикла
#     i=i+1
# else:
#     print ('Пожалуй')
#     print ('хватит')
# print (i)


# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:  # если остаток от деления числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2:  # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1


# a = 'qwerty'
# print (a[0])

# for i in a:
#     print (i)



# line = ""
# for i in range(5):
#     line=""
#     for j in range(5):
#         line += "*"
#     print(line)



text = 'СъЕШЬ еще этих МяГкИх  французских булок'
print(len(text))  # длина текста в символах
print('еще' in text) # поиск текста (тру или фолс)
print(text.lower()) #все буквы в нижний регистр
print(text.upper()) #все буквы в верхний регистр
print(text.replace('еще', '***'))  # замена текста

print(text[:])  # вывести весь текст
print(text[:2])  # первые две буквы
print(text[-1])  # последняя буква
print(text[2:])  # со второй буквы до конца
print(text[2:-1])  # Со второго элемента до последнего с конца (без его учета)
print(text[0:len(text):6]) #Идем от начала текста до конца строки с шагом 6 т.е. вывод каждого шестого элемента
print(text[::6]) #тоже самое как и текст выше

text = text[2:8] + text[-6] + text[:6]
print(text)


