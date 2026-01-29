#file = open("data.txt","mode->r,w,a")
"""file = open("Students.txt","w")
file.write("Name: rahul\n")
file.write("Course: Python\n")
file.close()

file = open("Students.txt", "r")
data=file.read()
print(data)
file.close()

file = open("Students.txt","a")
file.write("marks:90\n")
file.close()

file = open("Students.txt", "r")
data=file.read()
print(data)
file.close()

file = open("Students.txt","r")
#data = file.readline()
data2 = file.readlines()
print(data2)"""

##data file
"""file = open("data.txt","w")
file.write("Name: Henry\n")
file.write("City: Mussorie\n")
file.close()

file = open("data.txt","r")
dat = file.read()
print(dat)
file.close()

file = open("data.txt","a")
file.write("Age:20\n")
file.close()

file = open("data.txt", "r")
dat=file.read()
print(dat)
file.close()"""
file = open("data.txt","r")
#dat = file.read()
count = 0
for line in file:
    count+=1
    #print(line)
#print(dat)
print("Count =", count)
file.close()
