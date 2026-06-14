# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
#  який дозволяє змінювати середній бал студента. Виведіть інформацію про студента та змініть його
# середній бал.


class Student:
    def __init__(self, name, surname, age, average_score):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def show_info(self):
        print(
            f"Student: {self.name} {self.surname}. "
            f"Age: {self.age}. "
            f"Average score: {self.average_score}"
        )

    def change_average_score_and_show_info(self, new_score):
        self.average_score = new_score
        print(
            f"Student: {self.name} {self.surname}. "
            f"Age: {self.age}. "
            f"Average score: {self.average_score}"
        )


student1 = Student("Daryna", "Riabova", 90, 85)
student1.show_info()
student1.change_average_score_and_show_info(92)
