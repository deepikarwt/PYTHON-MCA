# Export all student records into a CSV file.

import sqlite3
import csv

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        SELECT id, name, age, marks
        FROM students
    """)

    records = cursor.fetchall()

    with open("students_export.csv", "w", newline="",
              encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["id", "name", "age", "marks"])
        writer.writerows(records)

    print("Data exported to students_export.csv")

except (sqlite3.Error, OSError) as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()