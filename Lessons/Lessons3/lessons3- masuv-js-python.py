# 🔹 реалізувати масив як в Js на python 1:05

class Array:
    def __init__(self, *args):
        self.__arr = [*args]

    def __str__(self):
        return str(self.__arr)
    def __len__(self):
        return len(self.__arr)
    def __setitem__(self, key, value): # index= key
        self.__arr[key] = value
    def __getitem__(self, key):
        return self.__arr[key]
    def __delitem__(self, key):
        del self.__arr[key]
    def push(self, item):
        self.__arr.append(item)
    # def pop(self):
    #     return self.__array.pop()
    def map(self, cb):# дає завжди новий масив на виході
        return Array(*[cb(item) for item in self.__arr])#  ств.новий екз.кл. а тут з for item переберемо весь наш масив і
         # будемо запускати цю ф-ю cb() і кладемо туди item,cb(item) і отримаємо масив який нам потрібно розкласти в екз.кл. *[], щоб у нас знову з'явився нрвий єкз
    def filter(self, cb):
        return Array(*[item for item in self.__arr if cb(item)]) # розпаковуємо новий масив, ітеруємо його по умові cb() і передаємо cb(item),ші в такому випадку записуємо його

#🔹 більш-менш реалізацію написали= тепер як з цим працювати
'''arr=Array()
arr.push(1)
arr.push(10)# [1,10]
print(arr)
print(arr[0])# по індексу із методу __getitem__ / #1
arr[0]=55 # звертаємося до індекса 0 і записуємо його=55 \ це дає на змогу метод __setitem__
del arr[0] # [10] 
print(arr)'''
arr=Array(3,4,5,6,7,8,9)
arr_map=arr.map(lambda x: x * 2)#передаємо колбек цеу випадку нашого лямда ф-я
print(arr_map) # [6, 8, 10, 12, 14, 16, 18]
arr_filter =arr.filter(lambda x: x < 5)
print(arr_filter) # [3, 4]

# ось такі речі можна робити завдяки перегрузок

''' ✅ Python: __setitem__, __getitem__
Це магічні методи, які дозволяють твоєму класу працювати як словник або список — через [].
🔹 __getitem__(self, key) — отримання значення за ключем

🔹__setitem__(self, key, value) — це спеціальний метод, який викликається, коли ти присвоюєш значення елементу по ключу за допомогою квадратних дужок:
 Для чого використовується?
Щоб створити свої словники або структури, які поводяться як списки або мапи.
Щоб контролювати логіку присвоєння значень, наприклад: валідацію, логування, автоматичні обчислення.

🔹 push (JS, іноді в Python списки через .append)=Додає елемент у кінець масиву

🔹 pop=Видаляє останній елемент

🔹map=Перетворює кожен елемент масиву за функцією
arr = [1, 2, 3]
doubled = list(map(lambda x: x * 2, arr))  # [2, 4, 6]

🔹filter=Повертає тільки ті елементи, які задовольняють умову
arr = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, arr))  # [2, 4]

 '''