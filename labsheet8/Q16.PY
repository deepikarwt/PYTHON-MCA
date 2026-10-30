# Update marks using a student's ID.

import sqlite3

try:
    student_id = int(input("Enter student ID: "))
    new_marks = float(input("Enter new marks: "))

    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        UPDATE students
        SET marks = ?
        WHERE id = ?
    """, (new_marks, student_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Marks updated successfully.")
    else:
        print("Student ID not found.")

except ValueError:
    print("Enter a valid ID and marks.")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()