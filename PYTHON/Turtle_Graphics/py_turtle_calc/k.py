# Add the calculator with turtle

import turtle

frank = turtle.Turtle()


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

turtle.mainloop()
