# Add parameter for turtle

import turtle

frank = turtle.Turtle()

def calc(number1, number2, operation, text_color):
    
    if operation == '+':
        answer = number1 + number2

    elif operation == '-':
        answer = number1 - number2

    elif operation == '*':
        answer = number1 * number2

    elif operation == '/':
        answer = number1 / number2

    # tell frank to listen for a text color
    frank.pencolor(text_color)
    
    frank.write(answer, move = True, font = ("Arial", 100, "bold"))

calc(int(raw_input("Please give me a number ")),
     int(raw_input("Please give me a number ")),
     raw_input("What operation would you like me to perform? "),
     raw_input("Type in a text color: ")
     )

turtle.mainloop()
