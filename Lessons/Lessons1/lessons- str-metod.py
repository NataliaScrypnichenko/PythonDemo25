#Ось найпоширеніші методи для роботи з рядками (str) у Python із поясненнями:
# МЕТОДИ
str.lower()# Перетворює всі літери рядка в нижній регістр.
# text = "Hello World"
# print(text.lower())  # "hello world"

str.upper()#Перетворює всі літери в верхній регістр.
# print(text.upper())  # "HELLO WORLD"

str.capitalize()#Робить першу літеру великою, а решту – малими.
# "text = "hello world"
# print(text.capitalize())  # "Hello world

str.title() # Робить першу літеру кожного слова великою.
# print("hello world".title())  # "Hello World"

str.strip() # Видаляє пробіли (та інші непотрібні символи) з початку та кінця рядка.
# text = "   hello world   "
# print(text.strip())  # "hello world"

str.lstrip() #– прибирає пробіли зліва.
str.rstrip() #– прибирає пробіли справа
# print(text.lstrip())  # "hello world   "
# print(text.rstrip())  # "   hello world"

str.replace() # str.replace(old, new)-Замінює всі входження підрядка old на new.
# print("hello world".replace("world", "Python"))  # "hello Python"

str.find() #str.find(sub)-Підраховує кількість входжень підрядка sub.
# print("hello hello world".count("hello"))  # 2

str.startswith(), str.endswith() #str.startswith(prefix), str.endswith(suffix)-Перевіряє, чи починається (startswith)
# або закінчується (endswith) рядок заданим підрядком.
# print("hello world".startswith("hello"))  # True
# print("hello world".endswith("world"))  # True

str.split() # str.split(sep) Розбиває рядок на список частин за роздільником sep (за замовчуванням – пробіл).
# print("hello world".split())  # ['hello', 'world']
# print("apple,banana,grape".split(","))  # ['apple', 'banana', 'grape']

str.join() #str.join(iterable)-Об'єднує елементи списку (iterable) у рядок, використовуючи даний рядок як роздільник.
# words = ["hello", "world"]
# print(" ".join(words))  # "hello world"
# print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape"

str.isalnum() # чи містить тільки букви та/або цифри.
# print("hello123".isalnum())  # True
# print("hello 123".isalnum())  # False (бо є пробіл)

str.zfill() #str.zfill(width)-Доповнює рядок нулями зліва до заданої довжини width.
# print("42".zfill(5))  # "00042"

str.center() #str.center(width, fillchar)-Вирівнює рядок по центру, заповнюючи пробілами або символом fillchar.
# print("hello".center(10, "-"))  # "--hello---"

str.isspace() #Метод str.isspace() перевіряє, чи містить рядок тільки пробіли, табуляції (\t),
# переведення рядка (\n) або інші пробільні символи.Метод корисний, коли потрібно перевірити, чи складається рядок лише з пробільних символів,
# наприклад, перед обробкою введених користувачем даних.
# Якщо так – повертає True, інакше False.
# print("   ".isspace())   # True (тільки пробіли)
# print("\t\n".isspace())  # True (табуляція + новий рядок)
# print("hello".isspace()) # False (є символи)
# print(" hello ".isspace()) # False (є пробіли, але також є букви)
# print("".isspace())  # False (порожній рядок)

