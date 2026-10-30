# DELETE removes all records but preserves the table structure.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    connection.execute("DELETE FROM students")
    connection.commit()

    print("All records deleted.")
    print("The students table still exists.")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()