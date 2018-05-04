"""
We can create, open, and write to a file, all from within a python program.
"""

# name the file and type of file
filename = 'my_program.txt'

with open(filename, 'w') as file_object:
	file_object.write("Ada Lovelace was the first computer programmer.")
	
# open() takes two arguments:
	# 1: the name of the file we want to open
	# 2: 'w' tells python we want to open the file in "write mode"
		# read mode: 'r', append mode: 'a', read&write: 'r+'
		# without the mode argument, python opens in read-only by default
		
# open() automatically creates the file if it does not already exist

# When you run this program, it stores the text in a file; instead of printing to the screen.

