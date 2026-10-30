# Create the courses table and insert sample data.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            student_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    courses = [
        (101, "Python", 1),
        (102, "Database Management", 2),
        (103, "Web Development", 3),
        (104, "Java", None)
    ]

    connection.executemany("""
        INSERT OR IGNORE INTO courses
        (course_id, course_name, student_id)
        VALUES (?, ?, ?)
    """, courses)

    connection.commit()
    print("Courses table created and data inserted.")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if "connection" in locals():
        connection.close()