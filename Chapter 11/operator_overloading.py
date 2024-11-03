class Number:
    def __int__(self,num):
        self.num = num

    def __add__(self,num2):
        print('lets add')
        return self.num + num2.num


    

n1 = Number()
n2 = Number()
sum = n1 + n2
print(sum)