str.isdecimal() #Метод str.isdecimal() перевіряє, чи складається рядок тільки з десяткових цифр (0-9).
# Якщо так – повертає True, інакше False.
#Приклади:
# print("123".isdecimal())   # True (тільки цифри 0-9)
# print("٣٤٥".isdecimal())   # True (арабські цифри)
# print("12.3".isdecimal())  # False (містить крапку)
# print("⅕".isdecimal())     # False (дробові символи)
# print("²".isdecimal())     # False (степінь, не стандартна цифра)
# print("123abc".isdecimal()) # False (містить літери)
# print("".isdecimal())      # False (порожній рядок)
# 🔹 Важливо:
# isdecimal() перевіряє тільки десяткові цифри.
# Він не працює з дробовими або надрядковими числами (наприклад, ² або ⅕).
# Якщо потрібно перевірити всі види чисел, краще використовувати .isdigit(), яке приймає більше числових символів.
# 🔍 Різниця між .isdecimal(), .isdigit() і .isnumeric():
# Метод	Десяткові цифри (0-9)	Надрядкові (², ³)	Дроби (⅕, ½)	Арабські цифри (٣٤٥)
# isdecimal()	✅ Так	❌ Ні	❌ Ні	✅ Так
# isdigit()	✅ Так	✅ Так	❌ Ні	✅ Так
# isnumeric()	✅ Так	✅ Так	✅ Так	✅ Так
# Якщо потрібно перевірити лише звичайні цифри (0-9) – використовуйте isdecimal().
# Якщо хочете врахувати степені та інші цифрові символи – використовуйте isdigit().
# Якщо потрібно перевірити будь-які числові символи (навіть дроби) – використовуйте isnumeric().

str.isdigit() #Метод str.isdigit() перевіряє, чи складається рядок тільки з цифрових символів.
# Якщо всі символи – цифри, метод повертає True, інакше False.
# 📌 Приклади:
# print("123".isdigit())   # True (звичайні цифри 0-9)
# print("٣٤٥".isdigit())   # True (арабські цифри)
# print("²³".isdigit())    # True (степені ², ³ вважаються цифрами)
# print("12.3".isdigit())  # False (є крапка)
# print("⅕".isdigit())     # False (дробовий символ)
# print("123abc".isdigit()) # False (літери)
# print("".isdigit())      # False (порожній рядок)
# 🔹 Важливі деталі:
# isdigit() повертає True для:
# Звичайних десяткових цифр (0-9).
# Арабських цифр (٠١٢٣٤٥٦٧٨٩).
# Степеневих чисел (², ³).
# Не працює для дробів (⅕, ½) або чисел з крапкою (12.3).
# 🔍 Різниця між .isdigit(), .isdecimal() і .isnumeric():
# Метод	Десяткові цифри (0-9)	Степені (², ³)	Дроби (⅕, ½)	Арабські цифри (٣٤٥)
# isdecimal()	✅ Так	❌ Ні	❌ Ні	✅ Так
# isdigit()	✅ Так	✅ Так	❌ Ні	✅ Так
# isnumeric()	✅ Так	✅ Так	✅ Так	✅ Так
# isdecimal() – тільки звичайні цифри (0-9).
# isdigit() – підтримує десяткові цифри + степені.
# isnumeric() – підтримує всі числові символи, включаючи дроби.
# ✅ Використання:
# Якщо потрібно перевірити звичайні числа → isdecimal().
# Якщо треба враховувати степені → isdigit().
# Якщо потрібно врахувати дроби та інші числові символи → isnumeric().

str.isalpha() #Метод str.isalpha() перевіряє, чи складається рядок лише з букв (алфавітних символів).
#Якщо всі символи – літери (без цифр, пробілів або спеціальних символів), метод повертає True, інакше False.
# 📌 Приклади:
# print("Hello".isalpha())   # True (тільки літери)
# print("Привіт".isalpha())  # True (українські літери)
# print("Python3".isalpha()) # False (є цифра)
# print("Hello!".isalpha())  # False (є спеціальний символ)
# print(" ".isalpha())       # False (пробіл)
# print("".isalpha())        # False (порожній рядок)
# 🔹 Важливі деталі:
# Метод працює з будь-якими літерами алфавітів (латиниця, кирилиця, грецький алфавіт тощо).
# Якщо у рядку хоч один не-алфавітний символ (цифра, пробіл, пунктуація), isalpha() поверне False.
# ✅ Використання:
# Перевірка, чи ім'я користувача містить лише букви:
# name = "Іван"
# if name.isalpha():
#     print("Ім'я коректне")
# else:
#     print("Ім'я має містити лише букви")
# Використання разом із .replace() для перевірки складених слів:
# full_name = "Jean-Luc"
# print(full_name.replace("-", "").isalpha())  # True
# Якщо потрібно перевірити слова з пробілами або дефісами, перед перевіркою їх варто очистити (replace, strip).

