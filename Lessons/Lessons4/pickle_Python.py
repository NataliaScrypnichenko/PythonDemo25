# Бібліотека pickle в Python використовується для серіалізації та десеріалізації об'єктів
# Python — тобто збереження будь-якого Python-об'єкта у файл або байтовий потік,
# а потім його відновлення у початковому вигляді.
# 📦 Що таке pickle?(картинка)
# pickle — це вбудований модуль Python, який дозволяє:
# зберігати складні об'єкти (наприклад, словники, списки, класи, функції) у файл або пам'ять
# відновлювати об'єкти з цих збережених даних
#🔧 Основні функції pickle
# Функція              	    Призначення
# pickle.dump(obj, file)	Серіалізувати об’єкт і записати його у файл
# pickle.load(file)	        Зчитати об’єкт із файлу (десеріалізувати)
# pickle.dumps(obj)	        Серіалізувати об’єкт у байти
# pickle.loads(bytes)	    Десеріалізувати об’єкт із байтів

#📘 Приклад використання:
import pickle

# Зберігаємо об'єкт
data = {'name': 'Ivan', 'age': 30}

with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Читаємо об'єкт назад
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)  # {'name': 'Ivan', 'age': 30}

# 🛠 Де використовується pickle:
# 📁 Збереження стану програми (наприклад, моделі ML)
# 🔁 Кешування результатів обчислень
# 🧠 Зберігання та відновлення об'єктів у нейронних мережах (наприклад, у scikit-learn)
# 💾 Збереження даних між сесіями без бази даних
# ⚠️ Важливо:
# Небезпечно відкривати pickle-файли з недовірених джерел, оскільки це може виконати шкідливий код.
# Для обміну між системами краще використовувати json, а не pickle.

#🧊 Серіалізація — це коли ми перетворюємо об'єкт Python
# (наприклад, словник, список, клас) у рядок, байти або файл, щоб:
# =зберегти на диск (файл)
# =передати по мережі
# =записати в базу даних
# 🗣 Уяви, що ти "заморожуєш" об'єкт — і кладеш у файл, як у морозилку.
#
# 🔥 Десеріалізація — це зворотний процес: ми "розморожуємо" об'єкт — читаємо з
# файлу назад у Python-об'єкт, щоб з ним знову працювати.
#📌 Простіше кажучи:
# Серіалізація — це "запакувати" Python-об'єкт у збережений вигляд.
# Десеріалізація — це "розпакувати" його назад у Python.
import pickle
data = {'name': 'Anna', 'age': 25}
# Серіалізуємо: зберігаємо в файл
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Десеріалізуємо: читаємо з файлу
with open('data.pkl', 'rb') as file:
    restored_data = pickle.load(file)

print(restored_data)  # {'name': 'Anna', 'age': 25}
