"""

Directions: Make each letter of your name a variable in Python.
            Make the value for each letter in your name the correct
            binary number associated with it.

            Then, have Python return your name in plain english and
            in binary, using the variables you just made!

"""

# Telling Python the Binary number associated with each letter
P = '01001010 '
E = '01001111 '
R = '01010011 '
C = '01000101 '
Y = '01000110 '

S = '01010011 '
M = '01001001 '
I = '01001100 '
T = '01010010 '
# (We don't need to redefine the same letters)

first_name = "percy"
last_name = "smit"

full_name = first_name + " " + last_name

print("Here is my first name coded in binary:")
print(P + E + R + C + Y)

print("\nHere is my last name coded in binary:")
print(S + M + I + T)

print("\nHere is my full name is plain english:")
print(full_name.title())


