# Save student records to a text file and read them

filename = "students.txt"

try:
    n = int(input("How many students? "))

    with open(filename, "w", encoding="utf-8") as file:
        for i in range(n):
            print(f"\nStudent {i + 1}")
            roll = input("Roll number: ").strip()
            name = input("Name: ").strip()
            marks = float(input("Marks: "))

            # Use a separator to store the fields.
            file.write(f"{roll}|{name}|{marks}\n")

    print("\nStudent data saved successfully.")

    print("\n--- Student Records ---")
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            roll, name, marks = line.strip().split("|")
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}")

except ValueError:
    print("Please enter a valid number for marks or student count.")
except OSError as e:
    print("File error:", e)