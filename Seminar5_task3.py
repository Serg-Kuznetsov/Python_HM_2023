# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def hak (a):
    print (a)
    min=a[0]
    max=a[0]
    for i in range(len(a)):
        if a[i]>max:
            max=a[i]
        elif a[i] < min:
            min=a[i]
    for j in range(len (a)):
        if a[j]==max:
            a[j]=min
    return a

    
a=[]
n = int(input())
for i in range(n):
    a.append(int(input()))
print (hak(a))
