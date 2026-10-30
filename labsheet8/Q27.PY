# Import student records from a CSV file into SQLite.

import sqlite3
import csv

try:
    with open("students_import.csv", "r", newline="",
              encoding="utf-8") as file:
        reader = csv.DictReader(file)
        records = [
            (
                int(row["id"]),
                row["name"],
                int(row["age"]),
                float(row["marks"])
            )
            for row in reader
        ]

    connection = sqlite3.connect("student_db.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students_import (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            marks REAL
        )
    """)

    connection.executemany("""
        INSERT OR REPLACE INTO students_import
        (id, name, age, marks)
        VALUES (?, ?, ?, ?)
    """, records)

    connection.commit()
    print("CSV data imported successfully.")

except (sqlite3.Error, OSError, ValueError, KeyError) as e:
    print("Import error:", e)

finally:
    if "connection" in locals():
        connection.close()