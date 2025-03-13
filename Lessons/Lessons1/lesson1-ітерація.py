# 🔄 **Як ітерувати кортеж (`tuple`) і словник (`dict`) у Python?**

# У Python можна легко перебирати елементи **кортежів (`tuple`)** і **словників (`dict`)** за допомогою **циклу `for`**.

## **✅ Висновки**
# - **Кортеж (`tuple`)** ітерується так само, як і список.
# - **Словник (`dict`)** можна перебирати:
#   - **за ключами** → `for key in dict`
#   - **за значеннями** → `for value in dict.values()`
#   - **за парами ключ-значення** → `for key, value in dict.items()`
# - `enumerate()` дає **індекси** під час перебору.
## **🔹 1️⃣ Ітерація кортежа (`tuple`)**
# Кортеж (`tuple`) — це **не змінюваний** послідовний тип даних у Python.

### 📌 **Приклад: простий перебір кортежа**
numbers = (10, 20, 30, 40, 50)

for num in numbers:
    print(num) #**Виведе:** #10, 20, 30, 40, 50
# ✅ Кожен елемент кортежа перебирається **по черзі**.


### 📌 **Перебір кортежа з індексами (`enumerate`)**Якщо потрібно **отримати індекс** кожного елемента:
words = ("Python", "Java", "C++")

for index, word in enumerate(words):
    print(f"Index {index}: {word}")
# 🔹 **Виведе:**
# Index 0: Python
# Index 1: Java
# Index 2: C++
# ✅ `enumerate()` повертає **(індекс, значення)**.

## **🔹 2️⃣ Ітерація словника (`dict`)**
# Словник (`dict`) зберігає **пари ключ-значення**.

### 📌 **Перебір тільки ключів (`keys()`)**
person = {"name": "Alice", "age": 25, "city": "New York"}

for key in person:
    print(key)
# 🔹 **Виведе:**
# name
# age
# city
# ✅ **За замовчуванням `for` перебирає ключі словника**.

### 📌 **Перебір ключів (`keys()`) явно**
for key in person.keys():
    print(key)
# 🔹 Результат такий самий, як і без `keys()`.


### 📌 **Перебір значень (`values()`)**Якщо потрібно **тільки значення**, використовуємо `values()`:
for value in person.values():
    print(value)
# 🔹 **Виведе:**
# Alice
# 25
# New York

### 📌 **Перебір пар (ключ-значення) через `items()`**
# Якщо потрібно перебирати **і ключ, і значення одночасно**:
for key, value in person.items():
    print(f"{key}: {value}")
# 🔹 **Виведе:**
# name: Alice
# age: 25
# city: New York
# ✅ `items()` повертає **кортеж `(ключ, значення)`**.

## **🛠 Застосування у реальних задачах**
### 🔹 **1️⃣ Перебір словника з кортежами**
students = {
    "Alice": (25, "Math"),
    "Bob": (22, "Physics"),
    "Charlie": (23, "Biology")
}
for name, (age, subject) in students.items():
    print(f"{name} is {age} years old and studies {subject}.")
# 🔹 **Виведе:**
# Alice is 25 years old and studies Math.
# Bob is 22 years old and studies Physics.
# Charlie is 23 years old and studies Biology.

### 🔹 **2️⃣ Перетворення словника у список кортежів**
person_list = list(person.items())
print(person_list)
# 🔹 **Виведе:**
# [('name', 'Alice'), ('age', 25), ('city', 'New York')]
# ✅ `items()` дозволяє **конвертувати словник у список кортежів**.

