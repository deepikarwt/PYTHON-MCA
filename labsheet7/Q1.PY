# Create a file and write text into it.

try:
    with open("sample.txt", "w") as file:
        file.write("Hello, welcome to Python!\n")
        file.write("This is a file handling program.\n")

    print("Data written successfully.")

except OSError as e:
    print("Error:", e)