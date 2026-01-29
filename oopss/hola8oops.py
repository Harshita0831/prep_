"""
class Student:
    print("Hey this is the first class")
s1 = Student()
print(s1)
"""
"""
##
class Student:
    def __init__(self):
        self.name = "Henry"
s1 = Student()
print(s1.name)
"""
"""
##
class Student:
    def __init__(self, fullname):
        self.name = fullname
s1 = Student("Henry horrid")
print(s1.name)
"""

"""
##
class Student:
    def __init__(self, fullname, classss):
        self.name = fullname
        self.classs = classss
s1 = Student("Horrid Henry",12)
s2 = Student("Harry",11)
print(s1.name)
print(s2.classs)
"""

"""
##
class Car:
    namee = "Karan"
    def __init__(self,color,modelno):
        self.name = color
        self.model = modelno
s1 = Car("Blue",12)
print(s1.name)
print(s1.model)
print(Car.namee)

##
class Student:
    collegename = "lpu"         #fixed address
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
s1 = Student("Harry", 45)
s2 = Student("Gun",44)
print(s1.name)
print(s2.collegename)
print(Student.collegename)
"""

"""
##
class Employee:
    companyname = "Google"
    def __init__(self,employeename,employeesalary):
        self.name = employeename
        self.salary = employeesalary
e1 = Employee("Peter", 3000000)
print(e1.name)
print(e1.salary)
print(e1.companyname)
print(Employee.companyname)


##
class Car:
    showroomname = "xyz"
    def __init__(self, modelname, carprice):
        self.name = modelname
        self.price = carprice
c1 = Car("SUV", 1000000)
print(c1.name)
print(c1.price)
print(c1.showroomname)
print(Car.showroomname)
"""

"""
##
class College:
    collegename = "Lpu"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
c1 = College("Abhi", 98)
print(c1.name)
print(c1.marks)
print(c1.collegename)
College.collegename = "IIT"
print(c1.collegename)

##
class Company:
    companyname = "Google"
    def __init__(self, employee_name, employee_salary):
        self.name = employee_name
        self.salary = employee_salary
s1 = Company("Karan", 20000)
print(s1.name)
print(s1.salary)
print(s1.companyname)
Company.employee_salary = 22000
print(s1.employee_salary)


##
class Student:
    total_student = 0
    def __init__(self, stud_name, stud_class):
        self.name = stud_name
        self.classs = stud_class
        Student.total_student += 1
s1 = Student("Gun",11)
s2 = Student("Gungun",10)
s3 = Student("Harry",11)
print(s1.name)
print(s2.classs)
print(s3.name)
print(Student.total_student)
"""

"""
##method
class Student:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("Welcome ", self.name)
s1 = Student("Karan")
s1.hello()



##
class College:
    @staticmethod
    def college_name():
        print("This is hell")
College.college_name()
"""
"""3
##
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Hi your name is",self.name,"and marks are ",self.marks)
s1=Student("Harry", 98)
s1.display()



##
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def college_name():
        print("This is hell")
s1 = Student("Henry", 99)
print(s1.name)
Student.college_name()
"""
"""
##Encapsulation
class Student:
    def __init__(self, marks):
        self.__marks = marks         #__ hides marks (data hiding)
    def get_marks(self):            #method
        return self.__marks
s1 = Student(99)
print(s1.get_marks())

"""
"""
##

class Bank_balance():
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, new_bal):
        self.__balance = new_bal
b1 = Bank_balance(90000000)
b1.set_balance(9000000000)
print(b1.get_balance())



"""
##
class Bank_account:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def deposit(self, amount):
        self.__balance+=amount
acc = Bank_account(5000)
acc.deposit(100)
print(acc.get_balance())



























