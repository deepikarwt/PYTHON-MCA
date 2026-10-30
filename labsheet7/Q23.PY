# Calculate the average of numeric CSV columns.

import csv

try:
    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        columns = reader.fieldnames or []

    if not rows:
        print("No records found.")
    else:
        for column in columns:
            try:
                values = [float(row[column]) for row in rows]

                average = sum(values) / len(values)
                print(f"Average of {column}: {average:.2f}")

            except (ValueError, TypeError):
                # Skip columns containing non-numeric data.
                continue

except FileNotFoundError:
    print("CSV file not found. Run program 21 first.")