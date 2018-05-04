# encapsulate/generalize by adding a parameter

import turtle

frank = turtle.Turtle()

def square(t):
    for rabit in range(4):
        t.fd(100)
        t.lt(90)

square(frank)

turtle.mainloop()
