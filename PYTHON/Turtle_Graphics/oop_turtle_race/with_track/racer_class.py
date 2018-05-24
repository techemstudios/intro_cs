"""
Creating and Using a Class for turtle racers
"""
import turtle
from random import randint

class Turtles():
    """A simple attempt to model a turtle racer."""

    def __init__(self, isTurtle):
        """Initialize turtle object."""
        self.isTurtle = isTurtle.Turtle()

    def looks(self, color, shape):
        """Sets shape and color of turtle objects."""
        self.isTurtle.shape(shape)
        self.isTurtle.color(color)

    def start(self, x, y):
        """Send turtle to starting position."""
        self.isTurtle.up()
        self.isTurtle.goto(x, y)
        self.isTurtle.down()

    def go(self):
        """Randomizes the winner in each race."""
        self.isTurtle.fd(randint(1, 5))

    def track(self):
        """Creates the track."""
        self.isTurtle.speed(0)
        self.isTurtle.up()
        self.isTurtle.goto(-130, 130)
        for step in range(15):
            self.isTurtle.write(step)
            self.isTurtle.rt(90)
            self.isTurtle.fd(10)
            self.isTurtle.down()
            self.isTurtle.fd(150)
            self.isTurtle.up()
            self.isTurtle.bk(160)
            self.isTurtle.lt(90)
            self.isTurtle.fd(20)

    def win_message(self):
        """Displays a win message when race has ended."""
        self.isTurtle.up()
        self.isTurtle.goto(-70, 150)
        self.isTurtle.write("WINNER!", move = True, font = ("Arial", 50, "bold"))
        


        
