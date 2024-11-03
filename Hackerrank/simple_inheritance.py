class A:
    def _a(self):
        print("I am parent class A and this is _a method .")

class B(A):
    def _b(self):
        print("I am child class B , I am inheriting properties from parent class A and this is _b method .")

b = B()
b._a()
b._b()
