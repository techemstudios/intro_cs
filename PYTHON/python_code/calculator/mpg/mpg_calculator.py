"""
As simple program that caluclates miles per gallon.

Orginal example from programacradegames.com
"""
import time

# use raw_input() for Python 2.7
miles_driven = float(input("Enter miles driven: "))
gallons_used = float(input("Enter gallons used: "))

mpg = miles_driven / gallons_used

time.sleep(1)
print("\nPerforming mpg (miles per gallon) calculations")
print("Estimated time: 2.5 sec")
time.sleep(0.5)

# for Python 3+
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".")
time.sleep(1)
print("Your miles per gallon: ", mpg)

# for Python 2.7
##print '.',
##time.sleep(0.5)
##print '.',
##time.sleep(0.5)
##print '.'
##time.sleep(1)
##print 'Your miles per gallon: ', mpg
