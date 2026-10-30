# Search for a word in a text file.

try:
    word = input("Enter the word to search: ")

    with open("sample.txt", "r") as file:
        content = file.read()

    if word.lower() in content.lower().split():
        print("Word found in the file.")
    else:
        print("Word not found.")

except FileNotFoundError:
    print("File not found.")