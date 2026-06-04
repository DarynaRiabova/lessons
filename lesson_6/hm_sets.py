python_students = {"Олексій", "Марія", "Ярослав", "Олена", "Дмитро"}
qa_students = {"Ярослав", "Олена", "Ірина", "Максим", "Дмитро"}

# Завдання 1.1: "Універсальні бійці"
# Знайди студентів, які одночасно навчаються і на курсі Python, і на курсі QA.
students_intersection = python_students.intersection(qa_students)
print(students_intersection)
# Завдання 1.2: "Списки на розсилку"
# Адміністрації академії потрібно зібрати повний список усіх унікальних студентів обох курсів, щоб надіслати їм спільне оголошення. Дублікатів імен у списку бути не повинно.
students_union = python_students.union(qa_students)
print(students_union)
# Завдання 2.1: "Суто програмісти"
# Знайди студентів, які вчать Python, але взагалі не цікавляться курсом QA.
students_difference = python_students.difference(qa_students)
print(students_difference)
# Завдання 2.2: "Тільки один курс"
# Знайди студентів, які обрали для себе тільки один напрямок (або суто Python, або суто QA), тобто виключи тих, хто ходить на обидва курси одночасно.
students_symmetric_difference = python_students.symmetric_difference(qa_students)
print(students_symmetric_difference)

active_users = [101, 102, 105, 107, 110, 120]
premium_users = [102, 105, 110, 115, 130]
churned_users = [105, 140, 115]
active_users = set(active_users)
premium_users = set(premium_users)
churned_users = set(churned_users)
# Завдання 3: "Аналітика SaaS-платформи" (Велика задача)
# Уяви, що ти працюєш над SaaS-платформою. У тебе є три списки ID користувачів:

# active_users — ті, хто заходив на платформу цього місяця.
# premium_users — ті, хто купив преміум-підписку.
# churned_users — ті, хто написав у саппорт і видалив акаунт.

# Тобі потрібно написати код, який відповість на 3 питання бізнесу:
#
# Які преміум-користувачі були активними цього місяця? (Кому не дарма капає підписка).
premium_active_users = premium_users.intersection(active_users)
print(premium_active_users)
# Які преміум-користувачі взагалі не заходили на платформу? (Їм треба надіслати email-нагадування, бо вони скоро скасують підписку).
premium_not_active_users = premium_users.difference(active_users)
print(premium_not_active_users)
# Чи є серед активних користувачів ті, хто вже офіційно вважається видаленим (churned_users)? (Якщо є, то це критичний баг у базі даних!).
fake_active_churned_users = active_users.intersection(churned_users)
print(fake_active_churned_users)
