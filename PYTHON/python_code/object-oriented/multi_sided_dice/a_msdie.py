#
# Start with Python for Kids Chapter 8, page 93
# Use Examples of classifications.
# Explain in Python (and most modern languages), it is a way
# to organize code (functions, called methods) that is easier
# for humans to understand.
# There are some simple examples of the syntax in the book.
# Run through a couple to show the
# class keyword, how "methods" are simply functions defined
# within a class, with a special first parameter that is
# a reference to the specific object.
# and then explain the initializer method.
#
# But, for our class, let's go back to some games and start
# playing with a multi-sided dice.
#
# Think of the dice and how we interact with the dice.
# We roll it and then we read the number.
#
# Ask, what would be the methods?
# What data/values would the class need to track for each object?
#
# Start sketching out the class...
# Remind them about the self keyword and how it is similar to a
# regular variable, except it is a variable for every object
# created.
# And a Class itself can be considered a container for functions
# where the class is defined once and then many objects are created
# for each class.
#
# So, a simple class for a multi sided die would look like this:

from random import randint

class MultiSidedDie:

    #
    # Most classes will have an initialization method.
    #
    # 'self' is a special parameter that is a reference
    # to the object (instance of this class).
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randint(1,self.sides)

    def getValue(self):
        return self.value


# Example usage:

my_die = MultiSidedDie(6)

print(my_die.getValue())

print("Roll the die!")
my_die.roll()
print(my_die.getValue())
print("Roll the die!")
my_die.roll()
print(my_die.getValue())


my_other_die = MultiSidedDie(6)
print("Roll my other die!")
my_other_die.roll()

print("My dice:")
print(my_die.getValue(),my_other_die.getValue())

