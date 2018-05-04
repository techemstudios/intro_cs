import random

nouns = ["bird","dog","house"]
verbs = ["ate","bought","smelled"]


sub = nouns[random.randint(0,2)]
verb = verbs[random.randint(0,2)]
obj = nouns[random.randint(0,1)]

print("The " + sub + " " + verb + " the " + obj + ".")


# To illustrate how easy Python and its libraries make it to grab a list of
# 187 animals to select from for the subject of your sentence, we import a library
# called json which knows how to unpack data available on the web into
# a regular Python list.
import json

# The urllib2 library enables your program to connect to a website and, in this
# case, get some random data.
import urllib2


# In one line of code we are connecting to a site, grabbing a random collection
# of 187 animal names and packing that into a Python list.
# Don't worry if this seems complicated -- we'll break this up and review every
# step again in class.
animals = json.load(urllib2.urlopen('https://www.randomlists.com/data/animals.json'))['data']

# Now, we reload a subject randomly picked from our new big list of animals
sub = animals[random.randint(0,len(animals)-1)]

print("The " + sub + " " + verb + " the " + obj + ".")