str.endswith()#Метод str.endswith(suffix[, start, end]) перевіряє, чи закінчується рядок вказаним суфіксом (suffix).
# Якщо так – повертає True, інакше False.
# 📌 Синтаксис:
# ### `.endswith()`
# Метод `str.endswith(suffix[, start, end])` перевіряє, чи закінчується рядок вказаним суфіксом (`suffix`).
# Якщо так – повертає `True`, інакше `False`.
#  📌 Синтаксис:
# string.endswith(suffix, start, end)
# - `suffix` – рядок або кортеж рядків, які потрібно перевірити.
# - `start` *(необов'язково)* – початковий індекс перевірки.
# - `end` *(необов'язково)* – кінцевий індекс перевірки.
# ### 📌 Приклади:
# print("hello.txt".endswith(".txt"))  # True (рядок закінчується на ".txt")
# print("document.pdf".endswith(".txt"))  # False (закінчується на ".pdf")

# # Перевірка кількох суфіксів
# print("report.docx".endswith((".pdf", ".docx")))  # True (є серед варіантів)

# # Перевірка з обмеженням області пошуку
# print("example.py".endswith(".py", 0, 7))  # False (перевіряємо тільки "example")

# # Використання з URL
# print("https://example.com".endswith((".com", ".org")))  # True

# ### 🔹 Важливі деталі:
# - Параметри `start` та `end` дозволяють перевірити тільки певну частину рядка.
# - Можна передавати **кортеж** суфіксів для перевірки декількох варіантів.
# - Метод чутливий до регістру (`"Hello".endswith("o") → True`, `"Hello".endswith("O") → False`).
# ### ✅ Використання:
# 1. **Перевірка розширення файлу:**
#    ```python
#    filename = "data.csv"
#    if filename.endswith(".csv"):
#        print("Це файл CSV")
#    ```
# 2. **Перевірка домену сайту:**
#    ```python
#    url = "https://example.org"
#    if url.endswith((".com", ".org", ".net")):
#        print("Популярний домен")
#    ```
# 3. **Фільтрація файлів у списку:**
#    ```python
#    files = ["report.pdf", "image.jpg", "script.py", "notes.txt"]
#    pdf_files = [f for f in files if f.endswith(".pdf")]
#    print(pdf_files)  # ['report.pdf']
#    ```
# Метод `endswith()` зручний для перевірки закінчень рядків, наприклад, у назвах файлів або URL.

