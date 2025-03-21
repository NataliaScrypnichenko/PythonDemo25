#
# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки
# (також використовуемо типізацію)
#
# Приклад:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
#

def expanded_form(num:int)->str:
        st=str(num) # перетворюємо число в стрінгу
        length = len(st)-1 # віднімаються 0 від числа і розбиває його
        result = [ ] # записуємо результат
        for i, char in enumerate(st): # розбтраю кожне число масива
            if char!=0:
                result.append(char + "0" * (length-i)) # додаємо 0 з кінця
        return '+'.join(result)+ f' = {st}' # об'єднює результат і додає

print(expanded_form(42))
print(expanded_form(70304))
print(expanded_form(12))