# Start with an empty list. You can 'seed' the list with
#  some predefined values if you like.
names = []

# Set new_name to something other than 'quit'.
new_name = ''


main():
    # Start a loop that will run until the user enters 'quit'.
    while new_name != 'quit':
        # Ask the user for a name.
        new_name = raw_input("Please tell me someone I should know, type <quit> to show the list of names so far: ")

        # Add the new name to our list.
        if new_name != 'quit':
            names.append(new_name)

    # Show that the name has been added to the list.
    print(names)
    
main()
