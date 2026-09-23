from functools import wraps

def logger(printres=True):
    def logger_inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"функция: {func.__name__}\nНеименованные аргументы :{args}\nИменованные аргументы :{kwargs} ")
            result = func(*args, **kwargs)
            if printres:
                print(f"Результат функции: {result}")
            return result
        return wrapper
    return logger_inner


@logger()
def sum(a, b):
    return a + b

res = sum(3, b=5)
print(sum.__name__)
