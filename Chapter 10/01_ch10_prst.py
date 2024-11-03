'''Create a class programmer for storing information of two programmers
 working at microsoft.'''

class programmer:
    pr1 = input("Enter the name of programmer 1:\t")
    pr2 = input("Enter the name of programmer 2:\t")
    dept1 = input("Enter department of programmer 1:\t")
    dept2 = input("Enter department of programmer 2:\t ")
    Spr1 = input("Enter salary of programmer1:\t")
    Spr2 = input("Enter salary of programmer2:\t")

    def programmer1(self):
        print("****************INFORMATION OF PROGRAMMERS WORKING AT MICROSOFT*************")
        print(f"Name of first programmer is : {self.pr1}\n")
        print(f"Department of first programmer is:{self.dept1}\n")
        print(f"Salary of first programmer is :{self.Spr1}\n\n")

    def programmer2(self):
        print(f"Name of second programmer is : {self.pr2}\n")
        print(f"Department of second programmer is:{self.dept2}\n")
        print(f"Salary of second programmer is :{self.Spr2}\n")    

pro = programmer()
pro.programmer1()
pro.programmer2()        



    
