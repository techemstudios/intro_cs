# Add background color parameter for turtle
import turtle

# set a name for the turtle:
frank = turtle.Turtle()

# Questions:
num1 = int(raw_input("Please give me a number "))
num2 = int(raw_input("Please give me a number "))
operation = raw_input("What operation would you like me to perform? ")

# Set output color:
txt = 'white'
bg = 'black'

def calculator(num1, num2, operation):
    """A function that takes user input to
        performs an operation on two numbers
        and displays the answer using Turtle Graphics."""

    # Operation Handlers
    if operation == '+':
        a = num1 + num2

    elif operation == '-':
        a = num1 - num2

    elif operation == '*':
        a = num1 * num2

    elif operation == '/':
        a = num1 / num2

    # setup for background (bg) & text (txt) listeners:
    window = turtle.Screen()
    window.bgcolor(bg)

    # Tell turtle how to show the answer:
    frank.pencolor(txt)
    frank.write(a, move = True, font = ("Arial", 100, "bold"))

# Call the function & pass the arguments
calculator(num1, num2, operation)

# Keep the window open until exit:
turtle.mainloop()
