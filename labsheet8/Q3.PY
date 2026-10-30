# Create the students table.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            marks REAL
        )
    """)

    connection.commit()
    print("Students table created successfully!")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()