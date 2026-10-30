# Display the first and last lines of a file.

try:
    with open("sample.txt", "r") as file:
        lines = file.read().splitlines()

    if lines:
        print("First line:", lines[0])
        print("Last line:", lines[-1])
    else:
        print("File is empty.")

except FileNotFoundError:
    print("File not found.")