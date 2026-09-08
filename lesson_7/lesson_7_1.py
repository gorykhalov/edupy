# num = 1000
# summa = 0
# i = 1
#
# while i <= num:
#      summa += i
#      i += 1
#
# print(summa)
import numbers

# correct_pwd = "пароль123"
# input_pwd = input("Введите пароль: ")
#
# while input_pwd != correct_pwd:
#     print("пароль не верен")
#     input_pwd = input("Введите пароль: ")
#
# print("пароль верен")


# correct_pwd = "пароль123"
# input_pwd = input("Введите пароль: ")
# counter = 1
#
# while input_pwd != correct_pwd:
#     print(f"пароль введен неправильно {counter} раз")
#     input_pwd = input("Введите пароль: ")
#     counter += 1
#     if counter == 5:
#         print(f"пароль нвведен неправильно {counter} раз. программа завершена")
#         break

# numbers = [23, 43, 75, 33, 80, 51, 62]
# result = []
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         result.append(numbers[i])
#     i += 1
# print(result)

num = 1
res_sum = 0
while num != 0:
    input_num = input("Введите целое число или 0 для выхода: ")
    if not input_num.isdigit():
        print("Введено не число, перезапустите программу")
        break
    num = int(input_num)

    if num % 2 == 0:
        continue
    res_sum += num
else:
    print(res_sum)