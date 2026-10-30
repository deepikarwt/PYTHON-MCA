# Delete the students table from the database.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    connection.execute("DROP TABLE IF EXISTS students")
    connection.commit()

    print("Students table deleted successfully.")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()