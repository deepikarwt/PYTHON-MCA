# Connect to SQLite and create the students table

import sqlite3

try:
    with sqlite3.connect("students_crud.db") as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                marks REAL
            )
        """)

    print("Database connected successfully.")
    print("Students table created or already exists.")

except sqlite3.Error as e:
    print("Database error:", e)