# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

a = (input('Введите шестизначный номер Вашего билета: '))
x1 = int(a[0])
x2 = int(a[1])
x3 = int(a[2])
x4 = int(a[3])
x5 = int(a[4])
x6 = int(a[5])
if x1+x2+x3 == x4+x5+x6:
    print('У Вас счстливый билет!')
else:
    print('Вам обязательно повезет, но в следующий раз...')
