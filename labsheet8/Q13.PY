# Display students from highest to lowest marks.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        SELECT * FROM students
        ORDER BY marks DESC
    """)

    for record in cursor.fetchall():
        print(record)

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()