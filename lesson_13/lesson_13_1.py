# декораторы это функции которые принимают в качестве аргументов другие функции и дополняют их собственной логикой

# def decor(func):
#         def wrapper(*args, **kwargs):
#             print("До выполнения функции")
#             print("args", args)
#             print("kwargs", kwargs)
#             func(*args, **kwargs)
#             print("После выполнения функции")
#
#         return wrapper
#
# @decor                            # пример вызова декоратора
# def print_text(text):
#     print(f"Простой текст, {text}")
#
# print_text(text="Доп текст")

# decor_print_text = decor(print_text)   # 2 пример вызова декоратора
# decor_print_text()
import time
def count_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения - {end_time - start_time} сек")
        return result
    return wrapper

@count_timer
def func_1():
    time.sleep(3)
    print("func_1 отработала")
    return "Возврат из функции"

# res = (func_1())
# print(res)

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"функция: {func.__name__}\nНеименованные аргументы :{args}\nИменованные аргументы :{kwargs} ")
        result = func(*args, **kwargs)
        print(f"Результат функции: {result}")
        return result
    return wrapper

@count_timer
@logger
def sum(a, b):
    return a + b

res = sum(3, b=5)
print(res)
