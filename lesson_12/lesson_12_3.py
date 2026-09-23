# замыкание - функция которая запоминает переменные из своего окружения даже после завершения своего выполнения

def say_name(name):
    def say_gb():
        print(f"Пока, {name}")

    return say_gb

say_dan = say_name("ДАНИИЛ")
say_igor = say_name("ИГОРЬ")

say_dan()
say_igor()


def printsome():
    print(1234)

print(say_dan.__closure__)   # проверка функции является ли она замыкающей или не является
print(printsome.__closure__)


