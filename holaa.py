"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a>b:
    print("a is bigger number")
elif b>a:
    print("b is bigger number")
else:
    print("Both are equal")

#Traffic
c = str(input("Enter color: "))
if c=="Green":
    print("You can go")
elif c=="Yellow":
    print("Ready")
elif c=="Red":
    print("You can stop")
else:
    print("Invalid input")

#table of 2
for i in range(1,11):
    print(2*i)

#odd number
for i in range(1,16):
    if i%2 != 0:
        print(i,"is odd")

#star tree
x = int(input("Enter the number: "))
for i in range(1,21):
    print("*"*i)

#loop
i = 1
while(i<=5):
    print(i)
    i+=1"""

#table of num using while loop
num = int(input("Enter number: "))
i = 1
while(i<=10):
    print(num,"x",i, "=" ,num*i)
    i+=1
    
