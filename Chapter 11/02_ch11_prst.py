'''Create a class pets from a class animal and further create class dog from pets . 
Add a method bark to class dog.'''

class Animal:
    print("I am animal class.")
    print("i am classified in wild and domestic animal.\n")

class pets(Animal):
    print("i am pets class...")
    print("I am inheriting the class animal . And I am classified in domestic species ...\n")

class Dog(pets):
    print("I am dog class..\nI am inheriting class pets .\n I am belong to domestic species..")
    def bark(self):
        print("Barking is my nature...")


d = Dog()
d.bark()