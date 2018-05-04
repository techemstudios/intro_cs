"""
Draw a circle out of squares
"""

import turtle
frank = turtle.Turtle()
def square(t):
    for i in range(4):
        t.fd(100)        # move forward 100 units
        t.rt(90)
        t.speed(10)           # turn right 90 degrees

	def draw_art():
		# Instantiate a Screen object, window. Then customize window.
		window = turtle.Screen()
		window.bgcolor("white")
		frank = turtle.Turtle()
	#    frank.shape("turtle")      # see Turtle doc
	#    frank.color("yellow")      # see Turtle doc

		# Draw a circle with 36 squares. We rotate each square by 10 degrees at a time.
		for i in range(36):
			square(frank)
			t.right(10)
			
		window.exitonclick()      

square(frank)
window = turtle.Screen()
window.bgcolor("white")
window.exitonclick() 
