# Лямдові вирази### 🔹 **Lambda-функція в Python**
# **Lambda-функція** – це **анонімна (безіменна) функція**, яка записується
# в один рядок і може мати будь-яку кількість аргументів,
# але тільки один вираз.
# #### **📌 Синтаксис:**
# lambda аргумент1, аргумент2, ... : вираз
# ### **1️⃣ Простий приклад lambda-функції**
# **🔹 Приклад:**
# add = lambda x, y: x + y  # Додає два числа
# print(add(3, 5))  # 8
# **Це еквівалентно звичайній функції:**
# def add(x, y):
#     return x + y
# print(add(3, 5))  # 8
# ### **2️⃣ Використання в `map()`**
# Lambda-функція часто використовується для **перетворення списків**.
# **🔹 Приклад:**
# numbers = [1, 2, 3, 4]
# squared = list(map(lambda x: x ** 2, numbers))  # [1, 4, 9, 16]
# print(squared)
# ### **3️⃣ Використання в `filter()`**
# Фільтрує список за умовою.
# **🔹 Приклад:**
# numbers = [1, 2, 3, 4, 5, 6]
# even = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4, 6]
# print(even)
# ### **4️⃣ Використання в `sorted()`**
# Сортує за довжиною слова.
# **🔹 Приклад:**
# words = ["apple", "banana", "kiwi", "grape"]
# sorted_words = sorted(words, key=lambda word: len(word))
# print(sorted_words)  # ['kiwi', 'grape', 'apple', 'banana']
# ### **📌 Висновок:**
# ✅ Lambda-функції – це **короткий запис звичайних функцій**.
# ✅ Вони **корисні для швидких операцій** у `map()`, `filter()`, `sorted()`.
# ✅ Але **lambda не підтримує складну логіку** – для цього краще використовувати `def`. 🚀


r=5
#тобто ф-ця щось приймає або не приймає і має тільки що щось повертає без тіл
#прописуємо що приймає (якщо нічого не приймає то стовимо дві крапкт)і через показуємо що повертає
fun = lambda a,b: a+b
print(fun(5, 6))

# змінює значення і повертає такою довжиною його 28.21
#map() # приймає лямду ф-ю і робить вона ходить покожному єлементу і якось
# видозмінює і повертає такою самою довжини список L
l=[1,2,3,4,5]

m=map(lambda item:item**2,l)# проходить кожний елемент і повертає кожне число піднесено до квадрату і отримуємо об'єкт m
# це генератор по якому можна пройтися один раз=інструкція яка буде виконуватися на кожній ітерації,
# по map() можна проітеруватися
# for i in m:
#     print(i)
f = filter(lambda x: x % 2 == 0, l) # кожній ітерації отримаю х і якщо числопарне то я його поверну
for item in f:
    print(item) # ітерували

#Приклад як використовувати лямда вирази
users = [
    {'name': 'Max', 'age':1},
    {'name': 'Nata', 'age':35},
    {'name': 'karina', 'age':20},
    {'name': 'kamila', 'age':2}
]

users.sort(key=lambda x:x['age'])
users.sort(key=lambda x:x['name'])
users.sort(key=lambda x:len(x['name'])) #
print(users)

