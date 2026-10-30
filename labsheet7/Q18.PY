# Store unique words in another file.
# Preserve the order of their first appearance.

try:
    with open("sample.txt", "r") as file:
        content = file.read()

    words = content.split()
    unique_words = []
    seen = set()

    for word in words:
        if word.lower() not in seen:
            seen.add(word.lower())
            unique_words.append(word)

    with open("unique_words.txt", "w") as file:
        file.write("\n".join(unique_words))

    print("Unique words saved to unique_words.txt")

except FileNotFoundError:
    print("Source file not found.")