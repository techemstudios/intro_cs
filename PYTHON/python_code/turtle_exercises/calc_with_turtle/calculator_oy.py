import turtle

frank = turtle.Turtle()

def calc():
        
        number1 = int(raw_input("Give me a number:   "))
        number2 = int(raw_input("Give me another number:   "))
        operation = raw_input("What operation?  ")
        color = raw_input("Type in a color: ")

        if operation == "+":
                answer = number1 + number2
        elif operation == "-":
                answer = number1 - number2
        elif operation == "*":
                answer = number1 * number2
        elif operation == "/":
                answer = number1 / number2

        frank.pencolor(color)

        frank.write(answer, move=True, font = ("Arial", 100, "bold"))

        turtle.exitonclick()

print("\n Check out the turtle window to see the answer!")

calc()

