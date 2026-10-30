# Convert file content into uppercase.

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    print(content.upper())

except FileNotFoundError:
    print("File not found.")