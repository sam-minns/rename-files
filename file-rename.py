import os

# Function to rename file
def rename_file(file_path, old_name, new_name):
    os.rename(os.path.join(file_path, old_name), os.path.join(file_path, new_name))
    print(f"Renamed {old_name} to {new_name}")

# Function to scan for files with double extensions
def scan_double_extensions(root_dir):
    double_ext_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            basename, extension = os.path.splitext(filename)
            if len(extension) > 0:
                if os.path.splitext(basename)[1] == extension:
                    double_ext_files.append(os.path.join(dirpath, filename))
    if len(double_ext_files) == 0:
        print("No files with double extensions found.")
    else:
        print(f"Found {len(double_ext_files)} file(s) with double extensions:")
        for file_path in double_ext_files:
            print(file_path)
        choice = input("Would you like to rename these files to have single extensions? (y/n) ")
        if choice.lower() == "y":
            for file_path in double_ext_files:
                file_dir, file_name = os.path.split(file_path)
                old_name = file_name
                new_name = os.path.splitext(os.path.splitext(file_name)[0])[0] + os.path.splitext(file_name)[1]
                rename_file(file_dir, old_name, new_name)

# Function to mass rename files
def mass_rename(root_dir):
    text_to_remove = input("Enter text to remove from file names: ")
    text_to_replace = input("Enter text to replace removed text with: ")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            basename, extension = os.path.splitext(filename)
            if text_to_remove in basename:
                new_basename = basename.replace(text_to_remove, text_to_replace).strip()
                new_filename = new_basename + extension
                if new_filename != filename:
                    rename_file(dirpath, filename, new_filename)

# Main function to prompt user for choice
def main():
    root_dir = input("Enter full directory path: ")
    choice = input("Enter 1 to scan for double extensions, 2 to mass rename files, or 3 to quit: ")
    if choice == "1":
        scan_double_extensions(root_dir)
    elif choice == "2":
        mass_rename(root_dir)
    elif choice == "3":
        print("Goodbye.")
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()
