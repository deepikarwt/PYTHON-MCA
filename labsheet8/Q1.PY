# Connect to an SQLite database.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    print("Database connected successfully!")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if "connection" in locals():
        connection.close()