class Employee:
    salary = 300
    company = 'Google'

falguni = Employee()
chhavi = Employee()
falguni.company = 'Microsoft' # changing class attribute.
print(chhavi.company)
print(falguni.company)
print(falguni.salary)
print(chhavi.salary) 

