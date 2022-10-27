# def calc(x):
#     return x+10
# # print(calc(10))
# def calc2(x):
#     return x*10
# # print(calc2(10))
# def math(op, x):
#     print(op(x))
# math(calc2, 10)
# math(calc, 10)
# Функция с двумя переменными!!

def sum(x, y):
    return x+y 
# функцию которая выше можно заменить с использованием lambda!
# Пример:
sum = lambda x, y: x+y

def mylt(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    
calc(sum, 4, 5)
calc(lambda x, y: x+y, 4, 5)
