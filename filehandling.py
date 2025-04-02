def modify_file_content(filename):
    try:
        # Try to open and read the file
        with open(filename, "r") as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Define the new file name
        new_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        
        print(f"✅ Successfully created '{new_filename}' with modified content.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Ask user for a filename
filename = input("Enter the filename to read: ")
modify_file_content(filename)
