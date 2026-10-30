# Copy all CSV data into another CSV file.

import csv

try:
    with open("students.csv", "r", newline="") as source:
        rows = list(csv.reader(source))

    with open("students_copy.csv", "w", newline="") as destination:
        writer = csv.writer(destination)
        writer.writerows(rows)

    print("CSV data copied successfully.")

except FileNotFoundError:
    print("Source CSV file not found.")

except OSError as e:
    print("Error:", e)