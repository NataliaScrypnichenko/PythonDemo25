from operator import index

l=[1,2,3,4,5]

l.append(78)# додати щось
print(l)
# # 🔹 Метод append() у Python
# # Метод append() додає один елемент в кінець списку.
# # ✅ Синтаксис:
# # список.append(елемент)
# # елемент — це значення, яке додається до кінця списку. Це може бути будь-який тип даних: число, рядок, список, об'єкт тощо.
# # ✅ Приклад використання append()
# список = [1, 2, 3]
# список.append(4)  # Додаємо число 4 в кінець списку
# print(список)  # [1, 2, 3, 4]
# # ✅ Додавання різних типів даних
# список = [1, "яблуко", True]
# список.append(3.14)  # Додаємо число з плаваючою точкою
# список.append([5, 6])  # Додаємо список
# print(список) #[1, 'яблуко', True, 3.14, [5, 6]]
# #  Зверни увагу: метод append() додає цілий об'єкт в кінець списку. У випадку додавання списку (як у прикладі вище)
# #  він буде доданий як один елемент, а не по елементах.
# # ✅ Використання в циклі
# список = []
# for i in range(5):
#     список.append(i)
# print(список)  # [0, 1, 2, 3, 4]
# # ✅ Додавання елементів в список з користувацьким ввід
# список = []
# елемент = input("Введіть елемент для списку: ")
# список.append(елемент)  # Додаємо введене значення в список
# print(список)
# # 🟢 Висновок
# # 📌 Метод append() дозволяє додавати елементи в кінець списку.
# # 📌 Він змінює сам список, додаючи новий елемент, і не повертає жодного значення (повертає None).

l.insert(2,89) # вставити щось, птшемо індекс а потім елемент який вставляємо
print(l)
# # 🔹 Метод insert() у Python
# # Метод insert() дозволяє вставити елемент на конкретну позицію в списку, вказавши індекс, де елемент буде розташований.
# # ✅ Синтаксис:
# # список.insert(індекс, елемент)
# # індекс — це позиція в списку, на яку ви хочете вставити елемент.
# # елемент — це значення, яке ви хочете вставити.
# # 📌 Зверніть увагу: Елементи після вставленого елемента зміщуються на одну позицію вправо.
# # ✅ Приклад використання insert()
# список = [1, 2, 3]
# список.insert(1, 4)  # Вставляє 4 на позицію 1
# print(список)  # [1, 4, 2, 3]
# # Тут ми вставляємо число 4 на позицію з індексом 1. Тобто між елементами 1 і 2.
# # ✅ Додавання в початок списку
# список = [2, 3, 4]
# список.insert(0, 1)  # Вставляє 1 на початок списку
# print(список)  # [1, 2, 3, 4]
# # У цьому випадку елемент 1 вставляється на першу позицію (індекс 0).
# # ✅ Додавання в кінець списку
# # Якщо ви хочете додати елемент в кінець списку, можна використати insert() з індексом, який дорівнює довжині списку:
# список = [1, 2, 3]
# список.insert(len(список), 4)  # Додає 4 в кінець
# print(список)  # [1, 2, 3, 4]
# # Це те ж саме, що і використання методу append().

pop=l.pop() # по замовчувані видаляє останній елемент і зберігає його в зміні # видаляє також по індексу pop(3)
print(pop)
print(l)

a=[34,55,66,77,66,55,34,88]
a2=[11,22,33,44]
a.remove(34)# видаляє по значенню і видаляє перше значення знайдене з ліва на право
print(a)

a.extend(a2) # розширити один список іншим і додає він його в кінець списка
print(a)
a3=a+a2
print(a) # можна додавати і отримаємо новий список
# або
a+=a2
print(a)

a.index(55) # знайти індекс по значеню
print(a.index(55))
print(a.index(55,3, 20))# можна задавати проміжки з чого задавати-стар і стоп

d=[4,5,77,6,78,94,56,77]
d.reverse()#перевернути список з ліва на право
print(d)

d.sort()# можемо сортувати
d.sort(reverse=True)# можна посортувати в зворотньому напряму
print(d)

d.count(77) #порахувати елементи по їх кількостi
print(d.count(77))

#d.clear() #очистити список
print(d)

d1=d[1:4]#  зрізи, за допомогою нього можемо створити новий масив,вказуємо з якого до якого індикса робимо зріз?0 можемо пропускати і воно буде зрізати з 0
d[::2]# зріз з початку до кінця кроком 2
d[::-2] # можна в зворотньому напряму.
print(d1)
