# Plethora of comments to follow
# The first line of the program begins the definition of a function called main:
def main():
# The line inside of main (the line below) is the beginning of our program.
    print("This program illustrates a chaotic function")
# This next line is an example of a variable, or a label of something.
# A variable is used to give a name or a value so that we can refer to it at
# other points in the program.
# Here, we created the variable x and we are telling Python that it labels
# getting input from the user.
# When Python get sto this statement, it displays the string inside.
# and then pauses, waiting for the user to type something on the keyboard and press enter.

    x = eval(input("Enter a number between 0 and 1: "))
# The value that the user types in is then stored as the variable x.
# The next line is an example of a loop.
# A loop is a device that tells Python to do the same thing over and over again.
# This loop says to do something 10 times.
    for i in range(10):
# These indented lined below the loop are the statements that are done 10 times.
# These statements form the body of the loop.
        x = 3.9 * x * (1-x)
        print(x)
# Using comments, here is the loop typed out (that you don't actually see) when you run it:
# x = 3.9 * x * (1-x)
# print(x)
# x = 3.9 * x * (1-x)
# print(x)
# x = 3.9 * x * (1-x)
# print(x)
# x = 3.9 * x * (1-x)
# print(x)
# x = 3.9 * x * (1-x)
# print(x)
# x = 3.9 * x * (1-x)
# print(x)
# x = 3.9 * x * (1-x)
# print(x)
# x = 3.9 * x * (1-x)
# print(x)
# x = 3.9 * x * (1-x)
# print(x)
# x = 3.9 * x * (1-x)
# print(x)

# You can see that by using the loop, it saves you a lot of time.
# Otherwise, if you didn't use the loop, you would have to actually type those variables
# and print statements 10 times!

# What these statements do: The first one performs a calculation
# x = 3.9 * x * (1-x)
# This is called an assignment
# The part on the right side of the = is a mathematical expression.
# Remember Python uses that character * to say it is multiplying something.

# When Python executes the print statement print(x)
# the current value of x is displayed on the screen
# Then the preceding statements take that first printed value (based on what the user type in)
# and executes the print statement again, 9 more times, each with the new value of x
# based on the last calculation from the previous statement.

# So you can see that the current value of x is used to compute a new value each time around the loop!

main()
