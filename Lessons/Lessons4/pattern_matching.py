#У Python pattern matching (структурне зіставлення з шаблоном) — це синтаксис для перевірки структури об'єкта
# та автоматичного витягування його частин. Це дуже потужна конструкція,  яка дозволяє, наприклад,
# ефективно обробляти різні типи даних (словники, списки, об'єкти) без великої кількості if/elif
#✅ Синтаксис
# # match вираз:
#     case шаблон1:
#         # дії
#     case шаблон2:
#         # дії
#     case _:
#         # інше (як else)
# 📌 Особливості:
# case _: — аналог else, спрацьовує, якщо нічого не підходить.
# Можна витягати значення без додаткового розпакування.
# Працює з будь-якими структурами: списками, кортежами, словниками, об'єктами класів.
#
# 🔧 Навіщо потрібен pattern matching?
# Заміна if...elif...else конструкцій
# Краще читання коду при обробці даних
# Особливо зручно при обробці JSON, API-відповідей, парсингу структур

'''any= input('enter any: ')
match any:# Дивиться за
    case'hi': # якщо
        print('hello')
    case 'no':
        print('nope')
    case _: # кейс по дефолту
        print('default')'''

# людина повина повернути на ліво і зробити 200 кроків

# a=['left','200']
# # вміє в автоматичном режимі розділяти навіть деструктуризувати і подивитися що там є
# match a:
#     case 'left', value: # якщо ліво то велю #
#         print('left', value) # left 200
#     case 'right', value:
#         print('right', value)

'''match-може слідкувати за кількістю елементів і також можна їх використовувати'''
a=['left','200']
# a=['left','200', '23435'] # має три значення
# match a:
#     case 'left' as k, value: # якщо ліво то велю # left1 left 200
#         print('left1', k,value) # left 200
#     case 'right', value:
#         print('right', value)
#     case f,s,t:
#         print('three',f,s,t) # дає відповідь three left 200 23435

# можна провірити що тут має бути 200
'''match a:
    case 'left' as k,'200' as value: #left1 left 200
        print('left1', k,value) #
    case 'right', value:
        print('right', value)
    case f,s,t:
        print('three',f,s,t)
    case _:
        print('haha')'''
# Беремо із реальності дікшері і клас юзерів

user_dict={'name':'Max', 'age': 15}

class User:
    __match_args__ = {'name','age'} # клас не працює з мачтом тільки тоді коли є спеціальний  прараметри і потім вписуємо поля з якими буде працювати
    def __init__(self,name,age):
        self.name=name
        self.age=age
user_class=User('Karina',20)

# створюємо функцію яка приймає те або те і виводить ім'я і роки(source= це дані приймає)

# def matcher(source:User | dict): # провіряє
#     if isinstance(source,dict):  # якщо
#         print(source['name'],source['age'])
#     elif isinstance(source,User): # інакше
#         print(source.name,source.age)
#
# matcher(user_dict)
# matcher(user_class)
# ми можемо удосконалити це щоб не провіряти це так

def matcher(source:User|dict):
    match source:
        case User(name,age):
            print(name,age)
        case {'name':'Max' as name,'age': age}: # dict якщо імя
            print(name,age)

matcher(user_dict)
