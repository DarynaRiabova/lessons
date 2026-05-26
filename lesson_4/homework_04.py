adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
replace_task1 = adwentures_of_tom_sawer.replace("\n", " ")
# task 02 ==
""" Замініть .... на пробіл
"""
replace_task2 = replace_task1.replace("....", " ")
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
task3 = " ".join(replace_task2.split())
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""


def task4_count_h():
    task4 = 0
    for h in adwentures_of_tom_sawer:
        if h == "h":
            task4 += 1
    return task4


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""


def task5_count_upper():
    task5 = 0

    words = task3.split()
    for word in words:
        if word[0].isupper():
            task5 += 1

    return task5


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

first_index = adwentures_of_tom_sawer.find("Tom")

second_index = adwentures_of_tom_sawer.find("Tom", first_index + 1)

print(second_index)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
task8 = adwentures_of_tom_sawer[3].strip().lower()
print(task8)
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
task9 = "By the time" in adwentures_of_tom_sawer
print(task9)
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence_words = adwentures_of_tom_sawer_sentences[-1].split()
task10 = len(last_sentence_words)
print(task10)
