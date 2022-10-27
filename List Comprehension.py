# List Comprehension - перевод Понимание списка!!
# Мы хотим создать список из чётных чисел в диапозоне от 1 до 100

list = []

for i in range(1, 50):
    if i % 2 != 0:
        list.append(i)
print(list)
#print(list)
# Улучшаем читабельность кода выше в строку!!
list = [i for i in range(1, 21) if i % 2 == 0]
#print(list)
# Если мы хоти получит пары чисел, делаем кортеж!!
list = [(i, i) for i in range(1, 21) if i % 2 == 0]
#print(list)
# Теперь полученые данные обработаем через функцию в кортеже!!!!

s = 1, 2, 3, 5, 8, 15, 23, 38

f = lambda x: x**2
for i in s:
    if i % 2 == 0:
        print((i, f(i)), end='')




# f = lambda x: x**3
# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)
# Вывод: [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744),
#  (16, 4096), (18, 5832), (20, 8000)]       
# выводит каждое чётное число из списка возводит в куб и делает кортеж!!