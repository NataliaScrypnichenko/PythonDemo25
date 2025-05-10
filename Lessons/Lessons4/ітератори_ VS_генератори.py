# будуємо свій рендж range = він іє генератор 28:47
# приклад нв класі але потім все це замінемо на гкнератор

class MyRange:
    def __init__(self, length): # приймає довжину MyRange
        self.__length = length  # будн приватною зміною
        self.__counter= 0       # самий початок буде 0

    def __iter__(self):  # він вказує на об'єкт в якому буде реалізованй фунцкіонал  next=це протокол по якому він буде щось віддавати
        return self # щоб не ускладнювати об'єктом буде self і в ньому реалізуємо next

    def __next__(self): # - next як раз описуємо логіку по якій щось буде віддаватися
        if self.__counter < self.__length: #якщо буде менша self.__counter
            res=self.__counter # то буде зміна res як = __counter
            self.__counter += 1  # __counter збільшує на 1
            return res   # повертаємо результат
        raise StopIteration   # якщо не підпадає під цю умову, то будемо кидати помилку (через спеціально raise)


for i in MyRange(5):
    print(i) # 0 1 2 3 4

# тепер через генератор менше коду
def my_range(length): # даємо довжину
    counter = 0 #
    while counter < length: # якщо counter менше, то він віддає його і збільшує на 1
        yield counter  #
        counter += 1 #


for i in my_range(5):
    print(i)  # 0 1 2 3 4



