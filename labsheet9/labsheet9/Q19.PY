# Find the student with the highest marks

import sqlite3

try:
    with sqlite3.connect("students_crud.db") as con:
        cursor = con.execute("""
            SELECT id, name, age, marks
            FROM students
            WHERE marks = (SELECT MAX(marks) FROM students)
        """)
        rows = cursor.fetchall()

    if rows and rows[0][3] is not None:
        print("Student(s) with the highest marks:")
        for row in rows:
            print(
                f"Roll: {row[0]}, Name: {row[1]}, "
                f"Age: {row[2]}, Marks: {row[3]}"
            )
    else:
        print("No student marks are available.")

except sqlite3.Error as e:
    print("Database error:", e)