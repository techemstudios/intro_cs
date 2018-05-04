import turtle

frank = turtle.Turtle()
frank.speed(0)
frank.color("blue")

side=10
frank.penup()
frank.goto(0,0) #position cursor at the bootom right of the screen
frank.pendown()

for i in range (1,300):
  frank.forward(side)
  frank.left(92)
  side=side+2


frank.penup()
frank.goto(500,500)

turtle.mainloop()
