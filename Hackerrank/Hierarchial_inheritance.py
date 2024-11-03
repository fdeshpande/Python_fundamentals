class A:
    def _a(self):
        print("I am parent class A and this is _a method .")

class C1(A):
    def _c1(self):
        print("I am Child 1 : class C1 and this is _b method .")

class C2(A):
    def _c2(self):
        print("I am Child 2 : Class C2 and this is _c2 method .")

o1 = C1()
o1._a()
o1._c1()
print()

o2 = C2()
o2._a()
o2._c2()