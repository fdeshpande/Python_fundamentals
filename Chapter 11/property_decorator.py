class employee:
    company = 'Bharat gas'
    salary = 5600
    salarybonus = 400

    @property    # it is same as @setter decorator.
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self , val):
        self.salarybonus = val - self.salary

e = employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)
