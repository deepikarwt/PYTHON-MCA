# Count student records

import sqlite3

try:
    with sqlite3.connect("students_crud.db") as con:
        cursor = con.execute("SELECT COUNT(*) FROM students")
        total = cursor.fetchone()[0]

    print("Total number of student records:", total)

except sqlite3.Error as e:
    print("Database error:", e)