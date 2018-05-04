# make a function to draw a square

import turtle

frank = turtle.Turtle()

def square():
    for rabit in range(4):
        frank.fd(100)
        frank.lt(90)

square()

turtle.mainloop()
