# Merge two text files into a third file.

try:
    with open("first.txt", "r") as file:
        content1 = file.read()

    with open("second.txt", "r") as file:
        content2 = file.read()

    with open("merged.txt", "w") as file:
        file.write(content1)

        if content1 and not content1.endswith("\n"):
            file.write("\n")

        file.write(content2)

    print("Files merged into merged.txt")

except FileNotFoundError:
    print("One or both source files were not found.")