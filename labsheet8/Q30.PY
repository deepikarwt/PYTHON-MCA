# Menu-driven student management system using SQLite.

import sqlite3

DATABASE = "student_db.db"


def create_table():
    """Create the students table if it does not exist."""
    connection = sqlite3.connect(DATABASE)

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                marks REAL
            )
        """)
        connection.commit()

    finally:
        connection.close()


def add_student():
    """Add a new student."""
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter name: ").strip()
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        with sqlite3.connect(DATABASE) as connection:
            connection.execute("""
                INSERT INTO students (id, name, age, marks)
                VALUES (?, ?, ?, ?)
            """, (student_id, name, age, marks))

        print("Student added successfully.")

    except ValueError:
        print("Enter valid numeric values.")

    except sqlite3.Error as e:
        print("Database error:", e)


def view_students():
    """Display all students."""
    try:
        with sqlite3.connect(DATABASE) as connection:
            cursor = connection.execute(
                "SELECT * FROM students ORDER BY id"
            )
            records = cursor.fetchall()

        if records:
            print("\nID | Name | Age | Marks")
            print("-" * 30)

            for record in records:
                print(
                    record[0], "|",
                    record[1], "|",
                    record[2], "|",
                    record[3]
                )
        else:
            print("No students found.")

    except sqlite3.Error as e:
        print("Database error:", e)


def update_student():
    """Update a student's marks using their ID."""
    try:
        student_id = int(input("Enter student ID: "))
        marks = float(input("Enter new marks: "))

        with sqlite3.connect(DATABASE) as connection:
            cursor = connection.execute("""
                UPDATE students
                SET marks = ?
                WHERE id = ?
            """, (marks, student_id))

        if cursor.rowcount:
            print("Student marks updated.")
        else:
            print("Student ID not found.")

    except ValueError:
        print("Enter valid numeric values.")

    except sqlite3.Error as e:
        print("Database error:", e)


def delete_student():
    """Delete a student using their ID."""
    try:
        student_id = int(input("Enter student ID to delete: "))

        with sqlite3.connect(DATABASE) as connection:
            cursor = connection.execute("""
                DELETE FROM students
                WHERE id = ?
            """, (student_id,))

        if cursor.rowcount:
            print("Student deleted successfully.")
        else:
            print("Student ID not found.")

    except ValueError:
        print("Enter a valid student ID.")

    except sqlite3.Error as e:
        print("Database error:", e)


# Main menu
try:
    create_table()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

except sqlite3.Error as e:
    print("Database initialization error:", e)