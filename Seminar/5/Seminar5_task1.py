# def tr (*args):
#     summ=0
#     for i in args:
#         summ+=i
#     return(summ)

# a= tr (3,4,3,4)
# print(a)

# Вычислить сколько раз укладывается число внутри в N

def recr(n, count =0):
    if n <0:
        return count-1
    elif n==0:
        return count
    return recr (n-3,count+1)

n = int(input())
print(recr(n))



