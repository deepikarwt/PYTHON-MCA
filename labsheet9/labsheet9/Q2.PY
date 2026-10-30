# Display student records

students = [
    {"roll": 101, "name": "Aman", "age": 20, "marks": 85},
    {"roll": 102, "name": "Priya", "age": 21, "marks": 92},
    {"roll": 103, "name": "Rahul", "age": 20, "marks": 76}
]

if not students:
    print("No student records found.")
else:
    print("\nStudent Records")
    for student in students:
        print(
            f"Roll: {student['roll']}, "
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Marks: {student['marks']}"
        )