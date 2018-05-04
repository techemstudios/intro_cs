import turtle
import math

frank = turtle.Turtle()
frank.speed(5)
frank.color("black")
size=200

frank.setheading(90) #Point the top
for i in range(0,6):
  frank.forward(size)
  frank.penup()
  frank.forward(-size)
  frank.left(60)
  frank.pendown()

frank.setheading(90) #Point the top
frank.forward(size)
frank.setheading(215) #Point the left
newSize=size
newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(65))
for i in range(0,30):  
   frank.forward(newSize)
   frank.left(60)
   newSize = (newSize*(math.sqrt(3)/2)) / math.sin(math.radians(70))
