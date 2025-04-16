# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

from typing import Self
class Rectangle: # прямоугольник

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return  str (self. __dict__)

    def __add__(self, other: Self): #  + сумма
        return self.x + other.y

    def __sub__(self, other): # - різниця
       return self.x - other.y

    def __eq__(self, other): # == площин
        return self.x == other.y

    def __ne__(self, other):
        return self.x != other.y

    def __lt__(self, other):  # < меньше
        return self.x < other.y

    def __gt__(self, other):  #  > більше
        return self.x > other.y

    def __len__(self,other):
        return self.x + self.y

r1=Rectangle(4,3)
r2=Rectangle(8,9)
# print(r1 + r2) # 13
# print(r1 - r2) # -5
# print(r2 < r1) # False
# print(r1 > r2) # False
# print(r1 == r2) # False
# print(r1 != r2) # True
print(len(r1+r2)) #

