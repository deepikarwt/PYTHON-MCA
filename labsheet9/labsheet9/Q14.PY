# Search for a student by roll number

import sqlite3

try:
    roll = int(input("Enter roll number to search: "))

    with sqlite3.connect("students_crud.db") as con:
        cursor = con.execute(
            "SELECT id, name, age, marks FROM students WHERE id = ?",
            (roll,)
        )
        student = cursor.fetchone()

    if student:
        print("Student found:")
        print(
            f"Roll: {student[0]}, Name: {student[1]}, "
            f"Age: {student[2]}, Marks: {student[3]}"
        )
    else:
        print("Student not found.")

except ValueError:
    print("Roll number must be an integer.")
except sqlite3.Error as e:
    print("Database error:", e)