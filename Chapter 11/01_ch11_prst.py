'''Create a class 2d vector and use it to create another class representing a 3-d vector:'''

class two_dim_vector:
    name = '2D vector'   
    print("I am 2-D vector...") 

class three_dim_vector(two_dim_vector):
    name = '3D vector'
    def display(self):
        print(f"I am {self.name} vector...")

d = three_dim_vector()
d.display()
print(d.name)        
