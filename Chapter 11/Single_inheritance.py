'''                         __________________
1] Simple Inheritance:      |  parent class  |
                                   |
                                   |
                                   v
                           __________________
                           | child class    |

Single inheritance occers when child class inherits from one parent class.                       
#########################################################################################'''

class parent:
    nature = 'soft'

    def showDetails(self):
        print("I am parent class.\n")
        print(f"I am {self.nature} by nature.\n")

class child(parent):
    favourite = 'chocolate'

    def showDetails(self): # function over-writing
        print("I am child class.\n")   
        print(f"I like {self.favourite} \n") 

    def display(self):
        print("I am inheriting some features from parent class.\n")

p = parent()
p.showDetails()
c = child()
c.showDetails()
c.display()
print(f"My parent class says it has a nature as {c.nature}.")
