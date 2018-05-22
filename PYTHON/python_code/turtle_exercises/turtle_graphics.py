import turtle

def square(t):
    for i in range (4):
        t.fd(100)
        t.rt(90)

def star(t):
    for i in range(5):
        t.fd(200)
        t.rt(144)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('black')
    # Create a turtle frank - draws a square
    frank = turtle.Turtle()
    frank.color('green')
    frank.pencolor('white')
    frank.shape('turtle')
    frank.speed(100)

    for i in range(28):
        square(frank)
        frank.rt(10)

    frank.up()
    frank.sety(50), frank.setx(-150)
    frank.down()

    for i in range(40):
        star(frank)
        frank.rt(10)
    
    window.exitonclick()
    
draw_art()
