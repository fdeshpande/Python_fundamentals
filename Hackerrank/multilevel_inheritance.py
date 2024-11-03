class A:
    def _a(self):
        print("I am parent class A and this is _a method .")

class B(A):
    def _b(self):
        print("I am Child class B and this is _b method .")
    
class C(B):
    def _c(self):
         print("I am Sub-child class C and this is _c method .")

c = C()
c._b()
c._a()
c._c()