str.startswith()# Метод `str.startswith(prefix[, start, end])` перевіряє, чи починається рядок із вказаного префікса (`prefix`).
# # Якщо так – повертає `True`, інакше `False`.
# ### 📌 Синтаксис:
# # string.startswith(prefix, start, end)
# # - `prefix` – рядок або кортеж рядків для перевірки.
# # - `start` *(необов'язково)* – початковий індекс перевірки.
# # - `end` *(необов'язково)* – кінцевий індекс перевірки.
#
# ### 📌 Приклади:
# print("hello world".startswith("hello"))  # True (рядок починається з "hello")
# print("hello world".startswith("world"))  # False (не на початку)
#
# # Перевірка кількох варіантів
# print("data.csv".startswith(("data", "info")))  # True (починається з "data")
#
# # Перевірка з обмеженням області пошуку
# print("example.py".startswith("py", 8))  # True (перевіряємо з 8-го символу)
# print("example.py".startswith("py", 0, 7))  # False (перевіряємо лише "example")
#
# # Використання з URL
# print("https://example.com".startswith("https://"))  # True
# print("http://example.com".startswith(("http://", "https://")))  # True
#
# ### 🔹 Важливі деталі:
# # - Метод чутливий до регістру: `"Hello".startswith("H") → True`, `"Hello".startswith("h") → False`.
# # - `start` і `end` дозволяють перевіряти тільки частину рядка.
# # - Можна передавати **кортеж префіксів** для перевірки кількох варіантів.
#
# ### ✅ Використання:
# # 1. **Перевірка протоколу URL:**
# #   url = "https://example.com"
# #    if url.startswith(("http://", "https://")):
# #        print("Це веб-адреса")
# # #
# # 2. **Фільтрація файлів за префіксом:**
# #    files = ["log_2024.txt", "report.pdf", "log_2023.txt", "data.csv"]
# #    logs = [f for f in files if f.startswith("log_")]
# #    print(logs)  # ['log_2024.txt', 'log_2023.txt']
# #
# # 3. **Перевірка формату номера телефону:**
# #    phone = "+380971234567"
# #    if phone.startswith("+380"):
# #        print("Український номер")
# # Метод `startswith()` корисний для перевірки початку рядків, наприклад, у файлах, URL-адресах або текстових документах.

str.capitalize()#Метод `str.capitalize()` перетворює **першу літеру рядка у велику**, а всі інші – у **малі**.
# ### 📌 Синтаксис:
# string.capitalize()
# - Не змінює сам рядок, а повертає **новий** із зміненим регістром.
# ### 📌 Приклади:
# print("hello world".capitalize())  # "Hello world"
# print("PYTHON".capitalize())       # "Python" (перша велика, інші малі)
# print("123abc".capitalize())       # "123abc" (цифри не змінюються)
# print("hELLO wORLD".capitalize())  # "Hello world"
# print(" привет мир ".capitalize()) # " привет мир " (пробіли залишаються)
#
# ### 🔹 Важливі деталі:
# - **Змінює тільки перший символ**, а інші переводить у нижній регістр.
# - **Цифри та символи на початку не змінюються**, якщо немає літер.
# - **Не змінює вихідний рядок**, а повертає **новий**.
#
# ### ✅ Використання:
# 1. **Форматування імен:**
#    name = "john doe"
#    formatted_name = name.capitalize()
#    print(formatted_name)  # "John doe"
#
# 2. **Форматування заголовків повідомлень:**
#    message = "wELCOME TO PYTHON!"
#    print(message.capitalize())  # "Welcome to python!"
#
# 3. **Очищення тексту перед виводом:**
#    text = input("Введіть текст: ").strip().capitalize()
#    print(text)
# Метод `capitalize()` корисний для форматування текстів, назв та повідомлень. 🚀

str.upper() #Метод `str.upper()` перетворює **всі літери** рядка у **великі**.
# - Не змінює вихідний рядок, а повертає **новий** зі зміненим регістром.
# ### 📌 Приклади:
# print("hello".upper())      # "HELLO"
# print("Hello World".upper())# "HELLO WORLD"
# print("python3".upper())    # "PYTHON3" (цифри не змінюються)
# print("123abc".upper())     # "123ABC"
# print("Привіт!".upper())    # "ПРИВІТ!"
#
# ### 🔹 Важливі деталі:
# - **Тільки літери** змінюють регістр, **цифри та символи залишаються** незмінними.
# - **Не змінює вихідний рядок**, а повертає новий.
#
# ### ✅ Використання:
# 1. **Переведення тексту у верхній регістр (заголовки, оголошення):**
#    title = "breaking news: python 3.12 released!"
#    print(title.upper())  # "BREAKING NEWS: PYTHON 3.12 RELEASED!"
#
# 2. **Перевірка введених даних (наприклад, кодів):**
#    code = input("Введіть промокод: ").upper()
#    if code == "DISCOUNT2025":
#        print("Код активовано!")
#
# 3. **Переведення користувацького тексту у ВЕЛИКІ ЛІТЕРИ:**
#    user_input = input("Напишіть коментар: ")
#    print(user_input.upper())  # Виведе у верхньому регістрі
#
# Метод `upper()` корисний для переведення тексту у верхній регістр, обробки введених даних та створення заголовків. 🚀

