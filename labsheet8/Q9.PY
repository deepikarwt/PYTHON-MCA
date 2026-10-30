# Insert multiple student records.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    students = [
        (2, "Priya", 21, 92),
        (3, "Rahul", 20, 76),
        (4, "Neha", 19, 88),
        (5, "Karan", 22, 35)
    ]

    connection.executemany("""
        INSERT INTO students (id, name, age, marks)
        VALUES (?, ?, ?, ?)
    """, students)

    connection.commit()
    print("Multiple records inserted successfully.")

except sqlite3.IntegrityError as e:
    connection.rollback()
    print("Insertion failed. Check for duplicate IDs:", e)

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()