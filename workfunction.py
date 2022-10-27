# Функция с двумя переменными!!!!
# def sum(x, y):
#     return x + y
sum = lambda x, y: x + y

# def mult(x, y):
#     return x * y
mult = lambda x, y: x * y

def calc(op, a, b):
    print(op(a, b))
    # return (op(a, b))


calc(sum, 4, 4)
calc(mult, 4, 5)
# calc(lambda x, y: x + y, 5, 5)
