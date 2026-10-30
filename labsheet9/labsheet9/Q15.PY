# Update marks of a student

import sqlite3

try:
    roll = int(input("Enter roll number: "))
    new_marks = float(input("Enter new marks: "))

    with sqlite3.connect("students_crud.db") as con:
        cursor = con.execute(
            "UPDATE students SET marks = ? WHERE id = ?",
            (new_marks, roll)
        )

        if cursor.rowcount > 0:
            print("Student marks updated successfully.")
        else:
            print("Student not found.")

except ValueError:
    print("Enter a valid roll number and marks.")
except sqlite3.Error as e:
    print("Database error:", e)