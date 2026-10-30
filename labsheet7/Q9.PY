# Copy the contents of one file to another.

try:
    with open("sample.txt", "r") as source:
        content = source.read()

    with open("sample_copy.txt", "w") as destination:
        destination.write(content)

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found.")