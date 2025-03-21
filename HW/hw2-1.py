# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# def notedook():
#     todo_list=[]
#     def add_todo(todo):
#         pass
#     def get_all():
#         pass
#
# #     return ...
# 2) протипізувати перше завдання
from typing import Callable

# типізуємо про писані нище ф-ї
def notebook():  #  -> tuple[Callable[[str], None],[Callable[[],list[str]]]:
    todo_list: list[str]=[]

    def add_todo(todo:str)->None:
        nonlocal todo_list # додаємо список в локальне сховище
        todo_list.append(todo) # додавати список

    def get_all()->list[str]:
        nonlocal todo_list # додаємо список в локальне сховище
        return todo_list.copy() #тому що на  todo_list не буде доступу із зовні тільки через ці 2-ї

    return add_todo, get_all

# створюємо 2 списка
add1, get_all1 = notebook()
add2, get_all2 = notebook()
#додаємо
add1 ('coffe')
add2 ('appel')
#виводимо
print(get_all1())
print(get_all2())


