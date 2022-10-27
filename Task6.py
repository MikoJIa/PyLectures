import json
# В файле хранятся числа, нужго выбрать чётные и составить список пар(число, квадрат числа)
# Пример:1 2 3 5 8 15 23 38
# Получить [(2, 4), (8, 64), (38, 1444)]

with open ('fileTask1.txt', 'w+') as data:
    data.write('1 2 3 5 8 15 23 38')
path = 'fileTask1.txt'
data = open(path, 'r')
for line in data:
    print(line)
res = line.split()
print(res)
m = list(map(int, res))
f = lambda x: x**2
for i in m:
    if i % 2 == 0:
        print((i, f(i)), end='')

# f.close()
# exit()

# def select(f, col): функция select нам по сути не нужна если мы используе функцию map!!!!
#     return [f(x) for x in col]
# def where(f, col): функцию where можно заменить на функцию filter()
#     return [x for x in col if f(x)]


# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# Использование функции map!!

# li = [x for x in range(1, 21)]
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int,'1 2 3 4 5'.split()))
# for i in data:
#     print(i)

# print('---','=)', 'map - это итератор, который проходится по числа только 1 раз')
# # но если в коде прописать что это список через функцию list, итераций будет несколько
# for i in data:
#     print(i)

# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта 
# и возвращяет итератор с теми объектами, для которых функция вернула True.
# Пример: f(x) => x - чётное
# filter = (f[1, 2, 3, 4, 5, 6])
# итог - [2, 4, 6]
# нельзя пройтись дважды!!!!!
# data = [x for x in range(1, 10)]
# res = list(filter(lambda x: not x % 2, data))
# print(res)

# Функция zip - приминяется к набору итерируемых объектов и возвращяет итератор с кортежами из
# элементов входных данных
# zip = ([1,2,3], ['о','д','е'], ['f','s','t'])
# [(1, 'о', 'f'), (2, 'д', 's'), (2, 'о', 't')]
# Нельзя пройтись дважды

# user = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 17]
# solure = [111, 222, 333]
#data = list(zip(user, ids, solure))
#print(data)
# Функция enumerate()
user = ['user1','user2','user3','user4','user5']
# data = list(enumerate(user))
# print(data)