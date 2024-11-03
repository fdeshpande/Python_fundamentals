class employee:
    company = 'camel'
    salary = 100
    location = 'Delhi'

    @classmethod          # decorator which takes function as a input....
    def changeSalary(cls,sal):
        cls.salary = sal

e = employee
print(e.salary)
e.changeSalary(400)
print(e.salary)
print(employee.salary)


