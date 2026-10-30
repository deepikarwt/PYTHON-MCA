# Create a new SQLite database.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    print("Database created successfully!")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()