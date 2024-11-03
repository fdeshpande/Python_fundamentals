'''write a __str__() mtd to print the vector as follows: Assume vector of dimentions  3 for this problem: '''

class vector:
    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"    


v1 = vector([2,5,8])
v2 = vector([5,9,2])
print(v1)      
print(v2)  