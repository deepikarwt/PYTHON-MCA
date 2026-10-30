# Calculate the sum and average of numbers in a file.

try:
    with open("numbers.txt", "r") as file:
        numbers = [
            float(line.strip())
            for line in file
            if line.strip()
        ]

    if numbers:
        total = sum(numbers)
        average = total / len(numbers)

        print("Numbers:", numbers)
        print("Sum:", total)
        print("Average:", average)
    else:
        print("No numbers found.")

except FileNotFoundError:
    print("Numbers file not found.")

except ValueError:
    print("Invalid number in the file.")