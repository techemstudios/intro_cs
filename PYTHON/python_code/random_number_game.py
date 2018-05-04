"""
A random number guessing game.

To finish guess the computer's random the quickest,
use the Binary Search Tree method
"""

import random
number = random.randint(1, 100)

print("I'm thinking of a number between 1-100")

GameRunning = True
while GameRunning:
    
    guess = int(raw_input("Guess a number between 1-100: "))

    # Handlers

    # Check if guess is too high
    if guess > number:
        print("Your guess is too high!")
        # Do not NEED, but good for understanding the loop
        GameRunning = True
        
    # Check if guess is too low
    elif  guess < number:
        print("Your guess is too low!")
        # Do not NEED, but good for understanding the loop
        GameRunning = True
        
    # Check if guess is spot on
    elif guess == number:
        print("You guessed correctly!")
        GameRunning = False
        raw_input("\n\nPress enter key to exit ")
        exit()
 
