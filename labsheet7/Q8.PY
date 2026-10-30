# Append new content without deleting old content.

try:
    with open("sample.txt", "a") as file:
        file.write("This is newly appended content.\n")

    print("Content appended successfully.")

except OSError as e:
    print("Error:", e)