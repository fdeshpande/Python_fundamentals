# Examples on Inheritance:

class parent:
    def _add(self):
        print("I am _add method present in parent class .")

class child(parent):
    def _sub(self):
        print("I am _sub method present in child class .")

c = child()
c._add()
c._sub()

# Example on Composition:

class demo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        print("My name is add and present in demo class .")

class sample:
    def __init__(self,d):
        self.d = d
    
    def sub(self):
        print("I am sub_ method and present in sample class .")

d = demo(10,20)
s = sample(d)
s.sub()
s.d.add()


