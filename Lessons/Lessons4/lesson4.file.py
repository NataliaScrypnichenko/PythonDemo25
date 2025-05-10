# щоб працювати із файло нам потрібно його відкрити і отримати об'єкт файл, щоб працювати із
# файлами то open()= передати шлях до нашого файла

"""file=open('1.txt', mode='r')
#file=open('1.txt') # він поверне об'єкт файла ми створюємо тіпа зміну
print(file.read()) # read() читає повністю файл= внизу видає інформацію,якщо відкрили файл то потрібно його закрити, а то це викликає проблеми із памятю
file.close() # закриваємо файл але є декілька але на допомогу ідуть трайексерти
# Але коли ми відкрили файл тоо повині вказувати які цілі ми хочемо по замовчувані іде # file=open('1.txt', mode='r')
# file=open('1.txt', mode='r')  це означає що читати (read), все інше потрібно прописувати.(read)- тягне за собою
# що можна тільки читати і якщо такого, файла не буде, то буде помилка.Для того щоб можна було хендлити тобто убрати помилку є механізм такий.
# З файлами може бути багато помилок і їх від хендлити можна - використовують тільки це він відхопить будь-яку помилку.try:except:
# якщо хочу відхопити конкретну помилку, то можна відхопити, але потрібно обов'язково ексепшин прописати."""
from Lessons.Lessons4.генератори import gen_jpg_file

# Як писали раніше щоб виправити помилку.
# try:
#     file = open('1.txt') # в цьому try: відкривали файл і якщо була якась помилка, то відхоплюю її except Exception as e:print(e), якщо файл не відкрився, то обов'язково закрився
#     try:
#         print(file.read())   # в цьому try читаємо
#     finally:
#         file.close()
# except Exception as e:
#     print(e)

# Є сучасне написання робота із файлами
# try:
#     with open('1.txt') as file:
#                                                                              # тут пишемо роботу із файлом
# except Exception as e:
#     print(e)

"""try:
    with open('1.txt') as file:
        # print(file.readline()) # читає по строково, кожний раз нову, строку
        # print(file.readline())
        #print([file.read()])  # читати весь і все  print([file.read()])-побачимо слеш ен?але так не потрібно робити уб'ю оперативну память
        # print(file.readlines()) # читає весь файл але заганяє кожну стрічку в масив
        for line in file:
            print(line)   # на кожній ітераціїї отримаємо нову стрічку
except Exception as e:
    print(e)"""

# Режими файла. читати-r, write-файл відкритий в режимі запису
'''try:
    with open('1.txt', 'w' ) as file: # це означає якщо файла не існувало то він його створить,якщо існує то
        file.write("hello, Nata!\nI am from Ukraine") # і він переписав файл ,то б то все удалив і написав те що йому вказали, якщо потріб на друга стрічка то (\n)


except Exception as e:
    print(e)'''

# додавати щось у файл append також створює файл якщо його не існує,і буде відкривати файл в режимі додавання і буде додавати туди де стояв курсор
'''try:
    with open('1.txt', 'a') as file:
        file.write("append") # потрібно чітко слідкувати за пробілами (\n)
except Exception as e:
    print(e)'''

# режим х=створення файлу, повертає помилку якщо файл уже існує
'''try:
    with open('2.txt', 'x') as file: # '1.txt' дає помилку тому, що файл існує ([Errno 17] File exists: '1.txt'),'2.txt' =створив 
        pass
except Exception as e:
    print(e)
'''
# комбінації
# читати-raed, write-файл відкритий в режимі запису
'''try:
    with open('1.txt', 'w+') as file:
        file.write('HELLO WORLD')
        file.seek(0) # повернути курсор,але коли прочитали і хочем щось написати то курсор знову потрібно перемістити
        print(file.read()) # але коли ми написали і курсор залишився там де написали після, і поросили прочитати то він і не показав ні чого,тому потрібно повернути курсор

except Exception as e:
    print(e)'''

# r+ відкриваємо в режимі читані правила ті самі, але можемо до писуввати
'''try:
    with open('1.txt', 'r+') as file:
        file.write('HELLO WORLD')
        file.seek(0)
        print(file.read())

except Exception as e:
    print(e)
'''

# БІДАРНІ ДАНІ= це робота із картинками тобто який із 1 і 0 будує картинку.
# Я хочу його копіювати в інший файл- використовуємо генератор.'rb' = читаня бінарних даних
'''try:
    with open('img.jpg', 'rb') as file:
        data = file.read() # читаємо весь файл
        with open(next(gen_jpg_file()), 'wb') as file2: # відкриваю ще один файл  вставляю генерацію ще одного файла і даю ім'я, запис бінарних даних запис файла 2
            file2.write(data)  # звертаюсь до файла 2 і записую те що було в data = буде новий файл
except Exception as e:
    print(e)
#  можна записати інакше і буде новий файл
# try:
#     with open('img.jpg', 'rb') as file,open(next(gen_jpg_file()), 'wb') as file2:
#         file2.write(file.read())
# except Exception as e:
#     print(e)
'''

# бібліотеки які допомогають в роботі/Звичайно записуємо їх вбінарні дані або в джейсонки в файли
'''У Python TypedDict — це спеціальний тип з модуля typing, який дозволяє додати типізацію до словників (dict),
тобто явно вказати,які ключі мають бути у словнику та які значення вони мають містити.
✅ Коли використовувати TypedDict?
Коли ти хочеш, щоб словник мав фіксовану структуру (наприклад, "name" → рядок, "age" → число).
🔐 Що це дає?
Контроль структури словника на етапі розробки (через статичну перевірку).
Легше читати та підтримувати код.
Не потрібно створювати повноцінний клас
🆚 Порівняння з dataclass:
                  TypedDict	dataclass
Створює словник	    ✅	     ❌ (об'єкт)
Типізація     	    ✅	     ✅
Зберігає порядок  	✅	     ✅
Використання пам’яті	Менше	Більше'''

import json
import pickle
from  typing import TypedDict

User=TypedDict('User',{'name':str,'age':int} )

users: list [User] =[
    {'name': 'Max', 'age': 18},
    {'name': 'Oleg', 'age': 16},
    {'name': 'Karina', 'age': 15},
    {'name': 'Masha', 'age': 20}
]

# try:
#     with open('user.json', 'w') as file: # записали і створили
#         json.dump(users, file) # це команда із бібліотеки json і dump() приймає об'єкт і хочу їх записати у вигляді джейсон
# except Exception as e:
#     print(e)

'''читати'''
'''try:
    with open('user.json', 'r') as file:
        users:list[User]=json.load(file)
        print(users)
except Exception as e:
    print(e)'''
# з pickle бібліотекою зберігатиме в бінарному виді
# try:
#     with open('user.data', 'wb') as file:
#         pickle.dump(users, file)
# except Exception as e:
#     print(e)

'''читати'''
try:
    with open('user.data', 'rb') as file:
        users:list[User]=pickle.load(file)
        print(users)
except Exception as e:
    print(e)