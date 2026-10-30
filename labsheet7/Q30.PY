# Combine multiple CSV files into one CSV file.

import csv
import os

files = ["students.csv", "students_extra.csv"]
output_file = "combined_students.csv"

try:
    header = None
    combined_rows = []

    for filename in files:
        if not os.path.exists(filename):
            print("File not found:", filename)
            continue

        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            current_header = next(reader, None)

            if current_header is None:
                continue

            if header is None:
                header = current_header
            elif current_header != header:
                print("Skipping file with different columns:", filename)
                continue

            combined_rows.extend(reader)

    if header is not None:
        with open(output_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(combined_rows)

        print("CSV files combined successfully.")
        print("Output file:", output_file)
    else:
        print("No valid CSV files found.")

except OSError as e:
    print("Error:", e)