
# 4) створити декоратор котрий буде підраховувати скільки разів була запущена
# функція продекорована цим декоратором, та буде виводити це значення після виконання функцій

def cuont_decor(func):
    cuont = 0 # скілтки раз викликають лічильник

    def inner(*args, **kwargs): #викликаємо ф
        nonlocal cuont # передаємо
        cuont += 1
        inner(f'{cuont=}') # викликаємо ф
    return inner # повертаємо

@cuont_decor
def func1():
    print('func1')

@cuont_decor
def func2():
    print('func2')

func1()
func2()
func1()
func2()
func1()
func2()