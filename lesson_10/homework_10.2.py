from abc import abstractmethod


class Figure:
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side


class Rectangle(Figure):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def area(self):
        return self.__a * self.__b

    def perimeter(self):
        return 2 * (self.__a + self.__b)


figures = [Square(5), Rectangle(4, 6)]
for figure in figures:
    print("area:", figure.area())
    print("perimeter:", figure.perimeter())
    print()
