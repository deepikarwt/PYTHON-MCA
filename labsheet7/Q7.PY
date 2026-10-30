# Take multiple lines from the user and save them.

try:
    with open("user_lines.txt", "w") as file:
        print("Enter text. Type END to finish.")

        while True:
            line = input()

            if line == "END":
                break

            file.write(line + "\n")

    print("Data saved successfully.")

except OSError as e:
    print("Error:", e)