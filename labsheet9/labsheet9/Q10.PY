# File-based CRUD using JSON for persistent storage

import json
import os

FILENAME = "student_records.json"


def load_records():
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as e:
        print("Could not read records:", e)
        return []


def save_records(records):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)


while True:
    print("\n--- File CRUD Menu ---")
    print("1. Add record")
    print("2. View records")
    print("3. Modify record")
    print("4. Delete record")
    print("5. Exit")

    choice = input("Enter choice: ").strip()
    records = load_records()

    try:
        if choice == "1":
            roll = int(input("Roll number: "))

            if any(r["roll"] == roll for r in records):
                print("Roll number already exists.")
                continue

            name = input("Name: ").strip()
            age = int(input("Age: "))
            marks = float(input("Marks: "))

            records.append({
                "roll": roll,
                "name": name,
                "age": age,
                "marks": marks
            })
            save_records(records)
            print("Record added successfully.")

        elif choice == "2":
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found.")

        elif choice == "3":
            roll = int(input("Roll number to modify: "))
            record = next(
                (r for r in records if r["roll"] == roll), None
            )

            if record:
                record["name"] = input("New name: ").strip()
                record["age"] = int(input("New age: "))
                record["marks"] = float(input("New marks: "))
                save_records(records)
                print("Record updated successfully.")
            else:
                print("Record not found.")

        elif choice == "4":
            roll = int(input("Roll number to delete: "))
            updated = [r for r in records if r["roll"] != roll]

            if len(updated) < len(records):
                save_records(updated)
                print("Record deleted successfully.")
            else:
                print("Record not found.")

        elif choice == "5":
            print("Exiting.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid numeric values.")
    except OSError as e:
        print("File error:", e)