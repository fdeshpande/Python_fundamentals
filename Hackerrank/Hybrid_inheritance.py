class A:
    def _a(self):
        print("I am Parent class A , this is _a method. ")

class B(A):
    def _b(self):
        print("I am Child class B and inheriting class A , this is _b method.")

class C(A):
    def _c(self):
        print("I am Sub Child class C and inherting Class A , this is _c method (Parent class for D)")

class D(B,C):
    def _d(self):
        print("I am Child class D and inheriting Class A and Class D.")

# simple inheritance:
o1 = B()
o1._a()
o1._b()
print()

# Multilevel inheritence:
o2 = C()
o2._a()
o2._c()
print()

# Multiple inheritance
o3 = D()
o3._a()
o3._b()
o3._c()
o3._d()
