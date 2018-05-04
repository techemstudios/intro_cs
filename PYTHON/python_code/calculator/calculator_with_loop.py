"""
A simple interactive calculator program
THe program will keep running until directed by the user.
Operators handled: addition (+), subtraction (-), multiplication (*), division (/)
"""

def main():
    while True:
        number1 = int(raw_input("Give me a number: "))
        number2 = int(raw_input("Give me another number: "))

        operation = raw_input("\nWhich operation would you like me to perform? " +
                              "\n+ for addition" +
                              "\n- for subtraction" +
                              "\n* for multiplication" +
                              "\n/ for division" +
                              "\n% for remainder\n"
                              )
        
        if operation == "+":
            answer = number1 + number2

        elif operation == "-":
            answer = number1 - number2

        elif operation == "*":
            answer = number1 * number2

        elif operation == "/":
            answer = number1 / number2

        elif operation == "%":
            answer = number1 % number2

        print answer

        again = raw_input("Would you like to calculate another pair of numbers? y/n: ")
        if again == "y":
            main()
        elif again == "n":
            raw_input("\n\nPress <enter> to exit ")
            break

main()

