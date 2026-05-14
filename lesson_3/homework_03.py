import math
alice_in_wonderland = """Would you tell me, please, which way I ought to go from here?
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where -—" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," 
Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, 
if you only walk long enough."""

for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)

print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
area_1 = 436402
area_2 = 37800
final_area = area_1 + area_2

print(f"The area is {final_area}")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
full_storage = 375291
storage_1_2 = 250449
storage_2_3 = 222950

storage_3 = full_storage - storage_1_2
storage_2 = storage_2_3 - storage_3
storage_1 = storage_1_2 - storage_2

print(f"Storage 1: {storage_1}")
print(f"Storage 2: {storage_2}")
print(f"Storage 3: {storage_3}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months = 18
monthly_payment = 1179
computer_price = months * monthly_payment

print(f"Final price is {computer_price}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_price = 274
medium_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21

big_pizza_total = 4 * big_pizza_price
medium_pizza_total = 2 * medium_pizza_price
juice_total = 4 * juice_price
cake_total = 1 * cake_price
water_total = 3 * water_price

total_price = (
    big_pizza_total
    + medium_pizza_total
    + juice_total
    + cake_total
    + water_total
)

print(f"Total price is {total_price}")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo = 232
one_page = 8
result = 232//8

print (f"final result is {result}")

#також можна зробити іншим способом

photo = 232
one_page = 8
pages = math.ceil(photo / one_page)

print(f"Final result is {pages}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_km = 1600
fuel_per_100km = 9
tank_capacity = 48
total_fuel_needed = distance_km / 100 * fuel_per_100km
refuels_needed = math.ceil(total_fuel_needed / tank_capacity)

print(f"Total fuel needed: {total_fuel_needed} liters")
print(f"Refuels needed: {refuels_needed}")