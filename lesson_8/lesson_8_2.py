N = 5

# res = []
# for num in range(1, N + 1):
#     res.append(num ** 2)

# res = [ num ** 2 for num in range(1, N + 1) ]

# numbers = [34, 63, 53, 93, 1, 0, 31]
# res_numbers = [num > 35 for num in numbers ]
#
# print(res_numbers)
#
# numbers = [34, 63, 53, 93, 1, 0, 31]
# res_numbers = [num for num in numbers if num > 35 or num == 0 ]
#
# print(res_numbers)

# numbers = [-1, 3, 5, -4, 0, 12, -921]
# # res = []
# # for n in numbers:
# #     if n >= 0:
# #         res.append(f"{n} - положительное")
# #     else:
# #         res.append(f"{n} - отрицательное")
#
# res = [f"{n} - положительное" if n >=0 else f"{n} - отрицательное" for n in numbers ]
# print(res)

# table_multiply = [
#     f"{x} * {y} = {x * y}"
#     for x in range (1, 10)
#     for y in range (1, 10)
# ]
# print(table_multiply)

table_multiply = []
for x in range(1, 10):
    for y in range(1, 10):
        table_multiply.append(f"{x} * {y} = {x * y}")
print(table_multiply)