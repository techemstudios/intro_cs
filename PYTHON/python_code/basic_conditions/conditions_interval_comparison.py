"""
A simple program with user input and conditions,
using interval comparsion to check if a value is between two numbers.
"""

name = raw_input("What is your name? ")

print(name + ", How old are you?")
age = float(raw_input())

# interval comparison
if 1 <= age <=8:
    return_statement = "Sorry, " + name + " you are too young to ride the rollercoaster!"
    return_statement += " Try again next year."
    print return_statement
    
# another interval comparison
elif 9 <= age <= 25:
    return_statement = "Congratulations " + name + "! "
    return_statement += "You are old enough to ride the rollercoaster!"
    print return_statement

else:
    return_statement = "Wowee " + name + "! "
    return_statement += "You are too old to ride the rollercoaster!"
    print return_statement
