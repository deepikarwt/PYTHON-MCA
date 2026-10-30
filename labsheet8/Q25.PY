# Group students by age and count each group.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        SELECT age, COUNT(*)
        FROM students
        GROUP BY age
        ORDER BY age
    """)

    print("Age | Number of students")

    for age, count in cursor.fetchall():
        print(age, "|", count)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if "connection" in locals():
        connection.close()