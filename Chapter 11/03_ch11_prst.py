'''Create a class employee and add salary and increment property to it .
with a mtd SalaryAfterIncreament with a @property decorator with a setter which changes 
the value of increament based on the salary . '''

class employee:
    company = 'Bharat gas'
    salary = 5600
    Insalarybonus = 400

    @property    # it is same as @setter decorator.
    def SalaryAfterIncreament(self):
        return self.salary + self.Insalarybonus

    @SalaryAfterIncreament.setter
    def SalaryAfterIncreament(self , val):
        self.SalaryAfterIncreament = val + self.salary

e = employee()
e.Insalarybonus = 300
print(e.SalaryAfterIncreament)
print(e.salary)
print(e.Insalarybonus)