# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


mystr = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea"
#mystr = mystr.upper()
print(mystr)
mystr = mystr.replace('.', ' ').split()
print(mystr)
mystr = [i.upper() for i in mystr]
set_mystr = set(mystr)
print(f'{len(set_mystr)}')



# a = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea".lower
# a= a.replace('.',' ')
# res= len(set(a.split()))
# print(res)