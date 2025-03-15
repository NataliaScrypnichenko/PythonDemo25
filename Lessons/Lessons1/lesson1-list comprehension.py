#хочу масив від 0 до 100
l=[i for i in range(100)]
print(l)
#  використовувати можна для фільтрів мапів
d=[4,2,7,2,4,1]
#записати тільки парні значення
res=[i for i in d  if i%2==0]
print(res)
# кожне значення хочу перемножити на 2
res=[i*2 for i in d]
print(res)
# можна поєднати
res=[i*2 for i in d if i%2==0]
print(res)
# перемножити всі парні і залишити всі інші(якщо if  інакше else отже for )
res=[i*2 if i%2==0 else i  for i in  d]
print(res)

l2d=[
    [1,2,3,4,5],
    [6,7,8,9,10]
]
# хочу вирівняти в один масив
l2=[i for j in l2d for i in j]
print(l2)
# звичайний цикл
l=[]
for j in l2d:
    for i in j:
        l.append(i)
print(l)

### 🔹 **List Comprehension у Python**
# 📌 **List comprehension** – це **скорочений спосіб** створення списків у Python.
# Він дозволяє **заповнювати список** у **одному рядку коду**, роблячи його більш **зрозумілим та компактним**.
### ✅ **Синтаксис**
# [вираз for елемент in ітерабельний_об'єкт if умова]
# 📌 `вираз` – це дія, яка виконується над кожним `елементом`.
# 📌 `ітерабельний_об'єкт` – список, range, рядок тощо.
# 📌 `if умова` – (необов’язково) фільтрує елементи.

## 🔹 **Приклади використання**
### ✅ **1. Створення списку чисел**
числа = [x for x in range(5)]
print(числа)  # [0, 1, 2, 3, 4]

### ✅ **2. Піднесення до квадрату**
квадрати = [x**2 for x in range(1, 6)]
print(квадрати)  # [1, 4, 9, 16, 25]

### ✅ **3. Фільтрація (з `if`)**
парні = [x for x in range(10) if x % 2 == 0]
print(парні)  # [0, 2, 4, 6, 8]

### ✅ **4. Використання `if-else`**
парні_непарні = ["парне" if x % 2 == 0 else "непарне" for x in range(5)]
print(парні_непарні)  # ['парне', 'непарне', 'парне', 'непарне', 'парне']

### ✅ **5. Робота з рядками**
слова = ["яблуко", "банан", "апельсин"]
довжини = [len(слово) for слово in слова]
print(довжини)  # [6, 5, 8]

### ✅ **6. List comprehension із вкладеними циклами**

матриця = [[x * y for x in range(1, 4)] for y in range(1, 4)]
print(матриця)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

## 🔹 **Висновок**
# ✅ **List comprehension** – це **швидкий та елегантний спосіб** створення списків.
# ✅ Дозволяє **скорочувати код** та робить його **читабельнішим**.
# ✅ Можна використовувати **`if` та `if-else` для фільтрації та трансформації даних**. 🚀