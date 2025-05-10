# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()  @abstractmethod
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який
# наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є
#            класом Book або Magazine інакше ігрнорувати додавання  @classmethod
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу @classmethod
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу @classmethod
'''# Приклад:
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()
#'''
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
'''Метод isinstance() у Python — це вбудована функція, яка перевіряє, чи є об'єкт певного типу (класу).
isinstance() також враховує успадкування'''
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This is Magazine {self.name}')

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'This is Book {self.name}')

class Main:
    __printable_list:list[Printable]=[]

    @classmethod
    def add(cls, item: Book | Magazine):
        if isinstance(item, ( Magazine, Book)):# одночасно провір'яє магазин і книгу
            cls.__printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list: # провір'яє
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_book(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))
Main.add(Magazine('Magazine3'))
Main.add(Book('Book3'))

Main.show_all_magazines()
print('-' * 60)
Main.show_all_book()