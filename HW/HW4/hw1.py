#1) Створити файл email.txt та наповнити його інформацію наступного формату (використайте для цього ШІ).
#
# 9d3dc7094d3dcb31ffe2960ad891dd04 34hrap@gmail.com
#
# ec4f2883e9eb74770d02b30f06659a5f tele_nat@mail.i
#
# 44ab3c993daee2a9655925d53fbdd7bf telepaev.sn@gmail.com
#
# ваша задача:  записати в новий файл тільки email’ /-ли з доменом gmail.com

try:
    with open('email.txt') as source, open('gmail.txt', 'w') as target:
        for line in source:
            email = line.split()[-1] # убераємо пробіли
            if email.endswith('gmail.com'): # перевіряє, чи закінчується рядок вказаним суфіксом
               #target.write(email)
               target.write(f'{email}\n') # буде із пробілами
               # print(email, file=target) # за допомогою прінта записується з пробілом в файл
except Exception as e:
    print(e)