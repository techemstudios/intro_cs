###### PART 1 ######





###### END PART 1 ######

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


some_dog = Dog('koa', 3)


###### PART 2 ######
# Put your dog's (or an imaginary dog) info below:



###### END PART 2 ######

print("My dog's name is " + some_dog.name.title() + ".")
print("My dog is " + str(some_dog.age) + " years old.")
print("\n")

some_dog.sit()
some_dog.roll_over()

print("\n")

###### PART 3 ######
# Tell your dog to sit and roll over:



###### END PART 3 ######
