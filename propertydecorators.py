class Employee:

    def __init__(self, first, last):
        self.first=first
        self.last=last 

    @property #when used this decorator parenthesis needn't be added for functions while printing
    def email(self):
        return'{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return'{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first 
        self.last = last 
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1= Employee('john', 'Smith')

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
