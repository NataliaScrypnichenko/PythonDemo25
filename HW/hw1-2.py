# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34'
# перетворюємо масив ch=елемент рядка
print([ch if ch.isdigit() else ' ' for ch in st])
# збираємо в стрічку
print("".join(ch if ch.isdigit() else ' ' for ch in st))
#видаляємо пробіли
print("".join(ch if ch.isdigit() else ' ' for ch in st).split())
#перетворюємо знову в стрічку
print(" ".join("".join(ch if ch.isdigit() else ' ' for ch in st).split()))