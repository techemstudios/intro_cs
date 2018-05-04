"""
Interval Comparison Challenge

Create a program that takes user input, has a return based on interval comparison.

For Example, a program asks the user for their name and age, checks
the position of the age between two numbers, and returns an appropiate statement.
In the example's case, a statement pertaining to certain rights in Virginia.
"""

#### EXAMPLE ####
"""
A more complicated  than it needs to be program with user input and conditions,
using interval comparsion to check if a value is between two numbers.
"""

import time

name = raw_input("What is your name? ")

print(name + ", How old are you?")
age = float(raw_input())

computer_message = ("I will check some Virginia requirements" +
                    "\nto see what you are eligble for at your age." +
                    "\nPlease wait while I pull the data.")
print computer_message

time.sleep(1)
seconds = "."
print(seconds)
time.sleep(1)
seconds += ".."
print(seconds)
time.sleep(1)
seconds += ".."
print(seconds)
time.sleep(1)
seconds += ".."
print(seconds)
time.sleep(1)

print("\n")

# interval comparison
if 1 <= age < 14:
    print("You are young! " +
          "\n" + name + "... Your parents own your rights!")
    
# another interval comparison
elif 14 == age < 16:
    age = str(age)
    print("You are still young " +
          "\nat age, " + age +
          "\nyou can work with a permit!")
    
elif 16 == age < 18:
    age = str(age)
    print("Congratulations! " +
          "\nat age, " + age +
          "\nyou can work without a permit!" +
          "\nand you can drive with a permit!" +
          "\nBut, society does not consider you to be an adult.")
    
elif 18 <= age < 21:
    age = str(age)
    print("Congratulations! " +
          "\nat age, " + age +
          "\nSociety considers you to be an adult!" +
          "\nYou can get your driver's license!" + 
          "\nScary!")

elif 21 <= age <= 24:
    age = str(age)
    print("You made it! " +
          "\nat age, " + age +
          "\nyou can have a glass of wine at a public establishment!")

elif 25 <= age <= 26:
    age = str(age)
    print("Go rent a car!")

else:
    age = str(age)
    print("Wowee!" +
          "\nat age, " + age +
          "\nYou should already know what you are eligble for!")
          
