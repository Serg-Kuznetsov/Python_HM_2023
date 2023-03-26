# def sumnumbers(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

# print (sumnumbers(5))

# def sumstr(*args):
#     res = ''
#     for i in args:
#         res+=i
#     return res
# print (sumstr('q','e','r'))
# print (sumstr('q','e','r','t','y'))


########## ВЫЗОВ МОДУЛЕЙ
# import modul1
# print (modul1.max1(5,9))

# from modul1 import max1
# print (max1(89,9))

# from modul1 import*
# print (max1(79,9))

# import modul1
# print (modul1.max1(69,9))

# import modul1 as m1
# print (m1.max1(59,9))



# def fib (n):
#     if n in [1,2]:
#         return 1 
#     return fib(n-1) + fib (n-2)
# list1 = []
# for i in range(1,10):
#     list1.append(fib(i))
# print(list1)



# ##### БЫСТРАЯ СОРТИРОВКА
# def quick_sort (array):
#     if len(array)<=1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort (less) + [pivot] + quick_sort (greater)
# print (quick_sort([10,5,2]))





# ##### СОРТИРОВКА СЛИЯНИЕМ
def merge_sort(nums):
    if len(nums)>1:
        mid=len(nums) // 2 
        left = nums [:mid]
        right = nums [mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i < len(left) and j < len (right):
            if left[i]<right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1
list1 = [1,5,6,9,7,1,5,8,111,1,1,22]
merge_sort(list1)
print (list1)