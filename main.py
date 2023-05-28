# Практическое задание 3
import random


def one():
    n = int(input("Введите количество слов: "))

    result = ""

    for i in range(n):
        word = input(f"Введите слово №{i + 1}: ")
        result += word + " "

    print("Результат:", result.strip())


def two():
    result = ""
    i = 0
    Check = True
    while Check == True:

        i += 1
        word = input(f"Введите слово №{i}: ")
        result += word + " "
        stop = input("Хотите продолжить? ")
        if stop == "Нет" or stop == "нет":
            Check = False

    print("Результат:", result.strip())


def three():
    found = False
    word = input("Введите слово: ")

    while found == False:
        if word.find("ф") != -1 or word.find("Ф") != -1:
            print("Ого! Это редкое слово")
            found = True
        else:
            return print("Эх, это не очень редкое слово")


def four():
    errors = 3
    correct = 0
    while errors != 0:

        x = random.randint(0, 100)
        y = random.randint(0, 100)
        anwser = int(input(f"{x} + {y} = "))
        if anwser == x + y:
            print("Правильно!")
            correct += 1
        else:
            print("Ответ неверный")
            errors -= 1
    print(f"Игра окончена! Правильных ответов: {correct}")
# one()
# two()
# three()
# four()