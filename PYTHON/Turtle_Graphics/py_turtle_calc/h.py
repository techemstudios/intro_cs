# Add another parameter to further generalize the function
# Also, we can start to see how we can create more unique animations

import turtle

frank = turtle.Turtle()
marie = turtle.Turtle()
albert = turtle.Turtle()

def square(t, length):
    for carrot in range(4):
        t.fd(length)
        t.lt(90)

square(frank, 100)
square(marie, 200)
square(albert, 300)

turtle.mainloop()
