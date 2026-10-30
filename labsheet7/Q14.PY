# Find and display the longest line in a file.

try:
    with open("sample.txt", "r") as file:
        lines = file.read().splitlines()

    if lines:
        longest = max(lines, key=len)

        print("Longest line:", longest)
        print("Length:", len(longest), "characters")
    else:
        print("File is empty.")

except FileNotFoundError:
    print("File not found.")