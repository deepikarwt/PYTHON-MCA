# Count lines and characters in a file.

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    lines = len(content.splitlines())
    characters = len(content)

    print("Number of lines:", lines)
    print("Number of characters:", characters)

except FileNotFoundError:
    print("File not found.")