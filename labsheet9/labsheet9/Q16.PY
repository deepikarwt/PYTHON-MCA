# Delete a student record

import sqlite3

try:
    roll = int(input("Enter roll number to delete: "))

    with sqlite3.connect("students_crud.db") as con:
        cursor = con.execute(
            "DELETE FROM students WHERE id = ?",
            (roll,)
        )

        if cursor.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

except ValueError:
    print("Roll number must be an integer.")
except sqlite3.Error as e:
    print("Database error:", e)