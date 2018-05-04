# Python Turtle Calculator  

Level: Beginner/Intermediate  
Ages: 8+  

## Introduction  

Students will recieve an introduction (or review) to programming/coding using the Python programming language. This project will serve as a great *icebreaker* to programming and will help students understand what to expect/expected of them for other project work in the Code Em class.  

During this project, students will learn how to create a basic calculator program in Python, which uses operator handlers to calculate two numbers based on a user's input. Students will then learn how to implement Turtle Graphics using the Python Turtle module. The end goal of the project is to have a basic calcualtor program which uses Turtle graphics to draw at any answer. There will be an opportunity to tweak the code to make it unique via program flow and different graphic outputs.  

The project will be broken up into 4 small parts:  

1. Calculator Logic  
2. Intro to Turtle Graphics  
3. Efficient Techniques  
    - for loops  
    - while loops  
    - create your own function  
        - without parameters and with parameters  
4. Combine the Calculator Program with Turtle  

#### Objectives:  

Students will be able to -  

* Understand programming fundamentals via Python  
* Create a working calculator program  
* Understand modules and how they are used
* Understand and create their own:  
    - Variables  
    - Functions  

***  

## Calculator Logic  

The basic calculator program with comments.  

```python  
"""
A calculator program that tells the computer to ask a user for two numbers to calculate, then returns the answer
from the user's input. Python automatically considers what the user types in as a string.

This text and the text above is surrounded by 3 double quotes, which makes it a "docstring".
Docstrings are one way to convey what is happening in a program, or what is supposed to happen, they do not have a program "do" anything.
"""

# Any line that starts with a pound sign (#) is known as a comment, Python knows to ignore comments.
# Comments are useful for explaining what you are doing in a program to yourself or someone else who might 
# be working on the same program.

print("Please give me a number")
number1 = raw_input()             # here's our first variable

print("Please give me another number")
number2 = raw_input()             # here's our second variable

# We need to convert the value of the variables to a whole number, so Python can calculate the numbers
number1 = int(number1)
number2 = int(number2)

print("What operation would you like me to do with the two numbers?")
operation = raw_input()

# Below is our condition statements, or IF and THEN statements
# notice the indentations, these are called blocks of code
# anything that is indented under a statement, is part of that first statement

# checking if the input from the user is addition
if operation == "+":
  answer = number1 + number2

# checking if the input from the user is subtraction
elif operation == "-":
  answer = number1 - number2

# checking if the input from the user is multiplication
elif operation == "*":
  answer = number1 - number2
  
# checking if the input from the user is division
elif operation == "/":
  answer = number1 / number2
  
# Now, to print the answer
print(answer)

### NOTE:
# For the first part of the program, we could shorten the amount we type by combining lines of code.
# For instance, lines 13 - 21 can be rewritten as:

# number1 = int(raw_input("Please give me a number"))
# number2 = int(raw_input("Please give me another number"))

# We'd get the program to do the same thing, only with fewer lines of code.
# Remember, engineers are concerned with building things efficiently!
```  

***  

## Intro to Turtle Graphics  

Python's turtle program (or **module**), is a program that holds a slew of functions waiting to be used. All we have to do is put `import turtle` towards the top of any python file we create and now, we can write instructions that display images using turtle graphics! Rather than explain the turtle module from scratch, take a look at the official python documentation on Turtle Graphics:  

