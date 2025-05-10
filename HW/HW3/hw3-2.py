# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод
# котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
from itertools import count


class Hunam():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Hunam):
    __count = 0 ## це не розуміла
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size
        Cinderella.__count += 1 ## це не розуміла
    def __str__(self):  # виводить
        return str (self.__dict__)

    # це не розуміла
    @classmethod # викликає ім'я класу
    def get_count(cls): # видає
        print(cls.__count) # виводить


class Prince(Hunam):
    def __init__(self, name, age,size_shoes):
        super().__init__(name, age)
        self.size_shoes = size_shoes
# це не розуміла
    def find_cinderella(self, cinderella_list:list[Cinderella]): # приймати список попелюшок
        for cinderella in cinderella_list: # шукати ту саму
            if cinderella.size==self.size_shoes:
                print(cinderella)
                return


cinderella_list:list[Cinderella]=[
    Cinderella ('Mariy', 25 ,36),
    Cinderella ('Marta', 15 ,38),
    Cinderella ('Masha', 20 ,39),
    Cinderella ('Nata', 24 ,40)
]
prince =Prince("Sasha", 25 ,36)

prince.find_cinderella(cinderella_list) # знаходить принцесу

Cinderella.get_count() # показує скільки було принцес