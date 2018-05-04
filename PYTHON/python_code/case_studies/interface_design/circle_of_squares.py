"""
Draw a circle out of squares
"""

import turtle

def draw_square(frank):
    for i in range(4):
        frank.forward(100)        # move forward 100 units
        frank.right(90)           # turn right 90 degrees

def draw_art():
	# Instantiate a Screen object, window. Then customize window.
	window = turtle.Screen()
	window.bgcolor("white")
	frank = turtle.Turtle()
#    frank.shape("turtle")      # see Turtle doc
#    frank.color("yellow")      # see Turtle doc
	frank.speed(10)
	# Draw a circle with 36 squares. We rotate each square by 10 degrees at a time.
	for i in range(36):
		draw_square(frank)
		frank.right(10)
		
	window.exitonclick()      # click on the window to exit

# Invoke the procedure!
draw_art()
