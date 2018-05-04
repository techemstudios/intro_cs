"""
Object Oriented Programming (Thanksgiving Giving style)

We start defining classes with Animals.
We can define that parent of the class, Animals, as well as the parent of that class.

However, to save time we start at Animals. Starting here; instead of
directly at the turkey class, should help keep in mind we can define everything
under the sun using OOP is we wanted to. Again, we will save time!
"""

class Animals():
    pass

class Turkey(Animals):
    """Attempt to model a turkey."""
    
    # Create an instance based on the class Turkey.
    # This instance will have three parameters: self, name, age
    
    def __init__(self, name, age):
        """Initialize name age and age attributes."""
        # Make accessible attributes or variables:
        self.name = name
        self.age = age

    # Tell Python what a turkey can do by
    # defining the methods of the class

    # Gobble Method
    def gobble(self):
        """Simulate a turkey gobbling in response to something."""
        print(self.name.title() + " is now gobbling!")

    # More methods can follow here
    

# Make an instance representing a specific turkey

my_turkey = Turkey('scrappy', 3)
print("My turkey's name is " + my_turkey.name.title() + ".")
print("My turkey is " +str(my_turkey.age) + " years old.")

# Calling methods
my_turkey.gobble()

# Make multiple instances
your_turkey = Turkey('lassy', 1)

        
        
