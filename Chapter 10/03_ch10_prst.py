'''Create a class with class attribute a , create an object from it and set directly using 
object a=0 Does this change the class attribute.'''

class alpha:
    a = 200
    def show(self):
        print(f"value of a is : {self.a}")

b = alpha()
b.a = 0
b.show()   
