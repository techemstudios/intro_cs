import turtle

def draw_square(some_turtle):
    for i in range (1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    # Create a turtle frank - draws a square
    frank = turtle.Turtle()
    frank.color('yellow')
    frank.shape('turtle')
    frank.speed(2)
    
    for i in range (1, 36):
        draw_square(brad)
        frank.right(10)
    
    window.exitonclick()
    
draw_art()
