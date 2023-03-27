# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0= 0, a1= 1, ak= ak-1 + ak-2 (k > 1).Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 21

def fib(n):
    a = 0
    a1 = 1
    summ = 0
    for i in range(2, n):
        summ = (a+a1)
        a = a1
        a1 = summ
    return summ


n = int(input())
print(fib(n))
