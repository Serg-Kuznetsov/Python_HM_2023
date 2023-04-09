# Задача №49. Решение в группах
# Создать телефонный справочник сивозможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилиючеловека)
# 4. Использование функций. Ваша программане должна быть линейной

import functions

while True:
    print ('1. Вывод, 2. Добавление, 3. Поиск 4. Удаление 5. Изменение')
    mode = int(input())
    if mode ==1:
        functions.show_data()
    elif mode == 2:
       functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.del_data()
    elif mode == 5:
        functions.change_data()
    else:
        break


# with open('book.txt','w', encoding='utf-8') as f:
#     f.write('ФИО , номер телефона')


# with open('book.txt','a', encoding='utf-8') as f:
#     f.write('\nФИО , номер телефона/ город')
    

# with open('book.txt','r', encoding='utf-8') as f:
#     print(f.read())