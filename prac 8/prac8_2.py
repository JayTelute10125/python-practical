# Read from one file and write uppercase content to another file

source_file = input("Enter source file name: ")
dest_file = input("Enter destination file name: ")

try:
    with open(source_file, 'r') as f1:
        content = f1.read()

    with open(dest_file, 'w') as f2:
        f2.write(content.upper())

    print("\nContent successfully copied in uppercase!")

    # Display content
    print("\nOriginal Content:\n", content)
    print("\nUppercase Content:\n", content.upper())

except FileNotFoundError:
    print("Source file not found!")