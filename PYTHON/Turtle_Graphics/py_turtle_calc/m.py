# send Frank's drawing instruction to go inside the calc() function
# This way he can use it

import turtle

frank = turtle.Turtle()

def calc():
    number1 = int(raw_input("Please give me a number "))
    number2 = int(raw_input("Please give me a number "))

    operation = raw_input("What operation would you like me to perform? ")

    if operation == '+':
        answer = number1 + number2

    elif operation == '-':
        answer = number1 - number2

    elif operation == '*':
        answer = number1 * number2

    elif operation == '/':
        answer = number1 / number2

    frank.write(answer, move = True, font = ("Arial", 100, "bold"))

calc()

turtle.mainloop()
