import time


# MODULE 1
def write_numbers_to_file(filename):
    try:
        # PT. 1 & 2: Measures (simulated by logic) and writes 1-100
        with open(filename, 'w') as f:
            for i in range(1, 101):
                f.write(f"{i}\n")
        print(f"Successfully wrote to {filename}")

    # PT. 3: Handle possible exceptions
    except FileNotFoundError:
        print(f"Error: The directory for '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")


# MODULE 2
def read_file_safely(filename):
    try:
        write_numbers_to_file(filename)

        with open(filename, 'r') as f:
            lines = f.readlines()
            print(f"Read {len(lines)} lines from the file safely.")

    except FileNotFoundError:
        print("Error: The file does not exist to be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_file_safely("numbers.txt")