str.index()# ndex() — це метод рядка в Python, який повертає індекс першого входження підрядка. Якщо підрядок не знайдено,
# викликається помилка ValueError.
# 📌 Синтаксис
# string.index(sub, start=0, end=len(string))
# Аргументи:
# sub — підрядок, який шукаємо.
# start (необов’язково) — початковий індекс пошуку.
# end (необов’язково) — кінцевий індекс пошуку.
# Повертає:
# 📍 Позицію (індекс) першого входження підрядка в рядку.
# ❌ Якщо підрядок не знайдено — ValueError.
# 🔹 Приклади використання
# ✅ 1. Знаходження першого входження
# text = "Hello, world!"
# print(text.index("o"))  # 4🔹 Пояснення:Перша літера "o" знаходиться на індексі 4.
# ✅ 2. Пошук у підрядку (start, end)
# text = "Hello, world!"
# print(text.index("o", 5))  # 8🔹 Пояснення:Шукаємо "o" починаючи з індексу 5 → Знайдено на позиції 8.
# ✅ 3. Якщо підрядка немає → ValueError
# text = "Hello, world!"
# print(text.index("z"))  # ❌ ValueError: substring not found🔹 "z" немає в рядку → отримаємо помилку.
# ✅ 4. Пошук слова
# text = "Python is amazing"
# print(text.index("amazing"))  # 10🔹 "amazing" починається з індексу 10.
# ✅ 5. Обхід помилки через try-except
# text = "Hello, world!"
# try:
#     index = text.index("z")
#     print("Found at:", index)
# except ValueError:
#     print("Not found!")
# 📌 Результат:
# mathematica
# Not found!
# 🔹 Використовуємо try-except, щоб уникнути ValueError.
# 🔹 Чим index() відрізняється від find()?
# Метод	Якщо знайдено	Якщо НЕ знайдено
# index()	Повертає індекс	Викликає ValueError
# find()	Повертає індекс	Повертає -1
# text = "Hello, world!"
# print(text.index("o"))  # 4
# print(text.find("o"))   # 4
# print(text.find("z"))   # -1
# 🔹 find() безпечніший, бо не викликає помилку.
# 🔥 Висновок
# ✅ index() — знаходить перше входження підрядка
# ✅ Використовує start і end для обмеження пошуку
# ✅ Викликає ValueError, якщо підрядка немає
# ✅ Альтернатива: find(), який повертає -1, а не помилку

