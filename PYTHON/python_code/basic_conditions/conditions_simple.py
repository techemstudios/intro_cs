"""
A simple program checking height requirements for a rollercoaster.

Objective:
    multi-way condition statement
"""

# Ask user for their name
# The value gets stored in the variable, name
name = raw_input("What is your name? ")

# Ask user for their height
# The value gets stored in the variable, height
# concatenate the variable, name with a string
print(name + ", Approximately how tall are you? (in inches)")
height = float(raw_input())

# we can merge the two lines above into just one line:
#height = float(raw_input(name + ", How tall are you, in inches? "))

# Check if the user's height is any less than 38
if height < 38:
    # if the value of height is below, then return this...
    print("You do not meet the rollercoaster's height requirements!" + 
          "\nTry again next year!")

# Check if the user's height is any number above 38
elif height > 38:
    # if the value of height is above, then return this...
    print("You are tall enough to ride the rollercoaster!")


