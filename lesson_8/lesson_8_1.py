"""
Итерируемые объекты:
строки (str)
списки (list)
кортежи (tuple)
диапазоны чисел (range)
словари (dict)
множества (set)
"""
from time import sleep

# numbers = [34, 63, 53, 93, 1, 0, 31]
# it_numbers = iter(numbers)
# print(type(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))
# print(next(it_numbers))

str1 = "Васисуалий"
it_str1 = iter(str1)
# print(type(it_str1))
# print(next(it_str1))
# print(next(it_str1))
# print(next(it_str1))
# print(next(it_str1))
# sleep(3)
# print(next(it_str1))
# print(next(it_str1))

for letter in str1:
    print(letter)