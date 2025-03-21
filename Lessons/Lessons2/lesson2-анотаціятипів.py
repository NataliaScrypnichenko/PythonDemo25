# # анотація типів- підсказки =типізація
# # щоб у функціїї написати команду потрібно вказати тип (стрінга)
# def func(name:str):
#     name.startswith('') # на яку букву починається,можемо вставляти зміні всі які можемо конвертувати в іншу(int,  bool,float,str)
#     print(name)
# # якщо масив
# list=[{'name': 'Max', 'age': 1}, {'name': 'Nata', 'age': 35}, {'name': 'kamila', 'age': 2}, {'name': 'karina', 'age': 20}]
# # типізація зміних
# def func1(names:list[str]):
#     names.sort()# методи списку
#     names[0].upper()# метод стрінги
#
# # для ф-ї
# def func2(names:list[str])->dict:# пишимо тип ключа і значення
#     name = '888'
#     return {'name':name}

##########################################################################
# біліотеки пайтона
# import typing #=забирати типи
# a:typing.Any       # це все
from typing import Any, TypedDict,Callable# краще так робити імпорт і можемо писати свої типи
a:Any='ghlol'
d: int= 1111 #можемо як хочеш типізувати

my_type= str| int | bool

def func()-> my_type: # за типом може виступати імя класу і тут ми пишемо її скілткм хочемо щоб її не розщирювати ми виносимо в окремий тип
    return 1111
    # return 'bjhhj'
    # return [] не дає

def func1()->None: # якщо ф-я не повертає нічого
    return
################################# ##################################################
# TypedDict
# так типізуємо
User=TypedDict('User',{"name":str,"age":int, "house":int})

users:list[User]=[
    {'name': 'Max', 'age': 1,'house':67},
    {'name': 'Nata', 'age': 35,'house':67},
]

# Як типізація ф-ї (a:str,b:int) це типізація (Callable)=на замиканя про типізована
def counter(a:str,b:int)->Callable[[bool,list[str]],int]:  # ф-я повертає ф-ію?[[bool,list[str]],int]=що пиймає, (,int)= що повртає=
                                                        # це є повністю протипізована ф-я
    count=0

    def inner(f:bool,y:list[str])->int: #
        nonlocal count #   дивиться на  count=0
        count+=1    # збільшує на 1
        return count  #
    return inner # повертає саму ф-ю


# ## 🔹 **Що таке `typing` у Python?**
#
# # Бібліотека **`typing`** у Python використовується для **статичної типізації**
# # (Type Hinting). Вона допомагає вказати **типи змінних, аргументів функцій і значень,
# # що повертаються**.
#
# # 📌 **Підключення бібліотеки:**
# # from typing import List, Dict, Tuple, Union, Optional
#
# ## 🔹 **Основні компоненти `typing`**
# ### **1️⃣ Просте зазначення типів**
# def greet(name: str) -> str:
#     return f"Привіт, {name}!"
# print(greet("Аня"))  # Привіт, Аня!
# 🔹 `name: str` – аргумент має бути рядком
# 🔹 `-> str` – функція повертає рядок
# ### **2️⃣ Списки (`List`)**
# # 📌 **Список цілих чисел (`List[int]`):**
# from typing import List
#
# def sum_numbers(numbers: List[int]) -> int:
#     return sum(numbers)
#
# print(sum_numbers([1, 2, 3, 4]))  # 10
# # 📌 **Список рядків (`List[str]`):**
# def join_words(words: List[str]) -> str:
#     return " ".join(words)
#
# print(join_words(["Hello", "world"]))  # Hello world
# ### **3️⃣ Словники (`Dict`)**
# # 📌 **Словник із ключами `str` і значеннями `int`:**
# from typing import Dict
#
# students: Dict[str, int] = {"Аня": 10, "Олег": 9}
# ### **4️⃣ Кортежі (`Tuple`)**
# # 📌 **Кортеж із двох чисел (`Tuple[int, int]`):**
# from typing import Tuple
#
# def get_coordinates() -> Tuple[int, int]:
#     return (10, 20)
#
# print(get_coordinates())  # (10, 20)
# ### **5️⃣ Кілька можливих типів (`Union`)**
# # Якщо функція може приймати **різні типи** даних:
# from typing import Union
#
# def convert_to_str(value: Union[int, float]) -> str:
#     return str(value)
#
# print(convert_to_str(10))  # "10"
# print(convert_to_str(5.5))  # "5.5"
# ### **6️⃣ Необов’язкові значення (`Optional`)**
# # Якщо аргумент може бути `None`:
# from typing import Optional
#
# def get_name(name: Optional[str] = None) -> str:
#     if name:
#         return f"Привіт, {name}!"
#     return "Привіт, гість!"
#
# print(get_name())       # Привіт, гість!
# print(get_name("Аня"))  # Привіт, Аня!
# # **📌 Висновок**
# ✅ `typing` **не змінює поведінку коду, а лише допомагає розробникам і аналізаторам коду**.
# ✅ Використовується в **анотаціях типів** (`List`, `Dict`, `Tuple`, `Union`, `Optional`).
# ✅ Полегшує **читабельність коду** та допомагає уникнути помилок. 🚀