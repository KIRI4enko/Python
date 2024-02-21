'''
    Декоратор-логгер
    Decorator-logger
'''
from functools import wraps


def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        res = None
        try:
            res = function(*args, **kwargs)
        except TypeError:
            print('Вы неправильно ввели аргументы')
        except ZeroDivisionError:
            print('НЕЛЬЗЯ ДЕЛИТЬ НА 0!!!')
        else:
            print(f'Выполнилась фунцкия {function.__name__},\nкоторая приняла в себя два аргумента', *args,
                  *kwargs.values(), f'.\nРезультат: {res}')
        finally:
            return res

    return wrapper


@logger
def div(a: (float, int), b: (float, int)):
    return a / b


div(10, 2)
