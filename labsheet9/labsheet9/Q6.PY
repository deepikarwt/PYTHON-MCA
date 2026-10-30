# CRUD operations using a dictionary

employees = {}

while True:
    print("\n--- Employee Management ---")
    print("1. Add employee")
    print("2. View employees")
    print("3. Update employee")
    print("4. Delete employee")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        emp_id = input("Employee ID: ").strip()

        if emp_id in employees:
            print("Employee ID already exists.")
        else:
            name = input("Employee name: ").strip()
            salary = input("Salary: ").strip()

            try:
                salary = float(salary)
                employees[emp_id] = {
                    "name": name,
                    "salary": salary
                }
                print("Employee added successfully.")
            except ValueError:
                print("Salary must be numeric.")

    elif choice == "2":
        if not employees:
            print("No employees found.")
        else:
            for emp_id, data in employees.items():
                print(emp_id, data)

    elif choice == "3":
        emp_id = input("Employee ID to update: ").strip()

        if emp_id in employees:
            employees[emp_id]["name"] = input("New name: ").strip()
            try:
                employees[emp_id]["salary"] = float(
                    input("New salary: ")
                )
                print("Employee updated successfully.")
            except ValueError:
                print("Invalid salary.")
        else:
            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Employee ID to delete: ").strip()

        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")