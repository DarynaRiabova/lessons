example = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]


def check_number(example):
    for item in example:
        try:
            numbers = item.split(",")
            sum = 0
            for number in numbers:
                sum += int(number)
            print(sum)
        except ValueError:
            print("Не можу це зробити")


check_number(example)
