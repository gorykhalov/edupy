a = [21, 54, 6.55, 567, 23242, 50]
print(a)

a.append(200)
a.append(290)
# a.append(False)
# a.append([True, False])
# a.insert(1, 53)
# print(a)
# a.remove(False)
# print(a)
# last_el = a.pop()
# print(a)
# print(last_el)

# index_el = a.pop(2)
# print(index_el)
# print(a)

# a.clear() #очистка списка
# print(a)

"""
b = a[:]
b = list(a)
"""
b = a.copy()

# print(b)
# print(id(a))
# print(id(b))
# print(a)
# print(a.count(False)) #найти элемент в списке
print(a)
# print(a.index(50, 4)) #найти индекс элемента

a.reverse()
print(a)

a.sort()
print(a)
a.sort(reverse=True)
print(a)

с = sorted(a)
print(с)