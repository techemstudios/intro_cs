# Python 2.7

# Objectives:
    # string methods
    # "make your own quiz":
        # while loop, adding to a score, making your own functions

import time

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

user_first_name = raw_input("Hi!" + "\nWhat is your first name? ")
user_last_name = raw_input("What is your last name? ")
user_full_name = first_name + " " + last_name

message = "\nNice to meet you " + user_full_name.title() + "!"
print(message)

def end():
    print("\nHere is your final score: ")
    print score
    exit()

def error_message():
    time.sleep(2)
    print("\nWhoops!")
    time.sleep(1)
    print("\n\t <error>")
    print("\n\t <rebooting>")
    time.sleep(0.5)
    print("\n\t.")
    time.sleep(0.5)
    print("\n\t..")
    time.sleep(0.5)
    print("\n\t...")
    time.sleep(0.5)
    print("\n\t.....")
    time.sleep(1)
    print("That's not your name is it?")
    time.sleep(1)
    print("I was thinking of someone else...")
    time.sleep(1)
    print("\nWhich reminds me, I wanted to ask you a few questions. " +
          "\nI'll score you on your accuracy.")
    time.sleep(2)

error_message()


############
# Quiz start
score = 0

QuizRunning = True

while QuizRunning:
    # First Question
    print("\nWho was " + full_name.title() + "?")
    choice1 = raw_input("\nA) first woman to go to mars, or" +
                        "\nB) first computer programmer, or" +
                        "\nC) first president of U.S." +
                        "\n")
    if choice1 == 'B':
        print("\tCorrect!" +
              "\n\tOne point is added to your score!")
        score += 1
        time.sleep(1)
        print("\n" + user_full_name.title() + " Your score is currently: ")
        print score
    
    elif choice1 == 'quit':
        end()
        QuizRunning = False
    else:
        print("\tClose!" +
              "\n\tPlease try again...")
        time.sleep(1)

    # Second Question
    print("\nWhat MACHINE did " + full_name.title() + " program?")
    choice2 = raw_input("\nA) The washer machine, or" +
                        "\nB) A car, or" +
                        "\nC) The Babbage Machine" +
                        "\n")
    if choice2 == 'C':
        print("\tCorrect!" +
              "\n\tOne point is added to your score!")
        score += 1
        time.sleep(1)
    elif choice2 == 'quit':
        end()
        QuizRunning = False
    else:
        print("\tClose!" +
              "\n\tPlease try again...")
        time.sleep(1)

    end()
        


