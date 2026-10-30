# Sort words alphabetically and save them to a new file.

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    words = content.split()
    words.sort(key=str.lower)

    with open("sorted_words.txt", "w") as file:
        file.write("\n".join(words))

    print("Sorted words saved to sorted_words.txt")

except FileNotFoundError:
    print("Source file not found.")