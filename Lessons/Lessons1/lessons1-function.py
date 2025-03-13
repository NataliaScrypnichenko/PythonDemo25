def fun(name, age=4,*args, **kwargs):
    print('Hello', name,age)
    print(args)
    print(kwargs)
fun('Michael', 55, 'KARINA',True,100, name_='Oleg', house=55)

def fun(a,b,c):
    print( a,b,c)
l=[1,6,3]
fun(*l)


#*args =можна додавати будь що
# **kwargs=іменновані параметри,і будуть словниками

# 1️⃣ Приклад простої функції
def fun():
    print("Hello, world!")
fun()  # Викликаємо функцію #Hello, world!
# ✅ Що тут відбувається?
# def fun(): — створюємо функцію fun, яка друкує "Hello, world!".
# fun() — викликаємо функцію.
# 2️⃣ Функція з параметрами-✅ Тут функція приймає один параметр name, і ми передаємо різні значення.
def fun(name):
    print(f"Hello, {name}!")
fun("Alice")  # Hello, Alice!
fun("Bob")    # Hello, Bob!
# 3️⃣ Функція, що повертає значення (return) ✅ return дозволяє повернути результат роботи функції.
def fun(a, b):
    return a + b
result = fun(5, 3)
print(result)  # 8
# 4️⃣ Функція з аргументом за замовчуванням✅ Якщо аргумент не передано, використовується "Guest".
def fun(name="Guest"):
    print(f"Hello, {name}!")

fun()         # Hello, Guest!
fun("John")   # Hello, John!
# 5️⃣ Функція з довільною кількістю аргументів (*args)✅ *args збирає позиційні аргументи у кортеж.
def fun(*args):
    print(args)
fun(1, 2, 3, "Hello")  # (1, 2, 3, 'Hello')
# 6️⃣ Функція з іменованими аргументами (**kwargs) ✅ **kwargs збирає іменовані аргументи у словник.
def fun(**kwargs):
    print(kwargs)
fun(name="Alice", age=25)  # {'name': 'Alice', 'age': 25}
# 🔥 Висновок
# Функція	    Опис
# def fun():	   Оголошення функції
# fun()	            Виклик функції
# def fun(a, b):	Функція з аргументами
# return	        Повернення значення
# *args          	Довільна кількість позиційних аргументів
# **kwargs	        Довільна кількість іменованих аргументі

# 🔹 Функції допомагають оптимізувати код та уникнути повторень!

# 1️⃣ Функція з кількома аргументами ✅ Функція приймає три аргументи та повертає їхню суму.
def add(a, b, c):
    return a + b + c
result = add(2, 5, 8)
# print(result)  # 1
# 2️⃣ Функція з декількома поверненнями ✅ return може повертати кілька значень у вигляді кортежу.
def get_values():
    return 10, 20, 30  # повертає кортеж

x, y, z = get_values()
print(x, y, z)  # 10 20 30
# 3️⃣ Функція з *args (необмежена кількість аргументів)✅ *args дозволяє передавати будь-яку кількість чисел у функцію.
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply(2, 3, 4))  # 24
print(multiply(5, 6))     # 30
# 4️⃣ Функція з **kwargs (іменовані аргументи) ✅ **kwargs збирає всі іменовані аргументи у словник
def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Alice", age=30, city="Kyiv")
# name: Alice
# age: 30
# city: Kyiv

# 5️⃣ Рекурсивна функція (факторіал числа) ✅ Рекурсія – це коли функція викликає сама себе.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # 120
# 6️⃣ Функція як аргумент іншої функції # ✅ Тут ми передаємо функцію як аргумент.
def square(x):
    return x * x
def apply_function(func, value):
    return func(value)
print(apply_function(square, 5))  # 25

#
# 7️⃣ Функція з lambda # ✅ lambda – це анонімна функція (коротка функція без def).
add = lambda x, y: x + y
print(add(3, 4))  # 7
# 8️⃣ Функція з map() # ✅ map() застосовує функцію до кожного елемента списку.
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))

print(squared)  # [1, 4, 9, 16]
# 9️⃣ Функція з filter() # ✅ filter() залишає тільки ті елементи, які відповідають умові.
numbers = [10, 25, 3, 45, 6]
filtered = list(filter(lambda x: x > 10, numbers))

print(filtered)  # [25, 45]

# 🔟 Вкладена функція # ✅ Функція може містити іншу функцію всередині.
def outer_function():
    def inner_function():
        return "Hello from inner!"
    return inner_function()

print(outer_function())  # Hello from inner!
# 🔥 Висновок
# Концепція	Опис
# *args	Передача необмеженої кількості аргументів
# **kwargs	Передача іменованих аргументів
# return	Повернення значень
# lambda	Анонімні функції
# map()	Функція для перетворення списку
# filter()	Функція для фільтрації списку
# Рекурсія	Функція викликає сама себе



# розтановка значення


