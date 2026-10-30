# Delete students whose marks are below 40.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        DELETE FROM students
        WHERE marks < ?
    """, (40,))

    connection.commit()

    print("Records deleted:", cursor.rowcount)

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()