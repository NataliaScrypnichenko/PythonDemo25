# # єкстенди наслідування класів (від класа User щоб зявився дочерний клас= дочерній батьківський )
# class User:
#     count = 0  # він відноситься, до самого класу і належать йому
#
#     def __init__(self, name, age):
#         self.__name = name  # робиться приватними змінні (__name__)
#         self._age = age
#
#     def get_name( self):  # якщо я хочу доступ, то є доступ до __name через метод get_name і можна зробити його приватним __get_name
#         return self.__name
#
# user = User('Max', 15)
#
# class Tools:
#     def greeting(self):
#         print("Hello ")
#
#     def go_to_home(self):
#         print("Welcome to home")
#
#
# class Car:
#     def start(self):
#         print("Welcome to car")
#
#
# class Parent(User, Tools, Car): # наслідування через, круглі душки= дочерній батьківськи
#     def __init__(selff, name, age,status):  # підчеркнутий і каже що потрібно звернутися до ініта супер клас і можна вказувати свої поля
#         super().__init__('Max', 15) # підставляє всі поля цього класу і викликає його
#         selff.status = status # тепер є наслідувальний клас
#     def get_status(self):
#         return self.status
#
# # в пайтоні можна наслідуати від декількох класів, але є нюанси коли робимо МН то будемо за звичай + якийсь функціонал наприклад class Tools і
# # class Car і Їх фунції (greeting, go_to_home, start)які розширюють Parent тобто можна розкачувати і додавати функціонал в клас,
# # що за чим запускається то з ліва на право (User, Tools, Car)
#
# parent=Parent ('Oleh', 24 , True)
# parent.go_to_home() # унаслідованя від Tools
# parent.greeting()
# print(parent.get_status())
# parent.start()

''' інкапсуляція'''
from abc import ABC

''' це був самий простий варіант, а коли багата то він може запутати 
class User:
    def __init__(self, name):
        self.__name = name # доступ закрили, але умовно можемо давати доступ до неї(гетерах будемо повіряти можно віддавати)а в сетах чи можна за сетити нове значення

    def get_name(self, password): # відкрили
        if password == '111111': #якщо то ...
            return self.__name #  то повертаємо
        return 'Error' # якщо ні то повернемо ерор

    def set_name(self, name): # приймаємо name і перезаписуємо зміну
        self.__name = name
        
    def del_name(self): # можемо видалити
        del self.__name # за допомогою нього можна видаляти із масиву, дікшері, і поля класів
    


user = User('Max') # ств.єкземпляр класу
print(user.set_name('Nata')) # замінила
#user.del_name() # не існує name
print(user.get_name('jdkdl')) # Error
print(user.get_name('111111')) # Max # взагалі задумка була тому, що можна було контролювати віддавати чи ні '''

# коли багато робимо приватними(__) може бути багато змінних якщо в блок __init__(self, name багато змінних .......)
# class User:
#     def __init__(self, name):
#         self.__name = name  # доступ закрили, але умовно можемо давати доступ до неї(гетерах будемо повіряти можно віддавати)а в сетах чи можна за сетити нове значення
#     @property # це є декоратор і ф-я (часто користуватися)
#     def name(self):  # також декоратор
#             return self.__name  # то повертаємо
#     @name.setter  # це робиться якщо є декоратор
#     def name(self, name):  # приймаємо name і перезаписуємо зміну
#         self.__name = name
#     @name.deleter
#     def name(self):  # можемо видалити
#         del self.__name  # за допомогою нього можна видаляти із масиву, дікшері, і поля класів
#
# #ств.зміну property і в середині вказуємо ф-її Які відповідають за конкретні речі, але передаємо як функцію
# #(не пишемо це)    name = property(fget=__get_name, fset=__set_name, fdel=__del_name) # тепер можемо звертатися до user=name і роздрукувати його(це декщратор)
#
# user = User('Max')
# #user. # нічого не бачимо то створювали ...property
# print(user.name) # Max
# user.name= 'Albina'
# print(user.name) # Albina
# # del user.name
# # print(user.name) # no!не має

'''Поліморфізм '''
'''Поліморфізм у Python — це принцип об'єктно-орієнтованого програмування, який дозволяє використовувати один і
 той самий інтерфейс для різних типів об'єктів.
 Поліморфізм — це коли одна і та ж функція або метод може працювати з об'єктами різних класів, і кожен клас реалізує її по-своєму.
 class Cat:
    def speak(self):
        return "Мяу!"

class Dog:
    def speak(self):
        return "Гав!"

def animal_sound(animal):
    print(animal.speak())

cat = Cat()
dog = Dog()

animal_sound(cat)  # Мяу!
animal_sound(dog)  # Гав!

✅ Обидва класи мають метод speak(), і ми можемо викликати його через одну й ту саму функцію animal_sound, не знаючи, який саме тип об'єкта.
 '''
