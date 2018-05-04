# https://github.com/davismohar/TechEmPython/blob/master/Variables.py

import random

def flip():
	flip = random.random()
	if (flip>=.5):
		return True
	else:
		return False

def main(num):
	heads = 0
	tails = 0
	resultString = ""

	for i in range(int(num)):
		if (flip()):
			heads+=1
			resultString += "H, "
		else:
			tails+=1
			resultString += "T, "



	#CHALLENGE: Print out percentage of heads and tails
	#percentage = ((float(heads)/float(num))*100.0)
	#print "The percentage of flips that were heads: " + str(percentage)
	print "Number of Heads: " + str(heads)
	print "Number of Tails: " + str(tails)


	seeResultString = raw_input("Would you like to see the flip log?")
	if seeResultString == "yes" or seeResultString == "y":
		print resultString


userInput = raw_input("Please enter a number of flips: ")
main(userInput)
