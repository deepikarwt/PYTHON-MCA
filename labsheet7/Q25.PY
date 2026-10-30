# Append a new student record to an existing CSV file.

import csv

try:
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, marks])

    print("New record added successfully.")

except FileNotFoundError:
    print("CSV file not found.")

except ValueError:
    print("Enter a valid age and marks.")

except OSError as e:
    print("Error:", e)