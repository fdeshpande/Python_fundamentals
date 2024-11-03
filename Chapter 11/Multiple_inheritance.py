'''#########################################################################################
2] Multilevel Inheritance: 

           __________________         __________________         
          | parent class 1  |         | parent class 2  |
                   |                           |
                   |                           |
                   v___________________________v
                                  |
                                  |
                                  v
                           __________________
                           | child class    |


Multiple inheritance occurs when the child class inherits from more that one parent class.

########################################################################################'''

class Daddy:
    pocketMoney = 400

    def show_poketmoney(self):

        print(f"I am from daddy's class and i give {self.pocketMoney} rupees monthly pocket money to my child class.\n")
    def love(self):
        print("I love child class .....from daddy....\n")
class Mom:
    makeDishes = input("Mom please tell me which dish today you are going toserve me ?? :\t")

    def show_makeDishes(self):
        print(f"I am from mom's class and today i am serving {self.makeDishes} in lunch time.")
    def love(self):  # function over writing
        print("I love child class .....from mommy....")

class child(Daddy , Mom):  # it gives first overwritten function priority frm daddy 's class because daddy is written in argument first .
     
     def display(self):
        print("Hey i am cute little child class.....\n")
        print(f"I get {self.pocketMoney} rupees from my daddy every month.\n")
        print(f"Today my mommy will serve me {self.makeDishes}")

d = Daddy()
d.show_poketmoney()
d.love()


print("*******************************************************************************\n")
m = Mom()
m.show_makeDishes()
m.love()


print("*******************************************************************************\n")
c = child()
c.show_poketmoney()
c.show_makeDishes()
c.love()
c.display()
