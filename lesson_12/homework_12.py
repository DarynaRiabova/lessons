import unittest


def count_sum(a, b):
    result = a + b
    return result


class CountSumTest(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(count_sum(3, 3), 6)

    def test_add_negative_numbers(self):
        self.assertEqual(count_sum(-3, -3), -6)

    def test_add_positive_and_negative(self):
        self.assertEqual(count_sum(6, -2), 4)


def average(n):
    return sum(n) / len(n)


class AverageTest(unittest.TestCase):
    def test_average_positive_numbers(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3)

    def test_average_negative_numbers(self):
        self.assertEqual(average([-2, -4, -6]), -4)


def string(text):
    return text[::-1]


class StringTest(unittest.TestCase):
    def test_reverse_one_character(self):
        self.assertEqual(string("d"), "d")

    def test_reverse_word(self):
        self.assertEqual(string("hello"), "olleh")

    def test_reverse_number_string(self):
        self.assertEqual(string("123"), "321")

    def test_reverse_empty_string(self):
        self.assertEqual(string(""), "")


def calculate(apples_count):

    bananas_count = apples_count * 4
    return f"Яблук: {apples_count}, бананів: {bananas_count}"


class CalculateTest(unittest.TestCase):
    def test_apples_1(self):
        self.assertEqual(calculate(1), "Яблук: 1, бананів: 4")

    def test_apples_0(self):
        self.assertEqual(calculate(0), "Яблук: 0, бананів: 0")

    # з цього тесту видно, що треба правити фунцію, щоб такий сценарій не був можливий.
    def test_apples_negative(self):
        self.assertEqual(calculate(-1), "Яблук: -1, бананів: -4")


if __name__ == "__main__":
    unittest.main()
