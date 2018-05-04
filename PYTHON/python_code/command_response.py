# Put your commands here
# Keep the values lowercase
COMMAND1 = "what?"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Huh?"

    else:
        response = "Why thank you, I don't know what else to say."
    return response

print ("Hi, I am sirexa, your own personal bot. Awaiting your command.")

while True:
    command = raw_input('\nsirexa -> ')
    response = handle_command(command)
    print response

