# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма ПЛОЩИН двох екземплярів ксласу
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
        self.area = self.x * self.y # потрібно її сюди винисти(я зробила помилку)

    # def __str__(self):
    #     return  str (self. __dict__)- це не потрібно робити в виведені мат.фігур.

    def __add__(self, other: Self): #  + сумма
        return self.area + other.area # Vself.x - other.y=так не потрібно робити моя помилка

    def __sub__(self, other: Self): # - різниця
       return self.area - other.area

    def __eq__(self, other: Self): # == площин def __eq__(self, other)=не вірно
        return self.area == other.area

    def __ne__(self, other: Self):
        return self.area != other.area

    def __lt__(self, other: Self):  # < меньше
        return self.area < other.area

    def __gt__(self, other: Self):  #  > більше
        return self.area > other.area

    # def __len__(self, other: Self):
    #     return self.area + self.area=не вірно

    def __len__(self):  # при виклику метода len() підраховувати сумму сторін
        return (self.x + self.y) *  2

r1=Rectangle(6,8)
r2=Rectangle(3,4)
print(r1+r2)
print(r1-r2)
print(r1 == r2)
print(r1 != r2)
print(r1 > r2)
print(r1 < r2)
print(len(r1))
print(len(r2))

'''зробила сама не вірно,формули прописала тільки сторони а не врахувала площину,не написала в загальном площину'''