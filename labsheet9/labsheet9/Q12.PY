# Insert a student into the database

import sqlite3

try:
    student_id = int(input("Enter roll number: "))
    name = input("Enter name: ").strip()
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    with sqlite3.connect("students_crud.db") as con:
        con.execute("""
            INSERT INTO students (id, name, age, marks)
            VALUES (?, ?, ?, ?)
        """, (student_id, name, age, marks))

    print("Student inserted successfully.")

except ValueError:
    print("Enter valid numeric values for roll number, age, and marks.")
except sqlite3.IntegrityError:
    print("That roll number already exists, or the record violates a constraint.")
except sqlite3.Error as e:
    print("Database error:", e)