# File: week4_assignment.py

def read_and_modify_file(input_filename, output_filename):
    """
    Reads content from a file and writes a modified version to another file.
    Modification: Converts all text to uppercase and adds line numbers.
    """
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        modified_lines = [f"{i+1}: {line.upper()}" for i, line in enumerate(lines)]

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"Modified file has been written to '{output_filename}'")

    except FileNotFoundError:
        print(f"Error ❌: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error ❌: You don’t have permission to read '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Ask user for input filename
    input_file = input("Enter the name of the file you want to read: ").strip()
    output_file = "modified_" + input_file  # create new filename

    # Process the file
    read_and_modify_file(input_file, output_file)


if __name__ == "__main__":
    main()
