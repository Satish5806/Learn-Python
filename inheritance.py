from abc import ABC, abstractmethod
class person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age= age

    @abstractmethod
    def getInfo(self):
        pass

class Student(person):
    def __init__(self, name, age, roll, fee):
        super().__init__(name, age)
        self.roll = roll 
        self.fee = fee

    def getInfo(self):
        return f'Student Name:{self.name}, Student age:{self.age}, student roll:{self.roll},student fee:{self.fee}'

class Teacher(person):
    def __init__(self, name, age, id, salary,employee_grade):
        super().__init__(name,age)
        self.id = id 
        self.salary = salary
        self.employ_grade = employee_grade
    def getInfo(self):
        return f'Teacher Name:{self.name}, Teacher age:{self.age}, Teacher ID:{self.id},Teacher Salaray:{self.salary}, Employee Grade:{self.employ_grade} '

class Peon(person):
    def __init__(self, name, age, id, salary, employee_grade):
        super().__init__(name,age)
        self.id = id 
        self.salary = salary
        self.employ_grade = employee_grade
    def getInfo(self):
        return f'Peon Name:{self.name}, Peon age:{self.age}, Peon ID:{self.id},Peon Salaray:{self.salary}, Employee Grade:{self.employ_grade}'

student=Student('Maria', 21, 25, 500)

teacher=Teacher('Luther', 31, 101, 5000,'A')

peon=Peon('Daniel', 36, 200, 400, 'B')

print(student.getInfo())
print(teacher.getInfo())
print(peon.getInfo())
