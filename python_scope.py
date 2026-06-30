# name = 'Wasna'
# def scopeTesting():
#     global age
#     age=2
#     # print(name)

# scopeTesting()

# print(f'Outside of the function {name}')
# print(f'Age outside of the function {age}')
class Student:
    def __init__(self, name, age, roll):
        self.name= name
        self._age=age
        self.__roll=roll
    
    def getName(self):
         return self.name
    
    def _getAge(self):
        return self._age
    
    def __getRoll(self): #two undrescore makes the function private
        return self.__roll
    
    def getStudentInfo(self):
        return f'Name:{self.name} Age:{self._age} Roll:{self.__roll}'
    
student = Student('Manjil',2,21)

# result=student.__getRoll()
# print(result)

print(student.getStudentInfo())
