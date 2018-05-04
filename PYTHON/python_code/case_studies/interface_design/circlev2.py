"""
 REFACTORING
 It is common you'll come to a point where your code will work, but
 you'll recognize that you could improve the code by breaking it up
 into a series of functions, each having a specific job.
 Refactoring makes your code cleaner, easier to understand,
 and easier to extend (or generalize)

"""
import math
import turtle

frank = turtle.Turtle()

def polygon(t, n, length):
	angle = 360.0/n
	polyline(t, n, length, angle)

"""
def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = angle /n
"""
	
def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = angle /n
	
def polyline(t, n, length, angle):
	for i in range(n):
		t.fd(length)
		t.lt(angle)

# Uncomment the two lines below to see the output
#circle(frank, 5)
#turtle.mainloop()

