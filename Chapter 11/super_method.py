'''Super method is used to access the methods of a super class in the derived class.
it runs in multilevel inheritance.
it can also runs for constructor.
 
syntax:
       
        super()__init__():
        
               or
                
        super().upclassfunction():         '''
#########################################################################################'''

class grandPaa:
    grand = 'granny'
    
    def getG(self):
        print("\n\n********************************************************************\n\n")
        print("From parent class........\n")
        print(f"Your grand paa and {self.grand} love child class and upchild class.")

class upChild(grandPaa):
    parent = 'mummy'
    def getD(self):
        print("\n\n********************************************************************\n\n")
        super().getG()
        print("From upchild class........\n")
        print(f"Your Daddy and {self.parent} love child class ...")

class child(upChild):
    print("\n\n********************************************************************\n\n")
    print("I am cute little child class........\n")

c = child()
c.getD()
c.getG()

