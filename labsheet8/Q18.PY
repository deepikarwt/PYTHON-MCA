# Delete one student using their ID.

import sqlite3

try:
    student_id = int(input("Enter student ID to delete: "))

    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (student_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student ID not found.")

except ValueError:
    print("Enter a valid student ID.")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()