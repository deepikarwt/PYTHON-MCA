# Find the student who obtained the highest marks.

import csv

try:
    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    if students:
        highest_student = max(
            students,
            key=lambda student: float(student["Marks"])
        )

        print("Student:", highest_student["Name"])
        print("Highest marks:", highest_student["Marks"])
    else:
        print("No student records found.")

except FileNotFoundError:
    print("CSV file not found.")

except (ValueError, KeyError):
    print("Invalid or missing Marks column.")