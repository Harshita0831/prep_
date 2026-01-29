##abstraction
class Payment:
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("Paid using UPI:",amount)
class Card(Payment):
    def pay(self,amount):
        print("Paid using Card:",amount)
class Cash(Payment):
    def pay(self,amount):
        print("Paid using cash:",amount)

obj = Card()
obj.pay(1100)
obj = Cash()
obj.pay(1234)
obj = UPI()
obj.pay(7890)
##

class Shape:
    def area(self,meter):
        pass
class Circle(Shape):
    def area(self,meter):
        print("Circle has radius of",meter,"m")
class Triangle:
    def area(self,meter):
        print("Triangle has area of",meter,"m")
class Rectangle:
    def area(self,meter):
        print("Rectangle has area of",meter,"m")
obj = Triangle()
obj.area(23)

##
class Payment:
    def start(self):
        print("Payment started")
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("Paid using UPI:",amount)
class Card(Payment):
    def pay(self,amount):
        print("Paid using Card:",amount)
class Cash(Payment):
    def pay(self,amount):
        print("Paid using cash:",amount)
ob = UPI()
ob.start()
ob.pay(23333)

##
class Store:
    def start(self):
        print("Welcome to store")
    def matter(self,amount):
        pass
class Clothes(Store):
    def matter(self,amount):
        print("The clothes cost is",amount)
class Shoes(Store):
    def matter(self,amount):
        print("The shoes cost is",amount)
obj = Clothes()
obj.start()
obj.matter(2000)

##interface
class Store:
    def matter(self,amount):
        pass
class Clothes(Store):
    def matter(self,amount):
        print("The clothes cost is",amount)
class Shoes(Store):
    def matter(self,amount):
        print("The shoes cost is",amount)
obj = Clothes()
obj.matter(2000)

##
class Course:
    def course_info(self):
        print("Course Information")
    def duration(self):
        #print("Duration of course")
        pass
class ExamInterface:
    def exam_type(self):
        pass
    
class PythonCourse(Course,ExamInterface):
    def duration(self):
        print("Course duration is 3 months")
    def exam_type(self):
        print("Exam is practical based")

class JavaCourse(Course,ExamInterface):
    def duration(self):
        print("Course duration is 2 months")
    def exam_type(self):
        print("Exam is theory based")
obj1=PythonCourse()
obj1.duration()
obj1.exam_type()

##
##
class Address:                                                          
    def __init__(self,city):
        self.city = city
    def show_address(self):
        print("City:",self.city)
#student class
class Student:
    def __init__(self,name,city):
        self.name = name
        #composition
        #creating object of address class inside student class
        self.address = Address(city)
    def show_student(self):
        print("Name:",self.name)
        #using object of another class
        self.address.show_address()
s = Student("Karan","Delhi")
s.show_student()

##has-a relationship
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.start()
        print("Car is moving")
ob = Car()
ob.drive()
        
#create a class teacher and subject HAS-A relationship 






































        





































    


















