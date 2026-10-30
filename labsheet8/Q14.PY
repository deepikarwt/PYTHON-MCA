# Count the total number of students.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        SELECT COUNT(*) FROM students
    """)

    count = cursor.fetchone()[0]
    print("Total students:", count)

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()