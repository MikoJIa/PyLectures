def calculater(expression):
    allowed = '+-*/'
    if not any(sing in expression for sing in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак {allowed}')
    for sing in allowed:
        if sing in expression:
            try:
                left, right = expression.split(sing)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sing](left, right)
            except(ValueError, TypeError):
                raise ValueError(f'Выражение должно содержать два целых числа')


def plus(a, b):
    return a + b


if __name__ == '__main__':
    print(plus(10, 10))