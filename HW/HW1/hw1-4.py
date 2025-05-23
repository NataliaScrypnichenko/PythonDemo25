# list comprehension
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#

print([i**2 for i in range(50) if i%2])

# function
#
#1 - створити функцію яка виводить ліст
# 2- створити функцію яка приймає три числа та виводить та повертає найбільше.
# 3- створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# 4- створити функцію яка повертає найбільше число з ліста
# 5- створити функцію яка повертає найменьше число з ліста
# 6- створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# 7- створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
#1
def new_list (list_): #1 - створити функцію яка виводить ліст
    for item in list_:
       print(item)

#2 # 2- створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_list (a,b,c):
    res =(max(a,b,c))
    print(res)# виводить
    return res # повертає

#3 створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def min_max (*args): # *args- приймає будь-яку кількість чисел
    print(max(args))#
    return min(args)
#4створити функцію яка повертає найбільше число з ліста
def max_num_list(List): #
   return max(List)

#5 створити функцію яка повертає найменьше число з ліста
def min_num_list(List):
    return min(List)

#6 створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_list(list_):
    return sum(list_)

# 7 створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень
def agv (list_):
    return sum(list_)/len(list_)