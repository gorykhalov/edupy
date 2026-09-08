# numbers = [23, 43, 75, 33, 80, 51, 62]
# for num in numbers:
#     print("Печатаем: ", num)

# for letter in "Даниил":
#     print("Буква:", letter)

# numbers = [23, 43, 75, 33, 80, 51, 62]
# for num in numbers:
#     num = 0
#
# print(numbers)


# print(list(range(0,10,2)))

# numbers = [23, 43, 75, 33, 80, 51, 62]
# for i in range(len(numbers)):
#     numbers[i] = 0
#
# print(numbers)

words = ["Привет,", "Даниил,", "как" , "дела?"]
result_str = ""
for word in words:
    result_str += " " + word

print(result_str.lstrip())