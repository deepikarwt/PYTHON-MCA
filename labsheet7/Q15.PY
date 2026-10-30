# Replace a word in a file and save the changes.

try:
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")

    with open("sample.txt", "r") as file:
        content = file.read()

    content = content.replace(old_word, new_word)

    with open("sample.txt", "w") as file:
        file.write(content)

    print("Word replaced successfully.")

except FileNotFoundError:
    print("File not found.")