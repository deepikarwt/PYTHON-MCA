# Search for a student by name in a CSV file.

import csv

try:
    name = input("Enter student name to search: ")

    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        found = False

        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Student record found:")
                print("Name:", row["Name"])
                print("Age:", row["Age"])
                print("Marks:", row["Marks"])
                found = True

        if not found:
            print("Student not found.")

except FileNotFoundError:
    print("CSV file not found.")

except KeyError:
    print("CSV file must contain a Name column.")