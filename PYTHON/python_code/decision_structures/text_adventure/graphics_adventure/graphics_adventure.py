# Choose your own adventure game
# MARS

# I am importing the Button class we created -- I created mine in a file
# called button.py (in the same directory)
from graphics import *
from button import *


# Create a window
win = GraphWin("Mars Adventure",500,600)

# Add three choice buttons
aButton = Button(Point(10,510),Point(110,550),"A")
aButton.draw(win)
bButton = Button(Point(130,510),Point(230,550),"B")
bButton.draw(win)
cButton = Button(Point(250,510),Point(350,550),"C")
cButton.draw(win)
qButton = Button(Point(370,510),Point(470,550),"Quit")
qButton.draw(win)
    
image = Image(Point(250,100),"icon.gif")
image.draw(win)

text = Text(Point(250,250),"")
text.setSize(18)
text.draw(win)

def gprint(message):
    text.setText(message)

def quit():
    aButton.text.setText("")
    aButton.undraw()
    bButton.text.setText("")
    bButton.undraw()
    cButton.text.setText("")
    cButton.undraw()
    while(True):
        click = win.getMouse()
        if qButton.inBounds(click):
            break
    
def die():
    gprint("The object fires a laser at you and you die.")
    quit()
    
def friendly_alien():
    gprint("""A little alien comes from the object.
    He has some spare O2 for you.""")
    quit()

gprint("""You land on mars and your oxygen generator has failed,
 so you only have a few hours on the planet.
 However, you see something in the distance!
 What do you do?
 A) Leave Now, B) Go to object, or C) Scan Object""")
aButton.text.setText("Leave Now")
bButton.text.setText("Go to Obj")
cButton.text.setText("Scan")

click = win.getMouse()

while(True):

    if aButton.inBounds(click):
        # First branch of story
        gprint("""You begin to leave and notice the object moves.
        What do you do?
        A) Continue leaving or B) Stay on the planet to investigate """)
        bButton.text.setText("Stay")
        cButton.text.setText("")
        cButton.undraw()
        
        while(not qButton.inBounds(click)):
            click = win.getMouse()
            if aButton.inBounds(click):
                die()
                break
            elif bButton.inBounds(click):
                friendly_alien()
                break
            else:
                pass
            # Your adventure can continue here.
        break
    
    elif bButton.inBounds(click):
        # Second branch of story
        gprint("""As you approach the object, it is clearly an alien.
        What do you do?
        A) Investigate the object or B) Leave """)

        aButton.text.setText("Investigate")
        bButton.text.setText("Leave")
        cButton.text.setText("")
        cButton.undraw()
        
        while(not qButton.inBounds(click)):
            click = win.getMouse()
        
            if aButton.inBounds(click):
                friendly_alien()
                break
            elif bButton.inBounds(click):
                die()
                break
            else:
                pass
        break

    elif cButton.inBounds(click):
        # Third branch of story
        gprint("""After scanning the object for 30 minutes, you get no usable information.
        What do you do now?
        A) Scan More or B) Leave the planet """)

        aButton.text.setText("Scan")
        bButton.text.setText("Leave")
        cButton.text.setText("")
        cButton.undraw()

        while(not qButton.inBounds(click)):
            click = win.getMouse()

            if aButton.inBounds(click):
                die()
                break
            elif bButton.inBounds(click):
                die()
                break
            else:
                pass
        break

    elif qButton.inBounds(click):
        break
    
    else:
        click = win.getMouse()
    
