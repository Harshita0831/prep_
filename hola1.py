"""#function in python
a = int(input("a is "))
b = int(input("b is "))
def sum(a,b):
    return a+b
print("Sum is", sum(a,b))

#Function comes in 2-3 lines but lambda function comes in 1 line
x = int(input("Enter number: "))
square = lambda x: x*x
print(square(x))

#Questions
#take input print its type then double of it
a = int(input("Enter number "))
print(type(a))
print(2*a)

#q-2
salary = str(input("Enter Salary: "))
print(salary)
print(type(salary))
print(int(salary))
b = int(salary) + 5000
print(b)

#q-3
temp = int(input("Enter temperature: "))
if (temp>=30):
    print("Hot")
elif (temp>=15):
    print("Normal")
else:
    print("Cold")

#q-4
table = []

for i in range(1, 11):
    value = 7 * i
    print(value)
    table.append(value)

print("Count:", len(table))"""

#q-5#revise
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)


#q-6
#check even/odd using functions
def check(a):
    if a%2==0:
        return "Even"
    else:
        return "odd"
a = int(input("a is "))
print("The number is:", check(a))


#q-7
x = int(input("Enter number: "))
cube = lambda x: x*x*x
print(cube(x))
