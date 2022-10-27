# Три версии создания файла

colors = ['Red', 'Green', 'Blue123']
data = open('File.txt', 'w')
data.writelines(colors)
# data.write('\nLine 11\n')
# data.write('Line 14\n')
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('Line 112\n')
#     data.write('Line 113\n')
#     data.write('Line 114\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# exit()


# def concatenatio(*params):
#     res: str = '' # Если хотим работать исключительно со строками, а если с числами то int = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'f', 'g')) # asdfg
# print(concatenatio('a', '1')) # a1
#print(concatenatio(1, 2, 3, 4, 5)) # TypeError

# Рекурсия 

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортежи
# a = (3, 4, 45, 7)
# print(a)
# print(a[0])
# a[0] = 12 Присваивание в кортеже нельзя
# for item in a:
#     print(item)

# Словари

dictionary = {} # Пустой словарь
dictionary = \
    {
        'up': 'Верх',
        'left': 'Влево',
        'right': 'Вправо',
        'down': 'Вниз'
    }
# print(dictionary['up'])
# dictionary['up'] = '3'
# print(dictionary['up'])   
# print(dictionary)
# print(dictionary['left'])

#for k in dictionary.keys():

#Списки

list1 = [1, 2, 3, 4, 5]

#print(list1.pop(2))# Удаление из списка по индексу
#print(list1.insert(2, 11))# Вставить в список по индексу
print(list1.append(3)) # Вставить элемент в конец списка
print(len(list1))
print(list1)

# list2 = list1
# list1[0] = 123
# list2[1] = 333
# for e in list1:
#     print(e)     
# print()
# for e in list2:
#     print(e)     
