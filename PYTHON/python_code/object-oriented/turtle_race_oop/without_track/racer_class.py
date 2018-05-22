"""
Creating a Class for racing turtle objects
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