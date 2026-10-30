# Create a CSV file and write student records.

import csv

try:
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write the column headings.
        writer.writerow(["Name", "Age", "Marks"])

        # Write student records.
        writer.writerow(["Asha", 20, 85])
        writer.writerow(["Ravi", 21, 91])
        writer.writerow(["Neha", 19, 78])

    print("CSV file created successfully.")

except OSError as e:
    print("Error:", e)