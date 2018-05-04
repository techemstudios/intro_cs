# first we'll setup a new file
filename = 'my_fourth_program.txt'

# We'll open that file and write to it
with open(filename, 'w') as file_object:
	file_object.write("Charles Babbage is known as the father of computers.\n")
	file_object.write("Babbage built a working Babbage machine.\n")
	
# Now, we will add to that file, or "append"
with open(filename, 'a') as file_object:
	file_object.write("Oh wait, there wasn't a working Babbage machine built until the next century.\n")
	file_object.write("You can use object-oriented design to model real world concepts.\n")

# For a challenge, you can create a Guest Book.
	# details: write a while loop which asks users for their name.
	# when they enter their name, print a small greeting to the screen,
	# then add a line that records their name to a file called guest_book.txt.
