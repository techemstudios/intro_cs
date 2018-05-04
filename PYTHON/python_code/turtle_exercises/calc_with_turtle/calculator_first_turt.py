import turtle

number1 = int(raw_input("Give me a number: "))
number2 = int(raw_input("Give me another number: "))

operation = raw_input("Give me an operator:" )

if operation == '+':
    a = number1 + number2
elif operation == '-':
    a = number1 - number1
elif operation == '*':
    a = number1 * number1
elif operation == '/':
    a = number1 / number1

frank = turtle.Turtle()
frank.write(a, move = True, font = ("Arial", 100, "bold"))
turtle.mainloop()
