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

favColor = 'orange'

print("Hi!")

Questions = True

while Questions:
	question = raw_input("\nGuess my favorite color: ")

	if question != favColor:
		print("Wrong!")
		print("Please, try again :)")
	elif question == favColor:
		print("\nHey...")
		print("That is my favorite color!")
		raw_input("\n\nPress the enter key to exit")
		Questions = False
		exit()
		
		# The program will close with exit()
"""
	Below is the same program with descriptive comments.
	
"""

# The "computer's" favorite color set as a variable.
favColor = 'orange'

print("Hi!")

# Setting a flag variable.
# This acts as a signal to the program. As long as the flag is True, the loop will continue.
Questions = True

# The while loop
while Questions:
	# Prompting the user for input. The input is automatically put in a variable for the program to check later.
	question = raw_input("\nGuess my favorite color: ")

	# Checking if the input (question) is NOT equal to favColor
	if question != favColor:
		print("Wrong!")
		print("Please, try again :)")
		# The flag is still true, so the loop continues...
		
	# Else-If satement to check if the input is exactly equal to FavColor
	elif question == favColor:
		print("\nHey...")
		print("That is my favorite color!")
		# The flag is set to False, so the loop is ended
		Questions = False
		# Another example of taking user input (which exits the program)
		raw_input("\n\nPress the enter key to exit")
