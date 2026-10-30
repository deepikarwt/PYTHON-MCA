# Count how many times a word occurs in a file.

try:
    word = input("Enter the word to count: ")

    with open("sample.txt", "r") as file:
        content = file.read()

    count = content.lower().split().count(word.lower())

    print("Word occurrence:", count)

except FileNotFoundError:
    print("File not found.")