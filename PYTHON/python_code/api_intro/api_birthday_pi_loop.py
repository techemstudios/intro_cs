import requests

r = requests.get('https://raw.githubusercontent.com/joetechem/birthday_pi/master/million_pi_digits/million_pi_digits.txt')

print("Status code:", r.status_code)

pi_string = r.text

for rs in r:
    pi_string += rs.strip()

while True:
    birthday = raw_input("\nEnter your birthday, in the form mmddyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")
