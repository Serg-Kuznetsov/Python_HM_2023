def show_data() -> None:  # Выводит информацию из справочника
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data() -> None:  # Добавляет информацию в справочник
    fio = (input('Введите ФИО: '))
    num = (input('Введите номер телефона: '))
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {num}')
    print('Информация добавлена')


def find_data() -> None:  # Осуществляет поиск по справочнику
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска: ')
    print(search(tel_book, data))


def search(book: str, info: str) -> str:  # Находит в строке записи по определенному критерию поиска
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])


def del_data() -> None:  # Осуществляет удаление записи
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    a = tel_book.split('\n')
    print(a)
    text = input('Введите данные для поиска и удаления: ')
    b = (search(tel_book, text))
    a[a.index(b)] = remove(b, text)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write('/n'.join(a))


def remove(text: str, remove_text: str) -> str:
    if remove_text.isalpha():
        num = text.split(' | ')[1]
        return f' | {num}'
    else:
        fio = text.split(' | ')[0]
        return f'{fio} | '


def change_data() -> None:  # Вносит изменения в справочник
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    a = tel_book.split('\n')
    print(a)
    text = input('Введите новую фамилию: ')
    b = (search(tel_book, text))
    a[a.index(b)] = edit(b)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write('/n'.join(a))


def edit(text: str) -> str:
    fio = input('Введите фамилию, которую нужно изменить: ')
    num = input('Введите номер, который нужно изменить: ')
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    else:
        num = text.split(' | ')[1]
    return f'{fio} | {num}'
