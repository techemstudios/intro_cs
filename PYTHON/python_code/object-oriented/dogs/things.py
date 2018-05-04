"""
"""

class Dog():
    """Attempt to model a dog."""

    # Create an instance based on the class Dog.
    # This instance will have three parameters: self, name, age
    def __init__(self, name, age):
        """Initialize name age and age attributes."""
        # Make accessible attributes or variables:
        self.name = name
        self.age = age

    # Define the methods of the class Dog

    # Bark Method
    def bark(self):
        """Simulate a dog barking in response to something."""
        print(self.name.title() + " is now barking.")

    # Your other methods here

# Make an instance representing a specific dog

my_dog = Dog('koa', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " +str(my_dog.age) + " years old.")

# Calling methods
my_dog.bark()

# Make multiple instances
your_dog = Dog('scrappy', 1)

        
        
