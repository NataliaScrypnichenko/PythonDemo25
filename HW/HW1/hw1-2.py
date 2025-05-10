# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdf56dg544 34' #введена строка
#   23,56, 544, 34              #вивело в консолі

'''st = 'as 23 fdfdg544 34'
# перетворюємо масив ch=елемент рядка
print([ch if ch.isdigit() else ' ' for ch in st])
# збираємо в стрічку
print("".join(ch if ch.isdigit() else ' ' for ch in st))
#видаляємо пробіли
print("".join(ch if ch.isdigit() else ' ' for ch in st).split())
#перетворюємо знову в стрічку
print(" ".join("".join(ch if ch.isdigit() else ' ' for ch in st).split()))'''

st = 'as 23 fdf56dg544 34'

# потрібно записати якщо число якщо ні ставимо пробіли (ch=вибор елемента)
# ітеруємо розбираємо ст
l=[ch if ch.isdigit() else  ' '  for ch in st]
print(l)
# збираємо все в стрічку
print(''.join(ch if ch.isdigit() else ' ' for ch in st))
# позбуваємось пробілів
print(''.join(ch if ch.isdigit() else ' ' for ch in st).split())
# збираємо все в стрічку
print(','.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))