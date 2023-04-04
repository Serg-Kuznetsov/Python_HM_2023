# Имеется список, заменить главные элементы нулями

a =[[1,2,3],[4,5,6],[7,8,9]]
for indOut,valOut in enumerate(a):
    for indIn,valIn in enumerate(valOut):
        if indIn == indOut:
                a[indOut][indIn] =0
print(a)
