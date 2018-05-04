import turtle

frank = turtle.Turtle()

def square(t, length):
	for i in range(0,4):
		t.fd(length)
		t.lt(90)

square(frank, 5)
turtle.mainloop()

