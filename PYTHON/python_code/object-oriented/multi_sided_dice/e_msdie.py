#
# Some fun stuff
# 
# Challenge:
# Unfair Die?
#
# Use Dice Stats
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

        self.die_stats = {}
        for side in range(self.sides):
            self.die_stats[side+1] = 0
        

    def roll(self):
        self.value = randint(1,self.sides)
        self.roll_history.append(self.value)
        self.die_stats[self.value] += 1

    def getValue(self):
        return self.value

    def getRollHistory(self):
        return self.roll_history

    def getDieStats(self):
        return self.die_stats

    def getSideProb(self,side):
        side = int(side)
        if self.die_stats.has_key(side):
            print(self.die_stats[side])
            prob = self.die_stats[side] / (len(self.roll_history) * 1.0)
            print(prob)
            return prob * 100
        else:
            return 0

# Example usage:

my_die = MultiSidedDie(6)
my_other_die = MultiSidedDie(6)

roll_again = "y"

while roll_again == "y":
    print("Dice Rolling...")
    my_die.roll()
    my_other_die.roll()

    print("My Dice: " + str(my_die.getValue()))
    print("My Other Dice: " + str(my_other_die.getValue()))

    
    roll_again = raw_input("Press 'y' to roll again ")

print("My Dice History: ")
print(my_die.getRollHistory())
print("My Other Dice History: ")
print(my_other_die.getRollHistory())
print("My Dice Stats:")
print(my_die.getDieStats())

side = raw_input("Type in a side to check probability ")
prob = my_die.getSideProb(side)
print("My Dice Prob - " + str(side) + " - " + str(prob))
prob = my_other_die.getSideProb(side)
print("My Other Dice Prob - " + str(side) + "-" + str(prob))

