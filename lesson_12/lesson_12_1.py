#  lambda функция  (испольщуется внутри других функций)

mult = lambda a, b : a * b

# def mult (a, b):                  # тоже самое что и lambda
#     return a * b

print(type(mult))
print(mult( 5, 6))

lst_1 = ["Курск", "Уфа", "Казань"]
sorted_lst = sorted(lst_1, key=lambda word: len(word))
print(sorted_lst)

func = lambda word: len(word)    # запись строго в 1 строку
func2 = lambda x: x + 5
print(func2(10))