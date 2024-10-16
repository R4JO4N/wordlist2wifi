#author: rajoan

import sys

def filter_passwords(input_file, output_file):
    try:
        number = int(input("Enter your password length: "))
        character = input("Do you want exact (E), greater than or equal (G), or less than or equal (L)? ").strip().lower()

        valid_conditions = {
            'e': lambda pwd: len(pwd) == number,
            'g': lambda pwd: len(pwd) >= number,
            'l': lambda pwd: len(pwd) <= number
        }

        if character not in valid_conditions:
            print("Wrong input, please run the program again.")
            return

        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
             open(output_file, 'w', encoding='utf-8', errors='ignore') as outfile:
            count = 0
            for line in infile:
                password = line.strip()
                if valid_conditions[character](password):
                    outfile.write(password + '\n')
                    count += 1

            print(f"Filtered {count} passwords based on your criteria.")

    except ValueError:
        print("Invalid input for password length. Please enter a number.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Check for command-line arguments
if len(sys.argv) < 3:
    print("Usage: python customfilter.py <input_file> <output_file>")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    filter_passwords(input_file, output_file)
        
