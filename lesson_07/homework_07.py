# task 1
"""Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def count_sum(a, b):
    result = a + b
    return result


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average(n):
    return sum(n) / len(n)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def string(text):
    return text[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def len_word(words):
    return max(words, key=len)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):

    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# 1
# apples = 2
# banana = apples * 4
# print(f"Яблук: {apples}, бананів: {banana}")
def calculate(apples_count):

    bananas_count = apples_count * 4
    return print(f"Яблук: {apples_count}, бананів: {bananas_count}")


# 2 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
def calculate_perimeter(side_1, side_2, side_3, side_4):
    perimeter = side_1 + side_2 + side_3 + side_4
    return perimeter


# 3 У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?
def calculate_trees(apples_count):
    pears_count = apples_count + 5
    plums_count = apples_count - 2
    total_trees = apples_count + pears_count + plums_count
    return total_trees


# 4
def calculate_evening_temperature(morning_temperature):

    afternoon_temperature = morning_temperature - 10
    evening_temperature = afternoon_temperature + 4
    return evening_temperature
