# Display students scoring more than 80 marks.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        SELECT * FROM students
        WHERE marks > ?
    """, (80,))

    records = cursor.fetchall()

    for record in records:
        print(record)

    if not records:
        print("No students scored above 80.")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()