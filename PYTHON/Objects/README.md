# Objects & Graphics  

*pg 79 in the Python Programming book by John Zelle.*  

### Generate a Window  

```python  
from graphics import *

win = GraphWin()
```  

### Drawing Shapes  

```python  
from graphics import *

win = GraphWin('Shapes')

### Draw a red circle centered at point (100, 100)
### with radius 30
center = Point(300, 300)
circ = Circle(center, 90)
circ.setFill('red')
circ.draw(win)

### Put a textual label in center of circle
label = Text(center, "Red Circle")
label.draw(win)

### Draw a square using Rectangle object
rect = Rectangle(Point(90, 90), Point(210, 210))
rect.draw(win)

### Draw a line segment using a Line object
line = Line(Point(60, 90), Point(540, 495))
line.draw(win)

### Draw an oval using the Oval object
oval = Oval(Point(60, 450), Point(540, 597))
oval.draw(win)
win.getMouse()
```  

### Getting Mouse Clicks  

```python  
from graphics import *

def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at: ", p.getX(), p.getY())

main()
```  

### Three Points to Create a Triangle  

```python  
from graphics import *

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    """Draw the three vertices of the triangle."""
    # Set the variables for the three points
    # Have the Python listen for the mouse click event by the user
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Wait for another click to exit
    message.setText("Click anywhere to quit.")
    win.getMouse()

main()

```  