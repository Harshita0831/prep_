##
class Human:
    def eat(self):
        print("Human can eat")
class Student(Human):
    def study(self):
        print("Student can study")
s1 = Student()
s1.eat()
s1.study()

##
class Animal:
    def speak(self):
        print("All animals can speak")
class Dog(Animal):
    def bark(self):
        print("Only dogs can bark")
d1 = Dog()
d1.speak()
d1.bark()

##
class Nokia:
    def call(self):
        print("Nokia can only make call")
class Iphone(Nokia):
    def internet(self):
        print("Iphone can access internet")
i1 = Iphone()
i1.call()
i1.internet()

##
class Parent:
    def __init__(self):
        print("This is parent constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is child constructor")
c1 = Child()    #object

##
class Parent:
    def work(self):
        print("I will go to work")
class Child(Parent):
    def work(self):
           super().work()
           print("I will go to school") 
obj = Child()    
obj.work()

##
class Father:
    def eyes(self):
        print("Same eyes as father")
class Mother:
    def eyes(self):
        print("Same eyes as Mother")
class Child(Father, Mother):
    def eyes(self):
        super().eyes()
        
        print("Child has mix of parents eyes")
ob1 = Child()
ob1.eyes()

##
class Parent:
    def shape(self):
        print("I am a shape")
class Child(Parent):
    def shape(self):
        print("I am circle")
obj1 = Child()
obj1.shape()

##
class Teacher:
    def teacher(self):
        print("he is teaching")
class Coder:
    def coding(self):
        print("Coding")
class Student(Teacher, Coder):
    pass
ob1 = Student()
ob1.coding()
ob1.teacher()

"""
##
class Parent:
    def __init__(self):
        self.__x = 10
class Child(Parent):
    def show(self):
        print(self.__x)
obj = Child()
obj.show()
"""

##
class Parent:
    def __init__(self):
        self.__x = 10
class Child(Parent):
    def show(self):
        print(self._Parent__x)
obj = Child()
obj.show()
        

##
"""
x is global variable/public
_x is protected variable
__x is private variable
"""

##
class Parent:
    def __init__(self):
        self._x = 100
class Child(Parent):
    def show(self):
        print(self._x)
obj = Child()
obj.show()

obj1 = Child()
print(obj1._x)
#to access private variable _Private__x

##
class Person:
    def __init__(self,name):
        self.__name = name

    def get_name(self):
        return self.__name
class Student(Person):
    def show(self):
        print("my name is",self.get_name())
obj = Student("Henry")
obj.show()

##
class Account:
    def __init__(self,balance):
        self._balance = balance
    def show_balance(self):
        return self._balance
class Saving_account(Account):
    def add_money(self):
        amount = int(input("enter amount: "))
        self._balance += amount
        print("Balance is", self._balance)
obj = Saving_account(1000)
obj.add_money()

##

class A:
    def fruit(self):
        print("Fruit's king is Mango")
class B(A):
    def apple(self):
        print(B)
class C(A):
    def app(self):
        print(C)
class D(B,C):
    pass
obj = D()
obj.fruit()



















