"""
	A simple program asking a user to guess the "computer's" favorite color.
	The favorite color of the computer is set in a variable, favColor.
	The computer checks the user's input to match the favColor variable.
	If it is any color other than the computer's favorite color, the loop continues.
	Otherwise, the loop is ended when the flag is set to False (or, the user enters the
	exact string equal to the favColor variable.
	
	Objectives:
			handling user input
			variables review
			conditions statements/blocks
			while loop
			stopping a loop w/ a  variable
			
"""
import random

colors = ['orange', 'red', 'blue', 'yellow', 'indigo', 'green', 'violet']

favColor = random.choice(colors)

print("Hi!")

GameRunning = True

while GameRunning:
	guess = raw_input("\nGuess my favorite color: ")

	if guess != favColor:
		print("Wrong!")
		print("Please, try again :)")
	elif guess == favColor:
		print("\nThat is my favorite color!")
		raw_input("\n\nPress the enter key to exit")
		GameRunning = False
		exit()
		
