# Display all students, including those without a course.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        SELECT students.name, courses.course_name
        FROM students
        LEFT JOIN courses
        ON students.id = courses.student_id
    """)

    for row in cursor.fetchall():
        print("Student:", row[0], "| Course:", row[1])

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if "connection" in locals():
        connection.close()