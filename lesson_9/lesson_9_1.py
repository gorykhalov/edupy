# dict_e = ["Даниил", "Николаев", "35"]  #список

dict_e = {"name": "Даниил", "lname": "Николаев", "age": 35, "cities": ["Москва", "Казань", "Самара"], "smoke": False}
#
# print(dict_e["age"])
# print(dict_e["name"])
# print(dict_e["lname"])

# dict_ex = dict(name="Даниил", lname="Николаев")
# print(dict_ex)

# dict_ex = [["name", "Даниил"], ["lname", "Николаев"]]
# print(dict(dict_ex))

"""
ключаами могут быть 
str
int
bool
tuple
"""
# del dict_e["name"]

# print(dict_e)
# print("name" in dict_e)

# dict_ex = dict.fromkeys(["Даниил", "Николаев", "35"], "qeqwe")
# dict_ex.clear()
# dict_ex = dict_e.copy()
# dict_ex = dict(dict_e)
# dict_ex["name"] = "Даня"
# print(dict_ex["name"])
# dict_ex["345"] = "gdfhdh"
# print(id(dict_e))
# print(dict_e)
# print(id(dict_ex))
# print(dict_ex)

# name = dict_e.get("name")
# print(name)

# dict_e.setdefault("1ge", 50)
# print(dict_e)
# print(dict_e)
# str1 = dict_e.pop("name")
# print(dict_e)
# print(str1)

# print(dict_e)
# item = dict_e.popitem()
# print(dict_e)
# print(item)

# print(list(dict_e.keys()))
# print(list(dict_e.values()))
# print(list(dict_e.items())

# for k, v in dict_e.items():
#     print(k, v)

dict_e1 = {"name": "Даниил"}
dict_e2 = {"lname": "Николаев"}

dict_e1.update(dict_e2)
print(dict_e1)
print(dict_e2)

dict_res = {**dict_e1, **dict_e2}
print(dict_res)

