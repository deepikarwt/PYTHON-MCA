# Display only student names and marks.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        SELECT name, marks
        FROM students
    """)

    for name, marks in cursor.fetchall():
        print("Name:", name, "| Marks:", marks)

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()