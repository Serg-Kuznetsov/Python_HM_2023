# Задача №21. Решение в группах.
# Напишите программу для печати всех уникальных значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

dictionary = {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ": " S009 "}, {" VIII": " S007 "}
list1 = []
for i in range(len(dictionary)):
    list1 += dictionary[i].values()
print(set(list1))


res = set([value.strip() for dct in dictionary for value in dct.values()])
print(*res)

res = []
for dct in dictionary:
    for value in dct.values():
        res.append(value.strip())
