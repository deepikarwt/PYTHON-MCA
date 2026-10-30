# Read and display a file line by line.

try:
    with open("sample.txt", "r") as file:
        for line_number, line in enumerate(file, start=1):
            print(line_number, line.rstrip())

except FileNotFoundError:
    print("File not found.")