filename = 'my_second_program.txt'

with open(filename, 'w') as file_object:
	file_object.write("George Boolean was a mathematician.")
	file_object.write("BOOL, is short for Boolean, and is considered a data type.")
	
	# When we run this, both lines are squished together.
	# We can insert the \n, newline to have statements appear on their own lines.
	

