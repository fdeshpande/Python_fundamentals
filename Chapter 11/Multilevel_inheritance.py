'''########################################################################################
                             __________________
1] Multilevel Inheritance:   |  parent class   |
                                     |
                                     |
                                     v
                              __________________
                              | child class  1 |
                                     |
                                     |
                                     v
                              __________________
                              | child class  2 |

When a child class becomes a parent for another child class.

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
        print("From upchild class........\n")
        print(f"Your Daddy and {self.parent} love child class ...")

class child(upChild):
    print("\n\n********************************************************************\n\n")
    print("I am cute little child class........\n")


c = child()
c.getD()
c.getG()


