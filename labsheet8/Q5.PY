# List all tables in the database.

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")

    cursor = connection.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        ORDER BY name
    """)

    tables = cursor.fetchall()

    if tables:
        print("Tables in database:")
        for table in tables:
            print(table[0])
    else:
        print("No tables found.")

except sqlite3.Error as e:
    print("Error:", e)

finally:
    if "connection" in locals():
        connection.close()