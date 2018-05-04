"""
A simple program that takes the user's input, and adds it to a list.
"""


cities = []

def main():
#    def instructions():
#        print("\n\tType in any city name I should visit, and I'll add it to a list.")
#        print("\tTo quit, type <done>")
#    instructions()
    prompt = "\n\tType in any city name I should visit, and I'll add it to a list."
    prompt += "\n\tTo quit, type <done>"
    prompt += "\n\nCity name: "
    
    active = True
    while active:
        new_city = raw_input(prompt)
        cities.append(new_city)
        print("\nI'd love to go " + new_city.title() + "!")

        if new_city == 'done':
            print("Here is the list of cities so far:")

            done = 'done'
            cities.remove(done)
            print(cities)
            active = False

            again = raw_input("\nWould you like to add more cities for me to visit? y/n?")
            if again == 'y':
                main()
            else:
                raw_input("\n\nPress Enter to Exit.")

main()




          
