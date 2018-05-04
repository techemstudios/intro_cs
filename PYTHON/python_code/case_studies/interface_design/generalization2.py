import turtle

frank = turtle.Turtle()

def polygon(t, n, length):
	angle = 360.0/n
	for i in range(n):
		t.fd(length)
		t.lt(angle)

polygon(frank, 20, 70)
turtle.mainloop()


