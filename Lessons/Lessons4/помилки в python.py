# помилки колись не так вказали індек і ще щось то це більше фітча чим пара ніж недоліки.За допомогую якихось помилок можемо
# робити якісь дії і це реалізовано.
from unittest.result import failfast

# коли не вірно записав код  і видає помилку(NameError: name 'mfldkkdmcmdl' is not defined) то виправити її можна  так
# try:
#     mfldkkdmcmdl
# # передаю цю помилку і код запуститься і можна вивести інформацію помилки через (as) і назву її (e)
# except NameError as e:
#     print('fixed', e)
# print('Hello world')
# не можна ділити на (0) і буде помилка (ZeroDivisionError: division by zero) і
# також except- можна використовувати їх багато
try:
    mfldkkdmcmdl
    print(1/0)
except NameError as e:
    print('fixed', e)
except ZeroDivisionError as e:
    print('fix zeroDivision')
# якщо не знаємо яка помилка а їх може бути багато в файлі  то він працює і обробляє з верху до низу і можемо поставити except головний
# і він виправить і покаже помилку (він знайшов хоч одну помилку,він зупиняється і іде по (except) якщо не знайде йогго то викине дію як і небуло цієї помилки )
except Exception as e:
    print(e) # division by zero
else:# працює тоді коли помилки не було
    print(' fll ok')
# finally: виконується вбудь якому випадку чи була помилка чи ні
finally:
     print('finish')


print('Hello world')