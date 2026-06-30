class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.email=first+'.'+ last +'@gmail.com' 
        self.pay=pay

        Employee.num_of_emps += 1

    def fullname(self):
        return'{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod #Alternative constructor
    def from_string(cls, emp_str):
        first, last, pay=emp_str.split('-')
        return cls(first, last, pay)

emp_1= Employee('Corey', 'Schafer', 60000)
emp_2= Employee('Test', 'User', 50000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe_90000'

new_emp_1=Employee.from_string(emp_str_1)

emp_1.set_raise_amt(1.1)
print(f'{Employee.raise_amount}')
print(new_emp_1.email)
print(new_emp_1.pay)