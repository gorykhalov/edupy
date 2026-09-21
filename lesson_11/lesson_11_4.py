# распаковака аргументов
# def example(*args):
#     a, b, c, d = args
#     print(a, b, c, d )
#
# example(3, 5, 7, "dfsdf")
#
# def example(**kwargs):
#     print(kwargs)
#
# example(name="Artem", age="46")

def printdata(name, age):
    print(f"My name is {name} and I am {age} years old")

dict_1 = dict(name="Artem", age="46")
dict_2 = {2:50, 4:"90"}
print(dict_1)
printdata(**dict_1)

print({**dict_1, **dict_2})