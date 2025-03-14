#хочу масив від 0 до 100
l=[i for i in range(100)]
print(l)
#  використовувати можна для фільтрів мапів
d=[4,2,7,2,4,1]
#записати тілтки парні значення
res=[i for i in d  if i%2==0]
print(res)
# кожне значення хочу перемножити на 2
res=[i*2 for i in d]
print(res)
# можна поєднати
res=[i*2 for i in d if i%2==0]
print(res)
# перемножити всі парні і залишити всі інші(якщо if  інакше else отже for )
res=[i*2 if i%2==0 else i  for i in  d]
print(res)

l2d=[
    [1,2,3,4,5],
    [6,7,8,9,10]
]
# хочу вирівняти в один масив
l2=[i for j in l2d for i in j]
print(l2)
# звичайний цикл
l=[]
for j in l2d:
    for i in j:
        l.append(i)
print(l)