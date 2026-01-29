##
class Human:
    def speak(self):
        print("Human is speaking")
class Baby:
    def speak(self):
        print("Baby is crying")
class Dog:
    def speak(self):
        print("Dog is barking")
h = Human()
b = Baby()
d = Dog()
h.speak()
b.speak()
d.speak()

##
class Car:
    def ride(self):
        print("Car is moving")
class Bike:
    def ride(self):
        print("Bike is moving")
class Truck:
    def ride(self):
        print("Truck is moving")
c = Car()
b = Bike()
t = Truck()
c.ride()
b.ride()
t.ride()

##
#polymorphism mix with inheritance
class Person:
    def role(self):
        print("To exist")
class Student(Person):
    def role(self):
        print("I am student")
class Teacher(Person):
    def role(self):
        print("I am teacher")
class Assistant(Student,Teacher):
    #def role(self):
        #print("I am assistant")
    pass
obj = Assistant()
obj.role()

##Reference and Object behavior
a =[1,2,3]
b = a
b.append(4)
print(b)
print(a)

##
a = 10
b = a
b = 20
print(b)
print(a)












