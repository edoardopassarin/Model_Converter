
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        # Should be how you call the object
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)        # prints the str(emp_1), if __str__ not defined it prints repr(emp_1)
print(repr(emp_1))      # It's printing emp_1.__repr__()

print(emp_1 + emp_2)        # how it is specified in the __add__ method, we are summing the pay
print(len(emp_1))

print(len('test'))      # equal to print('test'.__len__())

# repr(emp_1)
# str(emp_1)

# print(int.__add__(1, 2))
