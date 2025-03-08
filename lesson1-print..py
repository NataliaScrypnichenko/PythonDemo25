# hgh..#bjnm,
#
# """"
# блок коментар
# """
# '''
# також блочний коментар
# '''

print('Hello from Python')
# print() — це вбудована функція Python, яка виводить дані в консоль.
# 🔹 Синтаксис
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#Аргументи:
# *objects — одне або кілька значень для виводу.
# # sep=' ' — роздільник між об'єктами (за замовчуванням пробіл).
# # end='\n' — символ, який додається в кінці (за замовчуванням новий рядок).(використання два слеша \n\n-буде додатковий пробіл)
# file=sys.stdout — потік для виводу (можна змінити на файл).
# flush=False — примусовий вивід (важливо для логів).
# 🔹 1. Простий вивід
print("Hello, world!")  # Hello, world!
# 2. Вивід кількох значень
print("Hello", "Python", "3.10") # Hello Python 3.10
# 🔹 3. Використання sep (роздільник)
print("apple", "banana", "cherry", sep=", ") # apple, banana, cherry
# 🔹 4. Використання end (закінчення рядка)
print("Hello", end=" ")
print("world!")  # Hello world! (все в одному рядку)
# 🔹 5. Форматований вивід (f-рядки)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # My name is Alice and I am 25 years old.
# 🔹 6. Вивід у файл
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
#     📁 Вміст файлу output.txt:
# Hello, file!
# 🔹 7. Вивід без нового рядка
print("Loading", end="...")
print(" Done!")
# Loading... Done!
# 🔹 8. Вивід Unicode-символів
print("Smile: 😊, Heart: ❤️")  # Smile: 😊, Heart: ❤️
# 🔹 9. Вивід з flush=True (для логування)
#  flush=True змушує print() одразу вивести текст у консоль.
import time
print("Processing...", end="", flush=True)
time.sleep(2)
print(" Done!")  # Processing... Done!
# 🔹 10. Вивід у форматі таблиці
print(f"{'Name':<10} {'Age':<5}")
print(f"{'Alice':<10} {25:<5}")
print(f"{'Bob':<10} {30:<5}")
# Name       Age
# Alice      25
# Bob        30



# 🔥 Висновок
# print() — це гнучка функція для виводу даних.яка виводить в термінал дані. Вона підтримує: ✅ Форматування (f"...", .format())
# ✅ Роздільники (sep)
# ✅ Завершальні символи (end)
# ✅ Вивід у файл
# ✅ Вивід у логах (flush=True)



