###
set
###

# set_1 = {1, 2, 5, True, "stroka", (7, 9)}
# print(set_1)

"""
Изменяемые типы данных
list
dict
set

Неизменяемые типы данных
int
float
tuple
str
bool
"""
# set_2 = {} # Создастся словарь
# set_3 = set()
# print(type(set_2))
# print(type(set_3))

lst = [1, 2, 4, 5, 6, 6, (1, 2), (1, 2)]
# print(set(lst))   # при создании множества удаляются дубли и повторы
# str_1 = "qweqweqwe"
# print(set(str_1))  # при создании множества удаляются дубли и повторы букв
# range_1 = range(5)
# print(set(range_1))

set_4 = set(lst)
# print(len(set_4))
# print((1, 2) in set_4)

# for i in set_4:
#     print(i)    # вывод элементов мгножества в цикле

# it = iter(set_4)
# print(next(it))

# set_4.add("hello")
# print(set_4)
#
# set_4.update(["fsdf", "hrth", "546"])
# print(set_4)
# set_4.update("sdgdhge")   # строку разложит на буквы а если в []  то нет
# print(set_4)
#
# set_4.discard("hello") # извлечение элемента из множества так же работает метод .remove
# print(set_4)
#
# set_4.clear()  # очистка множества
# print(set_4)

set_6 = {1, 2, 3, 4, 5}
set_7 = {4, 5, 6, 7, 8}
set_8 = {9, 10}

# res = set_6 & set_7      # пересечение множеств
# res = set_6.intersection(set_7)   # пересечение множеств
# print(res)

# res = set_8 & set_7  # если нет общих элементов то пустое множество
# print(res)

# set_6 &= set_7  # удаление из сета 6 всех элементов не находящихся в сет 7  с изменением исходного мгножества
# print(set_6)

# res = set_6 | set_7 | set_8    # объединение множеств
# res = set_6.union(set_7)   # объединение множеств
# print(res)

# set_6 |= set_7    # {1, 2, 3, 4, 5, 6, 7, 8}
# print(set_6)

# res = set_6 - set_7   # вычитание множеств
# res = set_6.difference(set_7)    # вычитание множеств
# set_6 -= set_7    # вычитание с изменением исходного множества
# print(set_6)

# res = set_6 ^ set_7   # все элементы кроме общих(пересеченных)
# res = set_6.symmetric_difference(set_7)      # все элементы кроме общих(пересеченных)
# set_6 ^= set_7 # извлечение общих элементов с изменением исходного множества
# print(set_6)

print (set_6 != set_8)  # сравнение множеств





