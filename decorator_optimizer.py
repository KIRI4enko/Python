'''
    Декоратор-оптимизатор
    Decorator-optimizer
'''
from functools import wraps


def cache(size):
    cache_dir = {}

    def f(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            name = str(function.__name__) + '(' + ','.join(list(map(str, args))) + ')'

            if name in cache_dir.keys():
                return cache_dir[name]

            else:
                cache_dir[name] = function(*args, **kwargs)
                if size is not None:
                    if len(cache_dir) > size:
                        cache_dir.pop(list(cache_dir.keys())[0])


            return cache_dir[name]

        return wrapper

    return f


@cache(None)
def f(a):
    return a ** 2

