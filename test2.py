import sqlite3
class Employee:
    no_emp = 0
    def __init__(self,first,last,age):
     self.first= first
     self.last=last
     self.age=age
     Employee.no_emp +=  1

    def fullname(self):
        return self.first + " " + self.last

    

emp1=Employee('iman','dannan',50)
print(emp1.no_emp)
emp2=Employee('sawsan','dannan',51)

print(emp2.no_emp)
print(Employee.no_emp)
print(emp1.fullname())
print(emp2.fullname())







