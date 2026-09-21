# Передача позиционных и именованнных аргументов

# def get_num (x, y, z=5): # значение по умолчанию
#     print("x = ", x)
#     print("y = ", y)
#     print("z = ", z)

x1 = 1
y1 = 2
z1 = 3
# get_num(x1, y1, z1)
# get_num(y = x1, z = y1, x = z1)
# get_num (3 , 6)

# def get_lower_or_upper_str(str1, lower=True, upper=False):
#     if lower:
#         return str1.lower()
#     elif upper:
#         return str1.upper()
#     else:
#         return str1
#
# print(get_lower_or_upper_str("Артем"))
# print(get_lower_or_upper_str(str1= "Артем", lower=False))
# print(get_lower_or_upper_str(str1= "Артем", lower=False, upper=True))

def add_value(value, lst=None):
    if not lst:
        lst = []
    lst.append(value)
    return lst

print(add_value(1))
print(add_value(5, []))
print(add_value(2))
