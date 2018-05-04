import turtle

frank = turtle.Turtle()

def square(t):
	for i in range(0,4):
		t.fd(100)
		t.lt(90)

square(frank)
turtle.mainloop()

alice = turtle.Turtle()
square(alice)
turtle.mainloop()

