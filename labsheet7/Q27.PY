# Display only the Name and Marks columns.

import csv

try:
    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            print("CSV file has no header.")
        elif "Name" not in reader.fieldnames or "Marks" not in reader.fieldnames:
            print("Required columns were not found.")
        else:
            print("Name\tMarks")

            for row in reader:
                print(row["Name"], "\t", row["Marks"])

except FileNotFoundError:
    print("CSV file not found.")