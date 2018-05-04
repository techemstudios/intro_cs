from graphics import *

#
# We decided that we would like to have a button class that
# draws a rectangle with a text label and also provides a
# method that can be used to test if a point is within its bounds.
# That is, a method to see if the button has been "clicked".
class Button(Rectangle):

    def __init__(self,p1,p2,text):
        Rectangle.__init__(self,p1,p2)
        self.text = Text(self.getCenter(),text)
 
    def draw(self,canvas):
        super(Button,self).draw(canvas)
        self.text.draw(canvas)

    def inBounds(self,p):
        if p.x > self.p1.x and p.y > self.p1.y and p.x < self.p2.x and p.y < self.p2.y:
            return True
        else:
            return False


def test_button():
    win = GraphWin("Button Test")

    b = Button(Point(50,50),Point(150,150),"Hello")

    b.draw(win)

    r = Rectangle(Point(10,10),Point(30,30))

    r.draw(win)

    e = Entry(Point(40,40),4)
    e.draw(win)

    while (True):
        p = win.getMouse()
        print(p.x,p.y)
        if b.inBounds(p):
            break
        else:
            print(e.getText())
            e.setText("0.0")
            print("Out of Bounds")

    win.close()


test_button()
