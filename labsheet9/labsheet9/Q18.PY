# Display students in alphabetical order

import sqlite3

try:
    with sqlite3.connect("students_crud.db") as con:
        cursor = con.execute("""
            SELECT id, name, age, marks
            FROM students
            ORDER BY name ASC
        """)
        rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(
                f"Roll: {row[0]}, Name: {row[1]}, "
                f"Age: {row[2]}, Marks: {row[3]}"
            )
    else:
        print("No student records found.")

except sqlite3.Error as e:
    print("Database error:", e)