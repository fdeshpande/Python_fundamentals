'''In python compiler give first preference to object instance rather than class instance:'''

class Employee:
    salary = 300          #class instance
    company = 'Google'

falguni = Employee()
chhavi = Employee()
falguni.salary = 5000  #object instance
chhavi.salary = 4000   #object instance
print(falguni.salary)
print(chhavi.salary)