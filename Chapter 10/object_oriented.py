'''Solving a problem by creating objects is one of the most popular approaches 
in programming . This is called object oriented programming . 
This concepts focuses on using reusable code. 
A class is a blueprint of objects .
Object is an instantiation of class.
When class is defind , a template is defind and when object created then automatically memory is allocated.'''


class Employee:
    a = input("Enter your name :\t")
    b = float(input("Enter your salary:\t"))
    c = input("Enter your department:\t")
    def call(self):
        print(f"i am {self.a}")
        print(f"My salary is {self.b} Rs/month")
        print(f"I am working in {self.c} department")
e = Employee()
e.call()