*"Imagine a robotic turtle starting at (0, 0) in the x-y plane. After an import turtle, give it the command turtle.forward(15), and it moves (on-screen!) 15 pixels in the direction it is facing, drawing a line as it moves. Give it the command turtle.right(25), and it rotates in-place 25 degrees clockwise."* -[Python 3.3.7 Doc](https://docs.python.org/3.3/library/turtle.html?highlight=turtle)  

Here's the first program we wrote together using turtle graphics:  

```python  
import turtle

# name your turtle
frank = turtle.Turtle()

# tell your turtle where to go
frank.fd(100)
frank.lt(90)
frank.fd(100)

# so the window doesn't disappear right away, add:
turtle.mainloop()
# or turtle.exitonclick()
```  

*Think of the "turtle" as a pen, marker, etc. We are giving this writing tool instructions to draw lines on a separate window (or piece of paper) --similar to our brain giving instructions to our hand to write or draw*  

Above, we called **methods** to tell our turtle where to go. Methods are like functions, but use different syntax. Calling a method is like making a request (*or command*). You are telling frank (or whatever you named your turtle) to move forward, x-amount and turn, x-amount, and so on.  

**Challenge** the group to add to the right angle they just drew to display a complete square.  

Most of the class should end up with a list of command like this:  

```python  
frank.fd(100)
frank.lt(90)
frank.fd(100)
frank.lt(90)
frank.fd(100)
frank.lt(90)
frank.fd(100)
frank.lt(90)
```  

Ask the group if they see a pattern in the instructions. They should! We have the forward and turn command repeat, four times. We can make this program a little more efficient. Anytime we recognize code that repeats, we can look at using a loop to shorten our code. So our goal is to draw a square, and we know there are four sides to a square. We already see too, we have two lines of repeating code, the forward command and turn command.  

### Python `for` loop  

One way to repeat code in Python is to use a `for` loop. We can specify how many times we want a block of code to repeat. Substitute your instructions to make a square with the loop below:  

```python  
for i in range(4):
    frank.fd(100)
    frank.lt(90)
```  

a `for` statement is a loop because the flow of execution runs through the *body* (or, whatever is indented below), then loops back to the top. In this case, it does so 4 times.  

### Python `while` loop

We can also use another *repeat* technique, Python's `while` loop. This will run "as long as", or *while* a certain condition is true.  

```python  
while True:
    t.fd(100)
    t.lt(95)
```  

### Make a Reusable function  

We can make our code even more efficient by creating our function. This way, we can make our code more *reusable*.  
```python  
import turtle  

frank = turtle.Turtle()

def square(t):
    """Reusable function to draw a square."""
    for i in range(0, 4):
        t.fd(100)
        t.lt(90)

square(frank)
turtle.mainloop()
```  

It might seem silly to do this at first, but what if we wanted to have more than one turtle object draw out the same thing? You can check this out by defining a couple more turtle variables and calling the function with their names:  

```python  
import turtle  

# define turtle variables here
frank = turtle.Turtle()
marie = turtle.Turtle()
albert = turtle.Turtle()

def square(t):
    """Reusable function to draw a square."""
    for i in range(0, 4):
        t.fd(100)
        t.lt(90)

# call the function and pass the name of each turtle as an argument
square(frank)
square(marie)
square(albert)

turtle.mainloop()
```  

By wrapping up a piece of code and putting it inside a resuable function we are checking out **encapsulation**. Why? -to stay **DRY** (Don't Repeat Yourself), or reuse code, `"t"` can be  any turtle.  

We also introduce ourselves with some more important tools found in languages besides just Python: **parameters** and **arguments**.  


In the last exercise we also **generalized**, we made our code usable across more situations by adding the `t` parameter. We can further *generalize* by adding a another parameter to the mix, *length*. By adding this, we can have the output size change each time if we wanted to.  

Add the length parameter to the square() function:  

```python  
def square(t, length):
    for i in range(0, 4):
        t.fd(length)
        t.lt(90)
```  

Call the function:  
    - the function is expecting two arguments to be passed  

```python  
square(frank, 300)
```  

Again, we made the function more general, we can use it across more situations than we could before. Check out other situations by having each turtle you define draw out shapes in different sizes:  

`square(marie, 200)`  

`square(albert, 50)`  

#### Challenge  

Edit the function to now have *angle* as a parameter.  

***  

## Merging  
### Calculator Program with Turtle Graphics  

So now we know what we can do with turtle graphics and we have our calculator program, let's complete our project by combining the two. The idea is to have the answer *drawn* out from our basic calculator program.  

What the program needs to do:  
* Take user's input for two numbers  
* Take user input for type of operator  
* Correctly handle user input  
* Display the answer with turtle  

Project Goals:  
* Understand fundamental coding concepts  
* Learn How to harness the `turtle` module  
* Tweak the code to display your own unique twist  

We can make the code our own by choosing our own background color, pen color, font type and size, etc.    

Our first attempt at merging the programs:  

```python  
import turtle

number1 = int(raw_input("Give me a number: "))
number2 = int(raw_input("Give me another number: "))

operation = raw_input("Give me an operator:" )

if operation == '+':
    a = number1 + number2
elif operation == '-':
    a = number1 - number1
elif operation == '*':
    a = number1 * number1
elif operation == '/':
    a = number1 / number1

frank = turtle.Turtle()
frank.write(a, move = True, font = ("Arial", 100, "bold"))
turtle.mainloop()
```  

Earlier, we used encapsualtion and generalized our function. We can do that here as well to rewrite our code a little more efficiently:  

```python  
import turtle

def calc(number1, number2, operation, text_color):

        if operation == "+":
                answer = number1 + number2
        elif operation == "-":
                answer = number1 - number2
        elif operation == "*":
                answer = number1 * number2
        elif operation == "/":
                answer = number1 / number2

        # Setting up turtle name, creating the new window instance
        frank = turtle.Turtle()
        frank.pencolor(text_color)
        window = turtle.Screen()
        window.bgcolor(bg_color)
        frank.write(answer, move=True, font = ("Arial", 100, "bold"))
        turtle.mainloop()

# Call the function, pass it the arguments its waiting for.
# You can see the parameters at line three; we need an argument for each parameter
calc(int(raw_input("Give me a number:   ")),                            # number1
     int(raw_input("Give me another number:   ")),                      # number2
     raw_input("What operation?  "),                                    # operator
     raw_input("Type in a color for text: ")                            # text_color
     )
```  

Now add a parameter to your function to take a background color argument.  

Explore on your own how to have the output display something different each time by asking the user's input for more parmeters like, background color, text size, etc.






