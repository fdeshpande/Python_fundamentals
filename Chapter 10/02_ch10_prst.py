'''write a class calculator capable of finding square , cube , square root.'''

class calculator:
    s = float(input("Write any number of which you want to calculate square , cube , squareroot :\t"))
    
    def calculate_square(self):
        Square = print(f"The square of entered number is = {self.s * self.s}")

    def calculate_cube(self):
        cube =   print(f"The cube of entered number is = {self.s * self.s * self.s}") 

    def calculate_squareroot(self):
        sq_root = print(f"The square of entered number is = {self.s ** 0.5}")    

calculate = calculator()
calculate.calculate_square()
calculate.calculate_cube()
calculate.calculate_squareroot()        

