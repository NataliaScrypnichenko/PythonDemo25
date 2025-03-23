## 🔹 **Magic (Dunder) методи в Python**
# **Magic-методи** (або **dunder-методи**, від *double underscore*) – це
# спеціальні методи в Python, які мають формат `__method__` і викликаються автоматично при певних операціях.
# 📌 **Приклад magic-методу**:
class Example:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Об'єкт зі значенням {self.value}"

obj = Example(10)
print(obj)  # Викликається __str__: Об'єкт зі значенням 10
## 🔹 **Категорії та список magic-методів**

### **1️⃣ Конструктори та деструктори**
# Методи, які створюють або знищують об'єкти.
#
# | Метод | Опис |
# |--------|----------------------------|
# | `__init__(self, ...)` | Викликається при створенні об'єкта (конструктор) |
# | `__new__(cls, ...)` | Викликається перед `__init__`, створює новий екземпляр |
# | `__del__(self)` | Викликається при видаленні об'єкта |
#
# **📌 Приклад:**
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Створено об'єкт для {self.name}")

    def __del__(self):
        print(f"Об'єкт {self.name} видалено")

p = Person("Анна")
del p  # Викличе __del__
# ### **2️⃣ Перетворення вбудованих типів**
# Методи, які дозволяють конвертувати об'єкти в інші типи.
#
# | Метод | Опис |
# |--------|----------------------------|
# | `__str__(self)` | Перетворює об'єкт у рядок (для `print()`) |
# | `__repr__(self)` | Офіційне представлення об'єкта (`repr(obj)`) |
# | `__len__(self)` | Викликається при використанні `len(obj)` |
# | `__int__(self)` | Перетворення в `int(obj)` |
# | `__float__(self)` | Перетворення в `float(obj)` |
# | `__bool__(self)` | Викликається при `bool(obj)` |
# **📌 Приклад:**
class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __len__(self):
        return self.quantity

    def __str__(self):
        return f"Товар {self.name}, кількість: {self.quantity}"

item = Item("Яблука", 10)
print(str(item))  # Товар Яблука, кількість: 10
print(len(item))  # 10

### **3️⃣ Арифметичні операції**
# Дозволяють змінювати поведінку математичних операторів.
#
# | Метод                       Оператор |
# |--------|---------|
# | `__add__(self, other)` | `+` (додавання) |
# | `__sub__(self, other)` | `-` (віднімання) |
# | `__mul__(self, other)` | `*` (множення) |
# | `__truediv__(self, other)` | `/` (ділення) |
# | `__floordiv__(self, other)` | `//` (цілочисельне ділення) |
# | `__mod__(self, other)` | `%` (залишок) |
# | `__pow__(self, other)` | `**` (піднесення до степеня) |

# **📌 Приклад:**
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

n1 = Number(5)
n2 = Number(10)
print(n1 + n2)  # 15 (викликається __add__)

### **4️⃣ Операції порівняння**
# Модифікують поведінку операторів `==`, `<`, `>`, тощо.
# | Метод | Оператор |
# |--------|---------|
# | `__eq__(self, other)` | `==` (дорівнює) |
# | `__ne__(self, other)` | `!=` (не дорівнює) |
# | `__lt__(self, other)` | `<` (менше) |
# | `__le__(self, other)` | `<=` (менше або дорівнює) |
# | `__gt__(self, other)` | `>` (більше) |
# | `__ge__(self, other)` | `>=` (більше або дорівнює) |
#
# **📌 Приклад:**
class Box:
    def __init__(self, weight):
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

b1 = Box(10)
b2 = Box(20)
print(b1 < b2)  # True (викликається __lt__)
### **5️⃣ Робота з індексацією та ітерацією**
# Методи, які дозволяють об'єктам працювати як списки.
# | Метод | Опис |
# | `__getitem__(self, index)` = `obj[index]` |
# | `__setitem__(self, index, value)` = `obj[index] = value` |
# | `__delitem__(self, index)` | `del obj[index]` |
# | `__iter__(self)` | Повертає ітератор (`for item in obj`) |
# | `__next__(self)` | Повертає наступне значення в ітераторі |
#
# **📌 Приклад `__getitem__` та `__setitem__`:**
class CustomList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

my_list = CustomList([10, 20, 30])
print(my_list[1])  # 20 (__getitem__)
my_list[1] = 99  # (__setitem__)
print(my_list.data)  # [10, 99, 30]

### **6️⃣ Контекстні менеджери (`with ... as`)**
# Методи для автоматичного відкриття/закриття ресурсів.
# | Метод                         | Опис |
# | `__enter__(self)` = Викликається при вході в `with` |
# | `__exit__(self, exc_type, exc_value, traceback)` = Викликається при виході з `with` |
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager("test.txt") as f:
    f.write("Hello, world!")

## 🔹 **Висновок**
# ✅ Magic-методи дозволяють перевизначати поведінку об'єктів Python.
# ✅ Вони використовуються для **арифметичних операцій, порівнянь, індексації, ітерацій,
# контекстних менеджерів тощо**.
# ✅ Використання magic-методів допомагає створювати **гнучкі та зрозумілі класи**. 🚀