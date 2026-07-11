#  генератор, який повертає послідовність парних чисел від 0 до N.
def numbers(n):
    for number in range(0, n + 1, 2):
        yield number


for number in numbers(20):
    print(number)


# генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    first = 0
    second = 1

    while first <= n:
        yield first
        first, second = second, first + second


for number in fibonacci(10):
    print(number)


# ітератор для зворотного виведення елементів списку.
class Reverse:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = len(numbers)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1
        return self.numbers[self.index]


numbers = [1, 2, 3, 4, 5]

for number in Reverse(numbers):
    print(number)


# ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > self.n:
            raise StopIteration

        result = self.number
        self.number += 2
        return result


for number in EvenNumbers(10):
    print(number)


# декоратор, який логує аргументи та результати викликаної функції.
def logger(func):
    def wrapper(*args, **kwargs):
        print("arg:", args, kwargs)

        result = func(*args, **kwargs)

        print("result:", result)
        return result

    return wrapper


@logger
def add(a, b):
    return a + b


add(1, 2)


# декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print("Error:", error)

    return wrapper


@exception
def divide(a, b):
    return a / b


print(divide(20, 2))
print(divide(30, 0))
