# Copy python file content excluding comments

source_file = input("Enter source Python file: ")
dest_file = input("Enter destination file: ")

try:
    with open(source_file, 'r') as f1, open(dest_file, 'w') as f2:
        for line in f1:
            line_strip = line.strip()
            
            # Skip comments and empty lines
            if not line_strip.startswith("#") and line_strip != "":
                f2.write(line)

    print("\nContent copied without comments!")

    # Display both files
    print("\n--- Source File Content ---")
    with open(source_file, 'r') as f:
        print(f.read())

    print("\n--- Destination File Content ---")
    with open(dest_file, 'r') as f:
        print(f.read())

except FileNotFoundError:
    print("File not found!")