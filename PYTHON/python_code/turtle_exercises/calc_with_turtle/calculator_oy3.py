import turtle

def calc(number1, number2, operation, text_color, bg_color):

        if operation == "+":
                answer = number1 + number2
        elif operation == "-":
                answer = number1 - number2
        elif operation == "*":
                answer = number1 * number2
        elif operation == "/":
                answer = number1 / number2

        # Setting up turtle name, creating the new window instance
        frank = turtle.Turtle()
        frank.pencolor(text_color)
        window = turtle.Screen()
        window.bgcolor(bg_color)
        frank.write(answer, move=True, font = ("Arial", 100, "bold"))
        turtle.mainloop()

calc(int(raw_input("Give me a number:   ")),
     int(raw_input("Give me another number:   ")),
     raw_input("What operation?  "),
     raw_input("Type in a color for text: "),
     raw_input("type in another color for the background: ")
     )
