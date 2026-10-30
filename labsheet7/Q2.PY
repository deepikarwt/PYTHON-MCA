# Read the complete contents of a file.

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    print("File content:")
    print(content)

except FileNotFoundError:
    print("File not found. Run program 1 first.")