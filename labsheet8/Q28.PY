# Demonstrate handling of SQLite database errors.

import sqlite3

connection = None

try:
    connection = sqlite3.connect("student_db.db")

    # This query intentionally uses a nonexistent table
    # to demonstrate exception handling.
    connection.execute("SELECT * FROM unknown_table")

except sqlite3.Error as e:
    print("Database error occurred:")
    print(type(e).__name__)
    print("Error details:", e)

finally:
    if connection is not None:
        connection.close()
        print("Database connection closed.")