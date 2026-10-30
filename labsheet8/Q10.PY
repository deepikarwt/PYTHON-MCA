# Display all students.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if records:
        for record in records:
            print(record)
    else:
        print("No student records found.")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()