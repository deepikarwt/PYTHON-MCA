# Read and display all records from a CSV file.

import csv

try:
    with open("students.csv", "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

except FileNotFoundError:
    print("CSV file not found. Run program 21 first.")