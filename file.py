def read_and_modify_file():
    filename = input(" ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\nOriginal content:")
            print(content)
        modified_content = content.upper()
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"\nModified content written to: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: The file cannot be read or written.")
read_and_modify_file()
