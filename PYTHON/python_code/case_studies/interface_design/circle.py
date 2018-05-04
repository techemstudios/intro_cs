"""
A function to make a circle
Parameters: radius, r and turtle, t.

"""
import math
import turtle

frank = turtle.Turtle()

def polygon(t, n, length):
	angle = 360.0/n
	for i in range(n):
		t.fd(length)
		t.lt(angle)


#def circle(t, r):
	"""Draws a 50-sided polygon to mimic drawing a circle"""
	# The first line computes the circumference of a circle w/ radius
	# Heard of 2(pi)r?
#	circumference = 2 * math.pi * r
	# In order to use math.pi, we had to import the "math" module
	
	# number of line segments
#	n = 50
	# the length of each segment
#	length = circumference / n
#	polygon(t, n, length)

	
# The limitation to this solution is that n is constant,
# meaning for very large circles, the line segments are too long,
# and for small circles, we waste time drawing very small segments.
	# What should we do to fix this?
	# Answer: Generalize the function by taking n as a parameter
	
# This would give more control to the user, 
# but the interface wouldn't be as neat, or clean.

# INTERFACE of a function is a summary of how it's used:
	# What are the parameters?
	# What does the function do?
	# And what is the return value?
		# An interface is "clean" if it allows the caller
		# to do what they want without dealing w/ unnecessary details.
		
# In the example above, r belongs in the interface because it specifies
# the circle to be drawn. n is less appropiate becasue it pertains to
# the details of how the circle should be rendered.

# So, rather than clutter up the interface, it is better to choose
# an appropiate value of n depending on circumference:

def circle(t, r):
	circumference = 2 * math.pi * r
	n = int(circumference / 3) + 1
	length = circumference / n
	polygon(t, n, length)
	
# Uncomment the two lines below to see the output
#circle(frank, 5)
#turtle.mainloop()
	
# Having it this way instead the number of segments is an integer near
# circumference/3, so the length of each segment is approximately 3,
# which is small enough that the circles look good, but big enough
# to be efficient, and acceptable for any size circle.

# REFACTORING
# It is common you'll come to a point where your code will work, but
# you'll recognize that you could improve the code by breaking it up
# into a series of functions, each having a specific job.
# Refactoring makes your code cleaner, easier to understand,
# and easier to extend (or generalize)

