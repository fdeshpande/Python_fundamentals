'''class employee:
    def __init__(self,a,b):
        self.a = a
        self.b = b
e = employee(11,22)
print(e.__dict__)

class calculator:
    def add_(self,x,y):
        print(x+y)
    
    def sub_(self,x,y):
        print(x-y)
    
    def multiply_(self,x,y):
        print(x*y)

    def div_(self,x,y):
        print(x/y)
    
    def mod_(self,x,y):
        print(x%y)

c = calculator()
c1 = calculator()
c.add_(20,10)
c.sub_(15,10)
c.multiply_(3,4)
c.div_(10,5)
c.mod_(45,9)
c1.add_(20,10)
c1.sub_(15,10)
c1.multiply_(3,4)
c1.div_(10,5)
c1.mod_(45,9)

# Creating an alternate constructor:

class employee:
    fname= 'Radhika'
    lname = 'Sewak'
    Sal = 30000

    def display(self):
        print(f"the employee first name {employee.fname} and the last name is {employee.lname} she earns {employee.Sal} per month .")

e = employee()
e.display()

class employee:
    def __init__(self,fname,lname,Sal):
        self.fname= fname
        self.lname = lname
        self.Sal = Sal

    def display(self):
        print(f"the employee first name {self.fname} and the last name is {self.lname} she earns {self.Sal} per month .")

e = employee('Radhika','Sevak',30000)
e.display()

# Using instances to access the class variable

class points:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def show(self,x,y):
        self.a = self.a + x
        self.b = self.b + y

p = points(30,10)
p.show(10,10)
print(p.__dict__)



# Constructor with variable number of arguments .

class employee:
    def __init__(self,fname,lname,pay,*args):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.args = args

emp = employee('Steve','Scott',30000,'Anju','Raju','Sanket',40000,'Amit','Dishant')
print(emp.__dict__)

print()


# Constructor with default values.

class point:
    def __init__(self,a=10,b=20):
        self.a = a
        self.b = b

p1 = point(20,30)
print(p1.__dict__)

p2 = point()
print(p2.__dict__)

p3 = point(120,40)
print(p3.__dict__)

print()


# Instance Method 

class employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def create_email(self):
        print(f"Email id : {self.fname}{self.lname}@gmail.com")
    
    def display_details(self):
        print(f"Name of Employee : {self.fname} , Last name of Employee : {self.lname} , Pay of Employee : {self.pay}")

e = employee('Saket','Janbandhu',40000)
e.create_email()
e.display_details()


print()

# @classmethod

class employee:
    company = 'Amazon'

    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    @classmethod
    def display_company(cls):
        print(f"Company Name : {cls.company}")
    
    def display_details(self):
        print(f"Name : {self.fname} , Last Name : {self.lname} , Pay : {self.pay}")

e1 = employee('Saket','Tripathi',35000)
e1.display_company()
e1.display_details()

print()


# Modifying the class variables using object / instance variables.

class employee:
    company = 'Flipkart'

    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @classmethod
    def from_list(cls,l):
        return cls(l[0],l[1],l[2])

l = ['Arjun','Thakur',30000]
e = employee.from_list(l)
print(e.__dict__)
print(employee.__dict__)
'''

# Programs on class and object by using __call__ method :

class log:
    def __call__(self):
        print("hello everyone")

l = log()
l()

print()


# print name :

class log:
    def __call__(self,name):
        print(f"Name : {name}")

l1 = log()
l1('Samiksha')

print()

#check string palindrome:

class palindrome:
    def __call__(self,string):
        if string == string[::-1]:
            print(string, "is Palindrome .")
        else:
            print(string, "is not palindrome.")

p = palindrome()
p('MadaM')
p('Raja')
