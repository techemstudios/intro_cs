"""
Example if statments using And/Or
"""

# Our variables we'll use to compare
a = 10
b = 5
c = 20

##
# Checking if less than, greater than

# And
if a < b and a < c:
    print("a is less than b and c.")
# Non-exclusive or
if a > b or a < c:
    print("a is less than either b or c.")
    
print("\nDone.")

