# Add a THIRD parameter to further generalize the function
# Now, it becomes apparent we can make unique animations with minimal code

import turtle

frank = turtle.Turtle()
marie = turtle.Turtle()
albert = turtle.Turtle()

def square(t, length, angle):
    for carrot in range(10):
        t.fd(length)
        t.lt(angle)

square(frank, 100, 90)
square(marie, 200, 95)
square(albert, 300, 275)

turtle.mainloop()
