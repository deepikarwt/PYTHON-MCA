# Use separate functions to insert and fetch student records.

import sqlite3

def insert_student(student_id, name, age, marks):
    """Insert a student into the database."""
    connection = sqlite3.connect("student_db.db")

    try:
        connection.execute("""
            INSERT INTO students (id, name, age, marks)
            VALUES (?, ?, ?, ?)
        """, (student_id, name, age, marks))

        connection.commit()
        print("Student inserted successfully.")

    except sqlite3.Error as e:
        print("Insert error:", e)

    finally:
        connection.close()


def fetch_students():
    """Fetch and display all student records."""
    connection = sqlite3.connect("student_db.db")

    try:
        cursor = connection.execute("SELECT * FROM students")
        records = cursor.fetchall()

        for record in records:
            print(record)

        if not records:
            print("No student records found.")

    except sqlite3.Error as e:
        print("Fetch error:", e)

    finally:
        connection.close()


# Main program
try:
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    insert_student(student_id, name, age, marks)

    print("\nStudent records:")
    fetch_students()

except ValueError:
    print("Please enter valid numeric values.")