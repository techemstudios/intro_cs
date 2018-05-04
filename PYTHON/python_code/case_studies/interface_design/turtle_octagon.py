# a program showing turtle instructions to make an octagon
# using for loop
# this can be found as a method (or function?)...(same for square, circle, etc.)
import turtle

t = turtle.Pen()

for i in range(8):

    t.forward(100)
    t.left(315)

input("\n\nYou made an octagon! Press the enter key to exit.")
