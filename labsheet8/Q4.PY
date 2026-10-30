# Display the structure of the students table.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("PRAGMA table_info(students)")

    print("ID | Name | Data Type | Not Null | Primary Key")

    for column in cursor.fetchall():
        print(column)

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()