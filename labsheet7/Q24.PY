# Count rows and columns in a CSV file.

import csv

try:
    with open("students.csv", "r", newline="") as file:
        rows = list(csv.reader(file))

    if rows:
        print("Number of columns:", len(rows[0]))
        print("Number of data rows:", len(rows) - 1)
        print("Total rows including header:", len(rows))
    else:
        print("CSV file is empty.")

except FileNotFoundError:
    print("CSV file not found.")