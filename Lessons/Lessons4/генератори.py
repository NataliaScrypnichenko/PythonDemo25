# генератори описує що він повинен робити зі слідуючим кроком= це дуже економить память
# Генератори в Python — це спеціальні функції, які повертають значення поступово (одне за одним),
# не зберігаючи весь результат у пам’яті.
# 🔹 Відмінність від звичайних функцій:
# Замість return вони використовують ключове слово yield.
# 🔧 Переваги генераторів:
# Економлять пам’ять — не створюють повний список у пам’яті
# Швидші при роботі з великими обсягами даних
# Зручно для обробки потоків, файлів, нескінченних послідовно.
#
#
# Все що ми зберігаємо в зміних залишається воперативній памяті і займає її

# l=[i for i in range(50_000_000)]# воно буде давати кожний крок, але я хочу, щоб на кожній етереції дав щось інше тут використовуємо генератор
 # g=(i for i in range(50_000_000)) # генератори пишуться вкруглих душках,/ оперативна память використовується менше
# це інструкція по якій ми можемо ходити і ітеруватися,можемо писати умови писати як в list
# input()
# ЯК ПРАЦЮВАТИ З ЦИМ
'''g= (i for i in range(50_000_000))
# print(type(g)) # <class 'generator'>
# print(next(g))   # next звертаються до генератора і бере якийсь елемент, то б то перший працює як цикл # 0(по генератору можна пройтись
# # тільки в одну сторону і можна це робити в той момент коли це необхідно). можна взяти одне знначення і зробити зним якісь задачі
# print('some home')
# print(next(g))
# також можна пройтися фором
for i in g:
    print(i) # викликає той самий next'''
# g=(i for i in range(7))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# генератори можна створювати за допомогою ф-ї їх більше застосовують

'''def gen(name:str):
    for ch in name: # проходимося по кожній букві # return ch # зупиняє функцію
        yield ch  # він повертає з ф-ї, але не зупиняє роботу всіє її функцію, він її призупиняє тобто ось тут
        print('Hello') # він дасть букву М, а потім зупиниться і виконає Hello, а потім (а) тому що  він зупинився і робить далі, а потім видає
g =gen('Max') # в генератор вя кому віддаю Макса він тепер відасть об'єкт генератора після цього можна визати next
print(next(g))
print(next(g))
print(next(g))'''

#
'''def gen():
    yield 1
    yield 2
    yield 3
    yield 4
    return 'my return' # можна також використовувати / він дасть помилку, і потім можна дістати 'my return' через виправлення помилки
g=gen()
try:
    print(next(g))  # 1
    print(next(g))  # 2
    print(next(g))  # 3
    print(next(g))  # 4
    print(next(g))
except StopIteration as e:
    print(e) # my return '''

# приблизно жо реальності(човниковий біг 2 команди носять воду у відрі по черзі) це можна реалізувати за допомогою генератора

'''def gen1(n):# приймає кількість учасників команди
    for i in range(1,n+1): # проходимося по учаснику із команди починаючи з першого
         yield f'{i}-Time1' # видаємо учасника і підписуємо з якої команди
# те саме для другої команди
def gen2(n):
    for i in range(1,n+1):
         yield f'{i}-Time2'

# Робимо масив із команд які будуть мати готові генератори
teams=[gen1(5), gen2(7)] # кожний по черзі бігає з відром по воду до басейну
# реалізуємо, щоб вони бігали по черзі
while teams:
    team=teams.pop(0) # звертаємось до teams і методом pop() забераємо першого учасника з gen1(5) потім gen2(7)

    try:
        print(next(team)) # буду друкувати те що генератор team буде віддавати- то б то хто з якої команди
        teams.append(team) # якщо генератор не закінчився і не попав в помилку то його додаємо в масив
    except StopIteration:
        pass
'''

# потрібно генерувати нове ім'я файла і тут знаюмлюсь із бібліотекою uuid
import  uuid

def gen_jpg_file(): # генерувати нове ім'я кожного файла щоб не співпадало  \ вона не приймає нічого
    pattern = '{}.jpg'
    while True: # запускаємо безкінечний цикл
        yield pattern.format(uuid.uuid1()) # перебираємо pattern і передаємо uuid1(файл який створився впевний час)генерує на сонові часу

file_gen = gen_jpg_file()
print(next(file_gen))# коли потрібно ім'я файла нове