'''
Декоратор, позволяющий вызвать ф-ию заданное количество раз
A decorator that allows you to call a function a specified number of times
'''

from functools import wraps

n = int(input('Количество вызовов функции: '))


def repeat(n: int):
    def inner_func(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(function(*args, **kwargs))
            return

        return wrapper

    return inner_func


@repeat(n)
def greet():
    return 'HELLO world'


greet()
