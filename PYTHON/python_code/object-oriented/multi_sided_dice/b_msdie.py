#
# Some fun stuff
# 
# Challenge:
# Smart Die
#
# Add an instance variable to track roll history.
#
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
        self.roll_history = []

    def roll(self):
        self.value = randint(1,self.sides)
        self.roll_history.append(self.value)

    def getValue(self):
        return self.value

    def getRollHistory(self):
        return self.roll_history


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

print("My Die history")
print(my_die.getRollHistory())

print("My Other Die History")
print(my_other_die.getRollHistory())
