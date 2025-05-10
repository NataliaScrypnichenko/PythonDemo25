#У Python бібліотека json використовується для роботи з JSON-даними — тобто
# для серіалізації (перетворення в текст) та десеріалізації (читання з тексту)
# структур даних між Python і форматом JSON.
# 📦 JSON (JavaScript Object Notation)
# Це універсальний текстовий формат обміну даними, який:
# легко читається людиною
# підтримується багатьма мовами програмування
# часто використовується в API і файлах конфігурацій
# 3📚 Основні функції в модулі json
#     Функція	                          Призначення
# json.dump(obj, file)	           Запис Python-об'єкта у файл як JSON
# json.dumps(obj)	              Перетворення Python-об'єкта у JSON-рядок
# json.load(file)	              Зчитування JSON з файлу у Python-об'єкт
# json.loads(s)	                   Перетворення JSON-рядка в Python-об'єкт
#✅ Python ↔ JSON відповідність
# Python	         JSON
# dict	            object
# list, tuple	    array
# str	            string
# int, float     	number
# True / False	    true/false
# None	            null
#📌 Для чого використовують json:
# Передача даних між сервером і клієнтом
# Збереження налаштувань у JSON-файлах
# Зчитування API-відповідей
# Експорт/імпорт структур даних

# Приклад: перетворення Python → JSON
# import json
#
# data = {"name": "Anna", "age": 25}
# json_str = json.dumps(data)
#
# print(json_str)# Результат: {"name": "Anna", "age": 25}

# Приклад: JSON → Python
# import json
#
# json_str = '{"name": "Anna", "age": 25}'
# data = json.loads(json_str)
#
# print(data["name"])  # Anna

#Окей! Ось аналогічний приклад серіалізації та десеріалізації, але вже з використанням бібліотеки json,
# яка працює з текстом (рядками) — зручно для обміну між програмами та збереження "людинозрозумілих" даних:
#📦 Приклад з json
import json

data = {'name': 'Anna', 'age': 25}

# Серіалізуємо: зберігаємо у файл як JSON
with open('data.json', 'w') as file:
    json.dump(data, file)

# Десеріалізуємо: читаємо з JSON-файлу назад у Python
with open('data.json', 'r') as file:
    restored_data = json.load(file)

print(restored_data)  # {'name': 'Anna', 'age': 25}
#
# #📌 Різниця між pickle і json:
# Характеристика	   pickle	                     json
# Формат	           Бінарний (байти)	            Текстовий (рядок)
# Зрозумілий людині	    ❌ Ні                   	✅ Так
# Підходить для обміну	❌ Не дуже	            ✅ Так (API, мережа)
# Підтримка типів	   ✅ Будь-які Python-типи	     ⚠️ Лише базові типи (dict, list, str, int, float, bool, None)
#
# 🧠 Тобто:
# json — краще для обміну між різними мовами/системами.
# #
# pickle — краще для повного збереження Python-об'єктів всередині Python.