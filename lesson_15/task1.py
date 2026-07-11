import csv
import os

print(os.getcwd())
print(os.listdir())
rows = []

file1 = open("lesson_15/random.csv", "r", encoding="utf-8")
reader1 = csv.reader(file1)

for row in reader1:
    if row not in rows:
        rows.append(row)

file2 = open("lesson_15/rmc.csv", "r", encoding="utf-8")
reader2 = csv.reader(file2)

for row in reader2:
    if row not in rows:
        rows.append(row)

result = open("lesson_15/result_ryabova.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(result)

for row in rows:
    writer.writerow(row)

file1.close()
file2.close()
result.close()

print("work")
