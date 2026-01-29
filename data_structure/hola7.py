##operations with list

"""
l1 = [1,2,3,4,56,7,8,9]
print(l1)
for i in l1:        #looping through the list
    print(i)
    
l1.append("apple")
print(l1)       #adding element using append


fruit = ['Apple','Orange']
print(fruit)
fruit.append('Watermelon')
print(fruit)

#sum of all elements in a list
l2 = [1,2,3,4,56,7,8,9]
print(sum(l2))

#or
l3 = [1,2,3,7,8,9]
total = 0
for i in l3:
    total = total+i
print(total)
print(l3[::-1])

#remove duplicates    crazyyy
list = [1,22,22,3,4,5]
l4 = []
for i in list:
    if i not in l4:
        l4.append(i)
print(l4)"""

"""
##tuple
colors = ("red","green","blue")
print(colors[1])
print(colors[2])
print(type(colors))

##convert list into tuple
num = [1,2,3,4]
print(type(num))
num_tuple = tuple(num)
print(type(num_tuple))


##convert tuple to list
color = ['red','blue','green']
print(type(color))
color_list = list(color)
print(type(color_list))
print(color_list)
color.append('Yellow')
print(color)
tuple1 = tuple(color)
print(tuple1)
print(type(color))

##convert list to set
nums = [1,22,2,2,3,4]
num_set = set(nums)
print(num_set)
num_list = list(num_set)
print(num_list)

##convert dictionary to set
student = {"name":"henry","age":24}
student_set = set(student)              #set only fetches keys if dict is converted to set
print(student_set)
print(type(student_set))


##convert set into dictionary
sub = {'Maths','Science','english'}
sub_dict = dict.fromkeys(sub,0)
print(sub_dict)
print(type(sub_dict))
"""

"""###Error handling / type of error

ZeroDivisionError -  when any number divided by 0 eg-10/0

ValueError - when given wrong value to a function eg-num = int("abc")

TypeError - when performed operations between different data types eg - print(5+"abc")

IndexError -  when accessed wrong index eg -l1 = [1,2] print(l1[2])

KeyError - when accessed a missing key in dict

FileNotFoundError -when python cant find a file in pc

"""


"""
try:
    #risky code
except:
    #runs if error occurs

try - code that may fail
except - runs when error happen
"""
"""
#catching any specific error
try:
    x=int(input("enter number: "))
    print(10/x)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Enter only number")
#finally:
    #print("So cool")        #always run despite any error
else:
    print("broo")               #runs when there is error


##
try:
    f = open("moviess.txt")
except:
    print("File not found")
finally:
    print("Program ended")

##
age = int(input("Enter Age:"))
if age<18:
    raise ValueError("Age must be 18 or above to vote")
print("You can vote")"""

"""
#Custom Errors
class LowBalanceError(Exception):
    #this line creates a custom exception named LowBalanceError
    #pass is used because class can not be empty in python
    #we dont need to add any logic inside the class right now
    pass
balance = 500
withdraw = int(input("Enter amount: "))
if withdraw>balance:
    raise LowBalanceError("Insufficient Balance")
print("Withdraw Successfull")
"""
"""
try:
    num = int("10")
    n = int("0")    #converting into int
    print(num/n)
except ValueError:
    print("Error")
except ZeroDivisionError:
    print("ERr")
    
    
"""
###
"""
try:
    num = int(input("Enter a number: "))
    print(100/num)
except ValueError:
    print("Error")
except ZeroDivisionError:
    print("Broo")"""


###
"""
try:
    try:
        print(1/0)
    finally:
        print("inner finally")
except ZeroDivisionError:
    print("Outer Exception")
finally:
    print("outer finally")
"""

###
"""
def test():
    try:
        return 10
    finally:
        return 20
print(test())
"""

###
"""
try:
    try:
        x = int("abc")
    except ValueError:
        print("inner handled")
        raise
except Exception:
    print("Outer handled")

"""
###
"""
def test():
    try:
        return 10
    except:
        return 20
    #finally:
        #return 30          #if there is no error then only finally block will give o/p try won't give
    else:
        return 30
print(test())
"""

###
age = int(input("Enter your age: "))
if age<18:
    raise ValueError("age must more than 18")
print("eligible")



"""
exception - runtime error

try block - risky code

except - handles error

finally - always runs

else - run when no error

raise - exception creating new error manually

custom error - creating new error manually not in built in python"""


###
#takes number input from user
num = int(input("Enter a number: "))
#if number is negative, we manually raise an error
#python does not automatically treat negative number as wrong
if num<0:
    raise ValueError("Number must be positive")
#this will run if exception occur
print("You entered",num)




