str.partition() # розбиває стрічку на три частини це метод рядка, який розділяє рядок на три частини:1️⃣ Текст перед роздільником2️⃣ Сам роздільник
# 3️⃣ Текст після роздільника.Якщо роздільник не знайдено, повертається кортеж, де весь рядок буде у першому елементі, а два інших будуть порожніми ("").
# 📌 Синтаксис/string.partition(separator)
# Аргументи:separator — підрядок, за яким потрібно розділити рядок.
# Повертає:📍 Кортеж із трьох частин → (до роздільника, сам роздільник, після роздільника)
# 🔹 Приклади використання
# ✅ 1. Розділення за першим входженням роздільника
# text = "Hello, world!"
# print(text.partition(", "))  # ('Hello', ', ', 'world!')🔹 "Hello" — частина перед комою🔹 ", " — сам роздільник🔹 "world!" — частина після коми
# ✅ 2. Якщо роздільник відсутній
# text = "Hello world"
# print(text.partition(","))  # ('Hello world', '', '')🔹 Оскільки "," немає в рядку:Перший елемент — весь рядокДругий і третій — порожні ("").
# ✅ 3. Використання в змінних
# text = "apple-orange-banana"
# before, sep, after = text.partition("-")
# print(before)  # apple
# print(sep)     # -
# print(after)   # orange-banana
# 🔹 Розділення на три частини:
# 1️⃣ "apple" → перед "-"
# 2️⃣ "-" → сам роздільник
# 3️⃣ "orange-banana" → після "-"
#
# ✅ 4. Використання в умовах
# text = "user@example.com"
# name, at, domain = text.partition("@")
# if at:
#     print(f"Username: {name}, Domain: {domain}")
# else:
#     print("No email found.")
# 📌 Якщо @ є, розділяємо на ім'я користувача та домен.
#
# ✅ 5. Використання у while для обробки рядка
# text = "one,two,three"
# while text:
#     part, sep, text = text.partition(",")
#     print(part)#one two three
# 🔹 Метод partition() зручний для покрокового розділення рядка.
# 🔹 Чим partition() відрізняється від split()?
# Метод	Що робить	Кількість частин
# partition()	Розбиває на 3 частини	Завжди 3
# split()	Розбиває на всі можливі частини	Необмежено
# text = "apple-orange-banana"
# print(text.partition("-"))
# # ('apple', '-', 'orange-banana')
# print(text.split("-"))
# # ['apple', 'orange', 'banana']
# 📌 split() розбиває всі входження, а partition() — тільки перше.
#
# 🔥 Висновок
# ✅ partition() розбиває рядок на три частини
# ✅ Якщо роздільник не знайдено → повертає (рядок, '', '')
# ✅ Альтернатива split(), але partition() завжди дає 3 значення
# 🔹 Коли використовувати?
# Якщо потрібно знайти тільки перше входження роздільника
# Коли важливо отримати 3 частини (навіть якщо роздільник відсутній)

str.min()#min(iterable, *args, key=None) Повертає мінімальне значення у колекції або серед переданих чисел.
# numbers = [3, 7, 2, 9, 5]
# print(min(numbers))  # 2
# print(min(10, 5, 8))  # 5
# words = ["apple", "banana", "kiwi"]
# print(min(words, key=len))  # 'kiwi' (найкоротше слово)

str.max()# max(iterable, *args, key=None) Повертає максимальне значення у колекції або серед переданих чисел.
# print(max(numbers))  # 9
# print(max(10, 5, 8))  # 10
# print(max(words, key=len))  # 'banana' (найдовше слово)

str.sum()# sum(iterable, start=0)Повертає суму всіх елементів у послідовності (починаючи зі start).
# print(sum(numbers))  # 26
# print(sum(numbers, 10))  # 36 (до суми додається 10)

str.sorted() # sorted(iterable, key=None, reverse=False) Повертає відсортований список (за зростанням або спаданням).
# print(sorted(numbers))  # [2, 3, 5, 7, 9]
# print(sorted(numbers, reverse=True))  # [9, 7, 5, 3, 2]
# print(sorted(words, key=len))  # ['kiwi', 'apple', 'banana'] (за довжиною)

pow() #pow(base, exp, mod=None) Обчислює base ** exp (піднесення до степеня). Якщо передано mod, повертає (base ** exp) % mod.
# print(pow(2, 3))  # 8 (2³)
# print(pow(5, 3, 7))  # 6 (5³ % 7)
# 🔥 Висновок
# Функція	      Опис	                 Приклад
# min()	   Мінімальне значення	    min(3, 7, 2) → 2
# max()	   Максимальне значення	    max(3, 7, 2) → 7
# sum()	   Сума елементів	        sum([3, 7, 2]) → 12
# sorted()   Сортування	            sorted([3, 7, 2]) → [2, 3, 7]
# pow()	   Степінь	                pow(2, 3) → 8

len() # метод довжини в ньому передаємо словник або сет,стр.кортеж

print('*'*25) #можна умножати

# name = "Max"
# age = 18
# weight = 70.5
# string = f'Hello, my name is {name} and my age is {age} and my weight is {weight}'
# print(string) # створення