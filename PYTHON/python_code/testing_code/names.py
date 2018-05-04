"""
Use the code below to test the function get_formatted_name(),
found in name_function.py
"""

from name_function import get_formatted_name

print("Enter 'q' at anytime to quit.")

while True:
    first = raw_input("\nPlease insert a first name: ")
    if first == 'q':
        exit()
        # can use "break" here instead of exit()
        
    last = raw_input("Please insert a last name: ")
    if last == 'q':
        exit()
        # can use "break" here instead of exit()

    formatted_name = get_formatted_name(first, last)
    print("\tFormatted name: " + formatted_name + ".")