'''class Shape: # фігура # батько основна фігура від якої всі класи наслідуються
    def area(self): # метод площина
        print('Area', end= ': ')

    def perimeter(self): # периметр
        print('Perimeter', end= ': ')

class Triangle(Shape): # треугольник
    def __init__(self, a, b, c): # три сторони
        self.a = a
        self.b = b
        self.c = c

    # наслідують площину і периметр (є по замовчувані) але ми можемо ці методи переписати (оврайдети),
    # якщо натиснемо там де пишеться (def) ctrl+O то побачимо від чого мій клас наслідується
    def area(self):
        super().area() # super()- це показує звернення до класу якого наслідуємо area()-це його метод
        print((self.a * self.b * self.c))

    def perimeter(self):
        super().perimeter()
        print((self.a + self.b + self.c))

class Rectangle(Shape): # прямоугольник
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        super().area()
        print((self.a * self.b))

    def perimeter(self):
        super().perimeter()
        print((self.a + self.b))


triangle = Triangle(4, 5, 6)
triangle.area() # 120
triangle.perimeter() # 15

rectangle = Rectangle(4, 5)
rectangle.area() # 20
rectangle.perimeter() # 9
#можемо сказати що це масив Shape і можумо їх типізувати як список -> класи також можуть виступати типами записати їх як масив
shapes:list[Shape] = [
    rectangle,
    triangle,
    Triangle(9, 10, 11),
    Rectangle(5, 6),
]
for shape in shapes:
    shape.area()
    shape.perimeter() '''

# ускладнюємо

'''from abc import ABC, abstractmethod

class Shape(ABC):  # фігура зараз буде наслідуватися від (ABC)- це тепер дало заборону на створення екземпляра класу
                   # (shape)= тому, що це абстрактна річ яка має в собі якийсь функціонал
    @abstractmethod #
    def area(self):  # метод площина
        pass
    @abstractmethod
    def perimeter(self):  # периметр
        pass
# це означає якщо наслід. від Shape-це тобто я маю реалізувати його методи абстрактні обов'язково,
# якщо якийсь метод пропустила, то в класі видасть помилку і буде помилка
class Triangle(Shape):  # треугольник
    def __init__(self, a, b, c):  # три сторони
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a * self.b * self.c

    def perimeter(self):
        return self.a + self.b + self.c

class Rectangle(Shape):  # прямоугольник
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return self.a + self.b

triangle = Triangle(4, 5, 6)

rectangle = Rectangle(4, 5)

# можемо сказати що це масив Shape і можумо їх типізувати як список -> класи також можуть виступати типами записати їх як масив
shapes: list[Shape] = [
    rectangle,
    triangle,
    Triangle(9, 10, 11),
    Rectangle(5, 6),
]
for shape in shapes:
    print(shape.area())
    print(shape.perimeter())

# але тут виходить нам None, але щоб такого не було то використовуємо абстрактні класи то імпортуємо (from abc import ABC, abstractmethod)'''

# є ще декоратори.Декоратори в Python — це спеціальні функції, які дозволяють додавати нову функціональність до існуючих
# функцій або методів без зміни їх коду. Це один із ключових інструментів метапрограмування в Python.
#Декоратор — це функція, яка приймає іншу функцію як аргумент, щось із нею робить (наприклад, обгортає в нову логіку), і повертає нову функцію.
# Декоратори — це потужний спосіб розширити поведінку функцій без зміни їх коду.
# Вони базуються на тому, що в Python функції — це об’єкти, які можна передавати, повертати та обгортати.
'''метод самого класу User '''
# class User:
#     __count = 0 # в отримані змінні він знадобитися
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
# # викликаємо метод не від екземпляру класу, а від імені самого класу.потрібно використати(@classmethod)
#     # self-характеристика екземпляру
#     # @classmethod
#     # def hello(cls):# slc-це заміна цього (User)
#     #     print('Hello')
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#     @staticmethod
#     def greeting():# це метод який просто живе в обгорці юзера він ні кому не належить і цей метод можна викликати як від імені класу і від єкземпляру
#         print('hello world')
#
# '''Cтатисний метод( @staticmethod)- він нічого не робить не зміними класу,зміними екземпляру класу = додатковий функціонал але хочу щоб він жив у класі'''
#
# user=User('Max', 15)
# # User.hello(user)
# #User.hello() # Hello
# print(User.get_count()) # 0
# User.greeting() # hello world
# user.greeting() # hello world

'''перегрузка методів'''
"""У Python перевантаження методів (method overloading) — не таке як у мовах типу Java або C++, де можна створити кілька методів з однаковим ім'ям,
 але різними аргументами. Python не підтримує класичне перевантаження методів напряму.
Але! Існує кілька способів імітувати або реалізувати перевантаження в стилі Python 👇
❌ А чому не можна як у Java?У Python цього не буде — остання функція з тим самим ім’ям перепише попередню.
#✅ 1. Перевантаження через *args та **kwargs
#Це найчастіший спосіб. Дозволяє приймати змінну кількість аргументів:
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))        # 3
print(calc.add(1, 2, 3, 4))  # 10
#✅ 2. Перевірка типів аргументів вручну
class Printer:
    def print_data(self, data):
        if isinstance(data, str):
            print(f"Рядок: {data}")
        elif isinstance(data, list):
            print("Список:")
            for item in data:
                print(f" - {item}")
        else:
            print("Невідомий тип")

p = Printer()
p.print_data("Привіт")            # Рядок
p.print_data(["Привіт", "Світ"])  # Список

"""

