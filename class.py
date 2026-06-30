# class Student:
#     id = 101
#     name = "Aayush"
#     age = 22
#     fee = 99.99

# student = Student()
# print(student.id)
# print(student.name)

class Employee:
    def __init__(self,id= None,name = None,age = None,salary = None):
        self.id=id
        self.name=name
        self.age=age
        self.salary=salary
    def getEmployeeInfo(self):
        return str(self.id) + " " + str(self.name) +" " + str(self.age) + " " + str(self.salary)

employee=Employee(101,'Aayush',22,99.99)
# print(employee.id,employee.name,employee.age,employee.salary)
result=employee.getEmployeeInfo()
print(result)#This is written with files.py#This is written with files.py#This is written with files.py#This is written with files.py #This is written with files.py