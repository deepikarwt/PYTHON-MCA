# Menu-driven Student CRUD Application using SQLite

import sqlite3

DB_NAME = "students_crud.db"


def create_table():
    """Create the students table if it does not exist."""
    with sqlite3.connect(DB_NAME) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                marks REAL
            )
        """)


def add_student():
    """Add a new student record."""
    try:
        roll = int(input("Enter roll number: "))
        name = input("Enter student name: ").strip()
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        if not name:
            print("Student name cannot be empty.")
            return

        with sqlite3.connect(DB_NAME) as con:
            con.execute("""
                INSERT INTO students (id, name, age, marks)
                VALUES (?, ?, ?, ?)
            """, (roll, name, age, marks))

        print("Student added successfully.")

    except ValueError:
        print("Please enter valid numeric values.")
    except sqlite3.IntegrityError:
        print("This roll number already exists.")
    except sqlite3.Error as e:
        print("Database error:", e)


def view_students():
    """Display all student records."""
    try:
        with sqlite3.connect(DB_NAME) as con:
            rows = con.execute("""
                SELECT id, name, age, marks
                FROM students
                ORDER BY id
            """).fetchall()

        if not rows:
            print("No student records found.")
            return

        print("\n--- Student Records ---")
        print("-" * 50)

        for row in rows:
            print(
                f"Roll: {row[0]}, Name: {row[1]}, "
                f"Age: {row[2]}, Marks: {row[3]}"
            )

    except sqlite3.Error as e:
        print("Database error:", e)


def search_student():
    """Search for a student using roll number."""
    try:
        roll = int(input("Enter roll number to search: "))

        with sqlite3.connect(DB_NAME) as con:
            row = con.execute("""
                SELECT id, name, age, marks
                FROM students
                WHERE id = ?
            """, (roll,)).fetchone()

        if row:
            print("Student found:", row)
        else:
            print("Student not found.")

    except ValueError:
        print("Roll number must be an integer.")
    except sqlite3.Error as e:
        print("Database error:", e)


def update_student():
    """Update a student's marks."""
    try:
        roll = int(input("Enter roll number to update: "))
        marks = float(input("Enter new marks: "))

        with sqlite3.connect(DB_NAME) as con:
            cursor = con.execute("""
                UPDATE students
                SET marks = ?
                WHERE id = ?
            """, (marks, roll))

        if cursor.rowcount > 0:
            print("Student marks updated successfully.")
        else:
            print("Student not found.")

    except ValueError:
        print("Enter valid numeric values.")
    except sqlite3.Error as e:
        print("Database error:", e)


def delete_student():
    """Delete a student using roll number."""
    try:
        roll = int(input("Enter roll number to delete: "))

        with sqlite3.connect(DB_NAME) as con:
            cursor = con.execute("""
                DELETE FROM students
                WHERE id = ?
            """, (roll,))

        if cursor.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    except ValueError:
        print("Roll number must be an integer.")
    except sqlite3.Error as e:
        print("Database error:", e)


def main():
    """Display the menu and execute the selected operation."""
    try:
        create_table()

        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student Marks")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                update_student()
            elif choice == "5":
                delete_student()
            elif choice == "6":
                print("Thank you for using the application.")
                break
            else:
                print("Invalid choice. Select from 1 to 6.")

    except sqlite3.Error as e:
        print("Unable to initialize the database:", e)


if __name__ == "__main__":
    main()