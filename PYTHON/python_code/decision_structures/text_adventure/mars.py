# Choose your own adventure game
# MARS

def bad_alien():
    print("The object fires a laser at you!")
def friendly_alien():
    print("A little alien comes from the object with some spare O2 for you.")

print("You land on mars and your oxygen generator has failed, so you only have a few hours on the planet. However, you see something in the distance! What do you do?")
choice = raw_input("\nA) Leave Now, B) Go to object, or C) Scan Object ")

if choice == "A":
    # First branch of story
    print("\nYou begin to leave and notice the object moves. What do you do?")
    choice = raw_input("A) Continue leaving or B) Stay on the planet to investigate ")
    if choice == "A":
        bad_alien()
    else:
        friendly_alien()
        # Your adventure can continue here.
    
elif choice == "B":
    # Second branch of story
    print("\nAs you approach the object, it is clearly an alien. What do you do? ")
    choice = raw_input("A) Investigate the object or B) Leave ")
    if choice == "A":
        friendly_alien()
    else:
        bad_alien()

else:
    # Third branch of story
    print("\nAfter scanning the object for 30 minutes, you get no usable information. What do you do now?")
    choice = raw_input("A) Scan More or B) Leave the planet ")
    if choice == "A":
        bad_alien()
    else:
        bad_alien()
