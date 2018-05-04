# example of how generalizing works by adding more turtle to use the same
# function.

import turtle

frank = turtle.Turtle()
marie = turtle.Turtle()
albert = turtle.Turtle()

def square(t):
    for carrot in range(4):
        t.fd(100)
        t.lt(90)

square(frank)
square(marie)
square(albert)

turtle.mainloop()
