# Add parameters for calc input

import turtle

frank = turtle.Turtle()

def calc(number1, number2, operation):
    
    if operation == '+':
        answer = number1 + number2

    elif operation == '-':
        answer = number1 - number2

    elif operation == '*':
        answer = number1 * number2

    elif operation == '/':
        answer = number1 / number2

    frank.write(answer, move = True, font = ("Arial", 100, "bold"))

calc(int(raw_input("Please give me a number ")),
     int(raw_input("Please give me a number ")),
     raw_input("What operation would you like me to perform? ")
     )

turtle.mainloop()
