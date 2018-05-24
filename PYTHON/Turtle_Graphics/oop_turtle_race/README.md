# Set Up a Turtle Graphics Race Using Object Oriented  

## Introduction  

Reusing code at its finest (debatable). The process of creating a race between turtles (using TUrtle Graphics) can be organized a little more efficiently by approaching the design in an **Object-oriented** way. Since each turtle variable has similar attributes, we can use *generalization* by creating a class with these common attributes. This class tells Python how to make an object representing a turtle. After the creation of the class, you can use it to make individual instances of the class, each of whihc represents one specific turtle object.  

This approach to software design (object-oriented programming) allows you to be more efficient at writing software. Remember, *software* is a collection of programs. This will help you when we see that the turtle race uses more than one python file.  

Object-oriented programming (OOP) is GREAT for modeling real-world stuff. You can think of everything around you (even yourself) as objects, and each of these objects have characteristics and things they can do.  

**Before class:**  
* Print the walkthrough pdf.    
* clone `https://github.com/joetechem/OOP_TurtleRace`  

# Getting Started   

## Initial Questions  

After the introduction, help the class answer the questions from `walkthrough/initialqs_walkthrough.pdf`. Display a class hierarchy on the whiteboard; comparing a dog to a sidewalk.  

*Optional*: use the `class_cutouts` to have students create a physical class hierarchy.  

## Dog Model  

Open the `dog.py` file in the text editor, geany and explain the steps from *Model a Dog from the Real-World!*  

```  
geany dog.py
```  

#### Part 1 - Class Hiearachy  
We are establishing the class hierarchy in Python. We start with the most top level at `class Things()` and finish at the `Dog` class. You can follow each class and its parameter back up the *tree* to see each class branches from `Things`.  

#### Part 2 - Create an Instance of your own dog  
In class `Dog`, we are not telling Python about a specific dog; rather, we are specifying general characteristics of a dog starting with the characteristics, *name* and *age* and behaviors, *sit* and *roll over*. To represent a specific dog, we'll make inidividual **instances** belonging to the `Dog` class by accessing its **attributes**. This is already an example instance, `some_dog` for students to model from.  

#### Part 3 - Call Methods from the Dog class  
Now that we've told Python of an individual instance (a specific dog), we can tell the instance to call **methods** from the class.  

****  

# Object-Oriented Turtle Race

**Once students have finished**, have them navigate to the `with_track` folder, open the python files here, and check out the similarities found in `racer_class.py` to `dog.py`.  

In the turtle race, we have several of the same characteristics and behaviors for each turtle, so it makes sense to organize them all into one class. This significantly shortens the amount of code needed. All we need to do is import attributes and methods from the class.  

#### Challenge  
`main.py` runs without errors as is. After seeing what the program performs, challege the students to add more turtles to the race.  


