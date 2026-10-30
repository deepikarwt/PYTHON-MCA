# Insert one student record.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    student = (1, "Aman", 20, 85.5)

    connection.execute("""
        INSERT INTO students (id, name, age, marks)
        VALUES (?, ?, ?, ?)
    """, student)

    connection.commit()
    print("Student record inserted successfully.")

except sqlite3.IntegrityError:
    print("This student ID already exists.")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()