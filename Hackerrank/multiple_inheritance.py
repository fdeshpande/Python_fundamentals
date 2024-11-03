class A:
    def _a(self):
        print("I am Parent1 : class A  and this is _a method. ")

class B:
    def _b(self):
        print("I am Parent2 : Class B and this is _b method. ")
    
class C(A,B):
    def _c(self):
        print("I am Child : Class C and I am inheriting properties from Class A as well as Class B , this is _c method.")

c = C()
c._a()
c._b()
c._c()


