# Delete student by roll number

students = [
    {"roll": 101, "name": "Aman", "age": 20, "marks": 85},
    {"roll": 102, "name": "Priya", "age": 21, "marks": 92},
    {"roll": 103, "name": "Rahul", "age": 20, "marks": 76}
]

try:
    roll = int(input("Enter roll number to delete: "))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully.")
            break
    else:
        print("Student not found.")

    print("Remaining records:", students)

except ValueError:
    print("Roll number must be an integer.")