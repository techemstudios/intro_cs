import time

def main():
    while True:
        name = raw_input("Please, Tell me your name: ")
        greeting = "Welcome, " + name.title() + "!"
        greeting += "\nYou are added to guest_book.txt"
        print(greeting)

        filename = 'guest_book.txt'

        with open(filename, 'a') as file_object:
            file_object.write(name.title() + " " + time.asctime() + "\n")

main()
        
