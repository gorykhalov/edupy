# глобальные и локальные переменные

# NAME = "АРТЕМ"
#
# def func():
#     name = "артем"
#     print(NAME)
#
# func()
# print(NAME)
# print(name)    # локальная переменная внутри функции

"""
Очередность поиска переменных:
Local  локальная переменная (внутри функции)
global глобальная переменная (вне функции)
Built-in встроенная в пайтон  print, str и пр.
"""

# NAME = "АРТЕМ"
#
# def update_name():
# #   global NAME   # объявляем что берем глобально
#     global x # создаем глобальную переменную внутри функции
#     x = "Игорь"
#     NAME = "12345"
#     print(NAME)
#
# update_name()
# print(NAME)
# print(x)

# NAME = "АРТЕМ"

def update_name():
    NAME = "Даниил"
    def update_name2():
        nonlocal NAME   # создаем нелокальную переменную внутри вложенной функции что бы использовать ее в наружней
        NAME = "Игорь"
        print("update_name2", NAME)
    update_name2()
    print("update_name", NAME)

update_name()
