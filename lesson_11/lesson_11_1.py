# Функции

def print_text(addtext):
    text = f"текст для печати: {addtext}"
    print("addtext" , id(addtext))
    print(text)

str1 = "Курс от Даниила"
int1 = 1212

# print("str1", id(str1))
# print_text(str1)

def summarize_two(x, y):
    res1 = x + y
    return res1

def multiply_two(x, y):
    res2 = x * y
    return res2

def common(x, y):
    return summarize_two(x, y), multiply_two(x, y)

# print(common(4, 5))

# summa1, mult1 = summarize_two(1, 2)
# res = summarize_two(1, 2)
# print(res)
# print(summa1)
# print(mult1)

def is_negative(x):
    return x < 0

# print(is_negative(0))
# print(is_negative(5))
# print(is_negative(-5))

lst = [1, 0, -4, -7, -120]

for i in lst:
    if is_negative(i):
        print(i, end=" ")