from typing import Self
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # Людяне представлення об'єкта (для print())/Метод __str__() використовується, коли ти викликаєш print(obj) або str(obj)/Якщо __str__() не визначений, Python використовує __repr__() замість нього.
        return str (self. __dict__) # __dict__ — Атрибути екземпляра у вигляді словника/Це вбудований атрибут, який повертає всі змінні об'єкта у вигляді словника./Дуже зручно, коли треба подивитися, які дані є в об'єкті, або конвертувати в JSON.

    def __repr__(self): # Технічне представлення (для дебагу)/__repr__() має повертати рядок, який точно описує об'єкт і, бажано, може бути використаний для створення такого ж об'єкта знову.
        return self.__str__()

    def __add__(self, other: Self): # self=те що ми до чого додаємо, other= те що додаємо(# щоб давало підказки  типізуємо його і пишем це= from typing import Self)
        return self.age + other.age # описали поведінку як він має реагувати на +, але як він повинен реагувати я вирішую сама

    def __sub__(self, other):
        return self.age - other.age

    def __len__(self):
        return len(self.name)


user1=User('Max', 15)
user2=User('Oleh', 25)
# хочу + єкземпряри класу
user1+ user2 # дає помилку,але можу його навчити
print((user1 + user2)) # 40
print((user1 - user2)) #
#навчити узнавати довжину
print(len(user1)) # 3
print(len(user2)) # 4
# #  # можна і на інші мат. дії
#__eq__	Перевірка ==
# __ne__	Перевірка !=
# __gt__	Більше >
# __lt__	Менше <
# __len__	Додає підтримку len(obj)
# ''' + | __add__ | a + b
# - | __sub__ | a - b
# * | __mul__ | a * b
# / | __truediv__ | a / b
# // | __floordiv__ | a // b
# % | __mod__ | a % b
# ** | __pow__ | a ** b
# -a | __neg__ | -a
# +a | __pos__ | +a
#
# 🧠 Додатково:Якщо ти хочеш, щоб твій клас підтримував арифметику з числами, треба додатково враховувати тип:
# def __add__(self, other):
#     if isinstance(other, Money):
#         return Money(self.amount + other.amount)
#     elif isinstance(other, (int, float)):
#         return Money(self.amount + other)'''

# це патер у випадку якого не можемо створити більше чим одного екз.. кл. для нашого класу.
# Будь-який будемо створювати це буде посилання на один і теж екз..

# class User:
#     __instance = None # створюємо приватну зміну сюди ми будемо записувати саме екземпляр класу.
#
#     def __new__(cls, *args, **kwargs): # він запускає __init__ ,він є під капотним в об'єкті
#         if not isinstance(cls.__instance, cls):  # робимо перевірку якщо instance являється екземпляром нашого класу, якщо нан то буде тру
#             cls.__instance = super().__new__(cls) # то ми звертаємося до класу instance і вньому записуємо створеня нашого класу
#         return cls.__instance # іншому випадку будемо повертати instance якщо створений він то повертає його, якщо ні то також повертає його і поиім працює наш конструктор
#
#         # print(args, kwargs)
#         # return  super().__new__(cls)
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# # це і є наш патер singleton/тепер ми можемо створити юзер
# user1=User('Pety', 14)
# user2=User('Max', 24)
# print(user2.name)
# print(user1.name) # по факту це буде МАКс,вони переписують
# print(id(user2))# 2014541600080
# print(id(user1))# 2014541600080
# # скільки б ми створювали скільки і буде оде і теж ,нвіщо це потрібно = до прикладу контент базі даних, щоб не плодити багато конектів= роблять так
#
# # без new не  може створюється екземпляр класу, це означає своєю чергою, що в new можу маніпулювати як саме буде створено укз.. кл..
# # / спочатку завжди стартує new і він заносить інформацію в init
# # *args, **kwargs- получаємо коли створюємо юзера print(args, kwargs) # ('Pety', 34) {}- кортеж це що передав
# #user=User('Pety', 34)
# # print(user)# None=не існує чому? new=передає=init
# # print(user.name) # Pety

'''Metod __call__'''# дає можливість екземпляра класа бути ще й функцією

# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __call__(self, value):  # допомагає нам використовувати наш екземпляр класу як функцію
#         self.age += value # + до нього
#
# user1=User("John", 15)
# user1(15)# викликаю як ф-ю
# print(user1.age) # 30



