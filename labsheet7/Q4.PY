# Count the total number of words in a file.

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    words = content.split()
    print("Total words:", len(words))

except FileNotFoundError:
    print("File not found.")