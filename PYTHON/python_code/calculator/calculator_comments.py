"""
A simple interactive calculator program
Operators handled: addition (+), subtraction (-), multiplication (*), division (/)
"""

# initial user input/variables
number1 = raw_input("Give me a number: ")
number2 = raw_input("Give me another number: ")

# uncomment below to convert string input to integers (to make calculation of numbers work)
## number1 = int(raw_input("Give me a number: "))
## number2 = int(raw_input("Give me another number: "))

operation = raw_input("Which operation do you want me to perform? ")

# explain conditions and blocks of code
if operation == "+":
    answer = number1 + number2

elif operation == "-":
    answer = number1 - number2

elif operation == "*":
    answer = number1 * number2

elif operation == "/":
    answer = number1 / number2

print(answer)

