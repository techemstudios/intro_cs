class Things():
    pass

class Living(Things):
    pass

class Animals(Living):
    pass

class Mammals(Animals):
    pass

class Dog(Mammals):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('koa', 3)

######## Put your dog's (or an imaginary dog) info below:
your_dog = 

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

######## Tell your dog to sit and roll over:
